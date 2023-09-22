<script setup>
import NavBar from "./components/NavBar.vue";
import ItemDisplay from "./components/ItemDisplay.vue";
import Filter from "./components/filter.vue";
import Footer from "./components/Footer.vue";
import {DefaultService} from "./client";
import {onMounted, provide, ref, watch} from "vue";


const items = ref([]);
const search_string = ref("")
const min_price = ref()
const max_price = ref()
provide("search_string", search_string)
provide("max_price", max_price)
provide("min_price", min_price)

async function fetchItems(q = "") {
  try {
    let response = []
    items.value = []
    if (q != "") {
      response = await DefaultService.searchItemsSearchGet(q);
    }
    else{
      response = await DefaultService.searchItemsSearchGet();
    }
    items.value = response;
  } catch (error) {
    console.error("Error fetching items:", error);
  }
}

watch(search_string, () => {
    fetchItems(search_string.value)
    console.log("changed")
    }
)

watch(max_price, ()=>{
  console.log(max_price.value)
})



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
