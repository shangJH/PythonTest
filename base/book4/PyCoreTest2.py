'''
   chap03 因特网客户端编程
'''

from ftplib import FTP
f = FTP('10.142.80.21')
info = f.login(user='BSS-Jizhong',passwd='H6g!52et')
print(info)
print('current dir', f.pwd())
print('change dir', f.cwd('/shencong'))
print(f.dir())
print(f.nlst())
# 文件传输使用二进制传输方式！
f.retrbinary("RETR upload.sh", open("upload.sh", 'wb').write)  # 下载文件
f.quit()