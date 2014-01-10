#!/bin/bash
amixer get Master | grep "Front Left" | awk -F'[]%[]' '/%/ {if ($5 == "off") { print "mute" } else { print $2"%" }}'
