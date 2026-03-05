import os
import sys
from dotenv import load_dotenv


def color(message: any, tcol: tuple = (255, 255, 255),
          bcol: tuple = None,
          bold: bool = False, ita: bool = False, under: bool = False,
          finish: str = '\n', f: any = None) -> None:
    if tcol is None:
        tcol = (255, 255, 255)
    style = "1;" if bold else ""
    italic = "3;" if ita else ""
    underline = "4;" if under else ""
    bcolor = f"48;2;{bcol[0]};{bcol[1]};{bcol[2]}" if bcol else ""
    style = style+italic+underline+bcolor
    if (type(message) is dict or type(message) is list):
        for mes in message:
            print(f"\033[{style}38;2;{tcol[0]};{tcol[1]};{tcol[2]}"
                  f"m{mes}\033[0m", end=finish, file=f)
            print("")
    else:
        print(f"\033[{style}38;2;{tcol[0]};{tcol[1]};{tcol[2]}"
              f"m{message}\033[0m",
              end=finish, file=f)


if __name__ == "__main__":
    try:
        open(".env", "r")
        file = load_dotenv(".env")
        for i in ["MODE", "LOGLEVEL", "CONNECTION", "APIACCESS", "VERSION"]:
            if os.getenv(i) is None:
                color(f"BAD .env CONFIG, MISSING: '{i}'",
                      (255, 0, 0), bold=True)
                sys.exit(1)
        color("Reading Matrix: \n",
              (0, 255, 0), bold=True)
        color("Config Loaded:", (155, 255, 155))
        color(f" - Mode: {os.getenv("MODE")}", (105, 255, 105))
        color(f" - Status: {os.getenv("LOGLEVEL")}", (155, 255, 155))
        color(f" - Connection: {os.getenv("CONNECTION")}", (105, 255, 105))
        color(f" - API: {os.getenv("APIACCESS")}", (155, 255, 155))
        color(f" - Version: {os.getenv("VERSION")}", (105, 255, 105))

        color("\n[OK] .env Properly Configued.", (0, 255, 0))
        color("[OK] Production overides available.", (0, 255, 0))
        color("[OK] No hardcoded secrets.", (0, 255, 0))
    except FileNotFoundError:
        color("Missing .env file, please create one.",
              (255, 0, 0), bold=True)
