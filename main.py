from pathlib import Path
import tarfile
from typing import List
import shutil


def get_dirs(directory: Path) -> List[Path]:
    return [x for x in directory.iterdir() if x.is_dir()]


def get_files(directory: Path) -> List[Path]:
    return [x for x in directory.iterdir() if x.is_file()]


def get_compressed_path(directory: Path) -> str:
    compressed_filename = directory.name\
        .strip() \
        .lower() \
        .replace('á', 'a') \
        .replace('é', 'e') \
        .replace('í', 'i') \
        .replace('ó', 'o') \
        .replace('ú', 'u') \
        .replace('º', '') \
        .replace('ª', '') \
        .replace('[', '') \
        .replace(']', '') \
        .replace('(', '') \
        .replace(')', '') \
        .replace(' - ', '_') \
        .replace(' ', '-')

    compressed_path = Path.joinpath(Path.cwd(), compressed_filename)
    return compressed_path


def compress_dir(directory: Path) -> None:
    path = get_compressed_path(directory)
    shutil.make_archive(str(path), 'xztar')
    shutil.rmtree(str(directory))


def compress_files(files: List[Path]) -> None:
    path = get_compressed_path(files[0].parent)
    path = f'{path}.tar.xz'

    with tarfile.open(path, 'w') as tar:
        for file in files:
            tar.add(file)  # compress
            file.unlink()  # delete


def main() -> None:
    cwd = Path.cwd()
    for dir in get_dirs(cwd):
        compress_dir(dir)
    
    compress_files(get_files(cwd))


if __name__ == "__main__":
    main()
