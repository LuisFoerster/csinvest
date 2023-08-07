<script setup>

  const { caseName, skinName, year, dropPool } = defineProps([
    'icon_url','caseName', 'skinName', 'year', 'dropPool'
  ]);
</script>

<template>
    <div class="flex justify-center">
  <div class="shadow-2xl rounded-3xl pr-4 pl-0 w-[1200px] mb-6 flex items-center justify-between mx-4 md:mr-8">
    <!-- Linkes Element -->
    <div class="flex items-center">
      <div class="w-40 h-40 md:w-56 md:h-56">
        <a href="#">
        <img :src="'https://community.akamai.steamstatic.com/economy/image/'+icon_url" alt="Loading_Error">
        </a>
      </div>

      <div>
        <!-- Mittleres Element -->
        <div>
          <h3>{{ caseName }}</h3>
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
          <Button class="bg-[#1B6D68] text-white text-lg rounded-3xl py-2 px-8 whitespace-nowrap border-2 border-[#1B6D68] hover:bg-white hover:text-[#1B6D68] active:bg-gray-300 button-buy-transition">BUY NOW</Button>
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
