<script setup>
import NavBar from "./components/NavBar.vue";
import ItemDisplay from "./components/ItemDisplay.vue";
import Filter from "./components/filter.vue";
import Footer from "./components/Footer.vue";

</script>

<template>
    <NavBar></NavBar>
    <div class="flex max-w-6xl mx-auto py-2 mt-24 lg:mt-20">
        <!-- Filter -->
        <div class="md:w-1/4">
            <Filter></Filter>
        </div>
        <div class="w-full md:w-3/4">
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
            <ItemDisplay></ItemDisplay>
        </div>
    </div>
    <Footer></Footer>
</template>



<style scoped>

</style>
