import os
import time

def find_mod_path():
    """
    Updated function to detect the mod's installation path.
    """
    steam_path = "C:/Steam/steamapps/workshop/content/"
    stellaris_game_code = "281990"  # This might need updating if Stellaris' game code changes

    if os.path.exists(steam_path):
        # List all game codes in the steam workshop content directory
        game_codes = os.listdir(steam_path)
        
        # Check if Stellaris game code exists
        if stellaris_game_code in game_codes:
            stellaris_mod_path = os.path.join(steam_path, stellaris_game_code)
            mods = os.listdir(stellaris_mod_path)
            if mods:  # if there's any mod folder
                print("Multiple mods detected. Please ensure you know the mod's specific code.")
                for mod in mods:
                    print(f"- {mod}")
                mod_code = input("Enter your mod's specific code: ")
                return os.path.join(stellaris_mod_path, mod_code)
    
    # If the initial search failed, offer to search in a specific drive
    search_drive = input("Failed to find the mod path automatically. Would you like to search a specific drive for the Stellaris installation? (yes/no): ").lower()
    
    if search_drive == "yes":
        drive_letter = input("Enter the drive letter (e.g., D, E, F, etc.): ").upper()
        steamapps_path = search_steamapps_in_drive(drive_letter)
        if steamapps_path:
            workshop_path = os.path.join(steamapps_path, "workshop", "content", stellaris_game_code)
            if os.path.exists(workshop_path):
                mods = os.listdir(workshop_path)
                if mods:  # if there's any mod folder
                    print("Multiple mods detected. This mod should be code number \"XXXX\". Please ensure you know the mod's specific code.")
                    print(", ".join(mods))
                    mod_code = input("Enter your mod's specific code: ")
                    return os.path.join(workshop_path, mod_code)
                else:
                    print("There are no mods on your stellaris folder. Please ensure you installed \"More Picks\" mod before running this script.")
    
    # If all attempts fail, return None
    return None



def search_steamapps_in_drive(drive_letter):
    """
    Search for the steamapps folder in the specified drive.
    """
    # Construct the base path for the drive
    base_path = f"{drive_letter}:/"
    
    # Walk through the directories to find steamapps
    for dirpath, dirnames, filenames in os.walk(base_path):
        if "steamapps" in dirnames:
            return os.path.join(dirpath, "steamapps")
    return None


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
    else:  # mod defaults
        return {
            "ETHOS_MAX_POINTS": 5,
            "GOVERNMENT_CIVIC_POINTS_BASE": 5,
            "machine_trait_points": 4,
            "machine_max_traits": 8,
            "species_trait_points": 5,
            "species_max_traits": 8
        }

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

def modify_mod_files_with_defaults(mod_path, mode):
    """
    Update the mod files with default values based on mode.
    """
    values = set_default_values(mode)
    
    # Paths to the mod files
    defines_path = os.path.join(mod_path, "common", "defines", "00_defines.txt")
    species_path = os.path.join(mod_path, "common", "species_archetypes", "00_species_archetypes.txt")
    
    # Modify 00_defines.txt
    modify_value_in_file(defines_path, "ETHOS_MAX_POINTS", values["ETHOS_MAX_POINTS"])
    modify_value_in_file(defines_path, "GOVERNMENT_CIVIC_POINTS_BASE", values["GOVERNMENT_CIVIC_POINTS_BASE"])
    
    # Modify 00_species_archetypes.txt
    modify_value_in_file(species_path, "@machine_trait_points", values["machine_trait_points"])
    modify_value_in_file(species_path, "@machine_max_traits", values["machine_max_traits"])
    modify_value_in_file(species_path, "@species_trait_points", values["species_trait_points"])
    modify_value_in_file(species_path, "@species_max_traits", values["species_max_traits"])

    print(f"Mod files modified with {mode} defaults!")



def modify_mod_files_custom(mod_path):
    """
    Modify the mod files based on user's custom input.
    """
    # Paths to the mod files
    defines_path = os.path.join(mod_path, "common", "defines", "00_defines.txt")
    species_path = os.path.join(mod_path, "common", "species_archetypes", "00_species_archetypes.txt")
    
    # Gather user input for customization
    ethos_max_points = int(input("Enter number of ETHOS_MAX_POINTS (default is 3): "))
    civic_points_base = int(input("Enter number of GOVERNMENT_CIVIC_POINTS_BASE (default is 2): "))
    machine_trait_points = int(input("Enter number of machine_trait_points (default is 1): "))
    machine_max_traits = int(input("Enter number of machine_max_traits (default is 5): "))
    species_trait_points = int(input("Enter number of species_trait_points (default is 2): "))
    species_max_traits = int(input("Enter number of species_max_traits (default is 5): "))
    
    # Modify 00_defines.txt
    modify_value_in_file(defines_path, "ETHOS_MAX_POINTS", ethos_max_points)
    modify_value_in_file(defines_path, "GOVERNMENT_CIVIC_POINTS_BASE", civic_points_base)
    
    # Modify 00_species_archetypes.txt
    modify_value_in_file(species_path, "@machine_trait_points", machine_trait_points)
    modify_value_in_file(species_path, "@machine_max_traits", machine_max_traits)
    modify_value_in_file(species_path, "@species_trait_points", species_trait_points)
    modify_value_in_file(species_path, "@species_max_traits", species_max_traits)

    print("Mod files modified successfully!")


def main_updated():
    print("Ensure you've downloaded the mod first! Download link: [YOUR LINK HERE]")
    
    mod_path = find_mod_path()
    if not mod_path:
        print("Couldn't automatically detect the mod path.")
        print("Find the mod's path by navigating to C:/Steam/steamapps/workshop/content/ and locating Stellaris' game code which normaly is 281990.")
        mod_path = input("Paste the full path to the mod here: ")
    
    # Verify the mod path
    if not os.path.exists(mod_path):
        print("Provided path doesn't exist. Exiting...")
        time.sleep(2)
        return

    # Ask user for settings preference
    setting = input("Choose settings (vanilla, standard, custom) or reset: ").lower()
    while setting not in ['vanilla', 'standard', 'custom', 'reset']:
        print("Invalid choice. Please choose again.")
        setting = input("Choose settings (vanilla, standard, custom): ").lower()

    # Apply settings
    if setting == 'vanilla':
        modify_mod_files_with_defaults(mod_path, "vanilla")
    elif setting == 'standard':
        modify_mod_files_with_defaults(mod_path, "mod")
    elif setting == 'custom':
        modify_mod_files_custom(mod_path)
    else:
        main_updated()

    print("Mod customization complete!")



if __name__ == "__main__":
    main_updated()
