import printer
import cli_manager as cli
from state_manager import StateManager as State 
from config_manager import ConfigManager as Config

def configure_targets(state, config):
    printer.render_header("CONFIGURE TARGETS", "Add, update, or remove targets")
    
    target_list = config.get_target_list_options()
    display_names = []
    for item in target_list:
        display_names.append(item['display_name'])

    printer.render_menu("Target List", target_list)
    res = cli.get_input()


def video_transfer_menu(state, config):
    video_transfer_menu_options = ["Start Transferring", "Configure Targets"]
    
    printer.render_header("VIDEO TRANSFER", "Transfer video between two drives")
    
    # get all targets and status
    print("CURRENT CONFIGURED TARGETS")
    targets = config.get_target_list_options()
    for index, item in enumerate(targets):
        print(f"Target '{item['display_name']}' is enabled: {item['enabled']}")
    
    # print menu
    printer.render_menu("Video Transfer Menu", video_transfer_menu_options)
    res = cli.get_input()
    # for index, item in enumerate(video_transfer_menu_options):
    #     print(f"Target '{item['display_name']}' is enabled: {item['enabled']}")
    
    
    

def main_menu():
    state = State()
    config = Config()
    options = state.get_main_menu_options()
    printer.render_menu("Main Menu", options)
    
    response = cli.get_input()
    next_option = state.get_next_action(response)
    
    if next_option is "Configure":
        video_transfer_menu(state, config)


def welcome_screen():
    printer.render_header("NORTH MEDIA MANAGER", "A media management utility tool")

main_menu()