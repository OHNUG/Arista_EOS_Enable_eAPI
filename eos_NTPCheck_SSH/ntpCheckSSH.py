from netmiko import ConnectHandler
import getpass, json

with open('../hosts.json') as hostFile:
    hosts = json.load(hostFile)

with open('ntpServers.json') as ntpServers:
    ntpServers = json.load(ntpServers)

#Develop variable to check for NTP Servers

ntpMatch = ''''''
for server in sorted(ntpServers['ntpServers']):
    ntpMatch += "ntp server " + server + "\n"

#Remove empty line from ntpMatch
ntpMatch = ntpMatch[:-1]


#Get user credentials to initial SSH session
credUser = input("Please enter username: ")
credPass = getpass.getpass("Please enter password: ")


#Begin connection
for group in hosts['hosts']:
    if "eos" in group:
        for deviceName, deviceIP in hosts['hosts'][group].items():
            print("Establishing Connection to %s..." % deviceName)
            net_connect = ConnectHandler(device_type='arista_eos',ip=deviceIP,username=credUser,password=credPass)

            #Enter privileged Exec mode
            print("Entering priviledged exec mode...")
            net_connect.enable()

            #send command
            print("Checking NTP Servers...")
            checkNTP = net_connect.send_command("show run | section ntp server")


            #Compare strings to see if configs match.
            if ntpMatch == checkNTP:
                print("Configuration in Sync")

            #If strings don't match, remove only the invalid lines.
            else:
                print("Incorrect servers, updating configuration...")
                ntpRemove = checkNTP.splitlines()
                for line in ntpRemove:
                    if line not in ntpMatch:
                        print("Removing: " + line)
                        net_connect.config_mode()
                        net_connect.send_command("no " + line)


                ntpNew = ntpMatch.splitlines()

                for line in ntpNew:
                    if line not in checkNTP:
                        print("Adding: " + line)
                        net_connect.config_mode()
                        net_connect.send_command(line)

                    elif line in checkNTP:
                        print("Command '" + line + "' already exists. Ignoring this line.")

            print("Configuration updated for %s." % deviceName)


print("NTP Check Task Completed.")