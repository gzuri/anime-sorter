import os
import shutil
import argparse

def move_anime(file, source_folder, destination_folder):
    anime_directory_name = file[15:file.rfind('-') - 1]
    target_folder = os.path.join(destination_folder, anime_directory_name)
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)

    if not os.path.exists(os.path.join(target_folder, file)):
        os.remove(os.path.join(target_folder, file))
            
    shutil.move(os.path.join(source_folder, file), os.path.join(target_folder, file))

    print(file + " - processed")


parser = argparse.ArgumentParser()
parser.add_argument("--src", help="source folder")
parser.add_argument("--dst", help="Destination folder")
args = parser.parse_args()

for file in os.listdir(args.src):
    if file.endswith(".mkv") and file.startswith("[HorribleSubs]"):
        # print(os.path.join(source_folder, file))
        move_anime(file, args.src, args.dst)
