<script setup>
import footerCategory from "./footerCategory.vue";
</script>

<template>
<div class="bg-[#27233A]">
  <div class="w-full md:flex md:justify-between max-w-4xl mx-auto px-8">
    <!-- Bei kleinen Bildschirmgrößen (sm) die Elemente untereinander und mittig anordnen -->
    <div class="flex flex-col items-center md:flex-row justify-center md:justify-between w-full">
      <footer-category class="mt-10 md:my-16"></footer-category>
      <footer-category class="mt-10 md:my-16"></footer-category>
      <footer-category class="mt-10 mb-10 md:my-16"></footer-category>
    </div>
  </div>
</div>

</template>

<style scoped>

</style>