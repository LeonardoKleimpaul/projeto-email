<template>
  <div>
    <h1 class="text-3xl font-bold underline text-red-500">
    Hello worlad!
  </h1>
    <p>{{ msg }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const msg = ref('Carregando...');

onMounted(() => {
  axios.get('http://127.0.0.1:5000/api/email/hello')
    .then(res => {
      msg.value = res.data.msg;
    })
    .catch(err => {
      msg.value = 'Erro ao conectar com a API';
      console.error(err);
    })
})
</script>
