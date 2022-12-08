import os, click, sys
from oranize_via_shell import organize_images as shell_orginize
from organization_via_python import organize_images as python_organize
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
    # shell_orginize(source=source, destination=destination)
    python_organize(source=source, destination=destination)


if __name__ == "__main__":
    organize()
    sys.exit(0)
