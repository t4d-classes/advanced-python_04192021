import subprocess

result = subprocess.run("where chkdsk.exe")

print(f"result: {result}")
print(f"return code: {result.returncode}")

result = subprocess.run("where chkdsk12.exe")

print(f"result: {result}")
print(f"return code: {result.returncode}")
