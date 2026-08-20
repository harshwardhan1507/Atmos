import ctypes
from pathlib import Path


SPI_SETDESKWALLPAPER = 20
SPIF_UPDATE_INIFILE = 1
SPIF_SENDCHANGE = 2


def set_wallpaper(image_path):
    path = Path(image_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"Wallpaper not found: {path}")

    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        str(path),
        SPIF_UPDATE_INIFILE | SPIF_SENDCHANGE
    )