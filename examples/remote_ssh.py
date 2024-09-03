import paramiko

# SSH connection details
hostname = "192.168.10.10"
port = 22
username = "root"
password = "password"

# Command to run on the remote server
command = "ls -la /tmp"

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password)

# Execute the command
stdin, stdout, stderr = ssh.exec_command(command)

# Print command output
print(stdout.read().decode())

# Close the connection
ssh.close()