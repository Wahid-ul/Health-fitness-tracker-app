use serde::{Deserialize, Serialize};
use serde_json;
use std::io::{self,Read};
use rand::seq::SliceRandom;
use rand::thread_rng;

#[derive(Debug,Deserialize)]
struct Workout{
    exercise_type:String,
    duration:u32,//in minutes
}

fn main() {
    let mut input=String::new();
    io::stdin().read_to_string(&mut input).expect("Failed to read input");

    let workouts:Vec<Workout> =serde_json::from_str(&input).expect("Invalid JSON format");
    let recommendation=recommend_workout(&workouts);

    println!("{}",recommendation);
}

fn recommend_workout(workouts: &[Workout]) -> String {
    let all_exercises = vec![
        "Push-ups", "Squats", "Deadlifts", "Pull-ups", "Bench Press", "Running", "Cycling"
    ];

    let most_common = find_most_frequent(workouts);  // ✅ Fix: Assign return value
    let mut rng = thread_rng();
    
    if let Some(exercise) = most_common {  // ✅ Fix: Now correctly an `Option<String>`
        format!("You frequently do {}. Try adding {} for muscle balance!",
            exercise,
            all_exercises.choose(&mut rng).unwrap_or(&"Planks"))
    } else {
        format!("No workout data found. Start with {}!", 
            all_exercises.choose(&mut rng).unwrap_or(&"Jogging"))
    }
}

fn find_most_frequent(workouts: &[Workout]) -> Option<String> {
    let mut frequency_map = std::collections::HashMap::new();

    for workout in workouts {
        *frequency_map.entry(&workout.exercise_type).or_insert(0) += 1;
    }

    frequency_map.into_iter()
        .max_by_key(|entry| entry.1)
        .map(|(exercise, _)| exercise.to_string())  // Ensure correct type
}
