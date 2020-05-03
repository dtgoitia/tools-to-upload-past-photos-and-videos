from pathlib import Path
import tarfile
from typing import List, Tuple
import shutil


COMPRESSION_MODE = 'w:xz'  # https://docs.python.org/3/library/tarfile.html#tarfile.open
SKIP_FILES = ('Thumbs.db', 'blah')

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


def get_tree_paths(directory: Path) -> List[Path]:
    result = []
    for path in directory.iterdir():
        if path.name in SKIP_FILES:
            continue
        if path.is_dir():
            for subpath in get_tree_paths(path):
                result.append(subpath)
            continue
        if path.is_file():
            result.append(path)
    return result


def get_arcnames(paths: List[Path], base_path: Path) -> Tuple[str, str]:
    as_strings = [str(path) for path in paths]
    return [(path, path.replace(f'{base_path}/', '')) for path in as_strings]


def compress_dir(directory: Path) -> None:
    path = get_compressed_path(directory)
    path = f'{path}.tar.xz'
    print(f'compressing {path}')
    
    arcnames = get_arcnames(get_tree_paths(directory), directory.parent)
    with tarfile.open(path, COMPRESSION_MODE) as tar:
        for abs_path, arcname in arcnames:
            print(f'  > {arcname}')
            tar.add(abs_path, arcname=arcname)

    shutil.rmtree(str(directory))


def compress_files(files: List[Path]) -> None:
    path = get_compressed_path(files[0].parent)
    path = f'{path}.tar.xz'

    with tarfile.open(path, COMPRESSION_MODE) as tar:
        for file in files:
            if file.name in SKIP_FILES:
                continue
            tar.add(file, arcname=file.name)  # compress
            file.unlink()  # delete


def main() -> None:
    cwd = Path.cwd()
    compress_files(get_files(cwd))

    for dir in get_dirs(cwd):
        compress_dir(dir)
    


if __name__ == "__main__":
    main()
