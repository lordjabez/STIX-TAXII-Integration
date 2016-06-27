soltra2snort

About

soltra2snort is a simple python script that converts the MS-ISAC Soltra Edge AttakingIPs feed into Snort rules on your local Snort instance.

The AttackingIPs feed contains observables in the form of IP addresses and domains that have been detected to be malicious by the MS-ISAC SOC.

The rules created by this script are of two types:
1. Any traffic to or from the $Home_Net and the malicious IP addresses
2. DNS queries from the $Home_Net to any address for the malicious domains

Authentication is required to access the feeds from the MS-ISAC Soltra Edge server.
If you wish to gain access to the feeds, please email a request to soc@msisac.org.

Usage

$ python soltra2snort.py
Enter your MS-ISAC Soltra Username -> <username>
Enter your MS-ISAC Soltra Password ->  <password>
Enter your Snort rules directory location -> <dir>

These prompts can be avoided by adding this information to the script itself just under the import section near the top of the file

### EDIT THIS SECTION ###

# username:password for the Soltra Edge server we are polling from
# example: "username:password"
user_pwd = "<username>:<password>"

# Snort rule directory
# example: "/etc/snort/rules/"
outputLocation = "<dir>"

#########################

In order for Snort to use the rules created by this script, the rules file needs to be added to the snort.conf file on your Snort system. 

Add this line to your snort.conf file:
Import /path/to/file/ms-isac.rules

On the first run, this script will convert all observables from the AttackingIPs feed in the last year to Snort rules.
Each run after the initial will covert observables from the last 7 days.

This is intended to be added to your Snort system as a cron job to be ran each week in order to add the newest malicious IP addresses and domains to your Snort rule set.

This can be done by adding the following to your crontab:
$ crontab -e

append this line to run soltra2snort every Tuesday at midnight:
0 0 * * 2 python /path/to/soltra2snort.py

It is a good idea to verify that the user’s crontab that contains the job has access to the Snort rules directory.