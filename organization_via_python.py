import os
from os import path
import shutil
from typing import List

def organize_images(source: str, destination: str) -> None:


    source_dir_files = os.listdir(source)

    animated_dir = path.join(destination, "animated")
    normal_dir = path.join(destination, "random")

    for dir_ in (destination, animated_dir, normal_dir):
        _create_dir_if_doesnt_exist(dir_)


    # Iterate over the files in the source directory
    for file_name in source_dir_files:
        # Get the full path of the file


        file_path = path.join(source, file_name)


        images_extensions = ["jpg" , "png", "jpeg"]
        animated_images_extensions = ["gif", "apng", "avif"]
        
        _move_file(file_name, file_path, normal_dir, images_extensions )
        _move_file(file_name, file_path, animated_dir, animated_images_extensions )



def _create_dir_if_doesnt_exist(dir_path: str) -> None:
    """checks if the dir is there, and creates it if not

    Args:
        dir_path (str): path to the directory
    """
    if not path.exists(dir_path):
        os.makedirs(dir_path)

def  _move_file(file_name: str, file_path:str,  target_dir: str, extension_list:List[str] ) -> None:
    """checks the extension of the file and moves it to the appropreate directory

    Args:
        file_name (str): file name of the file in source directory files
        file_path (str): the path to the file in the source directory 
        target_dir (str): the target directory to which u want to move the file
        extension_list (List[str]): the iterator where u put the extensions u want moved
    """

    if file_name.split(".")[-1] in extension_list:
        dest_path = path.join(target_dir, file_name)
        shutil.move(file_path, dest_path)
