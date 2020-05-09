<template>
  <v-app id="app">
    <get-navbar />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import GetNavbar from '@/components/get-navbar'

export default {
  name: 'App',
  components: { GetNavbar }
}
</script>
