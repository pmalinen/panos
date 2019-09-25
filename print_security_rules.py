#!/usr/bin/env python
import pandevice
import panorama
from pandevice.panorama import Panorama
from pandevice import policies


panip = ''
dg = ''
key = ''


def main():
    pano = Panorama(panip, api_key=key)
    # Use devicegroup dg
    devicegroup = panorama.DeviceGroup(dg)
    pano.add(devicegroup)

    # Get all the post rules
    postrulebase = policies.PostRulebase()
    devicegroup.add(postrulebase)
    current_security_rules = pandevice.policies.SecurityRule.refreshall(
        postrulebase)

    for rule in current_security_rules:
	    print rule.name


if __name__ == "__main__":
    main()
