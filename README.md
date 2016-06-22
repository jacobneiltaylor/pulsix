Pulsix: The SixXS Heartbeat Client
==================================

Purpose
-------

This script is designed to generate the "heartbeat" required for dynamic SIT tunnels provided by SixXS. This work was adapted from the script available [here](https://help.ubnt.com/hc/en-us/articles/204976564-EdgeMAX-SIXXS-Connectivity-Without-AICCU-with-Minimum-System-Modification), but with a separate config file and designed to be called via a task scheduler, such as cron. It was designed for use with EdgeOS, but should work with any router or host with a task scheduler and python2. It has been tested to work on both CentOS and Windows, for example.

Usage
-----

Simply setup a SIT tunnel on your router or OS as usual, then configure your tunnel settings in the tunnel.json file, as follows:

1. **"remote":** Set this to the IPv4 endpoint as listed on the SixXS website.
2. **"local":** Set this to your assigned IPv6 address for the tunnel, as listed on the SixXS website. Usually ends in "::2".
3. **"password":** Set this to your tunnel password. This is **not** your SixXS login password, rather the unique tunnel password as listed under the "Live Tunnel Status on the PoP" link on the Tunnel Informatiuon page.

Place client.py and tunnel.json in the same directory and have cron or any other task scheduler call the script once every minute. Simple!