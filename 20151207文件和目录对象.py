# -*- coding: utf-8 -*-
class Directory():
    def __init__(self,name):
        self.name = name
        self.contents = []
    def add(self,file_or_directory):
        self.contents.append(file_or_directory)
    def delete(self,file_or_directory):
        self.contents.remove(file_or_directory)
    def rename(self,name):
        self.name = name
    def __contains__(self,file_or_directory):   # 判断文件是否在里面
        for i in self.contents:
            if i.name == file_or_directory.name:
                return 1
        return 0
    def child_directory(self,directory_name):   # 获取文件夹下面某个名字是 directory_name 的目录
        for file_or_directory in self.contents:
            if file_or_directory.name == directory_name:
                return file_or_directory
    def isFile(self):
        return False
    def isDir(self):
        return True
    def dictconvert(self):
        result = {}
        result['name'] = self.name
        result['is_directory'] = True
        result['children'] = []
        for i in self.contents:
            result['children'].append(i.dictconvert())
        return result
    def son_dir(self, name):  # 获取子目录,仅仅一层
        ''' root_dir.son_dir('/home') 前后有没有 '/' 都可以'''
        son_path = name.strip('/')
        for i in self.contents:
            if i.name == son_path:
                return i
        else:
            return None
    def child_dir(self, path):    # 根据子路径来获取子目录
        ''' root_dir.child_dir('/home/zettagedocker/nfs/3/workspace/'''
        father_dir, son_dir = os.path.split(path)
        if father_dir != '/':
            return self.child_dir(father_dir).son_dir(son_dir)
        else:
            return self.son_dir(son_dir)
        
class File():
    def __init__(self,name):
        self.name = name
        self.contents = []
    def rename(self,name):
        self.name = name
    def save(self,text):
        self.contents = text
    def isFile(self):
        return True
    def isDir(self):
        return False
    def dictconvert(self):
        result = {}
        result['name'] = self.name
        result['is_directory'] = False
        return result
def addFileToDirectory(father_directory,path_list):
    '''path_list,是直接 path.split('/').remove('')获取的，
        最后的空字符串存在与否来判断是文件还是目录
        ['home','guacamole'],
        ['home','guacamole','test.py'],
        '''
    if len(path_list) == 2 and path_list[1]=='':    # 最后一个目录
        leaf_directory = Directory(path_list[0])
        if leaf_directory in father_directory:
            print('路径完全一致')
            return 1
        else:
            father_directory.add(leaf_directory)
    elif len(path_list) == 2 and path_list[1]!='':  # 最后不是路径而是文件
        leaf_file = File(path_list[1])
        leaf_directory = Directory(path_list[0])
        if leaf_directory in father_directory:  # 如果有目录，则目录下添加文件
            father_directory.child_directory(leaf_directory.name).add(leaf_file)
        else:   # 没有最后一个目录,把文件添加到目录，把目录加入到父文件夹
            leaf_directory.add(leaf_file)
            father_directory.add(leaf_directory)
    else:   # 尚没有到最后一个目录
        next_directory = Directory(path_list[0])
        if next_directory in father_directory:  # 如果存在,获取子目录
            child_directory = father_directory.child_directory(next_directory.name)
        else:
            father_directory.add(next_directory)    # 如果不存在子目录，就创建子目录
            child_directory = father_directory.child_directory(next_directory.name)
        addFileToDirectory(child_directory,path_list[1:])
if __name__ == '__main__':
    path_list = [u'/home/zettagedocker/nfs/32/workspace/', u'/home/zettagedocker/nfs/32/workspace/edit_your_file_here', u'/home/zettagedocker/nfs/32/dataset/']
    root_dir = Directory('/')
    for i in path_list:
        tmp = i.split('/')
        tmp.remove('')
        addFileToDirectory(root_dir, tmp)
