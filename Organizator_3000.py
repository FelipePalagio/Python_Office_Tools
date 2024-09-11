import os
import shutil
import magic
from pathlib import Path


def organization(main_dir):
    os.chdir(main_dir)

    Path('IMAGENS').mkdir(exist_ok=True)
    Path('VIDEOS').mkdir(exist_ok=True)
    Path('OUTROS').mkdir(exist_ok=True)

    mime = magic.Magic(mime=True)

    for i in os.listdir():
        if os.path.isdir(i):
            if i in ['IMAGENS', 'VIDEOS', 'OUTROS']:
                print(f"PULAR PASTA: {i}")
            else:
                sub_dir_path = os.path.join(main_dir, i)
                os.chdir(sub_dir_path)
                for z in os.listdir():
                    try:
                        file_mime = mime.from_file(z)
                        if 'image' in file_mime:
                            shutil.move(z, f'{main_dir}/IMAGENS')
                        elif 'video' in file_mime:
                            shutil.move(z, f'{main_dir}/VIDEOS')
                        else:
                            shutil.move(z, f'{main_dir}/OUTROS')
                    except TypeError:
                        pass
                os.chdir(main_dir)
        else:
            try:
                file_mime = mime.from_file(i)
                if 'image' in file_mime:
                    shutil.move(i, f'{main_dir}/IMAGENS')
                elif 'video' in file_mime:
                    shutil.move(i, f'{main_dir}/VIDEOS')
                else:
                    shutil.move(i, f'{main_dir}/OUTROS')
            except TypeError:
                pass

    os.chdir(main_dir)
    for x in os.listdir():
        if os.path.isdir(x):
            if not os.listdir(x):
                os.rmdir(x)
                print(f"DELETANDO PASTA: {x}")
            else:
                print("")

