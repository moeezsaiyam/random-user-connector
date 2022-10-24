<template>
  <div>
    <h2>Random User Connector</h2>
    <list-users></list-users>

  </div>
</template>

<script>
import ListUsers from './components/ListUsers.vue'

export default {
  name: 'App',
  components: {
    ListUsers
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
