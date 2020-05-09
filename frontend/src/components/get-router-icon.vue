<template>
  <v-btn
    icon
    :to="url"
  >
    <v-icon>{{ iconName }}</v-icon>
  </v-btn>
</template>

<script>
export default {
  name: 'GetRouterIcon',
  props: {
    iconName: {
      type: String,
      required: true
    },
    url: {
      type: String,
      required: true
    }
  }
}
</script>
