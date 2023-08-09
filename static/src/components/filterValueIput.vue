<script setup>
import {defineProps, inject} from "vue";

//inputFormName Property definition
const { formName } = defineProps(['formName']);

</script>

<template>
<div class="whitespace-nowrap rounded-3xl shadow-lg px-2 my-2">
  <label class="flex items-center">
    <span class="m-2">{{ formName }}</span>
    <p class="text-black">{{ inputValue }}</p>
    <input type="text" class="focus:outline-none w-12"   placeholder="xx.xx" >
    <span class="ml-auto">$</span>
  </label>
</div>
</template>

<style scoped>

</style>