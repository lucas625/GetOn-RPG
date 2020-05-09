<template>
  <v-card>
    <v-card-title>
      {{ title }}
    </v-card-title>
  </v-card>
</template>

<script>
export default {
  name: 'GetBasePageHeader',
  props: {
    title: {
      required: true,
      type: String
    }
  }
}
</script>
