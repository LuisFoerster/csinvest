<script setup>
import NavBar from "./components/NavBar.vue";
import ItemDisplay from "./components/ItemDisplay.vue";
import Filter from "./components/filter.vue";
import Footer from "./components/Footer.vue";
import {DefaultService} from "./client";
import {onMounted, ref} from "vue";


const items = ref([]);

async function fetchItems() {
  try {
    const response = await DefaultService.searchItemsSearchGet();
    items.value = response;
  } catch (error) {
    console.error("Error fetching items:", error);
  }
}

onMounted(() => {
  fetchItems();
});
</script>

<template>
    <NavBar></NavBar>
    <div class="flex max-w-6xl mx-auto py-2 mt-24 lg:mt-20">
        <!-- Filter -->
        <div class="md:w-1/4">
            <Filter></Filter>
        </div>
        <div class="w-full md:w-3/4">
            <ItemDisplay v-for="item in items" v-bind="item"></ItemDisplay>
        </div>
    </div>
    <Footer></Footer>
</template>



<style scoped>

</style>
