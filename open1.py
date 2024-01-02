import os

'''
bb = open('C:/Users/15481/Desktop/11/jibbed2.jpg','rb')
print(bb)
bb.close()
'''
print(os.name)
print(os.getcwd())
path = 'C:/Users/15481/Desktop/11/jibbed2.jpg'
if os.path.exists(path):
    os.remove('C:/Users/15481/Desktop/11/jibbed2.jpg')
    print("该文件已经被删除")
else:
    print('文件不存在')
