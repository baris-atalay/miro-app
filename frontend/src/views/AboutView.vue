<template>
  <div class="about">
    <h1>This is an about page</h1>
    <input v-model="template"></input>
    <button @click="createBoard">create board</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const template = ref("");

const createBoard = async () => {
  const result = await fetch("http://localhost:8000/copy-miro-board", {
    method: "PUT",
    body: JSON.stringify({item: 2}),
    headers: {
      "Content-Type": "application/json",
    }
  })
    .then(data => data.json())
    .then(data => console.log(data))
}
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
