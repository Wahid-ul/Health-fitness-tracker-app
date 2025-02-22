import subprocess
import json

def get_ai_recommendation(workouts):
    try:
        workout_json=json.dumps(workouts)
        result =subprocess.run(["./rust_ai/recommend"],input=workout_json,text=True,capture_output=True)
        return result.stdout.strip()
    
    except Exception as e:
        return f"Error fetching AI recommendation:{str(e)}"

