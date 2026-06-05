import os
import subprocess

# Define paths relative to the 'src' directory where this script lives
SRC_DIR = os.path.abspath(os.path.dirname(__file__))
# Step up one level to find the true project root directory
ROOT_DIR = os.path.dirname(SRC_DIR)

# Points precisely to your actual lower-case main.py file
ENTRY_POINT = os.path.join(SRC_DIR, "main.py")

# PyInstaller execution flags
build_args = [
    "uv",
    "run",
    "pyinstaller",
    "--onefile",  # Compiles into a single standalone binary
    "--name=AutomationApp",  # Name of the output executable
    "--clean",  # Flushes the build cache directory completely
    f'"{ENTRY_POINT}"',  # Wrapped in quotes to handle potential spaces in Windows paths
]

print("🚀 Starting compilation via PyInstaller...")
# Run the compilation from the root directory so output folders mirror standard rules
result = subprocess.run(" ".join(build_args), shell=True, cwd=ROOT_DIR)

if result.returncode == 0:
    print("\n✅ Success! Your executable is ready in the './dist' directory.")
else:
    print("\n❌ Build failed. Check the error logs above.")
