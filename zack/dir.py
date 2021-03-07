import os

res = []

def get_file(path,res,file_type):
    files = os.listdir(path)
    for filename in files:
        file_path = os.path.join(path,filename)
        if os.path.isdir(file_path):
            get_file(file_path,res,file_type)
        elif filename[-len(file_type):] == file_type:
            res.append(filename)
path = input("请输入路径：").strip()
file_type = input("请输入文件扩展名：").strip()

get_file(path,res,file_type)

print('总共查找到{0:d}个文件'.format(len(res)))

for i in res:
    print(i)

