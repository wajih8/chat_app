import subprocess
import sys

def install_requirements():
    try:
        with open('requirements.txt', 'r') as file:
            requirements = file.readlines()
        
        for requirement in requirements:
            requirement = requirement.strip()
            if requirement:
                subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])
                print(f"Successfully installed {requirement}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {requirement}. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

install_requirements(requirements_file)
