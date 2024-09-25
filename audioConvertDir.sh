#!/bin/bash

echo "===>>>>> AUDIO CONVERTER <<<<<==="

dir_list=("/Volumes/WyDriveBlue/Parquet Courts/Sunbathing Animal [2014] [CD]" "/Volumes/WyDriveBlue/Passion Pit/Manners [2009] [CD]" "/Volumes/WyDriveBlue/Parliament/Mothership Connection [1975] [12_ Vinyl]" "/Volumes/WyDriveBlue/OutKast/Southernplayalisticadillacmuzik [1994] [CD]" "/Volumes/WyDriveBlue/of Montreal/Hissing Fauna, Are You the Destroyer_ [2007] [CD]" "/Volumes/WyDriveBlue/Muddy Waters/His Best, 1947 to 1955 [1997] [CD]" "/Volumes/WyDriveBlue/Moon Hooch/Moon Hooch [2013] [CD]" "/Volumes/WyDriveBlue/Electric Light Orchestra/Out of the Blue [1987] [CD]" "/Volumes/WyDriveBlue/Elton John/Captain Fantastic and the Brown Dirt Cowboy [1984] [CD]" "/Volumes/WyDriveBlue/Fatboy Slim/The Rockafeller Skank [1998] [CD]" "/Volumes/WyDriveBlue/Fela Kuti & Africa 70/Zombie [2001] [CD]" "/Volumes/WyDriveBlue/Fela Kuti & Africa 70/Confusion _ Gentleman [2010] [CD]" "/Volumes/WyDriveBlue/Fleet Foxes/Fleet Foxes [2008] [CD]" "/Volumes/WyDriveBlue/Fleet Foxes/Helplessness Blues [2011] [CD]" "/Volumes/WyDriveBlue/Foxygen/We Are the 21st Century Ambassadors of Peace & Magic [2013] [CD]" "/Volumes/WyDriveBlue/Frank Sinatra with Count Basie & His Orchestra/Sinatra at the Sands [1998] [CD]" "/Volumes/WyDriveBlue/Funkadelic/Maggot Brain [1989] [CD]" "/Volumes/WyDriveBlue/George Harrison/All Things Must Pass [2001] [CD]" "/Volumes/WyDriveBlue/Gojira/L’Enfant sauvage [2012] [CD]" "/Volumes/WyDriveBlue/Gojira/Fortitude [2021] [Digital Media]" "/Volumes/WyDriveBlue/Gorillaz/Plastic Beach [2010] [CD]" "/Volumes/WyDriveBlue/Grimes/Miss Anthropocene [2020] [Digital Media]" "/Volumes/WyDriveBlue/Grizzly Bear/Shields [2012] [CD]" "/Volumes/WyDriveBlue/Guns N’ Roses/Appetite for Destruction [1987] [12_ Vinyl]" "/Volumes/WyDriveBlue/John Wizards/John Wizards [2013] [CD]" "/Volumes/WyDriveBlue/Jungle/Jungle [2014] [CD]" "/Volumes/WyDriveBlue/Justice/✝ [2007] [CD]" "/Volumes/WyDriveBlue/Jurassic 5/Power in Numbers [2002] [CD]" "/Volumes/WyDriveBlue/Kamasi Washington/The Epic [2015] [CD]" "/Volumes/WyDriveBlue/Kanye West/The College Dropout [2005] [CD]" "/Volumes/WyDriveBlue/Kendrick Lamar/DAMN. [2017] [CD]" "/Volumes/WyDriveBlue/Kendrick Lamar/To Pimp a Butterfly [2015] [CD]" "/Volumes/WyDriveBlue/Kendrick Lamar/untitled unmastered. [2016] [CD]" "/Volumes/WyDriveBlue/King Tuff/King Tuff [2012] [CD]" "/Volumes/WyDriveBlue/Kraftwerk/Trans Europe Express [2009] [CD]" "/Volumes/WyDriveBlue/Kraftwerk/Minimum-Maximum [2005] [Copy Control CD]" "/Volumes/WyDriveBlue/Lauryn Hill/The Miseducation of Lauryn Hill [1998] [CD]" "/Volumes/WyDriveBlue/LCD Soundsystem/Sound of Silver [2007] [CD]" "/Volumes/WyDriveBlue/LCD Soundsystem/This Is Happening [2010] [CD]" "/Volumes/WyDriveBlue/Led Zeppelin/Led Zeppelin III [1970] [12_ Vinyl]" "/Volumes/WyDriveBlue/Led Zeppelin/Led Zeppelin II [1969] [Vinyl]" "/Volumes/WyDriveBlue/Led Zeppelin/[Led Zeppelin IV] [1971] [12_ Vinyl]" "/Volumes/WyDriveBlue/Led Zeppelin/How the West Was Won [2003] [CD]" "/Volumes/WyDriveBlue/Led Zeppelin/Coda [1990] [CD]" "/Volumes/WyDriveBlue/Louis Armstrong/Louis Armstrong Plays W.C. Handy [1987] [CD]" "/Volumes/WyDriveBlue/Mac DeMarco/2 [2012] [CD]" "/Volumes/WyDriveBlue/Mac DeMarco/Salad Days [2014] [CD]")

echo "===> Changing into album directory: $1"
cd "$1"

# album_path=$(echo "$1" | cut -d'/' -f2)
album=$(echo "$1" | cut -d'/' -f5)
artist=$(echo "$1" | cut -d'/' -f4)

echo "===> FOUND: Album ($album), Artist ($artist)"

echo "===> START: Create album folder"
mkdir "/Users/wyatt/Documents/music/$artist"
mkdir "/Users/wyatt/Documents/music/$artist/$album"


# ffmpeg -i 01.01\ The\ Woodworm.flac -b:a 320k -ar 44100 -map_metadata 0 -id3v2_version 3 output.mp3
for i in *.flac;
    #   do name=`echo "$i" | cut -d'.' -f2`
    do name="${i%.flac}"
    echo "===> START: Converting file..."
    echo "===> INFO: Name without extension: $name"
    ffmpeg -i "$i" -b:a 320k -ar 44100 -map_metadata 0 -id3v2_version 3 "/Users/wyatt/Documents/music/$artist/$album/${name}.mp3"

#   ARCHIVE
#   ffmpeg -i "$i" "${name}.mov"
done

echo "===> OUTPUT: MP3 directory: /Users/wyatt/Documents/music/$artist/$album"
echo "===> Conversion script compelte"