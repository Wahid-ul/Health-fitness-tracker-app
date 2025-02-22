<template>
    <div>
      <h1>User Profile</h1>
      <p v-if="user">Name: {{ user.name }}</p>
      <p v-if="user">Email: {{ user.email }}</p>
      <p v-else>Loading...</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Profile',
    data() {
      return {
        user: null,
      };
    },
    created() {
      axios.get('http://localhost:5000/api/user')
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          console.error('There was an error fetching user data!', error);
        });
    },
  };
  </script>
  
  <style scoped>
  h1 {
    color: #333;
  }
  </style>
  