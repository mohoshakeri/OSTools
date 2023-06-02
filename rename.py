import os

def new_name(file,i,zero_count,path,start):
    format = file.split('.')[-1]
    newname = (zero_count * '0') + str(i+1)
    if len(newname) > (zero_count + 1):
        newname = newname[abs(len(newname)-(zero_count+1)):]
    if os.path.isfile(os.path.join(path,file)):
        newname = newname + '.' + format
    return start + newname

def rename_all(path,start='',dir_ch=True,file_ch=True):
    if file_ch:
        if dir_ch:
            files = os.listdir(path)
        else:
            files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i))]
    else:
        if dir_ch:
            files = [i for i in os.listdir(path) if os.path.isdir(os.path.join(path,i))]
        else:
            files = []

    dir_len = len(files)
    zero_count = 1
    if dir_len > 99:
        zero_count = len(str((dir_len // 10)))
        
    force_renamed = []
    
    for i, file in enumerate(files):
        q_rename = []
        newname = new_name(file,i,zero_count,path,start)
        if newname == file or i in force_renamed:
            continue
        
        q_rename.insert(0,{'old' : file , 'new' : newname})
        while newname in files:
            i = files.index(newname)
            file = files[i]
            newname = new_name(file,i,zero_count,path,start)
            q_rename.insert(0,{'old' : file , 'new' : newname})
            force_renamed.append(i)
        
        for obj in q_rename:
            os.rename(os.path.join(path,obj['old']),os.path.join(path,obj['new']))