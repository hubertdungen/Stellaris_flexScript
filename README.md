# Flex Script v2.1.0 for Stellaris MPP

Welcome to the Flex Script for the Stellaris Mod "[More Picks & Points: Traits|Civics|Ethics [FLEX EDITION]](https://steamcommunity.com/sharedfiles/filedetails/?id=3038118849)" (MPP). This major update introduces a range of new features, optimizations, and user experience improvements, making the script more intuitive, versatile, and efficient.


## Features

- **Advanced Path Detection:** Automatically detects game and mod paths, with options for semi-autonomous and manual input.
- **Server Mode:** Simplified setup for server hosts, facilitating mod synchronization with clients/friends.
- **Customization Interface:** Streamlined process for adjusting Stellaris MPP game settings.
- **Efficient Settings Management:** Robust system for loading and saving settings, enhancing responsiveness.
- **User-Friendly Interaction:** Improved prompts and instructions for a smoother user experience.
- **Optimized Performance:** Adjusted for faster execution, with modes tailored for different user needs.
- **Auto-Update Feature:** This feature ensures that the MPP files are always equal to the Stellaris target files.
- **Steam Publishing:** After auto-updating, an admin can upload the mod directly to Steam using `steamcmd`.


## Installation

1. **Download the Script:** Download `flexScript.py` (or `flexScript.exe` if using the executable version) from the [GitHub repository](<https://github.com/hubertdungen/Stellaris_flexScript>).
2. **Python Requirements:** If using the Python script, ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/).


## Customization Usage

- Run `flexScript.py` using Python, or execute `flexScript.exe` if using the standalone version.
- Follow the on-screen prompts to locate your Stellaris installation and mod directories.
- Choose your customization options.
- Run and Play!

### Publishing to Steam

Flex Script can upload the mod to Steam Workshop after an auto-update. This requires Valve's command line tool [`steamcmd`](https://developer.valvesoftware.com/wiki/SteamCMD).

#### Installing SteamCMD
- **Windows**: double-click the bundled `install_steamcmd.bat`. It downloads `steamcmd.zip`, extracts it into a `steamcmd` folder next to the batch file and runs the initial setup.
- **Linux**: run `install_steamcmd.sh` (requires `curl` and `tar`). SteamCMD will be placed in a `steamcmd` folder alongside the script.

Ensure the SteamCMD directory is on your `PATH` or note its full path for later use.

#### Publishing
1. Set the environment variables `STEAM_USERNAME` and `STEAM_PASSWORD` for the Steam account that owns the mod (the script will prompt if unset).
2. Run Flex Script and let the auto-update complete. Once finished, the menu reveals a `PUBLISH: Upload mod to Steam` option.
3. Select the publish option. Flex Script creates a `workshop_build.vdf` with the necessary `appid`, `publishedfileid`, and `contentfolder`, then runs `steamcmd +login <user> <password> +workshop_build_item workshop_build.vdf +quit` to upload the mod files.

For more information consult Valve's [Workshop Publishing](https://developer.valvesoftware.com/wiki/Workshop_Publishing) guide.


## Server Mode Usage

The server mode streamlines the setup process for multiplayer sessions, making it easy to share custom settings with friends:

1. **Set Up Your Settings:** First, configure your Flex Script settings (follow the Customization Usage tips above) to your preference in NORMAL mode (or other than SERVER mode).
2. **Prepare Server Mode:** Convert your Flex Script into a server-ready version through the Flex Script Menu (select "SERVER MODE"). This process adjusts the script to work efficiently for multiplayer sessions.
3. **Share with Friends:** Distribute the server-ready Flex Script executable (`flexScript.exe`) and the corresponding settings file (`fs_settings.json`) to your friends.
4. **Easy Client Setup:** Your friends should place both the executable and the settings file anywhere in the same directory on their system.
5. **Run and Play:** Have your friends run the `flexScript.exe`. The script will automatically configure their game using the shared settings, ensuring everyone is synchronized for multiplayer gameplay. 
6. **Have fun!!!**

This mode ensures a quick and hassle-free setup for all players involved in the multiplayer session, providing a smooth and enjoyable gaming experience.


## Contributing

Feedback and contributions are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.


## Support and Contact

If you encounter any issues or have questions, please [open an issue](https://github.com/hubertdungen/Stellaris_flexScript/issues/new/choose) on GitHub or contact me through the [Steam MPP mod comment section](https://steamcommunity.com/workshop/filedetails/?id=3038118849).


## Version History

- **v2.1.0:** Major overhaul with new features and optimizations.
- Previous versions: See the [changelog](https://github.com/hubertdungen/Stellaris_flexScript/commits/main/) for detailed version history.


## License

This project is licensed under the MIT License.
