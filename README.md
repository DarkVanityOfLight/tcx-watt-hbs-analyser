# tcx-watt-hbs-analyser
A program with Tkinter GUI to analyse tcx files, plots the watt to heart rate of one or more tcx files against each other

## Setup
Run the setup.sh file with root for distributions with apt package manager,
else install the dependencies per hand. The setup script will copy all things needed into ```/opt/Trainings_Analyzer```
and generate a .desktop file. If it can find your Desktop directory it will generate the ```.desktop``` file there.
  ### Dependencies
  python3.6\
  python3-tk\
  pipenv
## Run
You have two options if you have set the program up with the setup.sh script run the generated desktop file,
else run the program using:
> pipenv run main

## Dev
The program is divided in two parts the ```parser.py``` and the ```main.py```.
Main contains the Tkinter main class and co.
Parser contains everything needed to parse the ```.tcx``` file and a Tkinter
class to display plots
