import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/index.js";
import {OpenAPI} from "./client";

OpenAPI.BASE = 'http://127.0.0.1:8000'

createApp(App)
    .use(router)
    .mount('#app')
