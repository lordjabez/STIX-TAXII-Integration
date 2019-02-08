# STIX-TAXII-Integration

The following scripts are designed to automatically convert the weekly MS-ISAC Malicious IPs and domains in to firewall rules or IDS/IPS signatures. This is done by querying our attacking IP and Domain API feed. If you wish to gain access to the API, please email a request to soc@msisac.org.


## Pre-requisites

Requires Python and pip to be installed. To download dependencies, run `pip install -r requirements.txt`.


## Basic Usage

TODO (turn the common thing into a standalone bit)


## Firewall Tools

Further usage documentation is available for your firewall or IDS/IPS solution:

*   [Cisco FW](cisco/README.md)
*   [Juniper FW](juniper/README.md)
*   [Sourcefire IDS](sourcefire/README.md)
*   [Snort IDS](snort/README.md)
