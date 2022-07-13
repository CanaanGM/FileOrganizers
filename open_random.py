import random, os, platform, click

@click.command()
@click.option('--source', default=r"D:\references", help="Where the images are")
def open_at_random( source: str) -> None:
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
    open_at_random()
