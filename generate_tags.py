import json
from tqdm import tqdm
from os import listdir,getcwd,path,chdir
old_cwd=getcwd()
chdir(path.join(getcwd(),"modules"))
from modules.img_tag_module import tag
chdir(old_cwd)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('image_path', type=str,nargs='?', default="./../test_images")
args = parser.parse_args()
IMAGE_PATH = args.image_path

ID_TAGS_ARR=[]
TAG_ONLY_IMPORT=True
file_names = listdir(IMAGE_PATH)
for file_name in tqdm(file_names):
    file_id=int(file_name[:file_name.index('.')])
    all_tags=tag(f"{IMAGE_PATH}/{file_name}")
    ID_TAGS_ARR.append({"id":file_id,"tags":all_tags})

with open('./id_tags.txt', 'w') as outfile:
    json.dump(ID_TAGS_ARR, outfile,ensure_ascii=False)