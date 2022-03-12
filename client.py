#!/bin/env python3
from guizero import *
import subprocess
def file_receive():
    command = f'scp '+ipenter.value+':'+fileenter.value+' '+locationenter.value
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
app = App(title="File Transfer", height=130, width=450, bg="white")
ipenter = TextBox(app, text="Enter target IP address here...", width=40)
fileenter = TextBox(app, text="Enter the path to the file on the target you wish to copy here...", width=51)
locationenter = TextBox(app, text="Enter the location where you wish to copy the file...", width=45)
enter = PushButton(app, text="Click here to receive file from target.", command=file_receive)
app.display()