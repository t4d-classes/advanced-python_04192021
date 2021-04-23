import subprocess

p = subprocess.Popen(
    "where chkdsk.exe",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)

retval = p.wait()
print(retval)

if p and p.stdout:
    for line in p.stdout.readlines():
        print(str(line, "UTF-8"))

