<script setup>
import {ref} from 'vue';
import { useShopItemStore } from "../store/shopItemStore.js";
import HamburgerMenuIcon from "./icons/hamburgerMenuIcon.vue";
import SearchIcon from "./icons/searchIcon.vue";

const showMenu = ref(false);
const isRotated = ref(false);
const showSearch = ref(false);
const toggleSearch = () => {
    showSearch.value = !showSearch.value;
    if(showMenu.value == true)
    {
        showMenu.value = false;
    }
};
const toggleMenu = () => {
    showMenu.value = !showMenu.value;
    if(showSearch.value == true)
    {
        showSearch.value = false;
    }
    isRotated.value = !isRotated.value;
};

const { loadItems, clearItems } = useShopItemStore();
const searchString = ref();

function search(){
    if(searchString.value.length > 0) {
        clearItems();
        loadItems(null, searchString.value);
    }
}




</script>

<template>
    <!-- navbar goes here -->
    <nav class="bg-[#27233A] fixed top-0 w-full shadow-lg rounded-b-xl z-10">
        <div class="max-w-6xl px-[8px] py-2 mx-auto">
            <div class="flex justify-between items-center py-1">
    <!-- Logo Section -->
                <button class="flex items-center space-x-2">
        <!-- Logo Image -->
                      <img class="h-10 w-10 md:h-12 md:w-12" src="../assets/logo_.svg" alt="failed loading image">
         <!-- Logo text -->
                  <div class="flex">
                      <h1 class="text-3xl text-white">CS</h1>
                      <h1 class="text-3xl text-[#FEBC42]">INVE$T</h1>
                  </div>
                </button>
    <!-- Searchbar-->
                <div>
                    <input
                            v-model="searchString"
                            @keyup.enter="search"
                            class="hidden md:flex h-[30px] w-[350px] rounded-[100px] bg-white shadow-md py-3 px-4 font-light text-sm focus:outline-none"
                            type="search"
                            placeholder="search for items..."
                    >
                </div>

    <!-- Nav Links-->
                <div class="space-x-6 hidden lg:flex">
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Portfolio</a>
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Shop</a>
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Profile</a>
                </div>
    <!-- Login-->
                <div>
                    <button class="hidden md:flex rounded-[100px] bg-white border-2 border-white px-4 py-1 text-xl text-gray-700 hover:border-white hover:border-2 hover:text-white hover:bg-[#27233A] active:bg-gray-500 btn-transition">LOGIN</button>
                </div>
    <!-- search Menu Toggle Switch -->
                <div class="md:hidden flex items-center ml-auto">
                    <button @click="toggleSearch">
                        <search-icon></search-icon>
                    </button>
                </div>
    <!-- mobile Menu Toggle Switch -->
                <Transition>
                <div class="md:hidden flex items-center">
                    <button @click="toggleMenu">
                        <hamburger-menu-icon class="rotating-element" :class="{ 'rotateActive': isRotated }"></hamburger-menu-icon>
                    </button>
                </div>
                </Transition>
            </div>
            <div class="hidden md:flex lg:hidden space-x-6 justify-between items-center px-64">
                    <a href="#" class="text-xl text-white active:text-gray-300">Portfolio</a>
                    <a href="#" class="text-xl text-white active:text-gray-300">Shop</a>
                    <a href="#" class="text-xl text-white active:text-gray-300">Profile</a>
                </div>
        </div>
    <!-- mobile menu-->
        <div class="md:hidden flex flex-col" v-if="showMenu">
            <a href="#" class="block py-2 px-4 font-semibold text-white hover:bg-gray-300">Portfolio</a>
            <a href="#" class="block py-2 px-4 font-semibold text-white hover:bg-gray-300">Shop</a>
            <a href="#" class="block py-2 px-4 font-semibold text-white hover:bg-gray-300">Profile</a>
        </div>
    <!-- Search Bar -->
        <div class="md:hidden flex" v-if="showSearch">
          <input
                  v-model="searchString"
                  @keyup.enter="search"
                  class="flex mx-auto my-4 h-[30px] w-[350px] rounded-[100px] bg-white shadow-md py-3 px-4 font-light text-sm focus:outline-none"
                  type="search"
                  placeholder="search for items..."
          >

        </div>
    </nav>

</template>


<style scoped>

.rotating-element
{
    transition-duration: 0.6s;
}

.rotateActive
{
    rotate: 180deg;
}
</style>
