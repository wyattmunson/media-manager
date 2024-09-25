#!/bin/bash

echo "===>>>>> AUDIO CONVERTER <<<<<==="

# ffmpeg -i 01.01\ The\ Woodworm.flac -b:a 320k -ar 44100 -map_metadata 0 -id3v2_version 3 output.mp3
for i in *.flac;
    #   do name=`echo "$i" | cut -d'.' -f2`
    do name="${i%.flac}"
    echo "===> START: Converting file..."
    echo "===> INFO: Name without extension: $name"
    ffmpeg -i "$i" -b:a 320k -ar 44100 -map_metadata 0 -id3v2_version 3 "${name}.mp3"

#   ARCHIVE
#   ffmpeg -i "$i" "${name}.mov"
done

echo "===> Conversion script compelte"