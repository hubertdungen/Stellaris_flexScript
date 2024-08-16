import sys
import os
import time
import string
import json
import shutil
# import pygame



# Declare IDs, Versions and Mode Variables
stellaris_id = "281990"          # This might need updating if Stellaris' game id changes
mod_id = "3038118849"            # This is the mod id that might need updating if the Mod id changes
flex_v = "2.1.0"                 # Flex Script version
flex_ab_v = "2.1.0"              # The real constant version of this FS Script
mod_v = "1"                      # Mod version
stellaris_v = "3.10.XX"          # Designed for Stellaris Version...
fs_set_st_v = None               # The version of "Designed for Stellaris Version" that was stored last time on the settings file  // This is intended for troubleshooting
virgin = True                    # Is it the first time FS is being run?
fs_mode = "NORMAL"                # NORMAL - Normal mode as it was intended to work /// RUSH - Fast mode, tries to run in the most autonomous & quick way /// DEBUG - Software Dev Mode  // SERVER - Server client ready
previous_fs_mode = "NORMAL"          # The mode that was previously of selecting the SERVER mode...


# Declare Folder Path Variables
game_directory = None         # Stellaris Game folder path
steam_mods_directory = None   # Steam Mods folder path
mod_directory = None          # Mod folder path

# Declare Mod Folderpath Variables
defines_van_folder_path = None  # Vanilla folder paths // paths that go into the folder where defines are at
species_van_folder_path = None
defines_mod_folder_path = None  # Mod folder paths
species_mod_folder_path = None 

# Declare Filepath Variables
defines_van_file_path = None  # Vanilla file paths // paths that go into the file path with the .txt
species_van_file_path = None
defines_mod_file_path = None  # Mod file paths 
species_mod_file_path = None 
fs_settings_present = False   # If fs_settings.js is on the same path of flexScript.exe

# Declare Booleans
optional_semi_search = False
tutorial_active = True
is_any_custom_none = True     # Check if any MPP customization variable is Null / None 
auto_update_enabled = False   # Turns auto-update on or off

## Declare General Variables
prompt = None
answer = None

## Declare Folder/File Path Keys
workshop_mod_key = "steamapps/workshop"
st_confirmation_key = "stellaris.exe"
descriptor_check = True
defines_name = "00_defines.txt"                     # The name of the file "00_define.txt"               // in case paradox changes it's name
species_arc_name = "00_species_archetypes.txt"      # The name of the file "00_species_archetypes..txt"  // in case paradox changes it's name


## Declare picks & points
ethos_max_points = None
civic_points_base = None
machine_trait_points = None
machine_max_traits = None
species_trait_points = None
species_max_traits = None

## Declare command dictionaries
p_yes = ["yes", "y", "p_yes"]
p_no = ["no", "n", "p_no"]
p_semi = ["semi", "semi-autonomous", "semiauto", "semiautonomous", "s", "p_semi"]
p_manual = ["manually", "manual", "alternative", "m", "p_manual"]
p_continue = ["", 'y', "yes", "continue", "next", "advance", "proceed", "agreed", "please", "yes, please", "ok", "okey", "avança", "execute", "run", "enter", "confirm", "a", "p_continue"]
p_cancel = ["cancel", "delete", "back", "return", "del", "none", "rewind", "stop", "undo", "go back", "c", "p_cancel"]
p_reset = ["reset", "retry", "replay", "reiniciar", "retentar", "r", "p_reset"]
p_help = ["help", "?", "I need help", "help me", "ajuda", "h", "p_help"]
p_tutorial = ["tutorial", "how to", "how to do this", "explanation", "t", "p_tutorial"]
p_quit = ["q", "quit", "exit", "shut", "shutdown", "turn off", "bye", "bye bye", "see ya", "p_quit"]
p_settings = ["settings", "config", "configuration file", "fs_settings"]
print_tut = ["print_tutorial", "print tutorial", "p_tutorial", "p tutorial"]


## Delcare headers
header = f"""
##################################################
#                                                #
#  Welcome to FLEX SCRIPT (FS):                  #
#  Enhancing your Stellaris MPP experience       #
#  "More Picks & Points: Traits|Civics|Ethics"   #
#  [FLEX EDITION]                                #
#                                                #
##################################################

## MPP v{mod_v} - FS v{flex_ab_v}
## Designed for Stellaris {stellaris_v}+
## Stellaris id: {stellaris_id} // MPP Mod id: {mod_id}

Flex Script, empowered by the community and crafted with care by Hubert Dungen,
and with the help of GPT 4, is your gateway to a tailored Stellaris adventure. 
Our script automates the customization of MPP, ensuring your galactic empire 
is uniquely yours.

Attention: MPP impacts both player and NPC Empires, enhancing genetic diversity and realism. 
It is designed for a richer gameplay experience, not as a cheat tool.

Discover my journey and other projects at: https://hubertdungen.com
To know more about this script visit: https://github.com/hubertdungen/Stellaris_flexScript
You can find MPP [FLEX EDITION] at: https://steamcommunity.com/workshop/filedetails/?id=3038118849
Support ongoing development and maintenance at: https://ko-fi.com/hubertkenobi


"MPP" stands for "More Picks & Points"
"FS" stands for "Flex Script"


Launching Flex Script... Please stand by.

--------------------------------------------------
"""


tutorial = """
##############################################
#                                            #
#          Flex Script Tutorial              #
#                                            #
##############################################

Welcome to Flex Script, your Stellaris MPP customization assistant. 
Here are some tips to ensure a smooth experience:

- User-Friendly Questions: The script asks clear, straightforward questions. 
  It intelligently interprets your responses, normalizing text and removing extra spaces.
  Responses have multiple valid forms for your convenience, some doesn't even appear on 
  the description suggestions but are intuitive.

- Sequential Approach: Simply follow the script's prompts one by one. 
  There's no need to rush; each step guides you through the customization process.
  
- You can cancel, reset, quit, tutorial or ask for help at any time just by writing that or similar.

- Autonomy in Detection: Flex Script autonomously detects paths for Stellaris installations and MPP mod folders.
  And its main task is to assist you in MPP mod customization, but will prompt for semi-autonomous or manual input when needed.

- Server Hosting Assistance: This script is tailored for server hosting, facilitating the sharing of mod customizations.
  Just ensure the executable and settings files are in the same folder. If possible, the script will handle the rest, 
  making multiplayer setup with friends a breeze.

- Semi-Automatic Mod Updates: Activate this feature in the settings to keep your mod updated accordingly to Stellaris updates. 
  With this, the script will automatically adapt to game updates, reducing your waiting time for manual mod maintenance.

For additional support or inquiries, consult the README on GitHub or ask on the Steam community page.

Here's to an enhanced and personalized Stellaris MPP experience!

##############################################
"""


## Declare Help texts 
help_parent = None
help_header = """
##############################################
#                                            #
#          Flex Script Help                  #
#                                            #
##############################################

Here are some tips of the {help_parent} menu:
    
"""

## Declare help texts
help_texts = {
    "find_game_folder": (
        "### Help: Find Game Files ###\n"
        "This function searches for the Stellaris game installation directory. "
        "\nIt checks common installation paths and tries to automatically locate the game."
    ),
    "find_mod_folder": (
        "### Help: Find Mod Files ###\n"
        "This function looks for the location of Stellaris mods within the Steam directory. "
        "\nIt aims to find where your Stellaris mods are stored for further customization."
    ),
    "semiautonomous_search_ui": (
        "### Help: Semi-Autonomous Search ###\n"
        "In this semi-autonomous mode, the software asks for a drive letter, then searches "
        "for a possible path for Stellaris or mods." 
        "\nYou should know in what driver your files are placed and then provide the driver letter."
        "\nThe search duration depends on drive size and contents."
    ),
    "insert_path_manually": (
        "### Help: Insert Path Manually ###\n"
        "This option allows you to manually input the full path of a file or directory. "
        "\n\n> Ensure the path is correctly typed and complete."
        "\n> Use this option if automatic or semi-automatic search methods fail to locate the desired path."
        "\n> Don't worry about the direction of slashes ('/') in the path;"
        "\n  the software automatically corrects them if they are inverted."
        "\n> It's not necessary to add or remove the trailing slash ('/');"
        "\n  the software automatically adjusts it for you."
    ),
    "help_prompt": (
        "### Help: Help Menu ###\n"
        "You already are at the \"Tutorial Menu\"... "
        "\nThere is no rush for this process, so you can just enter \"yes\" and go step by step."
        "\nYou can find detailed explanations at the following links:"
        "\n\nFLEX SCRIPT Github page: https://github.com/hubertdungen/Stellaris_flexScript"
        "\nMPP [FLEX EDITION] mod link at: https://steamcommunity.com/workshop/filedetails/?id=3038118849"
    ),
    "main_menu":(
        "### Help: Main Menu ###\n"
        "The main menu provides a central hub for navigating Flex Script's features. "
        "Here's a breakdown of the options available:\n"
        "1. Restart: Resets the entire path finding and customization process.\n"
        "2. Customization Menu: Access the customization interface for Stellaris MPP mod.\n"
        "3. Initial Header: Displays the initial header and information about Flex Script.\n"
        "4. Tutorial: Shows a detailed tutorial to guide new users through Flex Script.\n"
        "5. Settings: Modify script settings like mode (NORMAL, FAST, etc.) and update game/mod IDs.\n"
        "6. Update: Update mod files based on the latest game updates or customization changes.\n"
        "7. Prepare for Server Clients: Setup the script for server client use, optimizing for multiplayer game hosting.\n"
        "8. Quit: Exit Flex Script.\n\n"
        "Each option is designed to provide a specific functionality, from basic setup to advanced customization and preparation for server hosting."   
    ),
    "other": (
        "### Help: General ###\n"
        "This menu has no specific help function. Please navigate back to the previous menus "
        "\nand prompt 'help' for more info, or request a 'tutorial' for general guidance."
    )   
}

def display_main_menu_header():
    global fs_mode
    print("\n##############################################")
    print("#               Flex Script Menu             #")
    print("##############################################\n")
    print(f"# Mode: {fs_mode}\n")
    print("\nWelcome to the Flex Script main menu. Here you can:")
    print("1. RESTART:       Restart the path finding and customization process")
    print("                   \-> This will delete every value in settings!")
    print("2. CUSTOMIZE:     Go to the customization menu")
    print("3. CREDITS:       Show the initial FS header")
    print("4. TUTORIAL:      View the tutorial")
    print("5. SETTINGS:      Access settings")
    print("6. UPDATE:        Update mod files")
    print("7. SERVER MODE:   Prepare settings for server clients")
    print("8. QUIT:          Quit Flex Script\n")
    print("\n-- SAVE & LOAD --")
    print("9. Save Settings")
    print("10. Load Settings\n\n\n")


def display_server_mode_header():
    print("\n##############################################")
    print("#         Flex Script Server Mode Menu        #")
    print("##############################################\n")
    print("                                            ")
    print(" # All files are ready.                     ")
    print(" > You can quit and play Stellaris!         ")
    print("\n                                          ")
    print("\nServer Mode Active. Limited menu options:\n")
    print("1. Deactivate SERVER Mode                   ")
    print("2. Restart path and variable finding process")
    print("3. Quit Flex Script\n                       ")



 ### STRING OPERATORS ######################################################################


## String engineering    
def replace_slashes(input_string):
    return input_string.replace("\\", "/")


def separator_timer(timer):
    print("\n\n...\n\n")
    if timer != 0:
        custom_sleep(timer)
        

