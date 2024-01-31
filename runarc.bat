:: This batch file is used to run the AutoArchiver script in a loop
:: It is used to keep the AutoArchiver running in the background
:: make sure to change the path to the autoarch.py file to the correct path on your system

@echo off
:loop
python "C:\Development\Python Projects\AutoArchiver\autoarch.py"
goto loop
