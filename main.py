from pathlib import Path
import tarfile
from typing import List


def get_dirs(directory: Path) -> List[Path]:
    return [x for x in directory.iterdir() if x.is_dir()]


def get_files(directory: Path) -> List[Path]:
    return [x for x in directory.iterdir() if x.is_file()]


def compress_dir(directory: Path) -> None:
    print(f'compressing directory: {directory}')


def compress_files(files: List[Path]) -> None:
    cwd = files[0].parent

    compressed_filename = cwd.name\
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
    
    compressed_path = Path.joinpath(cwd, f'{compressed_filename}.tar.lzma')
    print(compressed_path)

    # with tarfile.open(compressed_path, 'w') as tar:
    #     for file in files:
    #         tar.add(file)

    print(f'compressing files:')
    for file in files:
        print(f'  >> {file}')
    import ipdb; ipdb.set_trace()
    print(file)


def main() -> None:
    cwd = Path.cwd()
    for dir in get_dirs(cwd):
        compress_dir(dir)
    
    compress_files(get_files(cwd))


if __name__ == "__main__":
    main()
