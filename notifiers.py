def oats() -> None:
    """
    10 min timer for waiting oh so painfully waiting till oats are ready to eat!

    """

    import time
    from rich.progress import Progress

    with Progress() as progress:
        oat_task = progress.add_task("[white]Cooking Oats. . . ", total=1095)

        while not progress.finished:
            progress.update(oat_task, advance=0.2)
            time.sleep(0.1)

    print("Oats are Done! ENJOY :3 !!")
    play_sound("./sounds/IT-is-done.ogg")
    exit()


def play_sound(path_to_file: str) -> None:
    """plays a sound 

    Args:
        path_to_file (str): path to sound file
    """
    import vlc
    player = vlc.MediaPlayer()

    media = vlc.Media(path_to_file)
    player.set_media(media)

    player.play()

    while player.get_state() != vlc.State.Ended:
        pass

    player.release()
    exit()


if __name__ == "__main__":
    oats()
