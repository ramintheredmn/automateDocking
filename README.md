place the main.py in the directory like this

--- main directory ----
  | +dock_1 
  | +dock_2
  | +dock_3
  | ...
  | main.py


each dock_* folder should contain r.gpf r.glg r.dpf l.pdbgt r.pdbqt and if you dont have autodock and autogrid in PATH, place their executable files in each folde (windows os)
  * in linux and unix like operationg systems autodock 4 and autogrid are in path if installed before

if you saved the files mentioned above with another names change the corresponding parts of the main.py

this script will run autogrid at first to produce map files in each folder then runs the autodock


in order to run the script open cmd in the main directory and run python main.py

        -------Be sure thar you have python3 installed------------------