def separator_btimer(btimer, atimer):
    custom_sleep(btimer)
    print("\n\n...\n\n")
    custom_sleep(atimer)


def custom_sleep(duration):
    global fs_mode
    if fs_mode == "NORMAL":
        time.sleep(duration)
    elif fs_mode == "FAST":
        if duration <= 1:
            time.sleep(0.5)
        else:
            time.sleep(1)
    elif fs_mode == "SERVER":
        if duration <= 1:
            time.sleep(0.05)
        else:
            time.sleep(0.4)
    elif fs_mode in ["RUSH", "DEBUG"]:
        # time.sleep(0)  # No delay for RUSH, DEBUG, and SERVER modes
        if duration <= 1:
            time.sleep(0)
        else:
            time.sleep(0.2)


def print_sep(print_p, sep_timer):
    print(print_p)
    separator_timer(sep_timer)


def misspell_exception():
    separator_timer(1)
    print("You have entered characters, words or phrases other than those that this software is programmed to respond to.")
    separator_timer(1)
    print("Going back a few steps.")
    separator_timer(1)
    custom_sleep(2)
    return


## This is a function to detect the function name and turn it into a "history" string variable
def with_history(func):
    def wrapper(*args, **kwargs):
        # If 'history' is not already in kwargs, set it to the function's name
        if 'history' not in kwargs:
            kwargs['history'] = func.__name__
        return func(*args, **kwargs)
    return wrapper


###########################################################################################






 ### PATH FINDERS #########################################################################   

@with_history
def find_game_folder(history=None):
    """
    # Attempt to find the game directory, workshop content and necessary files
    """
    
    # DECLARE VARS
    global game_directory
    global optional_semi_search
    game_directory = None
    confirmation_file = st_confirmation_key
    searched_subject = st_confirmation_key
    path_conf = None
    optional_semi_search = False


    # Common paths where Steam and Stellaris might be installed
    common_game_paths = generate_game_paths()
    
    
    ## Debug Paths
    if fs_mode == "DEBUG": 
        for game_path in common_game_paths:
            print(f"{game_path}")
    
   
    # Attempt to find the Stellaris directory in common paths
    while True:   
        for path in common_game_paths:
            if os.path.exists(path):
                
                path = path_checker("Stellaris", path, confirmation_file)
                if path == None: return None
                
                
                while True:
                    game_directory = path
                    
                    print("### FLEX SCRIPT has detected a Stellaris game folder! ###")
                    print(f"\n### At: \"{game_directory}\"")
                    separator_timer(3)
                    
                    ## CALL PRIMARY PATH QUESTION
                    path_conf = primary_path_question("Stellaris installation" ,"You will provide the drive letter where you think Stellaris is installed, and FS will search there", history)

                    if path_conf in p_continue or path_conf == "1":                                                  # Assign automatic folder 
                        return game_directory
                        break
                    
                    elif path_conf in p_semi or path_conf == "2":   # Semi-automatic search
                        game_directory = None
                        optional_semi_search = True
                        break
                    
                    elif path_conf in p_manual or path_conf == "3":                             # Manually apply folder
                        game_directory = insert_path_manually("Stellaris installation", "\"C:/Program Files (x86)/Steam/steamapps/common/Stellaris/\"", "Please ensure you have provided the correct path.", "stellaris.exe")  # 1st var: Content  \\ 2nd var: PATH  \\ 3rd var: Exception error alert  \\ 4rd var: confirmation_file which can be Stellaris exe file f.ex.
                        separator_timer(1)
                        if game_directory == "cancel" or game_directory == None:
                            game_directory == None
                            continue
                        
                        return game_directory
                    
                    elif path_conf == "cancel":
                        main_updated()
                    elif path_conf == "help":
                        help_prompt(path_conf, history=history)
                    else: 
                        misspell_exception()
                      
        
        if game_directory is None:
            # If the initial search failed, or it was optionally selected, offer to semi-autonomous search in a specific drive
            separator_timer(0)
            while True:
                if optional_semi_search == False:   # If it failed to automatically search
                    print("### FLEX SCRIPT has failed to find the Stellaris path automatically! ###")
                    separator_timer(2)
                    
                    ## CALL SECONDARY PATH QUESTION
                    prompt = secondary_path_question("Stellaris installation", "You will provide the drive letter where you think Stellaris is installed, and FS will search there", history)
                    
                    if prompt in p_yes or prompt in p_semi or prompt == "1":
                        game_directory = semiautonomous_search_ui("Stellaris game", searched_subject, confirmation_file)
                        if game_directory == "cancel" or game_directory == None:
                            game_directory == None
                            continue
                        return game_directory
                        
                    elif prompt in p_manual or prompt in p_no or prompt in ["other", "2"]:
                        game_directory = insert_path_manually("Stellaris installation", "\"C:/Program Files (x86)/Steam/steamapps/common/Stellaris/\"", "Please ensure you have provided the correct path.", "stellaris.exe")  # 1st var: Content  \\ 2nd var: PATH  \\ 3rd var: Exception error alert  \\ 4rd var: confirmation_file which can be Stellaris exe file f.ex.
                        separator_timer(1)
                        if game_directory == "cancel" or game_directory == None:
                            game_directory == None
                            continue
                            
                        return game_directory
                    
                    elif prompt in ["retry", "redo", "go back", "back", "3"]:
                        continue
                    
                    elif prompt in p_cancel:
                        prompt == None
                        continue
                    
                    else:
                        misspell_exception()             
                        
                    
                else:                               # If semiauto was optionally chosen 
                    print("## You have selected semiautonomous Stellaris path search. ##")
                    optional_semi_search = False
                    game_directory = semiautonomous_search_ui("Stellaris", searched_subject, confirmation_file)
                    if game_directory == "cancel" or game_directory == None:
                        game_directory == None
                        continue
                    return game_directory
                
                
    return game_directory

 



@with_history
def find_mod_folder(history=None):
    """
    # Attempt to find the steam stellaris mod directory, workshop content and necessary files
    """
    
    # DECLARE GLOBAL VARS
    global stellaris_id
    global mod_id
    global steam_mods_directory
    global mod_directory
    global optional_semi_search

    
    # DECLARE VARS
    potential_path = None
    mod_directory = None
    confirmation_key = mod_id
    confirmation_folder = os.path.join(stellaris_id, mod_id)  
    path_conf = None
    optional_semi_search = False

    # Common paths where Steam and Stellaris might be installed
    common_mod_paths = generate_mod_paths(stellaris_id, mod_id)
        
    ## Debug Paths
    if fs_mode == "DEBUG": 
        for mod_path in common_mod_paths:
            print(f"{mod_path}")


    # Attempt to find the Stellaris directory in common paths

    while True:   
        for path in common_mod_paths:
            if os.path.exists(path):
                
                steam_mods_directory = path_checker("Stellaris MPP Mod folder", path, confirmation_key)
                if steam_mods_directory == None: potential_path = path ; break
                

                while True:
                    mod_directory = os.path.join(steam_mods_directory, confirmation_key)
                    
                    print("### FLEX SCRIPT has detected the Stellaris Mods and MPP Mod folder! ###")
                    print(f"\n### At: \"{mod_directory}\"")
                    separator_timer(3)
                    
                    path_conf = primary_path_question("MPP Mod folder" ,"You will provide the drive letter where Steam is installed, and FS will search for MPP Mod on that drive", history)
                    
                    if path_conf in p_continue or path_conf == "1":                                                  # Assign automatic folder
                        return mod_directory
                    
                    elif path_conf in p_semi or path_conf == "2":   # Semi-automatic search
                        mod_directory = None
                        optional_semi_search = True
                        break
                    
                    elif path_conf in p_manual or path_conf == "3":                             # Manually apply folder                      
                        mod_directory = insert_path_manually("Steamapps -> Workshop -> Content folder", "\"C:/Program Files (x86)/Steam/steamapps/workshop/content/", "Please ensure you have provided the correct \"Steam\" / \"steamapps/\" \"workshop/\" \"content/\" path.\nThis is not to insert the MPP's Mod path directly\nBut to point where the stellaris workshop mods are located.", confirmation_folder).strip()  # 1st var: Content  \\ 2nd var: PATH  \\ 3rd var: Exception error alert  \\ 4rd var: confirmation_file which can be Stellaris MPP folder f.ex.
                        separator_timer(1)
                        if mod_directory == "cancel":
                            mod_directory == None
                            continue
                        return mod_directory
                    
                    elif path_conf == "cancel":
                        main_updated()
                    elif path_conf == "help":
                        help_prompt(path_conf, history=history)
                    else: 
                        misspell_exception()
                      
        
        if mod_directory is None:
            # If the initial search failed, or it was optionally selected, offer to semi-autonomous search in a specific drive
            separator_timer(0)
            
            
            
            if potential_path is not None:
                
                print("### FLEX SCRIPT has failed to find the Stellaris MPP Mod path automatically! ###")
                separator_timer(2)
                print("But it found a folder that may have the mods with different IDs.")
                custom_sleep(2)
                
                while True: 

                    print(f"\nThis is the path FS has found: \n{path}")
                    print("\n\nPlease provide the id of Stellaris:")
    
                    
                    prompt = input(
                        "\n> Enter the ID - It will check if that ID is inside {path}."
                        "\n> Press Enter / manual / cancel / 2 - Will ask for you to insert the entire MPP Mod folder entirely."
                        "\n> retry / 3 - Will retry the fully autonomous search. (only useful if you have changed the Steam folder path"
                        "\n\n(ID/manual/retry) Answer:  " 
                    ).lower()
                    separator_timer(1)
                    
                    prompt = prompt_handler(answer, history)
                    
                    if prompt.strip().isdigit():
                        potential_path = os.path.join(potential_path, prompt)
                        path = path_checker("Steam Workshop Stellaris folder", potential_path, confirmation_key)
                        if path == None: continue
                            
                        
                        if potential_path is not None:
                            print("### FLEX SCRIPT has found the Stellaris Mods File! ###")
                            separator_timer(2)
                            print("Now let's automatically try checking the MPP folder...")
                            separator_timer(2)
                            
                            potential_path = os.path.join(potential_path, mod_id)
                            path = path_checker("MPP Mod folder", potential_path, "descriptor")
                            if path == None: potential_path = path; continue
                            
                            print("### FLEX SCRIPT successfully found the MPP Mod folder! ###")
                            separator_timer(2)
                            
                            return mod_directory
                    
                    
                    elif prompt in p_yes or prompt in p_continue or prompt in p_semi or prompt == "1":
                        mod_directory = semiautonomous_search_ui("Stellaris MPP Mod", stellaris_id, confirmation_key)
                        separator_timer(1)
                        if mod_directory == "cancel" or mod_directory == None:
                            mod_directory == None
                            continue
                        return mod_directory
                    
                    
                    elif prompt in ["retry", "redo", "go back", "back", "3"]:
                        continue
                    
                    elif prompt in p_cancel:
                        prompt == None
                        continue
                    
                    else:
                        misspell_exception()    
                                
            
            else:
                
                while True:
                    if optional_semi_search == False:   # If it failed to automatically search
                        print("### FLEX SCRIPT has failed to find the Stellaris MPP Mod path automatically! ###")
                        separator_timer(2)

                        ## CALL SECONDARY PATH QUESTION
                        prompt = secondary_path_question("Stellaris MPP Mod", "You will provide the drive letter where Steam is installed, and FS will search for MPP Mod on that drive.", history)
                      
                        if prompt in p_yes or prompt in p_continue or prompt in p_semi or prompt == "1":
                            mod_directory = semiautonomous_search_ui("Stellaris MPP Mod", stellaris_id, confirmation_key)
                            if mod_directory == "cancel" or mod_directory == None:
                                mod_directory == None
                                continue
                            return mod_directory
                            
                        elif prompt in p_manual or prompt in p_no or prompt in ["other", "2"]:
                            mod_directory = insert_path_manually("Steamapps -> Workshop -> Content folder", "\"C:/Program Files (x86)/Steam/steamapps/workshop/content/", "Please ensure you have provided the correct \"Steam\" / \"steamapps/\" \"workshop/\" \"content/\" path.\nThis is not to insert the MPP's Mod path directly\nBut to point where the stellaris workshop mods are located.", confirmation_folder).strip()  # 1st var: Content  \\ 2nd var: PATH  \\ 3rd var: Exception error alert  \\ 4rd var: confirmation_file which can be Stellaris MPP folder f.ex.
                            separator_timer(1)
                            if mod_directory == "cancel" or mod_directory == None:
                                mod_directory == None
                                continue                     
                            return mod_directory
                        
                        elif prompt in ["retry", "redo", "go back", "back", "3"]:
                            continue
                        
                        elif prompt in p_cancel:
                            prompt == None
                            continue
                        
                        else:
                            misspell_exception()             
                            
                        
                        
                    else:                               # If semiauto was optionally chosen 
                        print("## You have selected semiautonomous MPP Mod path search. ##")
                        optional_semi_search = False
                        mod_directory = semiautonomous_search_ui("Stellaris MPP Mod", stellaris_id, confirmation_key)
                        if mod_directory == "cancel" or mod_directory == None:
                            mod_directory == None
                            continue
                        
                        return mod_directory
                    
                
    return mod_directory    

    
    

    ## BACKUP CODE
    # if os.path.exists(steam_mods_directory):
    #     # List all game codes in the steam workshop content directory
    #     game_codes = os.listdir(steam_mods_directory)
        
    #     # Check if Stellaris game code exists
    #     if stellaris_id in game_codes:
    #         steam_mods_directory = os.path.join(steam_mods_directory, stellaris_id)
    #         mods = os.listdir(steam_mods_directory)
    #         if mods:  # if there's any mod folder
    #             print("Multiple mods detected. Please ensure you know the mod's specific code.")
    #             for mod in mods:
    #                 print(f"- {mod}")
    #             mod_code = input("Please enter this mod's specific code which should be \"3038118849\". The mod id is the suffix number of it's steam link.\nMod ID: ")
    #             return os.path.join(steam_mods_directory, mod_code)
    
    # # If the initial search failed, offer to search in a specific drive
    # search_drive = input("Failed to find the mod path automatically. Would you like to search a specific drive for the Stellaris installation? (yes/no): ").lower()
    

    # if search_drive == "yes":
    #     drive_letter = input("Enter the drive letter (e.g., D, E, F, etc.): ").upper()
    #     steamapps_path = search_subject_in_drive(drive_letter, "steamapps", descriptor_check=True)
    #     if steamapps_path:
    #         workshop_path = os.path.join(steamapps_path, "workshop", "content", stellaris_id)
    #         if os.path.exists(workshop_path):
    #             mods = os.listdir(workshop_path)
    #             if mods:  # if there's any mod folder
    #                 print("Multiple mods detected. This mod should be code number \"3038118849\". Please ensure you know the mod's specific code.")
    #                 print(", ".join(mods))
    #                 mod_code = input("Enter your mod's specific code: ")
    #                 return os.path.join(workshop_path, mod_code)
    #             else:
    #                 print("There are no mods on your stellaris folder. Please ensure you installed \"More Picks\" mod before running this script.")
    
    # # If all attempts fail, return None
    # return None
    




