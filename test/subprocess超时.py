import subprocess


subprocess.run(["../anycode.sh", "1", "2"], timeout=1, check=True)
