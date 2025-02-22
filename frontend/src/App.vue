<template>
  <div id="app">
    <NavBar />
    <router-view></router-view>
    <FooterPage />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';
import FooterPage from './components/FooterPage.vue';

export default {
  components: {
    NavBar,
    FooterPage
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
}
</style>