@with_history
def find_mod_files(mod_directory, history = None):
    
    global defines_name
    global species_arc_name
    global defines_mod_folder_path
    global species_mod_folder_path
    
    
    if fs_mode == "DEBUG": print(f"DEBUG_mod_files_0:  mod_directory:{mod_directory} // defines_name:{defines_name} // defines_mod_folder_path:{defines_mod_folder_path} // species_mod_folder_path:{species_mod_folder_path} // species_arc_name:{species_arc_name}\n\n")
    
    ## DETECT 00_defines.txt
    defines_mod_folder_path = path_file_checker("MPP Mod folder", mod_directory, defines_name)
    if defines_mod_folder_path:
        # Implement logic to assign the mod files
        # defines_mod_folder_path = os.path.join(mod_directory, defines_name)
        if fs_mode == "DEBUG": print(f"DEBUG_mod_files_1:  mod_directory:{mod_directory} // defines_name:{defines_name} // defines_mod_folder_path:{defines_mod_folder_path} // species_mod_folder_path:{species_mod_folder_path} // species_arc_name:{species_arc_name}\n\n")

    
    ## DETECT 00_species_archetypes.txt
    species_mod_folder_path = path_file_checker("MPP Mod folder", mod_directory, species_arc_name)
    if species_mod_folder_path:
        # Implement logic to assign the mod files
        # species_mod_folder_path = os.path.join(mod_directory, species_arc_name)
        if fs_mode == "DEBUG": print(f"DEBUG_mod_files_2:  mod_directory:{mod_directory} // defines_name:{defines_name} // defines_mod_folder_path:{defines_mod_folder_path} // species_mod_folder_path:{species_mod_folder_path} // species_arc_name:{species_arc_name}\n\n")

    
    if fs_mode == "DEBUG": print(f"DEBUG_mod_files_3:  mod_directory:{mod_directory} // defines_name:{defines_name} // defines_mod_folder_path:{defines_mod_folder_path} // species_mod_folder_path:{species_mod_folder_path} // species_arc_name:{species_arc_name}\n\n")

    

    return defines_mod_folder_path, species_mod_folder_path



@with_history
def find_game_files(game_directory, history = None):
    
    global defines_name
    global species_arc_name
    global defines_van_folder_path
    global species_van_folder_path
    
    
    if fs_mode == "DEBUG": print(f"DEBUG_mod_files_0:  game_directory:{game_directory} // defines_name:{defines_name} // defines_van_folder_path:{defines_van_folder_path} // species_van_folder_path:{species_van_folder_path} // species_arc_name:{species_arc_name}\n\n")
    
    ## DETECT 00_defines.txt
    defines_van_folder_path = path_file_checker("Stellaris Installation", game_directory, defines_name)
    if defines_van_folder_path:
        # Implement logic to assign the mod files
        if fs_mode == "DEBUG": print(f"DEBUG_mod_files_1:  game_directory:{game_directory} // defines_name:{defines_name} // defines_van_folder_path:{defines_van_folder_path} // species_van_folder_path:{species_van_folder_path} // species_arc_name:{species_arc_name}\n\n")

    
    ## DETECT 00_species_archetypes.txt
    species_van_folder_path = path_file_checker("Stellaris Installation", game_directory, species_arc_name)
    if species_van_folder_path:
        # Implement logic to assign the mod files
        if fs_mode == "DEBUG": print(f"DEBUG_mod_files_2:  game_directory:{game_directory} // defines_name:{defines_name} // defines_van_folder_path:{defines_van_folder_path} // species_van_folder_path:{species_van_folder_path} // species_arc_name:{species_arc_name}\n\n")

    
    if fs_mode == "DEBUG": print(f"DEBUG_mod_files_3:  game_directory:{game_directory} // defines_name:{defines_name} // defines_van_folder_path:{defines_van_folder_path} // species_van_folder_path:{species_van_folder_path} // species_arc_name:{species_arc_name}\n\n")

    

    return defines_van_folder_path, species_van_folder_path




def define_van_files_path():
    # Declare globals
    global defines_van_folder_path
    global species_van_folder_path
    global defines_van_file_path
    global species_van_file_path
    global defines_name
    global species_arc_name
    
    # Paths to the mod files
    defines_van_file_path = os.path.join(defines_van_folder_path, defines_name)
    species_van_file_path = os.path.join(species_van_folder_path, species_arc_name) 
    
    print(f"Assigned defines vanilla file path at: \"{defines_van_file_path}\"")
    print(f"Assigned species vanilla file path at: \"{species_van_file_path}\"")
    separator_timer(2)

    


def define_mod_files_path():
    # Declare globals
    global defines_mod_folder_path
    global species_mod_folder_path
    global defines_mod_file_path
    global species_mod_file_path
    global defines_name
    global species_arc_name
    
    # Paths to the mod files
    defines_mod_file_path = os.path.join(defines_mod_folder_path, defines_name)
    species_mod_file_path = os.path.join(species_mod_folder_path, species_arc_name) 
    
    

    





###########################################################################################    
    








 ### SEARCH ENGINEERS & PATH INJECTORS ####################################################       

@with_history
def semiautonomous_search_ui(subject, searched_subject, confirmation_path, history=None):
   
    ## Declaring vars
    path = None
    global prompt
    global optional_semi_search
    optional_semi_search = True 
   
    
    while True:

            
            ## Confirming the user wants to continue
            separator_timer(0)
            print("### WARNING! ###")
            custom_sleep(1)
            print("\n\n### For your information, this process may take sometime. ###\n")
            custom_sleep(2)
            
            ## Proceed confirmation
            prompt = proceed_confirmation(history)
            if prompt in p_cancel or prompt in p_no:
                return "cancel"
            ###############################
            
            
            separator_timer(1)
            
            print("### INITIATING SEMI-AUTONOMOUS PROCESS ###")
            separator_timer(2)
            print("\n### STEP ONE \nEnter the drive letter\n\n(e.g., C, D, E, F, etc.)")
            # custom_sleep(1)
            drive_letter = input("\nDrive Letter: ").upper().strip()
            separator_timer(1)
            
            
            ## PATH AUTO SEARCH ON DRIVE
            # 'path' has the full file path including the file name
            path = search_subject_in_drive(drive_letter, searched_subject, descriptor_check=True)
            
            
            ## DEBUG 1
            if fs_mode == "DEBUG": print(f"DEBUG1: path:{path} // subject:{subject} // history:{history} // drive_letter:{drive_letter} // optional_semi_search:{optional_semi_search} // confirmation_path:{confirmation_path}")

            
            # Check if a path was found
            if path is not None:
                # If the path is a file, get the directory name
                if os.path.isfile(path):
                    path = os.path.dirname(path)
            
                # Ensure there is a trailing slash
                if not path.endswith(os.sep):
                    path += os.sep
            
            
            ## DEBUG 2
            if fs_mode == "DEBUG": print(f"DEBUG2: path:{path} // subject:{subject} // history:{history} // drive_letter:{drive_letter} // optional_semi_search:{optional_semi_search} // confirmation_path:{confirmation_path}")
 

            
            
            
            try:
                print("### STEP TWO")
                # custom_sleep(1)
                
                print(f"\nSearching for {subject} on the drive {drive_letter}...")
                if fs_mode == "DEBUG": print(f"\nWith the following searched_subject: {searched_subject}\nAnd the following history:{history}")
                
                if path is not None:
                    

                    separator_timer(0)
                    print("### STEP THREE\n")
                    # custom_sleep(1)
                    
                    print(f"Directory of {subject} found at {path}...")
                    separator_timer(2)
                    
                    
                    print("### STEP FOUR\n")
                    # custom_sleep(1)
                    
                    print("Checking for path integrity...")
                    separator_timer(2)
                    
                    path = path_checker(subject, path, confirmation_path)
    
                    print("Thinking...")
                    
                    separator_timer(2)
                    return path
                
                separator_timer(1)
                print("### ERROR: PATH NOT FOUND")
                custom_sleep(1)
                print (f"\nThe SEMI-AUTONOMOUS Process could not find any path related to {subject} on the \"{drive_letter}\" drive")
                separator_timer(3)
                print("Returning...")
                separator_timer(1)
                return None
            
            except:
                separator_timer(1)
                print("### ERROR: PATH ###")
                custom_sleep(1)
                print("\nThere was an error while trying to assign the directory path...")
                custom_sleep(1)
                print("\nTry again or try the manual method.")
                
                return "cancel"

   
     
    
