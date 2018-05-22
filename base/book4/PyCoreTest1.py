'''
   chap01 正则表达式
'''
import os
import re

# 扩展表达式最麻烦
# (?:\w+\.)   以句点作为结尾的字符串，但是这些匹配不会保存下来供后续的使用和数据检索
# (?#comment) 此处不做匹配，只是作为注释
# (?=.com) 如果一个字符串后面跟着".com"才做匹配操作，并不使用任何目标字符串
# (?!.net) 如果一个主辅材后面不是跟着".net"才做匹配操作
# (?<=800-) 如果一个字符串之前为"800-"才做匹配，假定为电话号码，同样不使用任何输入字符串
# (?<!192\.168\.) 如果一个字符串之前不是"192.168."才做匹配操作，假定用于过滤掉一组C类IP地址
# (?(1)y|x) 如果匹配组1(\1)存在，就与y匹配；否则就与x匹配

'''
    re模块：核心函数和方法
    compile(pattern, flags=0)
    match(pattern, string, flags=0)
    search(pattern, string, flags=0)
    findall(pattern, string[, flags])
    finditer(pattern, string[, flags])
    split(pattern, string, max=0)

    sub(pattern, repl, string, max=0)

    group(num=0)
    groups(default=None)
    groupdict(default=None)

    re.I、re.IGNORECASE
    re.L、re.LOCAL
    re.M、re.MULTILINE
    re.S
    re.X
'''

m = re.match('foo', 'foo')
if m is not None:
    print("match:", m.group())

m = re.match('foo', 'bar')
if m is not None:
    print(m.group())
else:
    print("not match")

# 使用match匹配，必须是从头开始匹配
m = re.match('foo', 'food on the table')
if m is not None:
    print("match:", m.group())

# 使用search()在一个字符串中查找模式，如果使用match进行匹配，开头不匹配的不会匹配到
m = re.search('foo', 'seafood')
if m is not None:
    print("search:", m.group())

# 匹配多个字符串
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print("match:", m.group())

m = re.match(bt, 'blt')
if m is not None:
    print("match:", m.group())

m = re.match(bt, 'He bit me!')   # 不是开头，所以也匹配不到
if m is not None:
    print("match:", m.group())

m = re.search(bt, 'He bit me!')
if m is not None:
    print("search:", m.group())

anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:
    print("match:", m.group())

m = re.match(anyend, 'end')
if m is not None:
    print("match:", m.group())

m = re.match(anyend, '\nend')        # .匹配任何处理\n之外的字符
if m is not None:
    print("match:", m.group())

m = re.search(anyend, 'The end.')   # .可以匹配空格
if m is not None:
    print("search:", m.group())

patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt, '3.14')
if m is not None:
   print("match", m.group())

m = re.match(patt314, '3014')
if m is not None:
   print("match", m.group())

m = re.match(patt314, '3.14')
if m is not None:
   print("match", m.group())

# 创建字符集
m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None:
   print("match", m.group())

m = re.match('[cr][23][dp][o2]', 'c2po')
if m is not None:
   print("match", m.group())

m = re.match('c2d2|c3po', 'c2do')   # 不匹配
if m is not None:
   print("match", m.group())

m = re.match('r2d2|c3po', 'r2d2')   # 匹配
if m is not None:
   print("match", m.group())

# 重复、特殊字符以及分组
patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print("match:", m.group())

m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print("match:", m.group())

m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print("match:", m.group())

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None:
    print("match:", m.group())

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print("match:", m.group())
    print("match groups:", m.groups())   # groups()方法来获取一个包含所有匹配子字符串的元组
    print("match 1:", m.group(1))
    print("match 2:", m.group(2))

# findall()和finditer()查找每一次出现的位置
m = re.findall('car', 'carry the barcardi to the car')
if m is not None:
    print("findall:", m)  # 返回的是一个list

s = 'This and that'
m = re.findall('(th\w+) and (th\w+)', s, re.I)
if m is not None:
    print("findall:", m)

mIter = re.finditer('(th\w+) and (th\w+)', s, re.I)
if mIter is not None:
    print("finditer", [g.groups() for g in mIter])

# sub()和subn()搜索域替换,subn()返回两个元素的元组，第二个元素为替换总数
print(re.sub('X', 'Mr. Smith', 'attn:X\n\nDear X,\n'))
print(re.subn('X', 'Mr. Smith', 'attn:X\n\nDear X,\n'))
print(re.subn('(\d{1,2})/(\d{1,2})/(\d{1,2})', r'\2/\1/\3', '2/20/91'))

# split()函数
print(re.split(':', 'str1:str2:str3'))

# 扩展符号, i表示忽略大小写, m表示匹配多行
print(re.findall(r'(?i)yes', 'yes?Yes.YES!'))
print(re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.'))
print(re.findall(r'(?im)th\w+', '''
     This line is first,
     another line,
     that line, it's the best
'''))

# re.S 表示点号(.)可以用来表示\n符号
print(re.findall(r'th.+', '''
     the first line
     the second line
     the third line
'''))

print(re.findall(r'(?s)th.+', '''
     the first line
     the second line
     the third line
'''))


print(re.search(r'''(?x)     # 抑制在正则表达式中使用空白符
     \((\d{3})\)
     [ ]
     (\d{3})
     -
     (\d{4})
''', '(800) 555-1212').groups())

# (?:...)
print(re.findall(r'http://(?:\w+\.)*(\w+\.com)',
                 'http://google.com http://www.google.com http://code.google.com'))

# (?P<name>) 和(?P=name)符号，这样匹配的结果可以用name来检索，最后使用groupdict函数来组成字典形式
# 上述匹配的结果可以使用\g<name>来检索
print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict())
print(re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212'))

print(re.findall(r'\w+(?= van Rossum)',
      '''
         Guido van Rossum
         Alex Martelli
         Just van Rossum
         Raymod Hettinger
     '''))

print(re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
      '''
         sales@phptr.com    
         postmaster@phptr.com
         eng@phptr.com
         noreply@phptr.com
         admin@phptr.com
     '''))

print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))

# f = open('../../resources/doc/whodata.txt', 'r')
# for eachLine in f:
#     print(re.split(r'\s\s+|\t', eachLine.rstrip()))
# f.close()

with open('../../resources/doc/whodata.txt', 'r') as f:
    for eachLine in f:
         print(re.split(r'\s\s+|\t', eachLine.rstrip()))

# 得到执行命令结果，后续python3中改为更为强大的subprocess, 处理DOS环境下tasklist命令的输出
f = os.popen('tasklist /nh', 'r')
for eachLine in f:
    print(re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)', eachLine.rstrip()))


# 搜索匹配还有贪婪    非贪婪符？     .*?  .+?




























