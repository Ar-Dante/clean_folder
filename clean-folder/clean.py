import sys
import os
import shutil
from pathlib import Path


def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter

legend = {
    ' ': '_',    ',': '_',
    '!': '_',    '@': '_',
    '$': '_',    '%': '_',
    '^': '_',    '&': '_',
    '*': '_',    '(': '_',
    ')': '_',    '?': '_',
    '№': '_',    ';': '_',
    '"': '_',    ':': '_',
    '-': '_',    'а': 'a',
    'б': 'b',    'в': 'v',
    'г': 'g',    'д': 'd',
    'е': 'e',    'ё': 'yo',
    'ж': 'zh',    'з': 'z',
    'и': 'i',    'й': 'y',
    'к': 'k',    'л': 'l',
    'м': 'm',    'н': 'n',
    'о': 'o',    'п': 'p',
    'р': 'r',    'с': 's',
    'т': 't',    'у': 'u',
    'ф': 'f',    'х': 'h',
    'ц': 'c',    'ч': 'ch',
    'ш': 'sh',    'щ': 'shch',
    'ъ': 'y',    'ы': 'y',
    'ь': "'",    'э': 'e',
    'ю': 'yu',    'я': 'ya',
    'А': 'A',    'Б': 'B',
    'В': 'V',    'Г': 'G',
    'Д': 'D',    'Е': 'E',
    'Ё': 'Yo',    'Ж': 'Zh',
    'З': 'Z',    'И': 'I',
    'Й': 'Y',    'К': 'K',
    'Л': 'L',    'М': 'M',
    'Н': 'N',    'О': 'O',
    'П': 'P',    'Р': 'R',
    'С': 'S',    'Т': 'T',
    'У': 'U',    'Ф': 'F',
    'Х': 'H',    'Ц': 'Ts',
    'Ч': 'Ch',    'Ш': 'Sh',
    'Щ': 'Shch',    'Ъ': 'Y',
    'Ы': 'Y',    'Ь': "_",
    'Э': 'E',    'Ю': 'Yu',
    'Я': 'Ya',
    }


def normalize(old_file):
    file_new = latinizator(old_file, legend)
    return file_new


#Функція для перенесення всіх файлів підкаталогів в кореневий каталог
def clearing_subfolders(path):
    Subfolders = os.listdir(path)
    print(Subfolders)
    filelist = []
    for tree, fol, fils in os.walk(path):
        filelist.extend([os.path.join(tree, fil) for fil in fils])
    for fil in filelist:
        os.rename(fil, os.path.join(path, fil[fil.rfind('\\') + 1:]))


#Функція для видалення порожніх каталогів
def delete_empty_folder(path):
    for dir in os.listdir(path):
        a = os.path.join(path, dir)
        if os.path.isdir(a):
            delete_empty_folder(a)
            if not os.listdir(a):
                print("Порожні теки було видалено")
                os.rmdir(a)



def rename_file(path):
    files = os.listdir(path)

    for file in files:
        os.rename(file, normalize(file))


def get_file_list(folder):
    folder = Path(folder)
    try:
        folder = Path(folder)
    except FileNotFoundError:
        print(f"file {folder} is not found")
    finally:
        print("Make this again")
    file_list = sorted(folder.glob("**/*"))
    return file_list


#Функція для сортування файлів по формату
def sort_file(put):
    file_list = get_file_list(put)
    documents = ['.pdf', '.docx', '.doc', '.txt','.xlsx',  '.pdf', '.pptx']
    images = ['.jpeg', '.jpg', '.svg', '.png']
    video = ['.avi', '.mp4', '.mov', '.mkv']
    music = ['mp3', '.ogg', 'wav', '.amr']
    compressedFiles = ['.zip', '.gz', '.tar']
    all = ['.pdf', '.docx', '.doc', '.txt', '.pdf','.xlsx',
           '.pptx', '.jpeg', '.jpg', '.svg', '.png', '.avi',
           '.mp4', '.mov', '.mkv', 'mp3', '.ogg', 'wav', '.amr',
           '.zip', '.gz', '.tar' ]
    DocumentsLocation = os.path.join(put, 'Documents')
    ImageLocation = os.path.join(put, 'Images')
    VideoLocation = os.path.join(put, 'Video')
    compressedFilesLocation = os.path.join(put, 'CompressedFiles')
    MusicLocation = os.path.join(put, 'Music')
    FilesLocation = os.path.join(put, 'Files')
    for file in file_list:
            if os.path.splitext(file)[1] in all:
                if os.path.splitext(file)[1] in documents:
                    try:
                        if not (os.path.exists(DocumentsLocation)):
                            os.mkdir(DocumentsLocation)
                        path = Path(file)
                        new_locations = shutil.move(path.absolute(), DocumentsLocation)
                        new_name = normalize(path.stem) + path.suffix
                        os.rename(new_locations, os.path.join(DocumentsLocation, new_name))
                    except Exception as err:
                        print(f'[ERROR]: {err}')
                        continue
                if os.path.splitext(file)[1] in images:
                    try:
                        if not (os.path.exists(ImageLocation)):
                            os.mkdir(ImageLocation)
                        path = Path(file)
                        new_locations = shutil.move(path.absolute(), ImageLocation)
                        new_name = normalize(path.stem) + path.suffix
                        os.rename(new_locations, os.path.join(ImageLocation, new_name))
                    except Exception as err:
                        print(f'[ERROR]: {err}')
                        continue
                if os.path.splitext(file)[1] in video:
                    try:
                        if not (os.path.exists(VideoLocation)):
                            os.mkdir(VideoLocation)
                        path = Path(file)
                        new_locations = shutil.move(path.absolute(), VideoLocation)
                        new_name = normalize(path.stem) + path.suffix
                        os.rename(new_locations, os.path.join(VideoLocation, new_name))
                    except Exception as err:
                        print(f'[ERROR]: {err}')
                        continue
                if os.path.splitext(file)[1] in music:
                    try:
                        if not (os.path.exists(MusicLocation)):
                            os.mkdir(MusicLocation)
                        path = Path(file)
                        new_locations = shutil.move(path.absolute(), MusicLocation)
                        new_name = normalize(path.stem) + path.suffix
                        os.rename(new_locations, os.path.join(MusicLocation, new_name))
                    except Exception as err:
                        print(f'[ERROR]: {err}')
                        continue
                try:
                    if os.path.splitext(file)[1] in compressedFiles:
                        if not (os.path.exists(compressedFilesLocation)):
                            os.mkdir(compressedFilesLocation)
                        path = Path(file)
                        new_locations = shutil.move(path.absolute(), compressedFilesLocation)
                        new_name = normalize(path.stem) + path.suffix
                        print(f'new_name {new_name}, new loc: {new_locations}')

                        os.rename(new_locations, os.path.join(compressedFilesLocation, new_name))
                        shutil.unpack_archive(Path(new_locations).absolute(), os.path.join(compressedFilesLocation, path.stem))
                except Exception as err:
                    print(f'ERROR {err}')
            else:
                 try:
                    if not (os.path.exists(FilesLocation)):
                        os.mkdir(FilesLocation)
                    path = Path(file)
                    shutil.move(path.absolute(), FilesLocation)
                 except Exception as err:
                        print(f'[ERROR]: {err}')
                        continue


def main():
    put = None
    try:
        put = sys.argv[1]
        clearing_subfolders(put)
        sort_file(put)
        delete_empty_folder(put)
    except IndexError:
        print("Перевірте шлях до необхідної директорії та спробуйте ще раз)")


if __name__ == '__main__':
    main()
