<script setup>
import filterCheckbox from "./filterCheckbox.vue";
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
    <div class="m-4 lg:ml-6 mb-6 max-w-[130px]">
      <filter-checkbox attribute-name="Prime"></filter-checkbox>
      <filter-checkbox attribute-name="Rare"></filter-checkbox>
      <filter-checkbox attribute-name="Discountinued"></filter-checkbox>
    </div>
</div>
</template>

<style scoped>

</style>