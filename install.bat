@echo off
echo Installing required Python packages...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Installation complete. You can now run the setup and main scripts.
pause
