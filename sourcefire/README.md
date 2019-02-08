Prerequisites

- install of the following module:
 - selenium for python (http://selenium-python.readthedocs.io/installation.html)
- The server should have a X server running
- Be sure that the X session of the user that is running the script is open (you can even "lock the screen" of the Desktop session)
- xterm should be installed on the system
- This script has been desgined to run with Firefox only (some Firefox version may be incompatible with some selenium version)
- An Intrusion policy should be already created. You have to get his uuid which is like xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (you can find it in the url when editing the policy)
- Install geckodriver (https://github.com/mozilla/geckodriver)

About

defensecenter_upload.py is a python script that automatically uploads and applies snort rules to your defense center and commits the policy to sourcefire devices. This script is intended to be used in conjuction with api2snort.py which converts MS-ISAC AttackingIPs into Snort rules on your local linux machine. The defensecenter_upload script then uploads those rules to your remote Defense Center.

The AttackingIPs feed contains observables in the form of IP addresses and domains that have been detected to be malicious by the MS-ISAC SOC.

Authentication is required to access the attacking IP data from the MS-ISAC API server.
If you wish to gain access to the feeds, please email a request to soc@msisac.org.

Usage

$ python defensecenter_upload.py
Enter your Defense Center Username -> <username>
Enter your Defense Center Password ->  <password>
Enter the IP address of the Defense Center -> <ip>
Enter the UUID of the Intrusion Policy -> <UUID>
Enter the full file path to your Snort rules file -> <dir>


These prompts can be avoided by adding this information to the script itself just under the import section near the top of the file:

### EDIT THIS SECTION ###

# Defense Center username
dcuser = ""

# Defense Center password
dcpass = ""

# Defense Center IP/domain name
dcip = ""

# Defense Center Intrusion Policy UUID to place the rules to
dcuuid = ""

# Snort rules file full path
snortfile = ""

#This section is optional. If you encounter certificate issues, permanently add the DC certificate to your browser and set the directory of the Firefox Profile 
# Example: profile = webdriver.FirefoxProfile('/home/user/.mozilla/firefox/wa84ceto.default')
profile = webdriver.FirefoxProfile()

#########################


This is intended to be added to your a system as a cron job to be run each week in order to add the newest malicious IP addresses and domains to your sourcefire devices.

This can be done by adding the following to your crontab:
$ crontab -e

append this line to run api2snort every Tuesday at midnight:
0 0 * * 2 python /path/to/defensecenter_upload.py
