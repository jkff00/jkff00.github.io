import os
import random
import re
import shutil

# 1 读取文件列表
image_dir = r'F:/dataset/fire/newsmoke/FIRE-SMOKE-DATASET/Train/Fire/' # 一开始存放有图片的文件夹，你需要修改成你的文件夹名字
img_name_list = os.listdir(image_dir)
print(img_name_list[:5])

# 2 创建一个目标文件夹
result_dir = r'F:/dataset/fire/newsmoke/FIRE-SMOKE-DATASET/Train/result/' # 目标文件夹（最终存放乱序后的文件夹），会自动创建
if not os.path.exists(result_dir):
    os.makedirs(result_dir)
    print(f'创建文件夹{result_dir}成功！')

# 3 创建随机数
random_len = len(img_name_list)
img_index = [i for i in range(random_len)]
random.shuffle(img_index)
# img_index

# 开始转移每个文件
for i, img in enumerate(img_name_list):
    dot_index = img.find('.')
    if dot_index > 0:
        img_name = str(img_index[i]) + img[dot_index:]
        shutil.copyfile(image_dir + img, result_dir + img_name) # 如果你的磁盘不够大，那么这个copyfile要改成move，但是此时需要注意备份好原来的文件夹里的文件！
