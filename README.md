# Mario Kart 8 Roster Swapper (Wii U)
![Version](https://img.shields.io/github/v/release/Scutlet/mk8-roster-swapper) ![Python Version](https://img.shields.io/badge/python-v3.8+-blue) ![License](https://img.shields.io/github/license/Scutlet/mk8-roster-swapper)

A small script that allows swapping characters in Mario Kart 8's (Wii U) roster by means of a [CEMU](https://github.com/cemu-project/Cemu) code mod.

## Usage
1. Modify the `NEW_ROSTER` in `roster.py`. The same character can appear multiple times if desired.
1. Run `python swap_roster.py`. Command line options are as follows:
    * `-n`, `--modname`: Name of the mod
    * `-d`, `--description`: Description of the mod
