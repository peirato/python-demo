import os



# 处理文件夹内文件名
# def process_file_name(dir_path):

# for file in os.listdir(dir_path):
#     # print(file)
#     path_file = dir_path + '/' + file
#     if (os.path.isdir(path_file)):
#         for file2 in os.listdir(path_file):
#             # print(file2)
#             path_file2 = path_file + '/' + file2
#             if (os.path.isdir(path_file2)):
#                 for file3 in os.listdir(path_file2):
#                     print(file3.replace('.png',''))
#                     if '@2x' in file3:
#                         file4 = file3.replace('@2x', '')
#                         os.rename(path_file2+'/'+file3, path_file2+'/'+file4)
#                         print('文件名修改:' + file3 + '改为' + file4)

# 检查文件夹和文件名
def check_file_name(dir_path):
    # TODO 检查type名 需要从数据库读取全部type name

    # 获取所有大图分类名
    standard_path_list = os.listdir(dir_path + '/standard')

    standard_path_list.remove('.DS_Store')
    print(standard_path_list)

    # 获取所有缩略图分类名
    sl_path_list = os.listdir(dir_path + '/sl')
    sl_path_list.remove('.DS_Store')
    print(sl_path_list)

    # 检查文件夹是否对应
    # 只有缩略图有套装
    sl_path_list.remove('tao')

    # 检查sl文件夹
    for fn in standard_path_list:
        if fn == 'hair_top' or fn == 'hair_back':
            if 'hair' not in sl_path_list:
                print('sl文件夹中不包含hair文件夹')
        else:
            if fn not in sl_path_list:
                print('sl文件夹中不包含' + fn + '文件夹')

    # 检查standard文件夹
    for fn in sl_path_list:
        if fn == 'hair':
            if 'hair_top' not in standard_path_list:
                print('standard文件夹中不包含hair_top文件夹')
            if 'hair_back' not in standard_path_list:
                print('standard文件夹中不包含hair_back文件夹')
        else:
            if fn not in standard_path_list:
                print('standard文件夹中不包含' + fn + '文件夹')

    # 大图和小图对应存在

    # 将所有文件放入列表 并判断文件格式
    all_standard_img = []
    for fn in standard_path_list:
        for img in os.listdir(dir_path + '/standard/' + fn):
            if img != '.DS_Store':
                if '.png' not in img:
                    print(dir_path + '/standard/' + fn + '/' + img + '不是png格式')
                else:
                    if 'hair' not in img:
                        all_standard_img.append(img)

    all_sl_img = []
    for fn in sl_path_list:
        for img in os.listdir(dir_path + '/sl/' + fn):
            if img != '.DS_Store':
                if '.png' not in img:
                    print(dir_path + '/sl/' + fn + '/' + img + '不是png格式')
                else:
                    if 'hair' not in img:
                        # 缩略图文件名需要修改
                        all_sl_img.append(img.replace('sl_', ''))

    for img in all_sl_img:
        if img not in all_standard_img:
            print('standard文件夹中不存在' + img)

    for img in all_standard_img:
        if img not in all_sl_img:
            print('sl文件夹中不存在' + img)



# 插入表

# 自动生成类别 根据缩略图生成资源名 根据type名生成type id

if __name__ == '__main__':
    check_file_name('/Users/yangzeqi/Desktop/2020.11.09 换装切图（更新又更新')
