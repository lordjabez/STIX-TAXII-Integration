import datetime
import json
import os
import time

import requests


STIX_TAXII_URL = 'http://54.244.134.70/api'
DOMAINS_URL = STIX_TAXII_URL + '/domains'
IPS_URL = STIX_TAXII_URL + '/ips'


class api():

    def getInfo(self, firstrun=True):
        """
        Get a list of bad domains and IPs.
        @param firstrun: If true, fetch all data, otherwise only go back the last ten days.
        """
        domainsurl = DOMAINS_URL
        ipsurl = IPS_URL
        if not firstrun:
            tendaysago = '/' + datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=10), '%Y%m%d')
            domainsurl += tendaysago
            ipsurl += tendaysago
        try:
            domains = requests.get(DOMAINS_URL, timeout=10)
            ips = requests.get(IPS_URL, timeout=10)
            return domains.json() + ips.json()
        except requests.exceptions.Timeout:
            print('ERROR: TIMEOUT! Check If You Are Whitelisted with the MS-ISAC. Please Contact indicator.sharing@cisecurity.org')


if __name__ == '__main__':
    info = api().getInfo(False)
    for i in info:
        print(i)
