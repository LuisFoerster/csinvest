<script setup>
import filterSectionDroppools from "./filterSectionDroppools.vue";
import filterSectionPrice from "./filterSectionPrice.vue";
import filterSectionReleaseYear from "./filterSectionReleaseYear.vue";
</script>

<template>
  <div class="sticky top-20 hidden md:flex md:flex-col ml-8">
  <filter-section-droppools filter-section-name="Droppool"></filter-section-droppools>
  <filter-section-price filter-section-name="Price"></filter-section-price>
  <filter-section-release-year filter-section-name="Release Year"></filter-section-release-year>
  </div>
</template>

<style scoped>

</style>