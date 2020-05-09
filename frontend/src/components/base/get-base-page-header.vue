<template>
  <div>
    <v-card>
      <v-card-title>
        {{ title }}
      </v-card-title>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'GetPageHeader',
  props: {
    title: {
      required: true,
      type: String
    }
  }
}
</script>
