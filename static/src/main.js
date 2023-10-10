import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from "./router/index.js";
import {OpenAPI} from "./client";

OpenAPI.BASE = 'http://192.168.179.3:8000'


 createApp(App)
     .use(createPinia())
     .use(router)
     .mount('#app')
