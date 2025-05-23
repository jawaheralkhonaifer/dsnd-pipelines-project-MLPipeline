import subprocess

# Install ipykernel (if not already installed)
subprocess.run(["python", "-m", "pip", "install", "ipykernel"])

# Register the Jupyter kernel
subprocess.run([
    "python", "-m", "ipykernel", "install",
    "--user", "--name=myenv", "--display-name", "Python (myenv)"
])