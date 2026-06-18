import subprocess
import sys

def run_script(script_path):
    print(f"========== Running {script_path} ==========")
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        print(f"Error: Execution failed for {script_path}")
        sys.exit(1)
    print(f"========== {script_path} completed successfully ==========\n")

if __name__ == "__main__":
    print("Starting AI Pipeline for Doctor Recommender System...\n")
    
    scripts_to_run = [
        "scripts/import_to_db.py",
        "scripts/preprocess.py",
        "scripts/feature_engineering.py"
    ]
    
    for script in scripts_to_run:
        run_script(script)
        
    print("Pipeline execution finished successfully!")

