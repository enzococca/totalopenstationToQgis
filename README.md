# Total Open Station To QGIS

Total Open Station To QGIS is a QGIS launcher for [Total Open Station](https://tops.iosa.it/), the free software program for downloading and processing data from total station devices. The plugin connects QGIS with Total Open Station, originally developed as part of the IOSA project by archaeologists Stefano Costa and Luca Bianconi.

## Requirements
- QGIS with Python plugin support
- Total Open Station installed on the same system and available on the PATH

## Installation
1. Copy or clone this repository into your QGIS plugin directory (e.g. `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`).
2. Restart QGIS so it discovers the plugin.
3. Enable the plugin from **Plugins → Manage and Install Plugins…**.

## Usage
1. Open QGIS and ensure the plugin is enabled.
2. From the plugin toolbar or menu, launch Total Open Station using the provided action.
3. Download or process data from your total station within Total Open Station.
4. Import the resulting data back into QGIS for visualization or further analysis.

## Contributing
Pull requests are welcome. Please include a short description of your change and any relevant steps to test it. If you encounter issues, file a bug report with details about your QGIS version, operating system, and steps to reproduce.
