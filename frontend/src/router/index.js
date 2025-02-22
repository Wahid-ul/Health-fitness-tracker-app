import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import ProfilePage from '../views/ProfilePage.vue';
import Register from '../views/RegisterPage.vue';
import Login from '../views/LoginPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/profile', component: ProfilePage },
  { path: '/register', component: Register },
  {path:'/login',component:Login}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
