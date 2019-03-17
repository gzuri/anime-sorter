import os
import shutil

source_folder = "D:\\Downloads\\Complete"
destination_folder = "D:\\AnimeInProgress"

def move_anime(file):
    anime_directory_name = file[15:file.rfind('-') - 1]
    target_folder = os.path.join(destination_folder, anime_directory_name)
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)

    if not os.path.exists(os.path.join(target_folder, file)):
        shutil.move(os.path.join(source_folder, file), os.path.join(target_folder, file))
    else: 
        shutil.rmtree(os.path.join(target_folder, file))

    print(file + " - processed")


for file in os.listdir(source_folder):
    if file.endswith(".mkv") and file.startswith("[HorribleSubs]"):
        # print(os.path.join(source_folder, file))
        move_anime(file)
