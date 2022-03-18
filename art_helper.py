from email.mime import image
from msilib.schema import Error
import consts
import subprocess , os, platform, random

#TODO: make this into a package for future ease of use :D

class ImagesHelper():

    def __init__(self, win_dir:str, wsl_dir:str) -> None:
        self.win_dir, self.wsl_dir = win_dir, wsl_dir

    def __repr__(self) -> str:
        return f"""
            {self} is an art helper class.
             two funcitons: 
             1. {self.organize}.
             2. {self.open_at_random}    
            """
    def organize(self, source:str, destination:str) -> bool:
        """takes all images from given directory into __BASE_FOLDER"""
        # takes in the directory 
            # checks os 
        current_os = platform.system()
        if current_os == "Windows":   
            # if theres a folder cool else create it 
            if not os.path.isdir(destination):
                os.mkdir(destination)
                # runs either powershell or bash command
            move_images = ["PowerShell", "-ExecutionPolicy", "Unrestricted",f"./commands/move_images.ps1 {source} {destination}" ]
            move_animated = ["PowerShell", "-ExecutionPolicy", "Unrestricted",f"./commands/move_animated.ps1 {source} {destination}" ]
            subprocess.call(move_images)
            subprocess.call(move_animated)
        
    @property
    def open_at_random(self) -> None:
        """opens a random image in given file tree"""
        current_os = platform.system()
        if current_os == "Windows":
            image_folder = random.choice(os.listdir(self.win_dir))
            img_base = image_folder 
            a = ""
            print(a)
            from PIL import Image
            try:
                while os.path.isdir(f"{self.win_dir}\\{a}\\"):
                    if (os.path.isfile(a)):
                        break
                    a = random.choice(os.listdir(f"{self.win_dir}\\{image_folder}\\"))
                file = os.path.join(f"{self.win_dir}\{img_base}\\{a}") 
                # spwan a process
                Image.open(file).show()
            except NotADirectoryError:
                file = os.path.join(f"{self.win_dir}\{image_folder}") 
                Image.open(file).show()

        elif current_os == "Linux" or current_os == "Darwin":
            # TODO: wsl is acting up, leaving for later ;-;
            image_folder = random.choice(os.listdir(self.wsl_dir))
            img_base = image_folder 
            a = ""
            print(a)
            from PIL import Image
            try:
                while os.path.isdir(f"{self.wsl_dir}\\{a}\\"):
                    if (os.path.isfile(a)):
                        break
                    a = random.choice(os.listdir(f"{self.wsl_dir}\\{image_folder}\\"))
                file = os.path.join(f"{self.wsl_dir}\{img_base}\\{a}") 
                Image.open(file).show()
            except NotADirectoryError:
                file = os.path.join(f"{self.wsl_dir}\{image_folder}") 
                Image.open(file).show()   




if __name__ == "__main__":
    image_helper = ImagesHelper(win_dir=consts.BASE_FOLDER_WIN, wsl_dir=consts.BASE_FOLDER_WSL)
    # image_helper.open_at_random()
    image_helper.organize("C:\\Users\\Sol\\Desktop","D:\\references")