import yaml, getpass # Import PyYAML and getpass
from netmiko import ConnectHandler # import ConnectHandler from the netmiko module

def main(): # Define main Python Module for the script
    # Open YAML file as "deviceYAML" and save it to a variable called "devices"
    with open('devices.yaml') as device_yaml: 
        devices = yaml.safe_load(device_yaml)
    
    # Collect username from user and store it to a variable called "cred_user"   
    cred_user = input("Please enter the username for ssh: ") 
   
    ''' Collect password from user, but use getpass in order to 
    keep the password from dispalying on the screen. '''
    cred_pass = getpass.getpass("Please enter the password for ssh: ")
    
    ''' Begin for loop to loop through devices and perform
    the necessary actions to enable eAPI via the Netmiko connection handler.'''
   
    for hostname, ip in devices.items():
            print("Establishing connection to %s..." % hostname)
            # Try to establish a connection to the device.
            try: 
                net_connect = ConnectHandler(device_type='arista_eos', ip=ip, 
                username=cred_user, password=cred_pass)
            
                # Enter Privileged EXEC mode
                net_connect.enable()
                
                # Enter Global Configuration
                net_connect.config_mode()
                
                ''' Print an output letting the user know that you are sending 
                the commands and then send the list of commands to enable eAPI '''
                print("Enabling eAPI...")
                net_connect.send_config_set(['management api http-commands', 'no shutdown', 'write'])
                
                # Inform user of completion on the device
                print("eAPI enabled on %s." % hostname)
                
            # If connection has an error, tell the user
            except:
                print("*****Error connecting to %s*****" % hostname)
            
if __name__ == '__main__':
        main()
