<template>
  <v-card>
    <v-toolbar
      color="blue accent-1"
    >
      <v-app-bar-nav-icon />

      <v-toolbar-title>GetOn-RPG</v-toolbar-title>

      <v-spacer />

      <get-router-icon
        icon-name="mdi-home"
        url="/"
      />

      <get-router-icon
        icon-name="mdi-account-circle"
        url="/sign-in"
      />
    </v-toolbar>
  </v-card>
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