# Method to insert stellaris or mod paths manually   
@with_history                  
def insert_path_manually(subject_var, text_path, text_exception, confirmation_path, history=None):
    """
    Allows the user to manually enter a directory path and retries if the path is invalid.
    """
    separator_timer(0)
    print(f"You chose to insert the {subject_var} path manually...")
    separator_timer(1)

    while True:
        

        print(f"Please, enter the directory path of {subject_var}.")
        path = input(f"\nThe path should look something similar to this: \n{text_path} \n \n\nPath: ").strip()
        path = replace_slashes(path)
        
        
        ## DEBUG 1
        if fs_mode == "DEBUG": print(f"DEBUG1: path:{path} // history:{history} // subject_var:{subject_var} // text_path:{text_path} // text_exception:{text_exception} // confirmation_path:{confirmation_path}")

        
        ## ASKING FOR THE PATH
        ## Prompt handler
        path = prompt_handler(path, history=history)
        if path == "cancel": return "cancel"
        ####################################
        
        
        
        ## DEBUG 2
        if fs_mode == "DEBUG": print(f"DEBUG2: path:{path} // history:{history} // subject_var:{subject_var} // text_path:{text_path} // text_exception:{text_exception} // confirmation_path:{confirmation_path}")

        
        separator_timer(1)
        print(f"The path you have inserted looks like this:\n.\n{path}\n.\n")
        
        
        ## ASKING FOR CONFIRMATION THE PATH
        ## Proceed confirmation
        prompt = proceed_confirmation(history)
        if prompt in p_cancel or prompt in p_no:
            return "cancel"
        ###############################
        
        separator_timer(1)
        
        ## DEBUG 3
        if fs_mode == "DEBUG": print(f"DEBUG3: path:{path} // history:{history} // subject_var:{subject_var} // text_path:{text_path} // text_exception:{text_exception} // confirmation_path:{confirmation_path}")

        
        
        if os.path.exists(path):
            separator_timer(0)
            print("\nThe path you provided has no spelling mistakes and it exists.")
            separator_timer(1)
            
            path = path_checker(subject_var, path, confirmation_path)
            
            ## DEBUG 4
            if fs_mode == "DEBUG": print(f"DEBUG4: path:{path} // history:{history} // subject_var:{subject_var} // text_path:{text_path} // text_exception:{text_exception} // confirmation_path:{confirmation_path}\n\n")

            
            if path is None:
                continue
            else:
                return path
            
        else:
            separator_timer(0)
            print(f"\n{text_exception}")
            separator_timer(1)

        print("The path you provided doesn't exist or is incorrect. \n\nDo you want to try entering the path again or go back in the process?")
        answer = input("\n\n(yes/return):  ").lower().strip()
        
        ## Prompt handler
        answer = prompt_handler(path, "insert_path_manually")
        if answer == "cancel": return "cancel"
        ####################################
        

            
    # Example usage
    # insert_path_manually('game', 'E:/Games/Game/', 'Invalid path. Please try again.', 'game.exe')    





    
###########################################################################################




        

 ### SMART PATH HANDLING & OPERATORS #########################################################


## Check if a path has the content files of folders accordingly to what is supposed to 
def path_checker(subject, path, confirmation_path):
    """
    Check if a path has the content files of folders accordingly to what is supposed to.
    
    Parameters:
    subject (str): The subject name that will appear on the prints.
    path (str): The path it's checking.
    confirmation_path (str): The confirmation key to check if there is this path within the "path".
    
    Returns:
    str: Returns "path" if it succeeds. Otherwise "None".
    """
        
    
    print(f"Checking if the path: \"{path}\" is related to {subject} \nand if it has {confirmation_path} in it")
    separator_timer(2)
    
    if os.path.exists(os.path.join(path, confirmation_path)):
        print(f"\nThe path has {confirmation_path} in it!")
        separator_timer(1)
        print("\nSelecting this path successfully!")
        separator_timer(1)
        return path
    else:
        print("!!! ERROR !!!")
        print(f"\nThe path that was provided has no {confirmation_path} and may not be associated with {subject}.")
        separator_btimer(1,1)
        print("# POSSIBLE ISSUES #")
        custom_sleep(1)
        print("\nEither you entered the wrong path or the folder is faulty.")
        custom_sleep(1)
        print("\nCheck your folders again and the path you provided to make sure you're entering the right {subject} folder...")
        separator_btimer(3,1)
        return None
    
## Check if a path has the content files of folders accordingly to what is supposed to 
def path_file_checker(subject, path, confirmation_path):
    print(f"Checking within {path} for {confirmation_path} related to {subject}.")
    separator_timer(2)

    # Check within subdirectories
    for dirpath, dirnames, filenames in os.walk(path):
        if confirmation_path in dirnames or confirmation_path in filenames:
            print(f"\nFound {confirmation_path} within {dirpath}")
            separator_timer(2)
            return dirpath

    # If confirmation_path is not found
    print("!!! ERROR !!!")
    print(f"\nNo {confirmation_path} found in any subdirectories of {path} related to {subject}.")
    separator_btimer(1,1)
    print("\nEither the path is incorrect or the specific file/folder is missing.")
    separator_btimer(3,1)
    return None



## Search a path inside a hard drive 
def search_subject_in_drive(drive_letter, search_subject, descriptor_check=True):
    """
    Search for the subject folder in the specified drive.
    """

    # Construct the base path for the drive
    base_path = f"{drive_letter}:/"
    global workshop_mod_key
    
    
    directories_to_skip = ["System Volume Information", "$Recycle.Bin", "Windows", 
                           "AppData", "Users", "Recovery", "Boot", "$WinREAgent",
                           "downloading", "shadercache", "temp"]
    
    
    if fs_mode == "DEBUG": print(f"DEBUG0:  drive_letter:{drive_letter} // search_subject:{search_subject} // stellaris_id:{stellaris_id} // descriptor_check:{descriptor_check}")
    
    # Walk through the directories to find search_subject



    try: 
        for dirpath, dirnames, filenames in os.walk(base_path):
            if any(skip_dir in dirpath for skip_dir in directories_to_skip):
                continue
            
  
            if fs_mode == "DEBUG" and stellaris_id in dirpath: print(f"DEBUG1:  Currently checking: dirpath:{dirpath}")  # Debug print
            # if fs_mode == "DEBUG" and stellaris_id in dirpath: print(f"DEBUG2:  Currently checking: dirname:{dirnames}\n")  # Debug print


            # Check if dirpath ends with the search_subject
            if dirpath.endswith(search_subject):

                return dirpath  # Return the path if conditions are met


            # Check if the directory name matches search_subject
            if search_subject in dirnames:
                potential_path = os.path.join(dirpath, search_subject)
                if workshop_mod_key and workshop_mod_key not in dirpath:
                    continue  # Skip if stellaris_id is not in the path
                if descriptor_check and not os.path.exists(os.path.join(potential_path, "descriptor.txt")):
                    continue  # Skip if descriptor.txt is not found in the directory
                return potential_path  # Return the path if it's a directory

            # Check if the file name matches search_subject
            if search_subject in filenames:
                potential_file_path = os.path.join(dirpath, search_subject)
                return potential_file_path  # Return the path if it's a file


        if fs_mode == "DEBUG" and stellaris_id in dirpath: print(f"DEBUG1:  dirpath: {dirpath} // drive_letter:{drive_letter} // search_subject:{search_subject} // descriptor_check:{descriptor_check}")  # Debug print    
        separator_timer(1)    

    
    except PermissionError:
        # Catch any permission exception that might occur during the os.walk
        separator_timer(0)
        print("### PERMISSION ERROR ###")
        custom_sleep(1)
        print(f"Permission denied: {dirpath}")        
    
    except Exception as e:
        # Catch any exception that might occur during the os.walk
        separator_timer(0)
        print("### EXCEPTION ERROR ###")
        custom_sleep(1)
        print(f"An error occurred while searching for {search_subject}: \n\n{e}")
        separator_timer(2)
        
    return None  # Return None if the search_subject was not found
    




## Generate the paths for stellaris possible folders
def generate_game_paths():
    # List of potential drive letters (C through Z)
    drive_letters = string.ascii_uppercase[2:26]

    # Patterns for game paths under different directories
    game_path_patterns = [
        "/Program Files (x86)/Steam/steamapps/common/Stellaris/",
        "/Program Files/Steam/steamapps/common/Stellaris/",
        "/Steam/steamapps/common/Stellaris/",
        "/Games/Steam/steamapps/common/Stellaris/",
        "/SteamLibrary/steamapps/common/Stellaris/"
    ]

    common_game_paths = []

    # Generate full paths for each combination of drive letter and path pattern
    for letter in drive_letters:
        for pattern in game_path_patterns:
            path = f"{letter}:{pattern}"
            common_game_paths.append(path)

    return common_game_paths    

# # Example usage
# common_game_paths = generate_game_paths()
# for path in common_game_paths:
#     if os.path.exists(path):
#         print(f"Stellaris directory found at: {path}")
#         break
# else:
#     print("Stellaris directory not found in common locations.")    


## Generate the paths for steam stellaris mods possible folders
def generate_mod_paths(stellaris_id, mod_id):
    # List of potential drive letters (C through Z)
    drive_letters = string.ascii_uppercase[2:26]

    # The common patterns for Steam workshop mod paths
    # 281990 is the app ID for Stellaris
    # Patterns for mod paths under different directories
    mod_path_patterns = [
        f"/Steam/steamapps/workshop/content/{stellaris_id}/",  # Default Steam installation
        f"/Program Files (x86)/Steam/steamapps/workshop/content/{stellaris_id}/",
        f"/Program Files/Steam/steamapps/workshop/content/{stellaris_id}/",
        f"/Games/Steam/steamapps/workshop/content/{stellaris_id}/",  # Common custom Steam library
        f"/SteamLibrary/steamapps/workshop/content/{stellaris_id}/",  # Default on separate drives
        # Add more custom patterns if you have specific ones in mind
    ]
    common_mod_paths = []

    # Generate full paths for each combination of drive letter and mod path pattern
    for letter in drive_letters:
        for pattern in mod_path_patterns:
            path = f"{letter}:{pattern}"
            common_mod_paths.append(path)

    return common_mod_paths





    
###########################################################################################




        
        
        
        
        


    
    
        











 ### PROMPT OPERATORS #####################################################################   
    
 

def prompt_handler(prompt, history):        ## This will ask for a prompt and for the name of the method from where it comes from
    prompt_result = reset(prompt)
    if prompt_result is not None:
        return prompt_result

    prompt_result = shutdown(prompt)
    if prompt_result is not None:
        return prompt_result

    prompt_result = cancel_message(prompt)
    if prompt_result is not None:
        return prompt_result

    # if "help_prompt" not in history: prompt_result = help_prompt(prompt)
    prompt_result = help_prompt(prompt)
    if prompt_result is not None:
        return prompt_result

    return prompt  # return the original prompt if none of the handlers matched


