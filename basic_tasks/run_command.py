# without programmatic output

import os

print(os.system('touch /tmp/test'))
print(os.system('echo Pippo'))

# with programmatic output

import subprocess

process = subprocess.run(['echo', 'Pippo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(process)
print(process.stdout)
print(process.returncode)


# modern, quick way

output = subprocess.check_output(['echo', 'Pippo'])
print(output)

output = subprocess.getoutput('echo Pippo')
print(output)