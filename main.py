import shutil
from pathlib import Path

folder = Path("Assets")

for item in folder.iterdir():

    if item.is_file():

        extension = item.suffix[1:].upper()
        if not extension:
            extension = "NO_EXTENSION"

        new_folder = folder / extension
        new_folder.mkdir(exist_ok=True)

        destination = new_folder / item.name
        shutil.move(str(item), str(destination))
