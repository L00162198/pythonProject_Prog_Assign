import paramiko
import time


def ssh_connection():
    global user_file
    global cmd_file

try:
    ip = "192.168.0.24"
    user_name='lydia'.rstrip("\n")
    user_password='jenkvm'.rstrip("\n")
    session = paramiko.SSHClient()



session.set_missing_host_key_policy(paramiko.AutoAddpolicy)
session.connect(ip.rstrip("\n"),username='lydia', password='jenkvm')
connection = session.invoke_shell()
#make folder labs
session.exec_command("mkdir labs\n")
#In the labs folder create  2 sub folders
session.exec_command("cd labs:mkdir lab1 mkdir lab2\n")