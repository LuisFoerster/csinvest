import {defineStore} from "pinia";
import {ref} from "vue";
import {useShopFilterValueStore} from "./shopFilterValue.js";
import {DefaultService} from "../client/index.ts";
export const useShopItemStore = defineStore('shopItemStore', () => {

    const items = ref([]);
    const loading = ref(false);
    let limit = 15;
    let skip = 0;
    let filtersStore = {}
    let queryStore = ""

    async function loadItems(filters, query) {
        if(filters){
            filtersStore = filters;
        }
        filters = filtersStore;

        if(query){
            queryStore = query
        }
        query = queryStore;


        if(loading.value) return;
        loading.value = true;
        try {
            const response = await DefaultService.getItemShopGet(
                skip,
                limit,
                query,
                filters ? filters.Type : null,
                filters ? filters.Exterior : null,
                filters ? filters.Quality : null,
                filters ? filters.Category : null,
                null,
                null,
                null,
                null,
                null,
                null,
                null
            ); //API URL
            items.value = items.value.concat(response.itemsWithVendorOffers);
            skip += limit;
        }   catch(error) {
            console.error(error);
        }   finally {
            loading.value = false;
        }
    }
    function clearItems(){
        limit = 15;
        skip = 0;
        items.value = []
    }
    return{loading, loadItems, clearItems, items}
})