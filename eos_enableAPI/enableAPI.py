import json, getpass
from netmiko import ConnectHandler
with open('../hosts.json') as hostFile:
    hosts = json.load(hostFile)

credUser = input("Please enter the username for ssh: ")
credPass = getpass.getpass("Please enter the password for ssh: ")


for group in hosts['hosts']:
    if "eos" in group:
        for hostname, ip in hosts['hosts'][group].items():
            print("Establishing connection to %s..." % hostname)

            #Establish Connection
            #Try to connect to device, if there is a failure, throw the error and move on
            try:
                net_connect = ConnectHandler(device_type='arista_eos', ip=ip, username=credUser, password=credPass)

                # Enter privileged exec, then Global Configuration
                net_connect.enable()
                config = net_connect.config_mode()

                # Send Commands to enable eAPIs
                print("Enabling eAPI...")
                net_connect.send_config_set(["management api http-commands", "no shutdown", "write"])

                print("eAPI enabled on %s." % hostname)

            except:
                print("*****Error connecting to %s*****" % hostname)

