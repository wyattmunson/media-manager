import shutil
import os
import printer
import cli_manager as cli

def copy_folder(source_dir, target_dir):
    print(f"Copying folder... '{source_dir}'")
    short_target_dir = source_dir.split("/")[-1]

    # add trailing slash to target dir if necessary
    targ = target_dir + "/" + short_target_dir if not target_dir.endswith("/") else target_dir + short_target_dir
    
    try:
        shutil.copytree(source_dir, targ, dirs_exist_ok=True)
        print(f"Folder copied to: {targ}")
    except OSError as e:
        print(f"ERROR: Failed to copy to: {targ}")
        print(f"Error copying dir: {e}")
    except:
        print(f"ERROR: Failed to copy to: {targ}")
        print("Unexpected error")

def get_input():
    source_dir = input("Enter source dir: ")


def run_app():
    source_dir = "/Users/wyatt/code/music-manager/source/folder"
    target_dir = "/Users/wyatt/code/music-manager/target"
    while True:
        source_dir = input("Enter source dir (or e[x]it): ")
        if source_dir is "x" or "X": exit(0)
        copy_folder()

if __name__ == "__main__":
    # source_dir = input("Enter source dir: ")
    
    head = "NORTH MEDIA MANAGER"
    sub = "Video Syncing Service"
    printer.render_header(head, sub)
    
    run_app()
    
    # copy_folder(source_dir, target_dir)
    