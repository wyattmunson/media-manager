class ConfigManager:
    def __init__(self):
        self.target_list = [""]
        self.target_list_options = [
            {
                'display_name': "WyDrive_MIA",
                'path_name': "/Volumes/WyDrive_MIA/videos/tv",
                'tv_path': "/Volumes/WyDrive_MIA/videos/tv",
                'movies_path': "/Volumes/WyDrive_MIA/videos/movies",
                'enabled': True
            }
        ]
    
    def set_target_list(self, list):
        self.target_list = list
    
    
    def get_target_list_options(self):
        return self.target_list_options