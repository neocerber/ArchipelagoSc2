# Ender lilies Randomizer Setup Guide

This guide contains instructions on how to install and troubleshoot the Ender Lilies client, as well as where to obtain a config file for Ender Lilies.


## Required Software

- [The most recent Archipelago release](https://github.com/ArchipelagoMW/Archipelago/releases)
- [LiveSplit](https://livesplit.org/downloads/)
- [Ender lilies Randomizer](https://github.com/Trexounay/EnderLilies.Randomizer/releases)


## How do I install this randomizer?

1. Install Archipelago and LiveSplit using the first two links above. 
2. Extract EnderLilies.Randomizer.zip **in** the "Components" folder of your LiveSplit installation. 
3. To make the randomizer available in LiveSplit, go to "Edit Layout" -> "( + )" -> "Control" -> "Randomizer for Ender Lilies"
4. dsa save thingy less 


## Where do I get a config file (aka "YAML") for this game?

The [Player Settings](https://archipelago.gg/games/Enders%20Lilies/player-settings) page on this website allows you to choose your personal settings for the randomizer and download them into a config file. 
Remember the name you type in the `Player Name` box; that's the "slot name" the client will ask you for when you attempt to connect!


### And why do I need a config file?

Config files tell Archipelago how you'd like your game to be randomized, even if you're only using default settings.
When you're setting up a multiworld, every world needs its own config file.
Check out [Creating a YAML](https://archipelago.gg/tutorial/Archipelago/setup/en#creating-a-yaml) for more information.


## How do I join a MultiWorld game?

1. Launch LiveSplit.
2. Go to "Edit Layout" -> "( + )" -> "Control" -> "Randomizer for Ender Lilies" -> dsa
3. Fill the Server, Port and Slot name, then click Connect.
4. Press "Launch Ender Lilies" dsa


## My controller is not working

If your controller is not detected by Ender Lilies, try launching the game via Steam (i.e., not with LiveSplit button).
However, do not forget that you need to be connected to LiveSplit before you load a save file. 


## Running in Linux

Note that Ender Lilies randomizer is not officially supported for Linux.
The following is a solution provided by a kind souls, use at your own risk.

- Download LiveSplit as requested.  
- Put it in the same folder as ENDER LILIES.
- Install the randomizer as outlined.
    - Using the "EnderLilies.Randomizer_splitted_dlls.zip" versions seems more stable on Linux.
- In the same folder as the ENDER LILIES executable is located, make a new document which will be a .bat script with the following lines:
    - start EnderLilies.exe
    - start LiveSplit/LiveSplit.exe
    - exit
- Save it as a .bat file. (e.g., launcher.bat)
- In Steam, add a new program. Pick the bat file as the program.
- Under compatibility, force compatibility.
    - Tested with Proton Experimental.
- In theory, lauching that game will launch both programs at the same time.


### Known issues
- LiveSplit freeze and then crash when the bat file is launched.
    - Try disconnecting internet before launching the bat file. If LiveSplit does not freeze, you can reconnect the internet. 
- I get "The component could not be loaded" when adding Ender Lilies to the layout of LiveSplit.
    - Use the component with each dll seperated.
- I get "Msft Visual C++ Runtime missing" when launching the bat file.
    - dsa something weird


## Tracker

A tracker is available via [Poptracker](https://github.com/black-sliver/PopTracker/releases). 
The data required for Ender lilies are availabe [here](https://github.com/lurch9229/ender-lilies-poptracker/releases).

