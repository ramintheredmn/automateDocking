import subprocess
import os
from concurrent.futures import ProcessPoolExecutor

def run_autodock_for_directory(directory):
    base_directory = "."
    os.chdir(os.path.join(base_directory, directory))
    print(f"Running autogrid and autodock for {directory}")
    subprocess.run("autogrid4 -p r.gpf -l r.glg", shell=True, check=True)
    
    if os.path.exists('r.glg'):
        print(f"'r.glg' created in {directory}")
        subprocess.run("autodock4 -p r.dpf -l r.dlg", shell=True, check=True)
        print(f"Autodock finished for {directory}")
    else:
        print(f"Error: 'r.glg' not created in {directory}")

def run(n):
    base_directory = "." 
    directories = [d for d in os.listdir(base_directory) if d.startswith('dock_') and os.path.isdir(os.path.join(base_directory, d))]
    
    # Process directories in batches
    for i in range(0, len(directories), n):
        batch = directories[i:i+n]
        with ProcessPoolExecutor(max_workers=n) as executor:
            executor.map(run_autodock_for_directory, batch)

def main():
    s_run_number = int(input("Enter the number of parallel runs, consider your CPU cores do not exceed n-1, where n is the number of cores: "))
    run(s_run_number)

if __name__ == "__main__":
    main()

