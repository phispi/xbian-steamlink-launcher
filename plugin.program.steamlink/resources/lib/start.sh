#!/bin/bash

DIRNAME=$( dirname "${BASH_SOURCE[0]}" )

sudo openvt -c 7 -s -f -- su xbian -c "bash ${DIRNAME}/heartbeat.sh & /usr/bin/steamlink &"
sudo service xbmc stop

exit
