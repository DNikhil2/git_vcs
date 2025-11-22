print(subprocess.run(["ps","-aux"], capture_output=True, text=True).stdout)

