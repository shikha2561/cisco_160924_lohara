import subprocess
result = subprocess.run(['python','-c','print(2**8)'],shell=True,capture_output=True,text=True)
print(result.stdout)