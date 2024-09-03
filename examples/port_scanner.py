import socket

# Host and port range to scan
host = "127.0.0.1"
port_range = range(20, 1025)

for port in port_range:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
        pass

    sock.close()
