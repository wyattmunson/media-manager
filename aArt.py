import os
import subprocess
import shutil
import re

print("Get AArt")

dir_list = ["/Users/wyatt/Documents/music/Grimes"]

base_dir = "/Volumes/WyDriveBlue"
target_dir = "/Users/wyatt/Documents/music"
target_dir = "/Volumes/homeblock/audio/music"

# lister = os.walk(base_dir)
artists = os.listdir(base_dir)

for x in artists:
    print("====> Checking ARTIST:", x)
    # exit loop for hidden files (not albums)
    if x in [".Spotlight-V100", ".TemporaryItems"]:
        continue

    artist_path = base_dir + "/" + x
    albums = os.listdir(artist_path)
    print("Albums", albums)

    for y in albums:
        # remove [YYYY] [CD] from album name
        album_short = re.sub(r"\[.*?\]", "", y)
        album_short = album_short[:-2]
        print(f"=> Short album is '{album_short}'")

        # check to if file is intarget
        album_path = artist_path + "/" + y
        target_parth = target_dir + "/" + x + "/" + album_short
        print("====> Checking album:", y)
        if os.path.exists(target_parth):
            print("==> Found album in target")
            try:
                image_path = album_path + "/cover.jpg"
                shutil.copyfile(image_path, target_parth + "/cover.jpg")
                print("==> SUCCESS:", album_short)
            except Exception as e:
                print("==> FAILED to COPY FILE:", e)
        else:
            print("==> No matching file in target")

# print(lister)