def cancel_message(prompt):
    if prompt in p_cancel:
        separator_timer(1)
        print("You have canceled the process")
        separator_btimer(2,1)
        print("Returning...")
        separator_timer(1)
        return "cancel"    
    else:
        return prompt

def reset(prompt):
    if prompt in p_reset:
        separator_timer(1)
        print("### RESETTING! ###")
        separator_timer(2)
        main_updated()
    else:
        return prompt
        
def shutdown(prompt):
    if prompt in p_quit:
        separator_timer(1)
        print("### SHUTING DOWN! ###")
        separator_timer(1)
        print("### See ya! I hope FLEX SCRIPT helped you!")
        custom_sleep(3)
        sys.exit()
    else:
        return prompt

@with_history      
def help_prompt(prompt, history):
    # First, check if prompt is not None and is a string
    
    global help_parent  # Declare help_parent as global if it's intended to be used outside this function
    
    # Debug print
    if fs_mode == "DEBUG": print(f"Debug: history is {history}")
    
    # Check if history is not None and is a string
    if history and isinstance(history, str):
        help_parent = history.replace("_", " ").title().strip()
        
        
        # Debug print
        if fs_mode == "DEBUG": print(f"Debug: help_parent is set to {help_parent}")
        
        if prompt in print_tut:
            print(tutorial)
            custom_sleep(2)
            ## Proceed confirmation
            prompt = proceed_confirmation(history)
            if prompt in p_cancel or prompt in p_no:
                prompt = "cancel"
                return "cancel"
            ###############################
            separator_timer(1)
            
            prompt == "p_tutorial"
            return prompt 
        
        elif prompt in p_manual or prompt in p_semi:
            return prompt
        
        elif prompt in p_tutorial:
            separator_timer(1)
            print("### CALM DOWN! ###")
            separator_timer(1)
            print("### DID YOU JUST ASK FOR A TUTORIAL? ###")
            separator_timer(1)
            print("### SO THAT'S WHY I'M HERE! ###")
            separator_timer(1)
            print("### LET ME SHOW YOU SMALL TIPS ;) ###")
            separator_timer(1)
            print(tutorial)
            custom_sleep(6)
            
            ## Proceed confirmation
            prompt = proceed_confirmation(history)
            if prompt in p_cancel or prompt in p_no:
                return "cancel"
            ###############################
            separator_timer(1)
            
            return prompt

        elif prompt in p_help:
            separator_timer(1)
            print("### CALM DOWN! ###")
            separator_timer(1)
            print("### DID YOU JUST ASK FOR A HELP? ###")
            separator_timer(1)
            print("### SO THAT'S WHY I'M HERE! ###")
            separator_timer(1)
            print("### LET ME SHOW YOU SMALL TIPS ABOUT THIS MENU ###")
            separator_timer(1)

            # Debug print
            if fs_mode == "DEBUG": print(f"Debug: help_parent is set to {help_parent}")

            help_text = help_texts.get(history, "No specific help available for this menu.")
            # Format and print the help_header here, where it uses the current value of help_parent
            print(help_header.format(help_parent=help_parent))
            print(help_text)
            # Rest of the function...
            
            # Debug print
            if fs_mode == "DEBUG": print(f"Debug: help_parent is set to {help_parent}")

            
            ## Proceed confirmation
            prompt = proceed_confirmation(history)
            if prompt in p_cancel or prompt in p_no:
                return "cancel"
            ###############################
            
            return "help_shown"
        
        else:
            print("### ERROR WHILE TRYING TO CALL FOR HELP ###")
            return prompt
    else:
        help_parent = "Unknown Context"  # Fallback value

    
def proceed_confirmation(history):
    while True:
        # PROCEED CONFIRMATION
        if fs_mode != "SERVER":
            prompt = input('\nDo You Want To Proceed? \n\n(yes/no) Answer: ').lower().strip() 
            
            prompt = prompt_handler(prompt, history)
            
            if prompt in p_continue or prompt in p_yes:
                separator_timer(1)
                return prompt
            
            elif prompt in p_cancel or prompt in p_no:
                separator_timer(0)
                print("### CANCELING THE PROCESS ###")
                separator_timer(1)
                return "cancel"
            
            elif prompt in p_help or prompt in p_tutorial:
                help_prompt(prompt, history=history)
                continue
                
            else:
                separator_timer(0)
                print("Unrecognized input. Please answer with 'yes' or 'no'.")
                separator_timer(1)
        else:
            print_sep("SERVER mode is active. Auto accepting...", 1)
            return "yes"
            


## IF FS DETECTS THE PATH AUTONOMOUSLY
def primary_path_question(subject, semi_description, history):
    
    print(f"Shall we assign that path? Is it the correct {subject} path?")
    if fs_mode != "SERVER":
        path_conf = input(
            "\n> Press Enter / yes / 1 - Will assign this detected path"
            f"\n> semi / 2 - Will initiate a semi-autonomous search for the {subject}. \n  {semi_description}."
            "\n> manual / 3 - Will ask for you to insert the Stellaris Mods path manually."
            "\n\n(yes/semi/manual) Your answer: " 
        ).lower().strip()
    else:
        print_sep("\nSERVER mode is active. Auto accepting...", 1)
        path_conf = "yes"
    separator_timer(1)
    
    path_conf = prompt_handler(path_conf, history)
    
    return path_conf



## IF FS FAILS TO DETECT THE PATH AUTONOMOUSLY 
def secondary_path_question(subject, semi_description, history):
    
    print("Would you like to follow a semi-autonomous way starting by searching a specific drive for the {subject} path or do you want to insert it manually?")
    path_conf = input(
        "\n> semi / 1 - Will initiate a semi-autonomous search for the Stellaris folder. \n  {semi_description}."
        "\n> manual / 2 - Will ask for you to insert the path manually."
        "\n> retry / 3 - Will retry the fully autonomous search. \n  (only useful if you have changed installation folder path)"
        "\n\n(semi/manual/retry) Your answer:  " 
    ).lower().strip()
    separator_timer(1)
    
    path_conf = prompt_handler(path_conf, history)
    
    return path_conf



## SUCCEEDED MESSAGE
def assigning_path_suc_message(path):
    print(f"### Successful path registration! \n\n### Assigned at: \"{path}\"")
    separator_timer(2)



## UNSUCCESSFUL MESSAGE
def assigning_path_unc_message(subject):
    print(f"### There was a problem registering {subject} path! \n\n### You can try to register it manually after this process via the menu...")
    print("Or you can ask for help on the steam MPP mod link at: \n\n# https://steamcommunity.com/workshop/filedetails/?id=3038118849")
    separator_timer(3)


## FIRST TIME RUNNING THIS FS?
def first_time_run_prompt():
    global virgin
    if virgin is True:
        print("This is the first time this software is being run on your computer!")
        separator_timer(3)
        print("Or maybe you just deleted the settings file...")
        separator_timer(3)
        print("Or the settings file isn't on the same folder as the .exe FS file...")
        separator_timer(3)
        print("Anyways \"at least it seems\" this is the first time you are running this file, so...")
        separator_timer(4)
        print("Maybe this is a good time for reading some FS tips!")
        separator_timer(2)
        print("Here they are!")        
        separator_timer(2)
        prompt = help_prompt("p_tutorial")
        if prompt in p_cancel or prompt in p_no:
            shutdown("quit")
        
        virgin = False
        return



###########################################################################################













 ### MPP CUSTOMIZATION  ###################################################################
 
 

def set_default_values(mode="vanilla"):
    """
    Return default values based on mode (either "vanilla" or "mod").
    """
    if mode == "vanilla":
        return {
            "ETHOS_MAX_POINTS": 3,
            "GOVERNMENT_CIVIC_POINTS_BASE": 2,
            "machine_trait_points": 1,
            "machine_max_traits": 5,
            "species_trait_points": 2,
            "species_max_traits": 5
        }
    elif mode == "standard":  # standard mode / mod defaults
        return {
            "ETHOS_MAX_POINTS": 5,
            "GOVERNMENT_CIVIC_POINTS_BASE": 5,
            "machine_trait_points": 4,
            "machine_max_traits": 8,
            "species_trait_points": 5,
            "species_max_traits": 8
        }
    elif mode == "beast": # BEAST mode
        return {
            "ETHOS_MAX_POINTS": 6,
            "GOVERNMENT_CIVIC_POINTS_BASE": 6,
            "machine_trait_points": 5,
            "machine_max_traits": 6,
            "species_trait_points": 9,
            "species_max_traits": 8
        }
    else:
        return None




