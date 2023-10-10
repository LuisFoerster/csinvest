import {defineStore} from 'pinia'
import {computed, reactive, ref} from 'vue'
import {DefaultService} from "../client/index.ts";
export const useShopFilterValueStore = defineStore('shopFilterValueStore', () => {
    const filterValue = ref({

        //types
        typePistol              : {category: "Type",        value: "Pistol",         checked: false,     toggle: function () {this.checked = !this.checked}},
        typeSMG                 : {category: "Type",        value: "SMG",            checked: false,     toggle: function () {this.checked = !this.checked}},
        typeRifle               : {category: "Type",        value: "Rifle",          checked: false,     toggle: function () {this.checked = !this.checked}},
        typeSniperRifle         : {category: "Type",        value: "Sniper Rifle",   checked: false,     toggle: function () {this.checked = !this.checked}},
        typeShotgun             : {category: "Type",        value: "Shotgun",        checked: false,     toggle: function () {this.checked = !this.checked}},
        typeMachinegun          : {category: "Type",        value: "Machinegun",     checked: false,     toggle: function () {this.checked = !this.checked}},
        typeContainer           : {category: "Type",        value: "Container",      checked: false,     toggle: function () {this.checked = !this.checked}},
        typeAgent               : {category: "Type",        value: "Agent",          checked: false,     toggle: function () {this.checked = !this.checked}},
        typeKnife               : {category: "Type",        value: "Knife",          checked: false,     toggle: function () {this.checked = !this.checked}},
        typeSticker             : {category: "Type",        value: "Sticker",        checked: false,     toggle: function () {this.checked = !this.checked}},
        typeGloves              : {category: "Type",        value: "Gloves",         checked: false,     toggle: function () {this.checked = !this.checked}},
        typeGraffiti            : {category: "Type",        value: "Graffiti",       checked: false,     toggle: function () {this.checked = !this.checked}},
        typeMusicKit            : {category: "Type",        value: "Music Kit",      checked: false,     toggle: function () {this.checked = !this.checked}},
        typePatch               : {category: "Type",        value: "Patch",          checked: false,     toggle: function () {this.checked = !this.checked}},
        typeCollectible         : {category: "Type",        value: "Collectible",    checked: false,     toggle: function () {this.checked = !this.checked}},
        typeKey                 : {category: "Type",        value: "Key",            checked: false,     toggle: function () {this.checked = !this.checked}},
        typePass                : {category: "Type",        value: "Pass",           checked: false,     toggle: function () {this.checked = !this.checked}},
        typeGift                : {category: "Type",        value: "Gift",           checked: false,     toggle: function () {this.checked = !this.checked}},
        typeTag                 : {category: "Type",        value: "Tag",            checked: false,     toggle: function () {this.checked = !this.checked}},

        //exterior
        exteriorFactoryNew      : {category: "Exterior",    value: "Factory New",    checked: false,     toggle: function () {this.checked = !this.checked}},
        exteriorMinimalWear     : {category: "Exterior",    value: "Minimal Wear",   checked: false,     toggle: function () {this.checked = !this.checked}},
        exteriorFieldTested     : {category: "Exterior",    value: "Field-Tested",   checked: false,     toggle: function () {this.checked = !this.checked}},
        exteriorWellWorn        : {category: "Exterior",    value: "Well-Worn",      checked: false,     toggle: function () {this.checked = !this.checked}},
        exteriorBattleScared    : {category: "Exterior",    value: "Battle-Scared",  checked: false,     toggle: function () {this.checked = !this.checked}},

        //category
        categoryNormal          : {category: "Category",    value: "Normal",         checked: false,     toggle: function () {this.checked = !this.checked}},
        categorySouvenir        : {category: "Category",    value: "Souvenir",       checked: false,     toggle: function () {this.checked = !this.checked}},
        categoryStatTrak        : {category: "Category",    value: "StatTrak™",      checked: false,     toggle: function () {this.checked = !this.checked}},
        categoryStar            : {category: "Category",    value: "★",              checked: false,     toggle: function () {this.checked = !this.checked}},
        categoryStarStatTrakStar: {category: "Category",    value: "★ StatTrak™",    checked: false,     toggle: function () {this.checked = !this.checked}},

        //quality
        qualityConsumerGrade    : {category: "Quality",     value: "Consumer Grade",  checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityMilSpecGrade     : {category: "Quality",     value: "Mil-Spec Grade",  checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityIndustrialGrade  : {category: "Quality",     value: "Industrial Grade",checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityRestricted       : {category: "Quality",     value: "Restricted",      checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityClassified       : {category: "Quality",     value: "Classified",      checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityCovert           : {category: "Quality",     value: "Covert",          checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityBaseGrade        : {category: "Quality",     value: "Base Grade",      checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityExtraordinary    : {category: "Quality",     value: "Extraordinary",   checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityDistinguished    : {category: "Quality",     value: "Distinguished",   checked: false,     toggle: function () {this.checked = !this.checked}},
        qualitySuperior         : {category: "Quality",     value: "Superior",        checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityMaster           : {category: "Quality",     value: "Master",          checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityExceptional      : {category: "Quality",     value: "Exceptional",     checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityHighGrade        : {category: "Quality",     value: "High Grade",      checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityRemarkable       : {category: "Quality",     value: "Remarkable",      checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityExotic           : {category: "Quality",     value: "Exotic",          checked: false,     toggle: function () {this.checked = !this.checked}},
        qualityContraband       : {category: "Quality",     value: "Contraband",      checked: false,     toggle: function () {this.checked = !this.checked}},



    });
    const categories = ref({})
    function getCategories() {
      const categorySet = new Set();

      for (const key in filterValue.value) {
        if (Object.prototype.hasOwnProperty.call(filterValue.value, key)) {
          const category = filterValue.value[key].category;
          categorySet.add(category);
        }
      }
      for (const c of categorySet){
          categories.value[c] = {
            checked: false,
            toggle: function () {
                    this.checked = !this.checked;
            },
          };
      }
    }
    function getTypeAssocToCategory(Category) {
        const result = {}
        for (const key in filterValue.value) {
            if (filterValue.value[key].category === Category){
                result[key] = filterValue.value[key]
            }
        }
        return result
    }
    function toggleCategory(category){
        for (const key in categories.value){
            if(key !== category){
                categories.value[key].checked = false;
            }
        }
        categories.value[category].checked = !categories.value[category].checked;
    }
    function getCheckedFilters(){
        const filters = {};
        for (const category in categories.value){
            filters[category] = [];
        }
        for (const key in filterValue.value){
            const entry = filterValue.value[key]
            if (entry.checked){
                filters[entry.category].push(entry.value);
            }
        }
        return filters;
    }

    const count = ref();
    async function fetchCount(){
        if(!count.value){
            count.value = 0;
        }
        const filterStore = ref(getCheckedFilters());
        //API Request
        try{
            const response = await DefaultService.getItemShopGet(
                null,
                null,
                null,
                filterStore ? filterStore.value.Type : null,
                filterStore ? filterStore.value.Exterior : null,
                filterStore ? filterStore.value.Quality : null,
                filterStore ? filterStore.value.Category : null,
                null,
                null,
                null,
                null,
                null,
                null,
                true
            );
            count.value = response.item_count;
            console.log(count.value);
        }   catch(error) {
            console.error(error);
        }
    }


    //reset function
    function reset()
    {
        for(const key in filterValue.value)
        {
            if(Object.hasOwnProperty.call(filterValue.value, key))
            {
                filterValue.value[key].checked = false;
            }
        }
    }


    return{ filterValue, reset, getCategories, getTypeAssocToCategory, categories, toggleCategory, getFilterFetch: getCheckedFilters, fetchCount, count }
})

