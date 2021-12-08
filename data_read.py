<<<<<<< HEAD
=======
from os import path
>>>>>>> 4df19cef41279b573a407d1e02617d1b6500e69d
import pathlib

def read_file(file_name):
    current_dir = pathlib.Path(__file__).parent.absolute()
    file_path = pathlib.Path(current_dir / "data" / file_name)

    with open(file_path, "r") as file:
        content = file.readlines()

    return content

