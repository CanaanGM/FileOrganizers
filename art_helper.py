import subprocess, os, platform, random

# TODO: make this into a package for future ease of use :D


class ImagesHelper:
    def __repr__(self) -> str:
        return f"""
            {self} is an art helper class.
             two funcitons: 
             1. {self.organize}.
             2. {self.open_at_random}    
            """

    def organize(self, source: str, destination: str) -> bool:
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

    def open_at_random(self, source: str) -> None:
        """
        Opens a random image in given file directory

        Parameters
        ----------
        source : str
            path to the directory housing the images you want opened.
        """
        current_os = platform.system()
        if current_os == "Windows":
            image_folder = random.choice(os.listdir(source))
            img_base = image_folder
            a = ""
            print(a)
            from PIL import Image

            try:
                while os.path.isdir(f"{source}\\{a}\\"):
                    if os.path.isfile(a):
                        break
                    a = random.choice(os.listdir(f"{source}\\{image_folder}\\"))
                file = os.path.join(f"{source}\{img_base}\\{a}")
                # spwan a process
                Image.open(file).show()
            except NotADirectoryError:
                file = os.path.join(f"{source}\{image_folder}")
                Image.open(file).show()

        elif current_os == "Linux" or current_os == "Darwin":
            image_folder = random.choice(os.listdir(source))
            img_base = image_folder
            a = ""
            print(a)
            from PIL import Image

            try:
                while os.path.isdir(f"{source}/{a}/"):
                    if os.path.isfile(a):
                        break
                    a = random.choice(os.listdir(f"{source}/{image_folder}/"))
                file = os.path.join(f"{source}/{img_base}/{a}")
                Image.open(file).show()
            except NotADirectoryError:
                file = os.path.join(f"{source}/{image_folder}")
                Image.open(file).show()


if __name__ == "__main__":

    image_helper = ImagesHelper( )
    # image_helper.open_at_random("D:\\references" )
    # image_helper.organize("C:\\Users\\Sol\\Desktop","D:\\references")
    # image_helper.open_at_random("/home/terra/references")
    # image_helper.organize("/home/terra/","/home/terra/references")
