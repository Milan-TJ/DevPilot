<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <Navbar />

    <main class="flex-1">
    <!-- <notifications></notifications> -->
    <router-view :key="$route.fullPath"></router-view>
    </main>

    <Footer />
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Inter, system-ui, sans-serif;
  background: #f4f6fa;
  color: #182230;
}

.dashboard {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 24px;
}

.eyebrow {
  font-size: 12px;
  letter-spacing: 2px;
  color: #596579;
}

header h1 {
  margin-bottom: 8px;
}

.summary,
.panel,
.project-card {
  background: white;
  padding: 20px;
  margin: 20px 0;
  border: 1px solid #e2e6ed;
  border-radius: 12px;
}

.summary h2 {
  font-size: 32px;
  margin: 8px 0 0;
}

form {
  display: grid;
  gap: 12px;
}

input,
button {
  padding: 12px;
  border-radius: 8px;
  font: inherit;
}

input {
  border: 1px solid #cbd2de;
}

button {
  border: 0;
  background: #253b80;
  color: white;
  cursor: pointer;
}

.project-card p {
  color: #596579;
}

.project-card span {
  font-size: 13px;
}
</style>
