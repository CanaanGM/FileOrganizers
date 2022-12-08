import subprocess, os, platform, click

# TODO: make this into a package for future ease of use :D

@click.command()
@click.option('--source',default=f"{os.path.expanduser('~')}\\Desktop", help="Where the images u wanna move are located")
@click.option('--destination', default=r"D:\references", help="Where to move the images")
def organize( source: str, destination: str) -> bool:
    """
    takes all images from source directory into destination directory.

    Parameters
    ----------
    source : str
        path to the directory housing the images you want organized.
    destination : str
        Path to the directory you want the images organized in.

    Returns
    -------
    bool
    If the operationg had any exceptions or not.
    """
    current_os = platform.system()
    if current_os == "Windows":
        try:
            if not os.path.isdir(destination):
                os.mkdir(destination)
            move_images = [
                "PowerShell",
                "-ExecutionPolicy",
                "Unrestricted",
                f"./commands/move_images.ps1 {source} {destination}",
            ]
            move_animated = [
                "PowerShell",
                "-ExecutionPolicy",
                "Unrestricted",
                f"./commands/move_animated.ps1 {source} {destination}",
            ]
            subprocess.call(move_images)
            subprocess.call(move_animated)
            print("Organized~!")
            return True
        except Exception:
            print("some thing went wrong in organizing the images ;=;")
            return False

    elif current_os == "Linux" or current_os == "Darwin":
        try:
            if not os.path.isdir(destination):
                os.mkdir(destination)

            subprocess.Popen(
                ["./commands/move_images.sh", f"-s{source}", f"-d{destination}"]
            )
            print("Organized~!")
            return True
        except Exception:
            print("some thing went wrong in organizing the images ;=;")
            return False




if __name__ == "__main__":
    organize()
