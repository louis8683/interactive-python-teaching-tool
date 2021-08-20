import os

python_path = "python"
os.chdir(os.path.dirname(__file__))
os.system(f"{python_path} main.py")
