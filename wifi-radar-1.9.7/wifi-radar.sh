#!/bin/bash
# Shell wrapper that calls wifi-radar.py using sudo
PATH=/sbin:/usr/sbin:/usr/local/sbin:$PATH
sudo /usr/sbin/wifi-radar $*