class StateManager:
    def __init__(self):
        self.current_state = 0
        self.menu_trail = []
        
        self.main_menu_options = ["Transfer videos", "Configure"]
    
    
    def get_current_state(self):
        return self.current_state
    
    
    def get_menu_trail(self):
        return self.menu_trail
    
    
    def set_menu_trail(self, item):
        self.menu_trail.append(item)
        

    def get_main_menu_options(self):
        return self.main_menu_options
    

    def main_menu_engine(self):
        options = ["Rewrite paths", "Sync videos"]
    
    
    def get_next_action(self, input):
        print("got input ", input)
        print(self.menu_trail)
        if len(self.menu_trail) == 0 and input == "1":
            print("Next action should be", self.main_menu_options[int(input)])
            return self.main_menu_options[int(input)]