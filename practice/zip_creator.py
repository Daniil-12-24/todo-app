import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_dir = pathlib.Path(dest_dir, '../compressed.zip')
    with zipfile.ZipFile(dest_dir, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=['homework.py', 'questions.json'], dest_dir='../dest')