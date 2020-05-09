<template>
  <v-container>
    <v-row>
      <v-col>
        <get-page-header title="Home View" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import GetPageHeader from '@/components/base/get-base-page-header'
export default {
  name: 'HomeView',
  components: { GetPageHeader }
}
</script>
