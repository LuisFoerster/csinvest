<script setup>

  import {inject} from "vue";
  import { ref } from "vue";

  const { icon_url, market_hash_name, lowest_price} = defineProps([
    'icon_url','market_hash_name', 'lowest_price'
  ]);
  //Buy Button Content Change
  const buyButtonContent = ref("$"+lowest_price);
  function handleMouseEnter() {
      buyButtonContent.value = "BUY NOW";
  };
  function handleMouseLeave() {
      buyButtonContent.value = "$" + lowest_price;
  }

</script>

<template>
    <div class="flex ">
  <div class="shadow-2xl rounded-3xl pr-4 pl-0 w-[1200px] mb-6 flex items-center justify-between mx-4 md:mr-8">
    <!-- Linkes Element -->
    <div class="flex">
      <div class="md:w-56 md:h-56 mt-6">
        <a href="#">
        <img class="" :src="'https://community.akamai.steamstatic.com/economy/image/'+icon_url" alt="Loading_Error">
        </a>
      </div>

      <div class="flex items-center ml-6">
        <!-- Mittleres Element -->
        <div>
          <h3 class="font-bold ">{{ market_hash_name }}</h3>
          <h3>${{ lowest_price }}</h3>
        </div>
      </div>

    </div>
    <!-- Rechtes Element -->
    <div class="flex items-center lg:space-x-32">
      <div class="hidden lg:flex flex-col">
        <h3>popularity</h3>
        <h3>invest value</h3>
        <h3>ranking</h3>
      </div>
      <!-- Button -->
      <div class="">
          <Button @mouseenter="handleMouseEnter()" @mouseleave="handleMouseLeave" class="w-[160px] bg-[#1B6D68] text-white text-lg rounded-3xl py-2 px-8 whitespace-nowrap border-2 border-[#1B6D68] hover:bg-white hover:text-[#1B6D68] active:bg-gray-300 button-buy-transition">{{ buyButtonContent }}</Button>
      </div>
    </div>
  </div>
</div>

</template>



<style scoped>
  .button-buy-transition {
      transition-property: background-color;
      transition-duration: 0.15s;
  }
</style>
