import psutil
print("CPU %:", psutil.cpu_percent(interval=1))
print("Memory %:", psutil.virtual_memory().percent)

