# Arista EOS Enable eAPI

This will take an Arista switch that has SSH Enabled and run the commands
 to enable eAPI.
 
*Lab Design included in repository.
###Instructions: 

######1 -  Enter your devices and management IP information into YAML. (Note: The Device name is only used for informational
output in the script and can be whatever you choose.)

Leave "devices" on the first line and indent.

  <br />DCA-Spine1: "10.10.10.101"
  <br />DCA-Spine2: "10.10.10.102"
  <br />DCA-Leaf1: "10.10.10.201"
  <br />DCA-Leaf2: "10.10.10.202"
  <br />DCA-BL: "10.10.10.203"
  
######2 - Run the script. It will ask you to enter your credentials using getpass:

$ python enableAPI.py
<br />Please enter the username for ssh: admin
<br />Please enter the password for ssh: *****

###Result:

<br />Establishing connection to DCA-BL...
<br />Enabling eAPI...
<br />eAPI enabled on DCA-BL.
<br />Establishing connection to DCA-Leaf2...
<br />Enabling eAPI...
<br />eAPI enabled on DCA-Leaf2.
<br />Establishing connection to DCA-Spine1...
<br />Enabling eAPI...
<br />eAPI enabled on DCA-Spine1.
<br />Establishing connection to DCA-Spine2...
<br />Enabling eAPI...
<br />eAPI enabled on DCA-Spine2.
<br />Establishing connection to DCA-Leaf1...
<br />Enabling eAPI...
<br />eAPI enabled on DCA-Leaf1.
<br />Process Completed.
 
Author - Drums090
