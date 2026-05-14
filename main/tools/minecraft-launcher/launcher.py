import sys
import subprocess
import os
import minecraft_launcher_lib

def main():
    print("=======================================================")
    print("         MINECRAFT CORE GAME RUNNER ENGINE             ")
    print("=======================================================")
    username = sys.argv[1] if len(sys.argv) > 1 else "MC_player"
    version = sys.argv[2] if len(sys.argv) > 2 else "1.20.1"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    minecraft_directory = os.path.join(base_dir, "minecraft_data")

    print(f"[ENGINE] Active User:    {username}")
    print(f"[ENGINE] Active Version: {version}")
    print(f"[ENGINE] Storage Path:   {minecraft_directory}")
    print("-------------------------------------------------------")
    print("[ENGINE] Syncing asset libraries and manifests...")
    try:
        minecraft_launcher_lib.install.install_minecraft_version(
            version, 
            minecraft_directory
        )
    except Exception as e:
        print(f"[CRITICAL ERROR] Failed to download game assets: {e}")
        sys.exit(1)
    options = {
        "username": username,
        "uuid": "",
        "token": ""
    }
    print("[ENGINE] Assembling runtime parameters...")
    try:
        launch_command = minecraft_launcher_lib.command.get_minecraft_command(
            version, 
            minecraft_directory, 
            options
        )
    except Exception as e:
        print(f"[CRITICAL ERROR] Failed to generate string configuration: {e}")
        sys.exit(1)
    print("[ENGINE] Opening Minecraft Java Edition. Have fun!")
    print("-------------------------------------------------------")
    subprocess.run(launch_command)

    print("this will take a while...")

if __name__ == "__main__":
    main()