import subprocess
print(subprocess.run(["df","-h"], capture_output=True, text=True).stdout)

