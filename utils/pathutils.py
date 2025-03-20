from os.path import isfile
from time import time

def get_filename_index(file_path:str, max_index:int=10000) -> str:
    r"string ``file_path`` may contain ``{index}``, and ``{epoch}``"
    for i in range(1, max_index+1):
        if not isfile(formatted := file_path.format(index=str(i), epoch=int(time()))):
            print(formatted)
            return formatted
    raise FileExistsError(f"Max index ({max_index}) reached for {file_path}!")

