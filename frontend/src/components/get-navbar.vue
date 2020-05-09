<template>
  <v-app-bar
    app
    color="blue accent-1"
    dark
  >
    <v-toolbar-title>GetOn-RPG</v-toolbar-title>
    <v-col>
      <get-router-icon
        icon-name="mdi-home"
        url="/"
      />
    </v-col>
  </v-app-bar>
</template>

<script>
import GetRouterIcon from '@/components/get-router-icon'

export default {
  name: 'GetNavbar',
  components: {
    GetRouterIcon
  }
}
</script>
