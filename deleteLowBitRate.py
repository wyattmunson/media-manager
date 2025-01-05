# Delete low bit rate songs.
import os
import glob
from mutagen.mp3 import MP3

target_dir = "/Volumes/homeblock/audio/music"

# "/music/MGMT/Oracular Spectacular/4th Dimensional Transition.mp3"


def delete_hidden_diles(dir):
    cadidate_list = glob.glob(f"{dir}/._*")
    for file in cadidate_list:
        try:
            os.remove(file)
            print(f"==> File deleted: {file}")
        except OSError:
            print(f"==> Failed to delete {file}")
    # print(dir + "/" + ".DS_Dtore")
    # try:
    #     os.remove(dir + "/" + ".DS_Dtore")
    #     print(f"==> File deleted: DS_Store")
    # except OSError:
    #     print(f"==> Failed to delete .DS_Store")
    print("==> Delete done")


artist = "blink-182"
artist = "MGMT"
artist = "9 Lazy 9"

delete_hidden_diles(target_dir)
artists = os.listdir(target_dir)

for artist in artists:

    artist_dir = target_dir + "/" + artist
    # delete crap files

    delete_hidden_diles(artist_dir)

    albums = os.listdir(artist_dir)

    print("==> Processing artist:", artist)

    for album in albums:
        print("==> Processing album:", album)
        if album == ".DS_Store" or album == "cover.jpg":
            print("==> Ejecting DS_Store")
            continue

        album_path = artist_dir + "/" + album
        print("album path is:", album_path)
        delete_hidden_diles(album_path)
        songs = os.listdir(album_path)

        # delete crap files
        # cadidate_list = glob.glob(f"{album_path}/._*")
        # for file in cadidate_list:
        #     try:
        #         # os.remove(file)
        #         print(file)
        #         print("==> File deleted")
        #     except OSError:
        #         print("==> cannot delete file")

        for song in songs:
            print("==> Processing song:", song)
            song_path = album_path + "/" + song
            delete_hidden_diles(album_path)
            try:
                audio = MP3(song_path)
                bitrate = audio.info.bitrate
                print("Got bit rate", bitrate)

                # delete if 128 kbps
                if bitrate == 128000:
                    try:
                        os.remove(song_path)
                        print(f"==> Deleted low quality song {song_path}")
                    except:
                        print(f"==> Failed to delete low quality song {song_path}")

            except Exception as e:
                print(f"Failed to extract {song} with error: {e}")
