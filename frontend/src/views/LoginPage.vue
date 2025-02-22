<template>
    <div class="login-container">
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: "Login",
    data() {
      return {
        email: "",
        password: "",
        message: "",
      };
    },
    methods: {
      async loginUser() {
        try {
          const response = await axios.post("http://localhost:5000/auth/login", {
            email: this.email,
            password: this.password,
          });
  
          const token = response.data.access_token;
          localStorage.setItem("token", token); // ✅ Store JWT token
          this.message = "Login successful!";
          
          this.$router.push("/"); // ✅ Redirect to HomePage.vue
        } catch (error) {
          this.message = error.response?.data?.error || "Login failed.";
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .login-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 10px;
  }
  button {
    background-color: #333;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background-color: #555;
  }
  </style>
  