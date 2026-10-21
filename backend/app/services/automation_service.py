
import asyncio
from pathlib import Path

# Change this to the actual project directory on your machine.
PROJECT_ROOT = Path(__file__).resolve().parents[2]


async def run_validation() -> dict:
    """
    Run an allowlisted validation command for the backend.
    This example checks Python syntax without executing the app.
    """

    main_file = PROJECT_ROOT / "main.py"

    if not main_file.is_file():
        return {
            "status": "failed",
            "message": f"Expected file not found: {main_file}",
        }

    process = await asyncio.create_subprocess_exec(
        "python",
        "-m",
        "py_compile",
        str(main_file),
        cwd=str(PROJECT_ROOT),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    try:
        stdout, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=30,
        )
    except asyncio.TimeoutError:
        process.kill()
        await process.wait()
        return {
            "status": "failed",
            "message": "Validation timed out",
        }

    return {
        "status": "success" if process.returncode == 0 else "failed",
        "return_code": process.returncode,
        "stdout": stdout.decode(errors="replace")[-3000:],
        "stderr": stderr.decode(errors="replace")[-3000:],
    }
