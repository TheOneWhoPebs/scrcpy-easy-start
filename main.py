import os
import time
local_ip = "insert local ip here"
scrcpy_folder="insert path to scrcpy folder here"
port = input("Port: ")
os.system(f"cd {scrcpy_folder} &&" + f".\scrcpy --tcpip={local_ip}:{port}")
time.sleep(2)
exit()