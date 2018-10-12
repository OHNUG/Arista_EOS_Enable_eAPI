# Arista EOS Enable eAPI

This will take an Arista switch that has SSH Enabled and run the commands
 to enable eAPI.
 
*Lab Design included in repository.

###Instructions: 

1 -  Enter your devices and management IP information into YAML. (Note: The Device name is only used for informational
output in the script and can be whatever you choose.)

Leave "devices" on the first line and indent.

```
devices:
 DCA-Spine1: "10.10.10.101"
 DCA-Spine2: "10.10.10.102"
 DCA-Leaf1: "10.10.10.201"
 DCA-Leaf2: "10.10.10.202"
 DCA-BL: "10.10.10.203"
```
  
2 - Run the script. It will ask you to enter your credentials using getpass:

```
$ python enableAPI.py
Please enter the username for ssh: admin
Please enter the password for ssh: *****
```

###Result:
```
Establishing connection to DCA-BL...
Enabling eAPI...
eAPI enabled on DCA-BL.
Establishing connection to DCA-Leaf2...
Enabling eAPI...
eAPI enabled on DCA-Leaf2.
Establishing connection to DCA-Spine1...
Enabling eAPI...
eAPI enabled on DCA-Spine1.
Establishing connection to DCA-Spine2...
Enabling eAPI...
eAPI enabled on DCA-Spine2.
Establishing connection to DCA-Leaf1...
Enabling eAPI...
eAPI enabled on DCA-Leaf1.
Process Completed.
```
 
Author - Drums090
