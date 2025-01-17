#!/bin/bash

mv "movies/The_Lord_of_the_Rings_Two_Towers (2002)/A1_t00.m4v"	"movies/The_Lord_of_the_Rings_Two_Towers (2002)/The_Lord_of_the_Rings_The_Two_Towers (2002).m4v"

mkdir "movies/The_Lord_of_the_Rings_Two_Towers (2002)/extras"
mv movies/The_Lord_of_the_Rings_Two_Towers\ \(2002\)/??_*.m4v movies/The_Lord_of_the_Rings_Two_Towers\ \(2002\)/extras
mv "movies/The_Lord_of_the_Rings_Two_Towers (2002)/E17_t03.m4v" "movies/The_Lord_of_the_Rings_Two_Towers (2002)/extras"
# mkdir "movies/Anger_Management (2003)"
# mv "movies/Anger_Managment (2003)/Anger_Managment (2003) - 720p H264.mp4" "movies/Anger_Management (2003)/Anger_Management (2003) - 720p H264.mp4"



# mkdir "movies/Argo (2012)"
# "movies/Argo_Extended_Cut (2012)/Argo_Extended_Cut (2012) - 1080p H264.mp4" "movies/Argo (2012)/Argo (2012) - Extended Cut 1080p H264.mp4"
# rm -rf "movies/Argo_Extended_Cut (2012)"

# mkdir "movies/From_Up_On_Poppy_Hill (2011)/extras"
# mv "movies/From_Up_On_Poppy_Hill (2011)/A1_t00.m4v" "movies/From_Up_On_Poppy_Hill (2011)/extras/A1_t00.m4v"
# mv "movies/From_Up_On_Poppy_Hill (2011)/A3_t02.m4v" "movies/From_Up_On_Poppy_Hill (2011)/extras/A3_t02.m4v"


rm "movies/Repo_Man (1984)/Repo Man 1984 Criterion BluRay 1080p HEVC x265 BONE.mkv"

# Corret Model - move to extras folder - not for poppy
# mkdir "movies/From_Up_On_Poppy_Hill (2011)/extras"
# mv "movies/From_Up_On_Poppy_Hill (2011)/A1_t00.m4v" "movies/From_Up_On_Poppy_Hill (2011)/extras/A1_t00.m4v"

OLD_DIR="movies/Argo_Extended_Cut (2012)"
NEW_DIR="movies/Argo (2012)"
OLD_NAME="Argo_Extended_Cut (2012) - 1080p H264.mp4"
NEW_NAME="Argo (2012) - [Extended Cut] 1080p H264.mp4"

mv "$OLD_DIR" "$NEW_DIR"
mv "$NEW_DIR"/"$OLD_NAME" "$NEW_DIR"/"$NEW_NAME"

mv "movies/Argo_Extended_Cut (2012)" "movies/Argo (2012)"
mv "movies/Argo (2012)/Argo_Extended_Cut (2012) - 1080p H264.mp4" "movies/Argo (2012)/Argo (2012) - [Extended Cut] 1080p H264.mp4"


# movies/Anger_Managment (2003)/Anger_Managment (2003) - 720p H264.mp4

OLD_DIR="movies/Anger_Managment (2003)"
NEW_DIR="movies/Anger_Management (2003)"
OLD_NAME="Anger_Managment (2003) - 720p H264.mp4"
NEW_NAME="Anger_Management (2003) - 720p H264.mp4"

mv "$OLD_DIR" "$NEW_DIR"
mv "$NEW_DIR"/"$OLD_NAME" "$NEW_DIR"/"$NEW_NAME"

# BILL BURR - GOOD 
mv "movies/Bill_Burr_Im_Sorry_You_Feel_That_Way (2014)" "standup/Bill_Burr_Im_Sorry_You_Feel_That_Way (2014)"
mv "movies/Bill_Burr_Live_At_Red_Rocks (2022)" "standup/Bill_Burr_Live_At_Red_Rocks (2022)"
mv "movies/Dave_Chappelle_The_Dreamer (2023)" "standup/Dave_Chappelle_The_Dreamer (2023)"
mv movies/*Gaffigan* standup/

# DELETE - GOOD
rm -rf movies/From_Russia_with_Love
rm -rf "movies/Howl's Moving Castle (2004) [1080p]/"

# DELETE movies in tv (ensure removal from Jellyfin metadata)
rm -rf "tv/Misery (1990)"
rm -rf "tv/Uncut_Gems (2019)"
rm -rf "tv/The_Vanishing (1988)"

# DELETE DUPLICATE TV
rm -rf "tv/Ted-Lasso_S1/"
mv -f "tv/Ted Lasso (2020)" "tv/Ted_Lasso (2020)"
rm -rf "tv/No Reservations - Season 8"


# Correct model - update names in place
mv "movies/From-Up-On-Poppy-Hill_2011/" "movies/From_Up_On_Poppy_Hill (2011)"
mv "movies/From-Up-On-Poppy-Hill_2001"  "movies/From_Up_On_Poppy_Hill (2011)"
mv "movies/From_Up_On_Poppy_Hill (2011)/A1_t00.m4v" "movies/From_Up_On_Poppy_Hill (2011)/From_Up_On_Poppy_Hill (2011).m4v"
mv "movies/From_Up_On_Poppy_Hill (2011)/A3_t02.m4v" "movies/From_Up_On_Poppy_Hill (2011)/From_Up_On_Poppy_Hill (2011) - Cinematic Cut.m4v"

# Correct model - update year (update parent folder)
mv "movies/Kill_Bill_Vol_2 (2003)" "movies/Kill_Bill_Vol_2 (2004)"
mv "movies/Kill_Bill_Vol_2 (2004)/Kill_Bill_Vol_2 (2003).mkv" "movies/Kill_Bill_Vol_2 (2004)/Kill_Bill_Vol_2 (2004).mkv"

mv "movies/Independence_Day (1999)" "movies/Independence_Day (1996)"
mv "movies/Independence_Day (1996)/Independence_Day (1999).mp4" "movies/Independence_Day (1996)/Independence_Day (1996).mp4"

mv "movies/Dallas_Buyers_Club (2012)" "movies/Dallas_Buyers_Club (2013)"
mv "movies/Dallas_Buyers_Club (2013)/Dallas_Buyers_Club (2012).mp4" "movies/Dallas_Buyers_Club (2013)/Dallas_Buyers_Club (2013).mp4"
mv "movies/Dallas_Buyers_Club (2013)/Dallas_Buyers_Club (2012) - 720p.mkv" "movies/Dallas_Buyers_Club (2013)/Dallas_Buyers_Club (2013) - 720p.mkv"

# DELETE TOR ARTIFACTS
find . -name RARBG.txt -delete
find . -name "*Downloaded from*.txt" -delete
find . -name "*INFINITY*.txt" -delete
find . -name "NEW upcoming releases by*.txt" -delete
find . -name "*Torrent downloaded from*.txt" -delete
rm -rf "tv/Hey_Arnold (1996)/OTHER Cartoons You'd PROBABLY Like, HERE"
find . -name "._*" -delete

mv "tv/Bridget_and_Eamon (2016)/Season 02" "tv/Bridget_&_Eamon (2016)"
rm -rf "tv/Bridget_and_Eamon (2016)/"

rm -rf "tv/An_Idiot_Abroad (2010)/"
mv "tv/An Idiot Abroad (2010)/" "tv/An_Idiot_Abroad (2010)"

