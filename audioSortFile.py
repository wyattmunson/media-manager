import os
import shutil

# PURPOSE
# This is for splitting file names from Lucida.
# It takes a file name with artists, puts it in artist folder

source_dir = "/Users/wyatt/Downloads/musicSourceDir"
target_dir = "/Users/wyatt/Documents/music"

songs = os.listdir(source_dir)

for song in songs:
    print("==> Processing song:", song)
    splitted = song.split(" - ")
    print("SPLIT", splitted)
    
    # create directory artist directory if necessary
    artist_dir = target_dir + "/" + splitted[0]
    try:
        os.mkdir(artist_dir)
    except FileExistsError:
        print(f"Directory '{artist_dir}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{artist_dir}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # copy song to artist dir in target
    new_file_loc = artist_dir + "/" + splitted[1]
    try:
        original_file_loc = source_dir + "/" + song
        shutil.copyfile(original_file_loc, new_file_loc)
        print("==> Transferred file")
    except:
        print("==> Failed to transfer file:", original_file_loc)


# print("SONGS:", songs)