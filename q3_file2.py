#In Networking Examples Part 1 another technique to run a command over ssh was shown. In this
#example commands are sent to the device using send().
import paramiko
import time
import re
# Open SSH connection to the device
def ssh_connection(ip):
    try:
        username = "lydia" #In an automation script read data from file
        password = "jenkvm" #never hard code
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username,
                        password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n") #unix command to list directory contents and save to file
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
            session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")

ssh_connection("192.168.0.24") #ip address of my VM, adjust to suit