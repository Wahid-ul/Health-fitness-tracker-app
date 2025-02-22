<template>
    <div>
      <h1>Welcome to Health & Fitness Tracker</h1>
      <p>Your personalized health and fitness journey starts here!</p>
      <form @submit.prevent="getPrediction">
        <label>Age:</label>
        <input type="number" v-model="form.age" required />

        <label>Gender:</label>
        <select v-model="form.gender">
          <option>male</option>
          <option>female</option>
        </select>

        <label>Weight (kg):</label>
        <input type="number" v-model="form.weight" required />

        <label>Height (cm):</label>
        <input type="number" v-model="form.height" required />

        <label>Exercise:</label>
        <input type="text" v-model="form.exercise" required />

        <label>Duration (minutes):</label>
        <input type="number" v-model="form.duration" required />

        <label>Calories Burned:</label>
        <input type="number" v-model="form.calories_burned" required />

        <label>Sleep Hours:</label>
        <input type="number" v-model="form.sleep_hours" required />

        <label>Stress Level:</label>
        <select v-model="form.stress_level">
          <option>low</option>
          <option>moderate</option>
          <option>high</option>
        </select>

        <button type="submit">Get Prediction</button>
      </form>
      <div v-if="prediction">
        <h3>AI Prediction:</h3>
        <p>{{ prediction }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  export default {
    name: 'Home',
    data(){
      return{
        form: {
          age: "",
          gender: "male",
          weight: "",
          height: "",
          exercise: "",
          duration: "",
          calories_burned: "",
          sleep_hours: "",
          stress_level: "moderate"
        },
        predict:null,
      };
    },
    methods:{
      async getPrediction(){
        try{
          // Retrieve JWT token from local storage (stored after login)
          const token=localStorage.getItem("access_token");
          // Send a request to Flask API with JWT authorization
          const response=await axios.post(
            "http://localhost:5000/api/predict",
            { user_input: this.inputData },
            {
              headers:{
                Authorization:`Bearer ${token}`,
                "Content-Type":"application/json",
              },
            }
          )
        } catch(error){
          console.error("Error fetching prediction:",error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  h1 {
    color: #333;
  }
  input {
  padding: 8px;
  margin: 10px 0;
  width: 100%;
}
button {
  padding: 8px;
  background: #333;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background: #555;
}
  </style>
  