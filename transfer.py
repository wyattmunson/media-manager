import sys
import subprocess, time
import logging

# logging.basicConfig(filename="logs.txt", filemode="a", level=logging.DEBUG)

logging.basicConfig(filename="log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.getLogger().addHandler(logging.StreamHandler())

print("......Tranfering......")
logging.info("======== START TRANSFER ========")

source_path = sys.argv[1]
source_dir = source_path.split("/").pop()

target_path = "/Volumes/WyDrive_MIA/videos/tv"
target_path = "/Volumes/WyDrive_NRT/tv/"
target_path = "/Volumes/wyblock/transfer/tv/"

# target_path = "/Volumes/WyDrive_NRT/movies/"
# target_path = "/Volumes/WyDrive_MIA/videos/movies"
# target_path = "/Volumes/wyblock/transfer/movies/"


# target_list = ["/Volumes/WyDrive_MIA/videos/tv", "/Volumes/WyDrive_NRT/tv/", "/Volumes/wyblock/transfer/tv/"]
# target_list = ["/Volumes/WyDrive_MIA/videos/movies", "/Volumes/WyDrive_NRT/movies/", "/Volumes/wyblock/transfer/movies/"]
target_list = ["/Volumes/WyDrive_MIA/videos/movies", "/Volumes/WyDrive_NRT/movies/"]
target_list = ["/Volumes/WyDrive_MIA/videos/tv", "/Volumes/WyDrive_NRT/tv/"]

print("..Preparing to transfer to all targets..")
logging.info(f'Selected targets: {target_list}')

total_time = time.time()

def do_transfer(x):
    # print("\n..Tranferring to target..")
    # print("\tSource:", source_path)
    # print("\tTarget:", x)
    logging.info("..Transferring to a target..")
    logging.info(f'\tSource: {source_dir} \n\tTarget: {x}')

    cmd_string = f'rsync -avz "{source_path}" "{x}"'

    start_time = time.time()
    print("CMD string:", cmd_string)
    # logging.info("CMD string:", cmd_string)
    print("\n...Tranferring files...")
    subprocess.run(cmd_string, shell=True)

    time_delta = time.time() - start_time
    # print(f'Tranfer to "{x}" complete')
    # print(f"Runtime was {time_delta} seconds")
    logging.info(f'Tranfer to "{x}" complete')
    logging.info(f"Runtime was {time_delta} seconds")
    
for x in target_list:
    do_transfer(x)

total_time_delta = time.time() - total_time
logging.info(f"Total runtime: {total_time_delta} seconds")
# print(f"Total runtime: {total_time_delta} seconds")