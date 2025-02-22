<template>
    <div class="register-container">
      <h2>Register</h2>
      <form @submit.prevent="registerUser">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="name" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Register</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: "Register",
    data() {
      return {
        name: "",
        email: "",
        password: "",
        message: "",
      };
    },
    methods: {
      async registerUser() {
        try {
          const response = await axios.post("http://localhost:5000/auth/register", {
            name: this.name,
            email: this.email,
            password: this.password,
          });
  
          this.message = response.data.message; // "User registered successfully"
          this.name = "";
          this.email = "";
          this.password = "";
          this.$router.push("/login"); // Redirect to login page after registration
        } catch (error) {
          this.message = error.response?.data?.error || "Registration failed.";
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .register-container {
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
  