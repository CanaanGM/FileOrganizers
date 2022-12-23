import random, os, click, sys 
from pathlib import Path



def open_at_random( image_dir_path: str) -> None:
    """
    Opens a random image in given file directory

    Parameters
    ----------
    source : str
        path to the directory housing the images you want opened.
    """
    #! if there's subfolders
    base_directory = [
        folder_path for folder_path in Path(image_dir_path).iterdir()
        if folder_path.is_dir()
    ]
    subfolders : bool = True

    #! if there's no subfolders to iter thru
    if len(base_directory) <= 0:
        base_directory = [ folder_path for folder_path in Path(image_dir_path).iterdir()]
        subfolders = False

    supported_extensions = ["jpg", "png", "gif", "jpeg", "avif", "apneg"]
    all_files_in_dir = []
    all_images = []

    #! this will combine all images from all subfolders into one iterable
    if subfolders:
        for folder_path in base_directory:
            all_files_in_dir.extend(folder_path.glob("**/*"))
    else:
        all_files_in_dir.extend(base_directory)

    if all_files_in_dir:
        all_images.extend(
            file_path for file_path in all_files_in_dir
            if file_path.suffix[1:] in supported_extensions
        )

        random_image_index = random.randint(0, len(all_images) - 1)
        random_image_path = all_images[random_image_index]

        if os.name == "nt":
            os.startfile(random_image_path)
        elif os.name == "posix":
            os.system(f"xdg-open {random_image_path}")
        elif os.name == "mac":
            os.system(f"open {random_image_path}")

        return True

    return False

@click.command()
@click.option('--source', '-s', default=r"D:\references\random", help="Where the images are")
def main(source: str):
    open_at_random(source)
    sys.exit()



if __name__ == "__main__":
    main()
    sys.exit()
