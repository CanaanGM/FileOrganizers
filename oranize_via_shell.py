import platform, subprocess, os

def organize_images(source :str,  destination: str) -> bool:
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
