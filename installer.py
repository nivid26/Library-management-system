import sys
from cx_Freeze import setup, Executable

sys.argv.append("build")  # replaces commandline arg 'build'

# change the filename to your program file
filename = "main.py"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "library",
    version = "1.0",
    description = "cx_Freeze Tkinter script",
    executables = [Executable(filename, base=base)])