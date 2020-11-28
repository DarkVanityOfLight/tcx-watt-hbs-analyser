#!/bin/sh
DESKTOP_FILE="[Desktop Entry]
Version=1.0
Type=Application
Name=Training Analyzer
Exec=bash -c \"(cd /opt/Trainings_Analyzer && pipenv run main)\""

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.6
apt-get install python3-tk
apt-get install python3-pip

pip install pipenv

cp -r . /opt/Trainings_Analyzer
cd /opt/Trainings_Analyzer

pipenv install

if [[ -d "$HOME/Desktop"  ]]; then
	echo "$DESKTOP_FILE" > "$HOME/Desktop/Training Analyzer.desktop"
	chown "$USER" "$HOME/Desktop/Training Analyzer.desktop"
else
	echo "Could not find your Desktop, please copy the Training Analyzer.desktop file from $HOME to your desktop"
	echo "$DESKTOP_FILE" > "$HOME/Training Analyzer.desktop"
	chown "$USER" "$HOME/Training Analyzer.desktop"

fi
echo "Finished installation"

