<script setup>
import {ref} from 'vue';

const showMenu = ref(true);
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
};

</script>

<template>
    <!-- navbar goes here -->
    <nav class="bg-[#1B6D68] fixed top-0 w-full shadow-xl">
        <div class="max-w-6xl px-6 py-2 mx-auto">
            <div class="flex justify-between items-center py-1">
    <!-- Logo -->
                <div>
                    <h1>csInvest.app</h1>
                </div>
    <!-- Searchbar-->
                <div>
                    <input class="hidden md:flex h-[30px] w-[350px] rounded-[100px] bg-white shadow-md py-3 px-4 font-light text-sm focus:outline-none" type="search" placeholder="search for items...">
                </div>
    <!-- Nav Links-->
                <div class="space-x-6 hidden lg:flex">
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Portfolio</a>
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Shop</a>
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Profile</a>
                </div>
    <!-- Login-->
                <div>
                    <button class="hidden md:flex rounded-[100px] bg-white border-2 border-white px-4 py-1 text-xl text-gray-700 hover:border-white hover:border-2 hover:text-white hover:bg-[#1B6D68] active:bg-gray-500 btn-transition">LOGIN</button>
                </div>
    <!-- search Menu Toggle Switch -->
                <div class="md:hidden flex items-center ml-auto mr-1">
                    <button @click="toggleSearch">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-7 h-7">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                      </svg>
                    </button>
                </div>
    <!-- mobile Menu Toggle Switch -->
                <div class="md:hidden flex items-center">
                    <button @click="toggleMenu">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-10 h-10">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                        </svg>
                    </button>
                </div>
            </div>
            <div class="hidden md:flex lg:hidden space-x-6 justify-between items-center px-64">
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Portfolio</a>
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Shop</a>
                    <a href="#" class="text-xl text-white hover:text-gray-400 active:text-gray-500 menuItem-transition">Profile</a>
                </div>
        </div>
    <!-- mobile menu-->
        <div class="md:hidden" v-if="showMenu">
            <a href="#" class="block py-2 px-4 text-sm text-white hover:bg-gray-300 btn-transition">Portfolio</a>
            <a href="#" class="block py-2 px-4 text-sm text-white hover:bg-gray-300 btn-transition">Shop</a>
            <a href="#" class="block py-2 px-4 text-sm text-white hover:bg-gray-300 btn-transition">Profile</a>
        </div>
    <!-- Search Bar -->
        <div class="md:hidden" v-if="showSearch">
          <input class="flex mx-auto my-4 h-[30px] w-[350px] rounded-[100px] bg-white shadow-md py-3 px-4 font-light text-sm focus:outline-none" type="search" placeholder="search for items...">
        </div>
    </nav>

</template>



<style scoped>
.menuItem-transition {
    transition-property: color, font-size;
    transition-duration: 0.1s;
}
  .btn-transition {
    transition-property: background-color;
    transition-duration: 0.15s;
  }

.transition-max-h {
  max-height: 0;
  transition-property: max-height;
}
</style>
