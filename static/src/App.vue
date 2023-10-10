<script setup>
//import of Components
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
import ItemDisplayInfiniteScroll from "./components/itemDisplayInfiniteScroll.vue";
import FilterShop from "./components/filterShop.vue";

//import of functions
import {onMounted, onUnmounted, ref} from "vue";
//definition of refs
const items = ref([]);



onMounted(() => {});

onUnmounted(() => {});


</script>
<template class="">
  <NavBar></NavBar>
  <filter-shop></filter-shop>
    <div class="flex max-w-6xl mx-auto py-2 mt-24 lg:mt-20 h-screen" ref="scrollComponent" id="itemDiv" >
      <div class="w-full md:w-3/4">
        <item-display-infinite-scroll></item-display-infinite-scroll>
      </div>
    </div>
</template>

<style scoped>
</style>
