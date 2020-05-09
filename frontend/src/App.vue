<template>
  <v-app id="app">
    <get-navbar title="GetOn-RPG" />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import GetNavbar from '@/components/get-the-navbar'
export default {
  name: 'App',
  components: { GetNavbar }
}
</script>
