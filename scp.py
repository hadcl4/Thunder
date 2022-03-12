#!/bin/env python3
from guizero import *
import subprocess
def file_send():
    command = f'scp '+fileenter.value+' '+ipenter.value+':'+locationenter.value
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
app = App(title="File Transfer", height=130, width=400, bg="white")
ipenter = TextBox(app, text="Enter target IP address here...", width=40)
fileenter = TextBox(app, text="Enter the path to the file you wish to copy here...", width=40)
locationenter = TextBox(app, text="Enter the location on the target here...", width=40)
enter = PushButton(app, text="Click here to send file to target.")
app.display()