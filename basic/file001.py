# -*- coding: utf-8 -*-

#%%

file = open('sanguo.txt', 'a')
file.write("test")
file.close()

#%%
f1 = open('sanguo.txt', 'r')
print(f1.read())
f1.close()

#%%
f1 = open('sanguo.txt', 'r')
print(f1.readline())

for line in f1.readlines():
    print(line)

f1.close()

#%%
f1 = open('sanguo.txt', 'r')
print(f1.tell())
print(f1.readline())
print(f1.tell())    # 输出文件指针位置
f1.seek(0)  # 将文件指针设置到0
print(f1.tell())

