<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getHealth } from '@/api/health'

const status = ref<string>('loading...')
const error = ref<string | null>(null)

onMounted(async () => {
  try {
    const data = await getHealth()
    status.value = data.status_app
  } catch (e) {
    error.value = e instanceof Error ? e.message : 'Unknown error'
  }
})
</script>

<template>
  <div>
    <h1>Jaba 🐸</h1>
    <p v-if="error">Backend error: {{ error }}</p>
    <p v-else>Backend status: {{ status }}</p>
  </div>
</template>

<style scoped></style>
