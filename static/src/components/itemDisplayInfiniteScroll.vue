<script setup>
import ItemDisplay from "./ItemDisplay.vue";
import { ref, onMounted, onUnmounted} from "vue";
import {useShopItemStore} from "../store/shopItemStore.js";
import {storeToRefs} from "pinia";
const {loadItems} = useShopItemStore()
const {items} = storeToRefs(useShopItemStore());
const handleScroll = () => {
    const { scrollHeight, scrollTop, clientHeight } = document.documentElement;
    if(scrollTop + clientHeight >= scrollHeight - 600) {
        loadItems();
    }
}

onMounted(() => {
    loadItems(null);
    window.addEventListener('scroll', handleScroll);

});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll)
})

</script>

<template>
    <ul>
        <ItemDisplay v-for="item in items" :key="item.id" :case-name="item.market_hash_name" :lowest-price="item.vendor_offers[0].lowest_price" :icon_url="item.icon_url"></ItemDisplay>
    </ul>
</template>

<style scoped>

</style>