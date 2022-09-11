import logging
import multiprocessing as mp
import os
import socket
import time

import buffer

HOST = "HOST/IP FOR CONNECT"
PORT = "PORT FOR CONNECT"

logger = mp.log_to_stderr(logging.DEBUG)


def worker(socket):
    while True:
        client, address = socket.accept()
        logger.debug("{u} connected".format(u=address))
        connbuf = buffer.Buffer(client)
        hash_type = connbuf.get_utf8()
        if not hash_type:
            break
        print("hash type: ", hash_type)

        file_name = connbuf.get_utf8()
        if not file_name:
            break
        file_name = os.path.join("uploads", file_name)
        print("file name: ", file_name)

        file_size = int(connbuf.get_utf8())
        print("file size: ", file_size)

        with open(file_name, "wb") as f:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = connbuf.get_bytes(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print("File incomplete.  Missing", remaining, "bytes.")
            else:
                print("File received successfully.")

        print(f"WORK LOGIC WITH FILE{file_name} AND HOST..{hash_type}")
        client.close()


if __name__ == "__main__":
    num_workers = 20

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.bind((HOST, PORT))
    serversocket.listen(20)

    workers = [
        mp.Process(target=worker, args=(serversocket,)) for i in range(num_workers)
    ]

    for p in workers:
        p.daemon = True
        p.start()

    while True:
        try:
            time.sleep(5)
        except:
            break
