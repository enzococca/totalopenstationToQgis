# Total Open Station To QGIS
It is a QGIS launcher for Total Open Station (TOPS for friends) and that is a free software program for downloading and processing data from total station devices. This one is a plugin to connect with totalopenstation software developed as part of the IOSA project by Stefano Costa and Luca Bianconi, archaeologists.

## Additional guidance for using different total station models

* **Serial/USB detection:** the plugin now reports failures when probing available serial ports. If your device uses a virtual COM/USB adapter, ensure the driver is installed and the port appears in the list before attempting a download.
* **Alternative data paths:** you can point the connector to any TOPS-compatible instrument definition by selecting the appropriate model in the combo box. The parser path is resolved using your QGIS profile directory, so custom instrument definitions placed there will be detected automatically.
* **Data review before import:** exported CSV files can be loaded directly as delimited layers or converted to shapefiles from inside QGIS. Use the preview table to verify point names, coordinates, and metadata before committing to a project layer.
* **Workflow tips for mixed devices:** when working with multiple total station brands, keep separate raw `.tops` downloads per session and convert them individually. This avoids mixing coordinate systems or job metadata during batch processing.

## Adding support for new total station models

1. Create a new Python module inside `totalopenstation/models` (for example `your_station.py`) that implements the expected TOPS model interface.
2. Place the module inside your QGIS profile's `python/plugins/totalopenstationToQgis/ext-libs/totalopenstation/models` directory (or install it with the plugin).
3. Restart QGIS. The plugin now enumerates the `totalopenstation.models` package at startup and automatically lists every available model in the **Model** dropdown, so the new station can be selected without further changes.

### Riconoscimento automatico del formato

Quando si seleziona un file di input, il plugin prova a riconoscere il formato della stazione totale provando tutti i parser disponibili in `totalopenstation`. Il parser che restituisce il maggior numero di punti viene impostato automaticamente nel menu a tendina del formato; se non viene riconosciuto nulla verrà mostrato un messaggio e sarà comunque possibile scegliere manualmente.
