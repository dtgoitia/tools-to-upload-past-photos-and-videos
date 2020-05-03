from pathlib import Path
import tarfile
from typing import List


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

    compressed_path = Path.joinpath(Path.cwd(), f'{compressed_filename}.tar.lzma')
    return compressed_path


def compress_dir(directory: Path) -> None:
    print(get_compressed_path(directory))


def compress_files(files: List[Path]) -> None:
    print(get_compressed_path(files[0].parent))

    # with tarfile.open(compressed_path, 'w') as tar:
    #     for file in files:
    #         tar.add(file)

    for file in files:
        pass
        # print(f'  >> {file}')
    # print(file)


def main() -> None:
    cwd = Path.cwd()
    for dir in get_dirs(cwd):
        compress_dir(dir)
    
    compress_files(get_files(cwd))


if __name__ == "__main__":
    main()
