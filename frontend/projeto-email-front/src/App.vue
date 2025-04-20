<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'

const msg = ref('')

onMounted(() => {
  axios.get('http://127.0.0.1:5000/api/hello')
    .then(res => {
      msg.value = res.data.message
    })
    .catch(err => {
      msg.value = 'Erro ao conectar com a API'
      console.error(err)
    })
})
</script>

<template>
  <h1>{{ msg }}</h1>
</template>
