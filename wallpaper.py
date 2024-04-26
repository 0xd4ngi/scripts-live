import subprocess

def change_wallpaper_to_black():
    # Command to change wallpaper using gsettings
    command = "gsettings set org.gnome.desktop.background primary-color '#000000'"
    
    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    change_wallpaper_to_black()
