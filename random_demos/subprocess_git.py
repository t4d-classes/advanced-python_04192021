import subprocess
import re

commit_re = re.compile("commit ([a-z0-9]*)")
parent_re = re.compile("parent ([a-z0-9]*)")
commit_message_re = re.compile("\n\n(.*)")

c = subprocess.run(
    "git log",
    shell=True,
    capture_output=True,
    text=True)
result = c.stdout

commit_sha1 = commit_re.match(result).group(1)

while True:
    c = subprocess.run(
        f"git cat-file -p {commit_sha1}",
        shell=True,
        capture_output=True,
        text=True)

    commit_msg_match = commit_message_re.search(c.stdout)

    print(f"{commit_sha1[:8]} {commit_msg_match.group(0).strip()}")
    
    parent_match = parent_re.search(c.stdout)
    if not parent_match:
        break
    commit_sha1 = parent_match.group(1)