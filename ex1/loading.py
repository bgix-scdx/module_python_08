
import sys
import random


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


color("Loading Programs...", (255, 0, 0), bold=True)

color("\nChecking dependencies:", (255, 0, 0))
try:
    import pandas
    color(f"{pandas.__name__} {pandas.__version__} [OK]",
          (0, 255, 0), bold=True)
except ModuleNotFoundError:
    color("Pandas [KO]", (255, 0, 0))
    sys.exit(1)
try:
    import matplotlib
    import matplotlib.pyplot
    color(f"{matplotlib.__name__} {matplotlib.__version__} [OK]",
          (0, 255, 0), bold=True)
except ModuleNotFoundError:
    color("matplotlib [KO]", (255, 0, 0))
    sys.exit(2)
try:
    import requests
    color(f"{requests.__name__} {requests.__version__} [OK]",
          (0, 255, 0), bold=True)
except ModuleNotFoundError:
    sys.exit(3)
    color("requests [KO]", (255, 0, 0))

color("\nAnalizing Matrix Data...", (255, 0, 0))
amm = []
for i in range(1000):
    amm.append(random.randint(0, i))

dat = pandas.DataFrame(amm)
matplotlib.pyplot.figure(figsize=(12, 6))
dat.plot()
matplotlib.pyplot.xlabel = "index"
matplotlib.pyplot.ylabel = "value"
matplotlib.pyplot.grid(True)
matplotlib.pyplot.savefig("analysis.png")
matplotlib.pyplot.close()
