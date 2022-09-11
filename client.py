import os
import socket
import sys
import threading

import buffer

HOST = "HOST/IP FOR CONNECT"
PORT = "PORT FOR CONNECT"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

with s:
    sbuf = buffer.Buffer(s)
    hostname = socket.gethostname()
    hash_type = f"{hostname}"
    # files = input('Enter file(s) to send: ')
    files = sys.argv[1]

    files_to_send = files.split()

    for file_name in files_to_send:
        print(file_name)
        sbuf.put_utf8(hash_type)
        sbuf.put_utf8(file_name)

        file_size = os.path.getsize(file_name)
        sbuf.put_utf8(str(file_size))

        with open(file_name, "rb") as f:
            sbuf.put_bytes(f.read())
        print("File Sent")

        print(f"HOST_HUYOST: {hash_type}")
