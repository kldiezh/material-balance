import subprocess

# List of scripts to run in order
scripts = [
    "Variables.py",
    "PVT.py",
    "Undersaturated_reservoir.py",
    "Saturated_reservoir.py",
    "Graphs.py"
]

for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script}: {result.stderr}")
        break
    else:
        print(f"Successfully ran {script}")

print("All scripts executed.")