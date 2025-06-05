<template>
  <div class="max-w-xl mx-auto mt-10 p-6 bg-white rounded-xl shadow-md">
    <h1 class="text-2xl font-bold text-gray-800 mb-2">Envio de E-mail</h1>
    <p class="text-gray-600 mb-6">Preencha os campos abaixo para enviar um e-mail.</p>

    <form @submit.prevent="handleSubmit" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Para</label>
        <input v-model="to" type="email" required class="w-full border border-gray-300 rounded-md p-2" />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Assunto</label>
        <input v-model="subject" type="text" required class="w-full border border-gray-300 rounded-md p-2" />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Mensagem</label>
        <textarea v-model="message" rows="5" required class="w-full border border-gray-300 rounded-md p-2"></textarea>
      </div>

      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Enviar
      </button>

      <div v-if="successMessage" class="mt-4 text-green-600">{{ successMessage }}</div>
      <div v-if="errorMessage" class="mt-4 text-red-600">{{ errorMessage }}</div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const to = ref('')
const subject = ref('')
const message = ref('')
const successMessage = ref('')
const errorMessage = ref('')

const handleSubmit = async () => {
  successMessage.value = ''
  errorMessage.value = ''

  try {
    const response = await axios.post('http://127.0.0.1:5000/api/email/new', {
      to: to.value,
      subject: subject.value,
      message: message.value
    })

    successMessage.value = 'E-mail enviado com sucesso!'
    // Limpa os campos
    to.value = ''
    subject.value = ''
    message.value = ''
  } catch (error) {
    errorMessage.value = 'Erro ao enviar o e-mail.'
    console.error(error)
  }
}
</script>
