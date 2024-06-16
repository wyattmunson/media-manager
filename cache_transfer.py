import sys
import subprocess, time

print("......Tranfering......")

source_path = sys.argv[1]
source_dir = source_path.split("/").pop()
# target_path = "/Volumes/WyDrive_NRT/tv/" + source_dir
target_path = "/Volumes/WyDrive_MIA/videos/tv"
target_path = "/Volumes/WyDrive_NRT/tv/"

# target_path = "/Volumes/WyDrive_NRT/movies/"
# target_path = "/Volumes/WyDrive_MIA/videos/movies"

target_path = "/Volumes/wyblock/transfer/tv/"

target_list = ["/Volumes/WyDrive_MIA/videos/tv",
"/Volumes/WyDrive_NRT/tv/",
"/Volumes/wyblock/transfer/tv/"]

print("Source:", source_path)
print("Target:", target_path)

cmd_string = f'rsync -avz "{source_path}" "{target_path}"'

cmd_array = ["rsync", "-avz", {source_path}, {target_path}]

start_time = time.time()
print("CMD string:", cmd_string)
print("\n...Tranferring files...")
subprocess.run(cmd_string, shell=True)

time_delta = time.time() - start_time
print(f"Runtime was {time_delta} seconds")