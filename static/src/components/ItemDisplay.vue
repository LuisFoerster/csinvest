<script setup>
  import { ref } from 'vue'
  const { caseName, skinName, year, dropPool, lowestPrice } = defineProps([
    'icon_url','caseName', 'skinName', 'year', 'dropPool', 'lowestPrice'
  ]);

  const buyButtonContent = ref(lowestPrice);
  function handleMouseEnter() {
      buyButtonContent.value = "BUY NOW";
  };
  function handleMouseLeave() {
      buyButtonContent.value = "$" + lowestPrice;
  }

</script>

<template>
    <div class="flex justify-center">
  <div class="shadow-2xl rounded-3xl pr-4 pl-0 w-[1200px] mb-6 flex items-center justify-between mx-4 md:mr-8 bg-white">
    <!-- Linkes Element -->
    <div class="flex items-center">
      <div class="w-40 h-40 md:w-56 md:h-56">
        <a href="#">
        <!-- Image Loading from Server -->
        <img :src="'https://community.akamai.steamstatic.com/economy/image/'+icon_url" alt="Loading_Error">
<!--         Placeholder
        <img src="https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXU5A1PIYQNqhpOSV-fRPasw8rsRVx4MwFo5_T3eAQ3i6DMIW0X7ojiwoHax6egMOKGxj4G68Nz3-jCp4itjFWx-ktqfSmtcwqVx6sT/360fx360f">-->
        </a>
      </div>

      <div>
        <!-- Mittleres Element -->
        <div>
          <h4>{{ caseName }}</h4>
          <a href="#">
            <h2>{{ skinName }}</h2>
          </a>
          <h3>{{ year }}</h3>
          <h3>{{ dropPool }}</h3>
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
          <button @mouseenter="handleMouseEnter()" @mouseleave="handleMouseLeave" class="w-[160px] bg-[#27233A] text-white text-lg rounded-3xl py-2 px-8 whitespace-nowrap border-2 border-[#27233A] hover:bg-white hover:text-[#27233A] active:bg-gray-300 button-buy-transition">{{ buyButtonContent }}</button>

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




