<script setup>
import filterValueInput from "./filterValueIput.vue";
import {defineProps, watch} from "vue";

const { filterSectionName } = defineProps(['filterSectionName']);
</script>

<template>
<div class="shadow-lg rounded-3xl flex flex-col max-w-[350px]">
    <!-- Filter Name -->
    <div class="m-4 lg:m-6">
        <h2>{{filterSectionName}}</h2>
    </div>
    <!-- Filter Inputs -->
    <div class="m-4 lg:ml-6 mb-8 max-w-[130px] flex flex-col ">
      <filter-value-input form-name="from" ></filter-value-input>
      <filter-value-input form-name="to" ></filter-value-input>
    </div>
</div>
</template>

<style scoped>

</style>