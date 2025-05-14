<template>
  <div>
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">Sobre</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
nav {
  padding: 1rem;
  background: #eee;
}
</style>
