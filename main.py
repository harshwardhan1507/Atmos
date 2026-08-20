from core.timemanager import current_time, get_timeperiod
from wallpaper.wallpaper_manager import set_wallpaper

WALLPAPERS = {
    "morning": "assets/wallpapers/morning.png",
    "afternoon": "assets/wallpapers/afternoon.png",
    "evening": "assets/wallpapers/evening.png",
    "night": "assets/wallpapers/night.png"

}


def main():
    hour = current_time()
    period = get_timeperiod()
    wallpaper = WALLPAPERS[period]

    print(f"Time period: {period}")
    print(f"Selected wallpaper: {wallpaper}")
    set_wallpaper(wallpaper)

if __name__ == "__main__":
    main()
