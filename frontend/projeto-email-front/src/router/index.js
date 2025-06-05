import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import ListarEmails from '../pages/modelos/listar.vue'
import CriarEmails from '../pages/modelos/criar.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/email/index', component: ListarEmails },
  { path: '/email/new', component: CriarEmails }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
