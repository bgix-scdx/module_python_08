import sys
import site
import os


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


print(sys.base_prefix, sys.prefix)
color("\n==> welcome to the Matrix <==\n", tcol=(255, 105, 255), bold=True)
color(f"Current python: {sys.executable}\n", tcol=(0, 255, 0))
if sys.prefix != sys.base_prefix:
    color("Status: ", tcol=(0, 255, 0), bold=True, finish="")
    color("VM, You are secured !\n"
          "Installations won't affect the global environement.\n",
          tcol=(155, 255, 155), bold=True)
    color(f"Virtual Environement: {os.path.basename(sys.prefix)}",
          tcol=(105, 255, 105))
    color(f"Environement Path: {sys.prefix}\n",
          tcol=(105, 255, 105))
    color(f"Package: {site.getsitepackages()[0]}\n",
          tcol=(105, 255, 105))
else:
    color("WARNING: ", tcol=(255, 0, 0),
          bold=True, finish="")
    color("You are not currently using a VM.", tcol=(255, 155, 155),
          bold=True)
    color("Data you use can be accessed by the machine.",
          tcol=(255, 105, 105))
    color("\nTo enter the matrix, proceed with the following steps:\n",
          tcol=(255, 155, 155), bold=True, under=True)
    color(" ► python -m venv matrix_env", tcol=(255, 255, 155))
    color(" ► source matrix_env/bin/activate", tcol=(255, 255, 155),
          finish="")
    color(" # On Unix\n", tcol=(105, 105, 105))

    color(" ► matrix_env", tcol=(255, 255, 155))
    color(" ► Scripts", tcol=(255, 255, 155))
    color(" ► activate", tcol=(255, 255, 155))

    color("\nThen run the program again.", tcol=(255, 155, 155))
