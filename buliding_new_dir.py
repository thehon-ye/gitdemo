import os   #创建一个文件夹

title=('')
def mkdir(title):
    path  =title.strip()#去除空格
    isExists = os.path.exists(os.path.join(r'D:\xmly\\',path))#判断路径是否存在
    if not isExists:
        print(u'创建一个叫做{}的文件夹'.format(title))
        os.makedirs(os.path.join(r'D:\xmly\\',title))
        return True
    else :
        print('名字叫做{}的文件架已经存在'.format(title))

a=mkdir(title)