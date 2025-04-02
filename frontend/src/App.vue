<template>
  <div id="app">
    <AgenciasTable />
  </div>
</template>

<script>
import AgenciasTable from "./components/AgenciasTable.vue";

export default {
  components: {
    AgenciasTable,
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
}
</style>