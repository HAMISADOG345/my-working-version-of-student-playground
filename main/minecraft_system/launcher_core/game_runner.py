import sys
import subprocess
import os
import minecraft_launcher_lib

def main():
    username = sys.argv[1] if len(sys.argv) > 1 else "StudentPlayer"
    version = sys.argv[2] if len(sys.argv) > 2 else "1.20.1"

    # Keeps all heavy download assets localized entirely in the subfolder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    minecraft_directory = os.path.join(base_dir, "minecraft_data")

    print(f"[ENGINE] Downloading/Verifying assets inside: {minecraft_directory}")
    minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)

    options = {
        "username": username,
        "uuid": "",
        "token": ""
    }

    print("[ENGINE] Assembling boot arguments...")
    launch_command = minecraft_launcher_lib.command.get_minecraft_command(version, minecraft_directory, options)
    
    print("[ENGINE] Booting client frame...")
    subprocess.run(launch_command)

if __name__ == "__main__":
    main()