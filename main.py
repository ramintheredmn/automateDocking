import subprocess
import os
import time

def main():
    # assuming you place this script where your dock_* folders are
    base_directory = "." 
    # create a list of availible dock_* folders to iterate 
    directories = [d for d in os.listdir(base_directory) if d.startswith('dock_') and os.path.isdir(os.path.join(base_directory, d))]
    # print(directories)
    for directory in directories:
        print(f"runing autofird for {directory} ")
        # Change the current working directory to 'directory'
        os.chdir(os.path.join(base_directory, directory))
        print("Current working directory:", os.getcwd())
        # Run autogrid
        # first place to change if you have diffetent file names
        process_grid = subprocess.Popen("autogrid4 -p r.gpf -l r.glg", shell=True)
        
        # Wait for autogrid to complete
        process_grid.wait()

        # Check if 'r.glg' is created
        if os.path.exists('r.glg'):
            print(f"'r.glg' created in {directory}")
            print("Current working directory:", os.getcwd())
            # now starting the docking process
            # second place to change if you have different file names
            process_dock = subprocess.Popen("autodock4 -p r.dpf -l r.dlg", shell=True)
            process_dock.wait()
            print(f'autodock finished for {directory}')
        
        # Change back to the base directory
        os.chdir(base_directory)
        print("Current working directory:", os.getcwd())
        os.chdir("..")


if __name__ == "__main__":
    main()
