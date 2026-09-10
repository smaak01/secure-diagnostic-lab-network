import subprocess
import platform

targets = ["192.168.100.1", "10.0.0.2"]

for ip in targets:
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", param, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        print(f"{ip}: REACHABLE")
    else:
        print(f"ALERT: {ip} is down!")