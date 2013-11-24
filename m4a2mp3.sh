#!/bin/sh # name of this script: m4a2mp3.sh # m4a to mp3
for i in *.m4a; do 
  faad "$i"
   x=`echo "$i"|sed -e 's/.m4a/.wav/'`
   y=`echo "$i"|sed -e 's/.m4a/.mp3/'`
   lame -h -b 192 "$x" "$y" rm 
   "$x" 
done

Read more: http://linuxpoison.blogspot.com/2008/02/script-to-convert-m4a-to-mp3.html#ixzz2g8to1FlR
