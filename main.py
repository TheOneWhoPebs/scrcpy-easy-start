import os
import time
local_ip = "insert ip here"
scrcpy_folder="insert scrcpy folder here"
port = input("Port: ")
os.system(f"cd {scrcpy_folder}")
os.system(f".\scrcpy --tcpip={local_ip}:{port}")
time.sleep(2)
exit()