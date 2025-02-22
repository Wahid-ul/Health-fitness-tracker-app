import subprocess
import json

def run_rust_ai(input_data):
    """
    Calls the Rust AI executable and returns predictions.
    """
    try:
        # Convert input data to JSON and pass it to Rust AI binary
        process = subprocess.run(
            ["../rust_ai/target/release/rust_ai"],
            input=json.dumps(input_data),
            capture_output=True,
            text=True
        )
        
        # Parse the output from Rust AI
        return json.loads(process.stdout)
    
    except Exception as e:
        return {"error": f"Failed to run Rust AI: {str(e)}"}
