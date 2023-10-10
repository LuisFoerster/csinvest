<script setup>
import {onMounted, ref} from "vue";
import {useShopFilterValueStore} from "../store/shopFilterValue.js"
import {useShopItemStore} from "../store/shopItemStore.js";
import SortIcon from "./icons/sortIcon.vue";
import FilterIcon from "./icons/filterIcon.vue";
import PlusIcon from "./icons/plusIcon.vue";
import {storeToRefs} from "pinia";
import CheckIcon from "./icons/checkIcon.vue";


//stores import
const {filterValue, categories, getCategories, getTypeAssocToCategory, getFilterFetch, toggleCategory, fetchCount} = useShopFilterValueStore();
const {count} = storeToRefs(useShopFilterValueStore());
const {loadItems, clearItems} = useShopItemStore();


const filterMenu = ref({
    show: false, toggle: function () {
        if (sortMenu.value.show) sortMenu.value.show = false;
        this.show = !this.show ^ sortMenu.value.show
    }
});
const sortMenu = ref({
    show: false, toggle: function () {
        if (filterMenu.value.show) filterMenu.value.show = false;
        this.show = !this.show
    }
});



onMounted(()=>{ getCategories()})

</script>

<template>
    <div class="w-full mt-12 bg-[#27233A] rounded-b-xl px-[8px] pt-[28px] pb-[16px] sticky top-0">


        <div id="filterHead"
             :class="filterMenu.show || sortMenu.show ? 'border-b-[1px] border-b-white' : ''"
             class="flex justify-between pb-[6px]">
            <!-- PageName -->
            <div class="navigationItem">Shop</div>
            <!-- Icon Buttons -->
            <div class="flex items-center">
                <button
                    @click="sortMenu.toggle()"
                >
                    <sort-icon></sort-icon>
                </button>
                <button
                    @click="filterMenu.toggle()"
                >
                   <filter-icon></filter-icon>
                </button>
            </div>
        </div>


        <div v-show="filterMenu.show">
            <div
                v-for="(value, category) in categories"
                class="flex py-[8px] border-b-[1px] border-white flex-col"
            >
                <button
                    class="flex items-center"
                    @click="toggleCategory(category)"
                >
                    <!--plus/minus Icon-->
                    <plus-icon></plus-icon>
                    <!--Filter category name-->
                    <p class="navigationItem">{{ category }}</p>
                </button>

                <!--Filter options-->
                <div v-show="value.checked" class="mt-[8px]">
                    <template v-for="(filterVal) in getTypeAssocToCategory(category)">
                        <button
                                :class="filterVal.checked ? 'shopFilterValueButtonActive' : 'shopFilterValueButton'"
                                class="buttonText"
                                @click="filterVal.toggle(); fetchCount()">
                            {{ filterVal.value }}
                        </button>
                    </template>
                </div>


            </div>
            <div class="flex items-center justify-center mt-[16px]">
                <button
                    @click="clearItems();loadItems(getFilterFetch(), null)"
                    class="flex text-[20px] px-[22px] items-center rounded-[10px] border-[2px] space-x-[4px]"
                    :class="count == null ? 'border-gray-700 text-gray-700' : 'buttonText'"
                    :disabled="count == null"
                >
                    <check-icon></check-icon>
                    <div class="text-[20px]">
                        {{ count }} results
                    </div>
                </button>
            </div>
        </div>
        <div v-show="sortMenu.show">
            <div>Placeholder</div>
        </div>
    </div>

</template>

<style scoped>

.shopFilterValueButton {
    border: 1px solid white;
    border-radius: 10px;
    padding: 1px 8px 1px 8px;
    margin: 4px;
}

.shopFilterValueButtonActive {
    border: 1px solid #39A0ED;
    border-radius: 10px;
    padding: 1px 8px 1px 8px;
    margin: 4px;
    color: #39A0ED;
}

</style>