#
#   $Id: README.WPA-Mini-HOWTO.txt 72 2006-09-27 19:05:14Z finley $
#
#   WPA Mini-HOWTO
#       Initial text by Gary Case <gcase@redhat.com>
#       2006.09.26 Brian Elliott Finley
#       - misc updates
#       
#

Here are my directions for installing wpa_supplicant, wifi-radar and all
necessary support packages on RHEL4 U2 to enable WPA/WPA2 encrypted
wireless ethernet access. 

1. Wireless-tools package: I didn't need to update this as the version
we ship (v27) was sufficient for use with the latest drivers.


2. Wireless-extensions: I didn't update this. The kernel is using v16
according to iwconfig --version, which is sufficiently new to support
everything we need here.


3. Updated wireless card driver, firmware and kernel module precompiled
RPMs retrieved from here:

http://atrpms.net/dist/el4/ipw2200-testing/

Newer driver: ipw2200-1.0.10-36.el4.at
Newer firmware: ipw2200-firmware-2.4-7.at
Newer kernel module: ipw2200-kmdl-2.6.9-22.0.2.EL-1.0.10-36.el4.at

Be sure to get the packages from the "testing" branch, as the regular
ones are the same as the one we ship with RHEL 4 (1.0.0). You need the
newer driver and associated files to make WPA work. The web page link I
posted will take you to the testing packages. 


4. WPA Supplicant, found here: http://hostap.epitest.fi/wpa_supplicant/

4a. I tried using the precompiled wpa_supplicant RPM packages from the
atrpms site, but they were built with all options enabled and needed
additional packages to solve dependencies. I decided to build the latest
stable version myself (version 0.4.8) instead of playing "find the RPM"
to solve the dependencies present in the precompiled package. My home
setup is very simple, so all I needed in my .config file were these
three lines:

CONFIG_IEEE8021X_EAPOL=Y
CONFIG_EAP_PSK=y
CONFIG_DRIVER_IPW=y

If your customer is using PEAP or LEAP or some other external
authentication protocol their .config file may vary. All the available
options are listed in the README file included in the wpa_supplicant
tarball.

4b. After building I copied the wpa_cli and wpa_supplicant binaries to
/usr/local/bin (the location suggested in the README. Feel free to
relocate if desired.). Then I copied the included wpa_supplicant.conf
file to /etc/wpa_supplicant/wpa_supplicant.conf. There's a great deal of
information and several example configurations in the supplied .conf
file. The customer can use the examples to select the proper options for
their config file if their network doesn't match my simple WPA2-PSK
setup:

#Gary's WPA2 home network
network={
        ssid="my-secret-ssid"
        scan_ssid=0
        proto=WPA2
        key_mgmt=WPA-PSK
        pairwise=CCMP
        group=CCMP
        psk="my-secret-pre-shared-key"
        priority=2


Be sure to change the SSID and PSK to the real values for your network.
All the other options in the file were left at their default state. 


5. WPA Supplicant testing

With the configuration set up as described, I could issue this command
to bring up the interface:

wpa_supplicant -Bw -ieth1 -c/etc/wpa_supplicant/wpa_supplicant.conf

(The -Bw option runs the daemon in the background and waits for the
interface to be added, if necessary. Have the customer change -ieth1 to
match their wireless interface.)

This command was then used to get a DHCP address on the card.

dhclient eth1

I wrote an extremely simple script to do the two commands for me:

#!/bin/bash
# Script to start WPA Supplicant for secure wireless communication
wpa_supplicant -Bw -ieth1 -c/etc/wpa_supplicant/wpa_supplicant.conf
sleep 8
dhclient eth1

If the network connection isn't coming up, check /var/log/messages for
errors and try dropping the -B option on wpa_supplicant to have the
program output information to stdout.


6. Wifi-radar

Although it's not needed for wireless or WPA to work, the wifi-radar
package can provide users with an alternative method for choosing and
connecting to a secure wireless access point. It has no options in the
GUI for WPA/WPA2, but it's capable of using a properly configured
wpa_supplicant installation to handle the more secure levels of
encryption. 

6a. After completing steps one through 5 above (step 5 is there to make
sure the supplicant is working properly), download and install
wifi-radar from the CVS site (directions are present on the CVS site):

http://svn.systemimager.org/

6b. Edit the configuration file to match your installation. An example
setup that works with my home network is shown below. The DEFAULT
section is already populated by the installer, but make sure that the
interface matches your wireless interface. As in all the other examples,
change "my-secret-ssid" to match the SSID in use at your site:

[DEFAULT]
ifup_required = False
auto_profile_order = my-secret-ssid
speak_up = False
scan_timeout = 5
interface = eth1
commit_required = False

[my-secret-ssid]
use_dhcp = yes
wpa_driver = ipw
use_wpa = yes
mode = Auto

6c. Edit the /usr/sbin/wifi-radar script to use dhclient instead of
dhcpcd:

The % DHCP_TIMEOUT section from the DHCP_COMMAND line needed commenting
out to make the wifi-radar script work. I suspect there's no timeout
value for dhclient or it's implemented differently from dhcpcd.

6d. Continue editing the /usr/sbin/wifi-radar script to use
wpa_supplicant. You'll need to change the command, conf, and driver
lines to match the locations of your command and configuration files as
well as the wpa driver you're using in wpa_supplicant.

# WPA_SUPPLICANT
WPA_SUPPLICANT_COMMAND  = "/usr/local/bin/wpa_supplicant"
WPA_SUPPLICANT_KILL_COMMAND=""
WPA_SUPPLICANT_CONF="/etc/wpa_supplicant/wpa_supplicant.conf"
WPA_DRIVER="ipw"
WPA_SUPPLICANT_PIDFILE  = "/var/run/wpa_supplicant.pid"
WPA_SUPPLICANT_ARGS     = "-B -i " + INTERFACE + " -c " + WPA_SUPPLICANT_CONF + " -D " + WPA_DRIVER + " -p " + WPA_SUPPLICANT_PIDFILE


7. Run wifi-radar

After making those script changes, I could run wifi-radar, select the
proper SSID and click the "Connect" button to get a DHCP address.

