<script setup>
import { defineProps} from "vue";

const { filterSectionName } = defineProps(['filterSectionName']);

</script>

<template>
<div class="shadow-lg rounded-3xl flex flex-col max-w-[350px]">
    <!-- Filter Name -->
    <div class="m-4 lg:m-6">
        <h2>{{filterSectionName}}</h2>
    </div>
    <!-- Filter Inputs -->
    <div class="m-4 lg:ml-6 mb-8 max-w-[130px]">
      <div class="whitespace-nowrap rounded-3xl shadow-lg px-2 my-2">
        <label class="flex items-center">
          <span class="m-2">from</span>
          <input type="text" class="focus:outline-none w-12" placeholder="YYYY">
          <span class="ml-auto"></span>
        </label>
      </div>
      <div class="whitespace-nowrap rounded-3xl shadow-lg px-2 my-2">
        <label class="flex items-center">
          <span class="m-2">to</span>
          <input type="text" class="focus:outline-none w-12 ml-auto" placeholder="YYYY">
          <span class="ml-auto"></span>
      </label>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>