import subprocess

cmd = "brownie run scripts/deploy.py"
subprocess.Popen(cmd, cwd=r"scripts")
