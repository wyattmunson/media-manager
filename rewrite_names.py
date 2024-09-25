import os
import printer
import sys
import cli_manager as cli

class Remover:
    def __init__(self):
        self.prefix = "[SPOTIFY-DOWNLOADER.COM] "
        self.dir = None
    
    
    def set_prefix(self, prefix):
        self.prefix = prefix
    
    def get_dir(self):
        return self.dir
    
    
    def set_dir(self, dir):
        self.dir = dir

    def remove_prefix(self):
        print("==> Removing prefix...")
        dir = self.dir
        for filename in os.listdir(dir):
            # print("Evaluating", filename)
            prefix = " - fiveofseven"
            prefix = "20240701_"
            prefix = "[SPOTIFY-DOWNLOADER.COM] "
            # if filename.startswith(prefix):
            # if filename.endswith(prefix):
            if prefix in filename:
                new_filename = filename.replace(prefix, "", 1)
                # Construct the full paths for old and new filenames
                old_path = os.path.join(dir, filename)
                new_path = os.path.join(dir, new_filename)
                # Rename the file
                os.rename(old_path, new_path)
                print(f'Renamed: "{filename}" -> "{new_filename}"')

def remove_prefix(dir):
    for filename in os.listdir(dir):
        prefix = "20240701_"
        # prefix = " - fiveofseven"
        if filename.startswith(prefix):
            new_filename = filename.replace(prefix, "", 1)
            # Construct the full paths for old and new filenames
            old_path = os.path.join(dir, filename)
            new_path = os.path.join(dir, new_filename)
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")


def get_unquoted_text(text):
    start_index = text.find('"') + 1  # Skip the opening quote
    end_index = text.find('"', start_index)  # Find the closing quote

    # Extract the text between quotes (assuming no escaped quotes)
    if start_index > 0 and end_index > start_index:
      extracted_text = text[start_index:end_index]
      print(f"Extracted text: {extracted_text}")
      return extracted_text
    else:
      print("No quotation marks found or invalid format.")
      return None


def get_configs(rmv):
    # check argments for configs
    print(sys.argv)
    
    if len(sys.argv) > 1:
    
        if sys.argv[1] in ["h", "H", "-h", "--help"]:
            print("HELP HIT")
        
        for item in sys.argv:
            print("Evaluating item:", item)
            if item.startswith("--prefix"):
                print("Setting prefix from CLI argument")
                prefix = item.replace("--prefix=", "")
                print("Ending prefix: ", prefix)
                rmv.set_prefix(prefix)
            
            if item.startswith("--dir"):
                dir = item.replace("--dir=", "")
                rmv.set_dir(dir)
    
    if not rmv.get_dir():
        cli.get_input("Set input dir")

        
    

printer.render_header("NORTH MEDIA MANAGER", "Path rewriter")

# GOOD !!!!!!
# dir_name = input("Enter dir name: ")
# remove_prefix(dir_name)
rmv = Remover()
get_configs(rmv)
rmv.remove_prefix()