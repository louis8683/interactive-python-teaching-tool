import os
import subprocess
from sys import stderr

target_file = os.path.join(os.path.dirname(__file__), "error_script.py")
# Bad method: cannot redirect with os.system
# try:
#     os.system(f"python {target_file}")
# except:
#     print("error is caught")
# else:
#     print("error is not caught")

# Method 1: Popen to redirect stderr
p = subprocess.Popen(f"python {target_file}", stderr=subprocess.PIPE)

print("Method 1: Popen")
print(p.stderr.read().decode(encoding="UTF-8"))
print(" ")

# Method 2: 
print("Method 2: try block")
try:
    1 / 0
except Exception as e:
    print(f"{str(type(e))[8:-2]}: {str(e)}")

# We choose method 2 because we want to save the current progress when an exception occurred.

