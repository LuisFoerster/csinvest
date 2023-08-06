<script setup>
import {ref, defineProps} from "vue";

//attributeName Property definition
const { attributeName } = defineProps(['attributeName']);

//isChecked = true --> filter is selected
const isChecked = ref(false);
const toggleChecked = () => {
    isChecked.value = !isChecked.value;
}

</script>

<template>
<label class="flex inline items-center">
    <input
    type="checkbox"
    class="text-blue-600"
    v-model="isChecked"
    @click="toggleChecked"
    >
    <span class="ml-2">{{attributeName}}</span>
</label>
</template>

<style scoped>

</style>