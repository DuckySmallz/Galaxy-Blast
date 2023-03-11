if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
@echo off
TITLE GALAXY BLAST LAUNCHER
python main.py
exit