def modify_value_in_file(file_path, key, new_value):
    """
    Search for a specific key in the file and update its value.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Look for the pattern (e.g., "@machine_trait_points =") and replace its value
    lines = content.split("\n")
    for index, line in enumerate(lines):
        if key in line:
            lines[index] = f"{key} = {new_value}"
            break

    # Save modified content
    with open(file_path, 'w') as file:
        file.write("\n".join(lines))



def modify_mod_files_with_defaults(mode):
    """
    Update the mod files with default values based on mode.
    """
    
    
    
    define_mod_files_path()
    values = set_default_values(mode)
    assign_custom_mpp_vars(mode)
    
    # Modify 00_defines.txt
    modify_value_in_file(defines_mod_file_path, "ETHOS_MAX_POINTS", values["ETHOS_MAX_POINTS"])
    modify_value_in_file(defines_mod_file_path, "GOVERNMENT_CIVIC_POINTS_BASE", values["GOVERNMENT_CIVIC_POINTS_BASE"])
    
    # Modify 00_species_archetypes.txt
    modify_value_in_file(species_mod_file_path, "@machine_trait_points", values["machine_trait_points"])
    modify_value_in_file(species_mod_file_path, "@machine_max_traits", values["machine_max_traits"])
    modify_value_in_file(species_mod_file_path, "@species_trait_points", values["species_trait_points"])
    modify_value_in_file(species_mod_file_path, "@species_max_traits", values["species_max_traits"])
    
    separator_timer(1)
    print(f"MPP Mod files have been modified with the {mode} preset!")
    separator_timer(1)



def modify_mod_files_custom():
    """
    Modify the mod files based on user's custom input.
    """
    # # Paths to the mod files
    # defines_path = os.path.join(mod_path, "common", "defines", "00_defines.txt")
    # species_path = os.path.join(mod_path, "common", "species_archetypes", "00_species_archetypes.txt")
    
    define_mod_files_path()
    
    # Gather user input for customization
    ethos_max_points = int(input("Enter number of ETHOS_MAX_POINTS (vanilla is 3).\n\nValue: "))
    civic_points_base = int(input("\nEnter number of GOVERNMENT_CIVIC_POINTS_BASE (vanilla is 2).\n\nValue: "))
    machine_trait_points = int(input("\nEnter number of machine_trait_points (vanilla is 1).\n\nValue: "))
    machine_max_traits = int(input("\nEnter number of machine_max_traits (vanilla is 5).\n\nValue: "))
    species_trait_points = int(input("\nEnter number of species_trait_points (vanilla is 2).\n\nValue: "))
    species_max_traits = int(input("\nEnter number of species_max_traits (vanilla is 5).\n\nValue: "))
    
    # Modify 00_defines.txt
    modify_value_in_file(defines_mod_file_path, "ETHOS_MAX_POINTS", ethos_max_points)
    modify_value_in_file(defines_mod_file_path, "GOVERNMENT_CIVIC_POINTS_BASE", civic_points_base)
    
    # Modify 00_species_archetypes.txt
    modify_value_in_file(species_mod_file_path, "@machine_trait_points", machine_trait_points)
    modify_value_in_file(species_mod_file_path, "@machine_max_traits", machine_max_traits)
    modify_value_in_file(species_mod_file_path, "@species_trait_points", species_trait_points)
    modify_value_in_file(species_mod_file_path, "@species_max_traits", species_max_traits)
    
    separator_timer(1)
    print("Mod files modified with custom values successfully!")
    separator_timer(2)
    if virgin:
        print("You can now share the settings file with your friends!")
        separator_timer(2)
        print("But if you are creating a server, prepare this flexScript turning it into: SERVER MODE.")
        separator_timer(3)
        print("You can do it on the Flex Script Menu...")
        separator_timer(2)
    
    
## Assign mod custom variables to their actual global variables
def assign_custom_mpp_vars(mode):
     
    global defines_van_file_path, species_van_file_path
    global defines_mod_file_path, species_mod_file_path
    global defines_van_folder_path, species_van_folder_path
    global defines_mod_folder_path, species_mod_folder_path
    global ethos_max_points, civic_points_base, machine_trait_points
    global machine_max_traits, species_trait_points, species_max_traits
    
    values = set_default_values(mode)
    if values != None:
        ethos_max_points     =  values["ETHOS_MAX_POINTS"]
        civic_points_base    =  values["GOVERNMENT_CIVIC_POINTS_BASE"]
        machine_trait_points =  values["machine_trait_points"]
        machine_max_traits   =  values["machine_max_traits"]
        species_trait_points =  values["species_trait_points"]
        species_max_traits   =  values["species_max_traits"]
    else:
        print("### ERROR VARIABLES REGISTER\n\nSomething went wrong while assigning the custom values to the variables...")
        separator_timer(3)
        print("Returning...")
        separator_timer(1)
        return None

    
    
    

def display_customization_header():
    print("\n#####################################################")
    print("#            Stellaris MPP Mod Customization        #")
    print("#####################################################\n")
    print("This menu allows you to customize various aspects of the Stellaris MPP mod.")
    print("You can choose 'vanilla' for default game settings, 'standard' for mod default presets,")
    print("'custom' to manually enter your preferred settings, 'reset' to attempt loading")
    print("the saved settings (if possible) and 'return' to cancel and skip this step.")
    print("\nPlease note that choosing 'custom' will prompt you to input values for each setting.")
    print("Refer to the displayed tables for Vanilla and Standard values as a guide.")
    print("\n")

    
def display_values_table():
    print("Vanilla Values:")
    print("- ETHOS_MAX_POINTS: 3")
    print("- GOVERNMENT_CIVIC_POINTS_BASE: 2")
    print("- Machine Trait Points: 1")
    print("- Biological Trait Points: 2")
    print("- Max Machine Traits: 5")
    print("- Max Biological Traits: 5")

    print("\nStandard (Mod Default Preset) Values:")
    print("- ETHOS_MAX_POINTS: 5")
    print("- GOVERNMENT_CIVIC_POINTS_BASE: 5")
    print("- Machine Trait Points: 4")
    print("- Biological Trait Points: 5")
    print("- Max Machine Traits: 8")
    print("- Max Biological Traits: 8")
    
    print("\nBEAST (Mod Default Preset) Values:")
    print("- ETHOS_MAX_POINTS: 6")
    print("- GOVERNMENT_CIVIC_POINTS_BASE: 6")
    print("- Machine Trait Points: 5")
    print("- Biological Trait Points: 6")
    print("- Max Machine Traits: 9")
    print("- Max Biological Traits: 8")

    
    

####################################################################################










### LOADING AND SAVING METHODS  ####################################################


## Saving...
def save_settings():
    settings = {
        "stellaris_id": stellaris_id,
        "mod_id": mod_id,
        "flex_v": flex_v,
        "mod_v": mod_v,
        "fs_designed_to_stellaris_v": stellaris_v,
        "defines_name": defines_name,
        "species_arc_name": species_arc_name,
        "game_directory": game_directory,
        "steam_mods_directory": steam_mods_directory,
        "mod_directory": mod_directory,
        "defines_van_file_path": defines_van_file_path,
        "species_van_file_path": species_van_file_path,
        "defines_mod_file_path": defines_mod_file_path,
        "species_mod_file_path": species_mod_file_path,
        "defines_van_folder_path": defines_van_folder_path,
        "species_van_folder_path": species_van_folder_path,
        "defines_mod_folder_path": defines_mod_folder_path,
        "species_mod_folder_path": species_mod_folder_path,
        "fs_mode": fs_mode,
        "previous_fs_mode": previous_fs_mode,
        "auto_update_enabled": auto_update_enabled,
        "ethos_max_points": ethos_max_points,
        "civic_points_base": civic_points_base,
        "machine_trait_points": machine_trait_points,
        "machine_max_traits": machine_max_traits,
        "species_trait_points": species_trait_points,
        "species_max_traits": species_max_traits,
        "virgin": virgin
    }

    with open('fs_settings.json', 'w') as f:
        json.dump(settings, f, indent=4)
    
    separator_timer(0)
    print("Settings saved successfully!")
    separator_timer(2)


## Loading...
def load_settings():
    global stellaris_id, mod_id, fs_set_st_v, flex_v, mod_v 
    global game_directory, steam_mods_directory, mod_directory
    global defines_van_file_path, species_van_file_path
    global defines_mod_file_path, species_mod_file_path
    global defines_van_folder_path, species_van_folder_path
    global defines_mod_folder_path, species_mod_folder_path
    global fs_mode, previous_fs_mode, virgin, defines_name, species_arc_name
    global auto_update_enabled
    global ethos_max_points, civic_points_base, machine_trait_points
    global machine_max_traits, species_trait_points, species_max_traits
    
    global flex_ab_v

    try:
        with open('fs_settings.json', 'r') as f:
            settings = json.load(f)

        stellaris_id = settings.get("stellaris_id")
        mod_id = settings.get("mod_id")
        flex_v = settings.get("flex_v")
        mod_v = settings.get("mod_v")
        fs_set_st_v = settings.get("fs_designed_to_stellaris_v")
        defines_name = settings.get("defines_name")
        species_arc_name = settings.get("species_arc_name")
        game_directory = settings.get("game_directory")
        steam_mods_directory = settings.get("steam_mods_directory")
        mod_directory = settings.get("mod_directory")
        defines_van_file_path = settings.get("defines_van_file_path")
        species_van_file_path = settings.get("species_van_file_path")
        defines_mod_file_path = settings.get("defines_mod_file_path")
        species_mod_file_path = settings.get("species_mod_file_path")
        defines_van_folder_path = settings.get("defines_van_folder_path")
        species_van_folder_path = settings.get("species_van_folder_path")
        defines_mod_folder_path = settings.get("defines_mod_folder_path")
        species_mod_folder_path = settings.get("species_mod_folder_path")
        fs_mode = settings.get("fs_mode")  # Default to 'NORMAL' if not set
        auto_update_enabled = settings.get("auto_update_enabled")
        previous_fs_mode = settings.get("previous_fs_mode", "NORMAL")
        ethos_max_points = settings.get("ethos_max_points")
        civic_points_base = settings.get("civic_points_base")
        machine_trait_points = settings.get("machine_trait_points")
        machine_max_traits = settings.get("machine_max_traits")
        species_trait_points = settings.get("species_trait_points")
        species_max_traits = settings.get("species_max_traits")
        virgin = settings.get("virgin")
        
        if flex_ab_v != flex_v:
            print_sep("## WARNING! SETTINGS FILES NOT BUILT FOR THIS FS VERSION!", 3)
            print(f"The fs_settings.json file you have was built for Flex Script v{flex_v}.")
            print(f"\nthis Flex Script is version {flex_ab_v}!")
        

    except FileNotFoundError:
        # File doesn't exist, settings will remain at their default values
        pass
    except json.JSONDecodeError:
        separator_timer(0)
        print("Error reading the settings file. It might be corrupted.")
        separator_timer(2)


def is_settings_present():
    global fs_settings_present

    # Check if the script is running as a frozen executable (e.g., .exe file)
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        # Otherwise, it's a regular Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the settings file
    settings_path = os.path.join(script_dir, 'fs_settings.json')

    # Check if the settings file exists
    fs_settings_present = os.path.isfile(settings_path)

    


## Verify loading paths...
def verify_loading_paths(subject, path, confirmation_path):
    
    print(f"Verifying if {subject} path was loaded correctly...")
    separator_timer(1)
    
    if path:
        path = path_checker(subject, path, confirmation_path)
        
        if path is not None:
            print(f"{subject} path was successfully loaded...")
            separator_timer(1)
            return path
    
    print(f"Due to a failure loading the {subject} data, \nFS has to start the PATH DETECTION PROCESS....")
    
    ## DEBUG
    if fs_mode == "DEBUG": print(f"DEBUG_verify_loading_paths:  subject:{subject} // path:{path} // confirmation_path:{confirmation_path}")
    
    separator_timer(2)
    return None
        

def check_if_any_custom_is_none():

    # Call globals
    global is_any_custom_none
    global ethos_max_points
    global civic_points_base 
    global machine_trait_points 
    global machine_max_traits
    global species_trait_points
    global species_max_traits
    
    is_any_custom_zero = False
    
    # Check if any variable is None
    variables = [ethos_max_points, civic_points_base, machine_trait_points, machine_max_traits, species_trait_points, species_max_traits]
    
    for var in variables:
        if fs_mode == "DEBUG": print(f"DEBUG_check_if_any_custom_is_none:  custom_var:{var}")
    
    is_any_custom_none = any(var is None for var in variables)
    is_any_custom_zero = any(var == 0 for var in variables)
    
    if is_any_custom_zero: is_any_custom_none == True
    
    if is_any_custom_none or is_any_custom_zero:
        if fs_mode == "DEBUG": print("DEBUG:  At least one variable is None or Zero")
    else:
        if fs_mode == "DEBUG": print("DEBUG:  No variables are None or Zero")


####################################################################################






### MENU HELPER METHODS  ############################################################

def change_fs_mode():
    global fs_mode
    separator_timer(1)
    print("\n##############################################")
    print("#        Flex Script Settings: Mode          #")
    print("##############################################\n")
    print("\nCurrent FS Mode:", fs_mode)
    print(
        "\n> NORMAL - This was the mode intended for FS to run."
        "\n           (so you can read everything step by step, and pay attention)"
        "\n> FAST   - A quicker mode that will show messages a bit faster"
        "\n> RUSH   - This mode will skip every FS 'separator' time delay."
        "\n> DEBUG  - The developer mode. It's actually RUSH with DEBUG messages."
        "\n> SERVER - Server mode to prepare this FS and Settings file to share with your friends."
        "\n            \-> This helps making the process cleaner and quicker."
        "\n                You setup the settings, prepare server and share."
        "\n                Ask your friends to run FS with settings files on the same location."
        "\n                As this is a manual option, you should go back and toggle the \"auto-update\" feature."
        "\n                (It's recommended just to go back to Flex Script Menu and chose \"SERVER MODE\"')."
        )
    while True:
        new_mode = input("\n\nEnter new mode (NORMAL, FAST, RUSH, DEBUG, SERVER).\n\nNew FS mode: ").upper()
        separator_timer(1)
        if new_mode in ["NORMAL", "FAST", "RUSH", "DEBUG", "SERVER"]:
            fs_mode = new_mode
            print("Flex Script mode updated to:", fs_mode)
            break
        elif new_mode in p_cancel or new_mode in p_no:
            print("Returning...")
            separator_timer(1)
            return
        else:
            print("Invalid mode. Please enter a valid mode.")
    separator_timer(2)
    settings_menu()  # Return to settings menu


def update_stellaris_id():
    global stellaris_id
    print("\nCurrent Stellaris Game ID:", stellaris_id)
    new_id = input("Enter new Stellaris Game ID: ").strip()
    stellaris_id = new_id
    print("Stellaris Game ID updated to:", stellaris_id)
    settings_menu()  # Return to settings menu


def update_mod_id():
    global mod_id
    print("\nCurrent Mod ID:", mod_id)
    new_id = input("Enter new Mod ID: ").strip()
    mod_id = new_id
    print("Mod ID updated to:", mod_id)
    settings_menu()  # Return to settings menu


def toggle_auto_update():
    global auto_update_enabled
    print("\nAuto-Update is currently", "Enabled" if auto_update_enabled else "Disabled")
    choice = input("Do you want to toggle Auto-Update? (yes/no): ").lower()
    if choice in ["yes", "y"]:
        auto_update_enabled = not auto_update_enabled
        print("Auto-Update", "Enabled" if auto_update_enabled else "Disabled")
    settings_menu()  # Return to settings menu
    
    
def update_mod_files():
    print_sep("### Updating Mod Files ###", 2)
    
    if not auto_update_enabled:
        print("This process will copy the vanilla '00_defines.txt' and '00_species_archetypes.txt'"
              "\nfiles from the Stellaris installation directory. It then pastes them into the"
              "\nmod's respective folders, overwriting the existing mod files. After this,"
              "\na 'find and replace' operation updates the files with the values you've customized"
              "\nthrough Flex Script."
              "\n\nEssentially, this ensures that the mod files contain exactly what's in the"
              "\nvanilla files, plus your customizations."
              "\n\nAre you sure you want to continue?"
              "\n\n")
        proceed_confirmation(history=None)
        separator_timer(2)

    # Check if the necessary file paths are available
    if not all([defines_van_file_path, species_van_file_path, defines_mod_file_path, species_mod_file_path]):
        print_sep("Error: Necessary file paths are not set.", 2)
        separator_timer(1)
        return

    # Check if vanilla files exist
    if not os.path.exists(defines_van_file_path) or not os.path.exists(species_van_file_path):
        print_sep("Error: Vanilla files not found.", 2)
        separator_timer(1)
        return

    try:
        # Copy vanilla files to mod directory
        shutil.copy(defines_van_file_path, defines_mod_file_path)
        shutil.copy(species_van_file_path, species_mod_file_path)
        print("Vanilla files copied to mod directory.", 2)

        # Update the mod files with current customizations
        # Assuming modify_value_in_file function exists and works as intended
        modify_value_in_file(defines_mod_file_path, "ETHOS_MAX_POINTS", ethos_max_points)
        modify_value_in_file(defines_mod_file_path, "GOVERNMENT_CIVIC_POINTS_BASE", civic_points_base)
        modify_value_in_file(species_mod_file_path, "@machine_trait_points", machine_trait_points)
        modify_value_in_file(species_mod_file_path, "@machine_max_traits", machine_max_traits)
        modify_value_in_file(species_mod_file_path, "@species_trait_points", species_trait_points)
        modify_value_in_file(species_mod_file_path, "@species_max_traits", species_max_traits)

        print_sep("Mod files updated with current customization values.", 2)
        separator_timer(2)
    
    except Exception as e:
        print(f"An error occurred while updating mod files: {e}")
        separator_timer(2)


def prepare_for_server_clients():
    global fs_mode, auto_update_enabled

    print("\n##############################################")
    print("#       Preparing for Server Clients         #")
    print("##############################################\n")

    print("This mode configures Flex Script for server hosting, ensuring")
    print("all clients (your friends) have consistent mod settings.")
    print("\nIn SERVER mode, Flex Script enables auto-updates and")
    print("prepares a configuration file for easy distribution.")
    print("After completing this process, share the Flex Script and")
    print("fs_settings.json with your server clients for a harmonized multiplayer experience.\n\n\n")


    # Confirmation to proceed
    proceed = proceed_confirmation(history=None)
    if proceed not in p_yes or proceed not in p_continue:
        print_sep("Process cancelled. Returning to the previous menu.", 2)
        return
    separator_timer(3)

    # Set fs_mode to SERVER and enable auto-update
    original_fs_mode = fs_mode
    fs_mode = "SERVER"
    auto_update_enabled = True

    print_sep("Flex Script is being prepared for server client use.", 2)
    print_sep("FS Mode has been set to SERVER and auto-update is enabled.", 2)

    # Assuming save_settings() function saves the current state to fs_settings.json
    try:
        save_settings()
        print_sep("Current settings saved. Flex Script is ready for server client use.", 3)
        print_sep("You can now send a copy of this FS and Settings to your friends!", 3)
    except Exception as e:
        print(f"ERROR saving settings: {e}")
        separator_timer(2)
        fs_mode = original_fs_mode  # Revert fs_mode on error
        return

    # Prompt to keep in SERVER mode or revert to NORMAL
    choice = input("Press Enter to continue in SERVER mode or type 'normal' to revert to NORMAL mode. \n\nCommand: ").lower().strip()
    if choice == "normal":
        fs_mode = "NORMAL"
        print("Flex Script mode reverted to NORMAL.")
        separator_timer(2)
        save_settings()  # Save the settings again after reverting mode
    else:
        print("Continuing in SERVER mode.")
    separator_timer(2)
        

    # Return to main menu or perform other actions as needed
    


def reset_settings_to_default():
    """
    Resets all the settings files to global default.
    """
    
    global game_directory, steam_mods_directory, mod_directory, defines_van_file_path, species_van_file_path
    global defines_mod_file_path, species_mod_file_path, ethos_max_points, civic_points_base, machine_trait_points
    global machine_max_traits, species_trait_points, species_max_traits, fs_mode

    # Resetting all relevant variables to their initial default values
    game_directory = None
    steam_mods_directory = None
    mod_directory = None
    defines_van_file_path = None
    species_van_file_path = None
    defines_mod_file_path = None
    species_mod_file_path = None
    ethos_max_points = None
    civic_points_base = None
    machine_trait_points = None
    machine_max_traits = None
    species_trait_points = None
    species_max_traits = None
    # fs_mode = previous_fs_mode  # or any other default mode you prefer

    # Saving the reset settings
    save_settings()
    print("Settings have been reset to default.")
    separator_timer(2)
    
    
def update_defines_name():
    global defines_name
    defines_name = input("Enter the new name for the Defines file\nincluding the filetype suffix (e.g., '00_defines.txt').\n\nNew name: ").strip()
    separator_timer(2)
    print(f"Defines file name updated to {defines_name}.")
    separator_timer(2)
    save_settings()
    

def update_species_arc_name():
    global species_arc_name
    species_arc_name = input("Enter the new name for the Species Archetypes file\nincluding the filetype suffix (e.g., '00_species_archetypes.txt').\n\n New name: ").strip()
    separator_timer(2)
    print(f"Species Archetypes file name updated to {species_arc_name}.")
    separator_timer(2)
    save_settings()
    

def update_st_confirmation_key():
    global st_confirmation_key
    st_confirmation_key = input("Enter the new Stellaris confirmation key (e.g., 'stellaris.exe'): ").strip()
    separator_timer(2)
    print(f"Stellaris confirmation key updated to {st_confirmation_key}.")
    separator_timer(2)
    save_settings()
    
    
    
####################################################################################






### MENU METHODS  ##################################################################


@with_history
def main_menu(history):
    
    while True:    
        separator_timer(0)
        global fs_mode, previous_fs_mode

        # Display a different header based on the current mode
        if fs_mode == "SERVER":
            display_server_mode_header()
        else:
            display_main_menu_header()
    
        # SERVER mode specific menu
        if fs_mode == "SERVER":
            
            choice = input("\nEnter your choice (1-3): ").strip().lower()
            separator_timer(1)
            if choice in ["1", "remove", "deactivate"]:
                # Revert to the previous mode
                fs_mode = previous_fs_mode if previous_fs_mode and previous_fs_mode != "SERVER" else "NORMAL"
                previous_fs_mode = fs_mode
                print("SERVER Mode removed. Flex Script mode reverted to:", fs_mode)
                save_settings()  # Save the current state
                main_menu()  # Return to main menu
            
            elif choice == "2" or choice in p_reset:
                prompt = proceed_confirmation(history)
                if prompt in p_yes or prompt in p_continue:
                    main_updated()
            
            elif choice == "3" or choice in p_quit:
                shutdown("quit")  # Quit Flex Script
    
            else:
                print("Invalid choice, please try again.")
                main_menu()  # Return to main menu
     
        else:
            
            choice = input("Enter your choice (1-10): ").strip()
            separator_timer(1)
            if choice == "1" or choice in p_reset:
                print ("### WARNING!\n\nYou have chosen to reset the settings file.\nThis will reset paths and customization values on that file and restart the whole process...\n")
                answer = proceed_confirmation(history)
                if answer in p_yes or answer in p_continue and not (answer in p_cancel or answer in p_no):
                    reset_settings_to_default()  # Reset the settings to default
                    main_updated()  # Restart the whole process
                    continue
            elif choice in ["2", "customize", "custom"]:
                main_customization()  # Customization menu
            elif choice in ["3", "print_header", "p_header", "print header"]:
                print(header)  # Initial software header
                proceed_confirmation(history=history)
                main_menu()  # Return to main menu
            elif choice == "4" or choice in print_tut:
                # help_prompt("print_tut", history=history)
                print(tutorial)
                separator_timer(2)
                proceed_confirmation(history)
                main_menu()  # Return to main menu
            elif choice == "5" or choice in p_settings:
                settings_menu()  # Settings menu (to be implemented)
            elif choice == "6" or choice == "update":
                update_mod_files()  # Update mod files (to be implemented)
            elif choice == "7" or choice in ["prepare", "server", "client"]:
                prepare_for_server_clients()  # Prepare for server clients (to be implemented)
            elif choice == "8" or choice in p_quit:
                shutdown("quit")  # Quit Flex Script (to be implemented)
            elif choice in ["9", "save"]:
                save_settings()  # Save settings
                main_menu()  # Return to main menu
            elif choice in ["10", "load"]:
                load_settings()  # Load settings
                main_menu()  # Return to main menu    
            else:
                print("Invalid choice, please try again.")
                separator_timer(2)
                main_menu()  # Return to main menu

        separator_timer(1)
    
    
    
@with_history
def main_customization(history=None):
    while True:
        separator_timer(0)
        display_customization_header()  # Display the header
        custom_sleep(4)
        display_values_table()  # Display the value tables
    
        # Ask user for settings preference
        setting = input("\nChoose MPP settings (vanilla, standard, beast, custom) or reset the whole process. \n\nAnswer:  ").lower().strip()
        separator_timer(1)
        # setting = prompt_handler(prompt, history)
        while setting not in ['vanilla', 'standard', 'custom', 'beast', 'reset', 'cancel', 'return']:
            separator_timer(0)
            print("\nInvalid choice. Please choose again.")
            setting = input("\nChoose settings (vanilla, standard, beast, custom): ").lower()
            separator_timer(1)
    
        # Apply settings
        if setting == 'vanilla':
            modify_mod_files_with_defaults("vanilla")
            return True
        elif setting == 'standard':
            modify_mod_files_with_defaults("standard")
            return True
        elif setting == 'beast':
            modify_mod_files_with_defaults("beast")
            return True
        elif setting == 'custom':
            modify_mod_files_custom()
            return True
        elif setting == "return":
            if is_any_custom_none:
                print("This is not possible to do since there are MPP Customizable variables that have null or zero values...\n\nPlease choose a preset of customize it at your taste.")
                continue
            return
        else:
            main_menu()   
    separator_timer(1)
    
    
    
    
def settings_menu():
    while True:
        global fs_mode
        print("\n##############################################")
        print("#            Flex Script Settings            #")
        print("##############################################\n")
        print("Choose an option to modify Flex Script settings:\n")
        print("1. Change Flex Script Mode (NORMAL, FAST, RUSH, DEBUG, SERVER)")
        print("    \-> Or directly enter a mode (e.g., 'NORMAL', 'DEBUG')")
        print("2. Update Stellaris Game ID")
        print("3. Update Mod ID")
        print("4. Toggle Auto-Update Feature")
        print("5. Update Defines File Name")
        print("6. Update Species Archetypes File Name")
        print("7. Update Stellaris Confirmation Key")
        print("8. Return to Main Menu\n")
    
        valid_modes = ["NORMAL", "FAST", "RUSH", "DEBUG", "SERVER"]
        choice = input("\n\nEnter your choice (1-8) or a mode: ").strip().upper()
        
        if choice in valid_modes:
            fs_mode = choice
            separator_timer(1)
            print(f"Flex Script mode changed to {fs_mode}.")
            separator_timer(2)
            save_settings()  # Save the new mode setting
        elif choice == "1":
            change_fs_mode()  # Change Flex Script Mode
        elif choice == "2":
            update_stellaris_id()  # Update Stellaris Game ID
        elif choice == "3":
            update_mod_id()  # Update Mod ID
        elif choice == "4":
            toggle_auto_update()  # Toggle Auto-Update
        elif choice == "5":
            update_defines_name()  # Update Defines File Name
        elif choice == "6":
            update_species_arc_name()  # Update Species Archetypes File Name
        elif choice == "7":
            update_st_confirmation_key()  # Update Stellaris Confirmation Key
        elif choice == "8":
            return  # Return to Main Menu
        else:
            print("Invalid choice, please try again.")
            separator_timer(1)
            settings_menu()  # Re-display settings menu


####################################################################################







### MAIN METHODS  ##################################################################


def main_updated():
    global game_directory
    global steam_mods_directory
    global mod_directory
    global is_any_custom_none
    global virgin
    global fs_mode
    global any_settings_alteration
    global auto_update_enabled
    register_problems = False
    any_settings_alteration = False
    
    
    # audio_process("play", 0.5)
    
    ## PRINT THE BIG HEADER
    print(header)
    separator_btimer(3,1)
    
    
    ## WARNING 
    print("Ensure you've downloaded the mod first before messing with this software! \n\nDownload link: [https://steamcommunity.com/sharedfiles/filedetails/?id=3038118849]")
    separator_timer(2)
    
    



    ## ATTEMPT TO LOAD FS_SETTINGS.JS
    is_settings_present()
    if fs_settings_present:
        load_settings()
        virgin = False
        print_sep("fl_settings.jason has been successfully loaded....",1)
        print(f"Loaded FS Mode: {fs_mode}...")
        separator_timer(1)
        
    else:
        print("Because it's the first time you're running this FS \nand/or because the fs_settings.jason file isn't in the same directory as flexScript...")
        print("\nFS has to start the PATH DETECTION PROCESS...")
        any_settings_alteration = True
        separator_timer(3)
        
        
    ## IS IT THE FIRST TIME? 
    ## YES? THEN TUTORIAL!
    first_time_run_prompt()  ## Is this the first time this software is running on your computer?
        
    
    ## STELLARIS DIRECTORY FINDING PROCESS
    separator_timer(0)
    print("### PART ONE")
    
    check_path = None
    if game_directory: check_path = path_checker("Stellaris Installation", game_directory, st_confirmation_key)
    # if there is an error on the checked path or if it as no data... Starts the process...
    if check_path is None or game_directory is None:    
        
        any_settings_alteration = True
        print("\n### ATTEMPTING TO AUTOMATICALLY DETECT YOUR STELLARIS INSTALLATION FOLDER ###")   
        separator_timer(2)
     
        game_directory = find_game_folder()
        if game_directory:
            assigning_path_suc_message(game_directory)   
        else:
            assigning_path_unc_message("Stellaris Installation")
            register_problems = True
    else:
        separator_timer(2)
    
    
    ## MPP MOD DIRECTORY FINDING PROCESS
    separator_timer(0)
    print("### PART TWO")
    part_two_error = False
    if steam_mods_directory and mod_directory: mod_directory = path_checker("Stellaris Mods", steam_mods_directory, mod_id)
    else: part_two_error = True, print_sep("There was a error loading the Steam mods or MPP mod directory path...\n\nWe need to start the MPP Mod folder finding process...", 2)
    # if there is an error on the checked path or if it as no data... Starts the process...
    if mod_directory is None or mod_directory == "" or steam_mods_directory is None or steam_mods_directory == "" or part_two_error:    

        any_settings_alteration = True
        part_two_error = False
        print("\n### ATTEMPTING TO AUTOMATICALLY DETECT YOUR STELLARIS MPP MOD FOLDER ###")   
        separator_timer(2)
        mod_directory = find_mod_folder()
        if mod_directory:
            assigning_path_suc_message(mod_directory) 
            if fs_mode == "DEBUG": print(f"DEBUG_PARTTWO_0: steam_mods_directory:{mod_directory} // steam_mods_directory:{steam_mods_directory}")
        else:
            assigning_path_unc_message("Stellaris Mod Path")
            register_problems = True
    else:
        separator_timer(2)
    
        
    ## STELLARIS FILES FINDING PROCESS
    separator_timer(0)   
    print("### PART THREE")
    print("\n### ATTEMPTING TO AUTOMATICALLY DETECT STELLARIS \"VANILLA\" FILES ###")   
    separator_timer(1)
    defines_van_folder_path, species_van_folder_path = find_game_files(game_directory)
    if defines_van_folder_path and species_van_folder_path:
        subject_message = defines_van_folder_path + " and " + species_van_folder_path
        assigning_path_suc_message(subject_message) 
        if fs_mode == "DEBUG": print(f"DEBUG_PARTTWO_0: defines_van_folder_path:{defines_van_folder_path} // species_van_folder_path:{species_van_folder_path}")
        define_van_files_path()
    else:
        assigning_path_unc_message("Stellaris Vanilla Files Path")
        register_problems = True
        
        
    ## MPP FILES FINDING PROCESS
    separator_timer(0)   
    print("### PART FOUR")
    print("\n### ATTEMPTING TO AUTOMATICALLY DETECT MPP FILES ###")   
    separator_timer(1)
    defines_mod_folder_path, species_mod_folder_path = find_mod_files(mod_directory)
    if defines_mod_folder_path and species_mod_folder_path:
        subject_message = defines_mod_folder_path + " and " + species_mod_folder_path
        assigning_path_suc_message(subject_message) 
        if fs_mode == "DEBUG": print(f"DEBUG_PARTTWO_0: defines_mod_folder_path:{defines_mod_folder_path} // species_mod_folder_path:{species_mod_folder_path}")
    else:
        assigning_path_unc_message("Stellaris Mod MPP Files Path")
        register_problems = True
 
        
    ## MPP MOD CUSTOMIZATION PROCESS
    separator_timer(0)
    print("### PART FIVE")
    print_sep("\n### ATTEMPTING TO AUTOMATICALLY ASSIGN MPP CUSTOMIZATION VALUES ###",2)   
    check_if_any_custom_is_none()
    customization_succeeded = False
    if is_any_custom_none == True:
        any_settings_alteration = True
        customization_succeeded = False
        if not virgin and fs_settings_present: separator_timer(1), print("At least one of the customization variable is null or zero in fs_settings..."), separator_timer(2) 
        print("\n### INITIATING MPP CUSTOMIZATION PROCESS ###")   
        separator_timer(2)
        customization_succeeded = main_customization()
        if customization_succeeded:
            print("# Values submitted")
            separator_timer(1)
            print("### CUSTOMIZATION PROCESS's DONE!")
            separator_timer(2)
    
            if fs_mode == "DEBUG": print(f"DEBUG_PARTTWO_0: mod_directory:{mod_directory} // steam_mods_directory:{steam_mods_directory}")
            is_any_custom_none = False
        else:
            print("Something went wrong while assigning the variables...")
            separator_timer(2)
            print("Don't worry...")
            separator_timer(1)
            print("You can set them now, and change them later on FS Menu or set on the jason settings file...")
            separator_timer(3)
            print("Thinking...")
            separator_timer(1)
            register_problems = True

    else:
        customization_succeeded = True
        print_sep("Customization values loaded successfully!", 1)

        
    separator_timer(1)        
    
    
    ## ATTEMPT AUTO-UPDATE
    if auto_update_enabled:
        print_sep("### ATTEMPTING TO AUTO-UPDATE MPP...", 1)
        try:
            virgin = False
            update_mod_files()
            print_sep("MPP files updated successfully!", 2)
        except Exception as e:
            print("### ERROR: UPDATE NOT POSSIBLE")
            print(f"Something went wrong while updating...\n\nError: {e}")
            separator_timer(4)
            register_problems = True
    
    
    
    ## ATTEMPT SAVING
    if register_problems or virgin or customization_succeeded or any_settings_alteration:
        print("### ATTEMPTING TO SAVE SETTINGS FILE...")
        separator_timer(1)
        try:
            virgin = False
            save_settings()
            print_sep("fs_settings.jason has been saved successfully!", 2)
        except Exception as e:
            print("### ERROR: SAVING")
            print(f"Something went wrong while saving...\n\nError: {e}")
            separator_timer(4)
            register_problems = True
        
        
        ## IF NO ERRORS
        if not register_problems:
            print_sep("Congratulations!", 1)
            print_sep("Everything is set!", 1)
            print_sep("Now you can play or checkout the flexScript menu for more features!", 2)
        else:
            print_sep("Something went wrong with this process\n\nYou should check out what happened through the FS Menu, troubleshoot or contact us on the steam mod link...", 4)
    
    print_sep("Calling Flex Script Menu...", 1)
    

if __name__ == "__main__":
    main_updated()  # Start with the updated main process
    while True:
        main_menu()     # Then, proceed to the main menu


####################################################################################
































### AUDIO FUNCTIONS  ###############################################################


# def init_audio(file_name):
#     pygame.mixer.init()  # Initialize the mixer module
#     pygame.mixer.music.load(file_name)  # Load the music file

# def play_audio():
#     pygame.mixer.music.play()  # Play the music

# def pause_audio():
#     pygame.mixer.music.pause()  # Pause the music

# def unpause_audio():
#     pygame.mixer.music.unpause()  # Unpause the music

# def set_volume(volume):
#     pygame.mixer.music.set_volume(volume)  # Set volume, range 0.0 to 1.0

# # Example usage
# def audio_process(function, vol):
#     init_audio("sleepless_city.mp3")  # Replace with your audio file name
    
#     if function == "play":
#         play_audio()
#     elif function == "pause":
#         pause_audio()
#     elif function == "unpause":
#         unpause_audio()
#     else:
#         return
#     set_volume(vol)  # Set volume to 50%

# ## "Sleepless City" by Keys of Moon Music is a great


####################################################################################


