Scripts
=======
CyanBlob's useful scripts

DownloadSort.py
===============
Looks in your ~/Downloads folder and moves files to the folders in which they belong.
I recommend giving this execute permissions, copying it into /usr/bin, and then automating it by adding 
*/30 * * * * /usr/bin/DownloadSort.py

into your crontab (crontab -e).
NOTE: When adding this into crontab, a blank line is required at the end of the file.

vol.sh
======
Prints alsa audio level. Prints "mute" if the device is muted.

m4a2mp3.sh
==========
Looks in a directory and converts .m4a audio files to .mp3.
