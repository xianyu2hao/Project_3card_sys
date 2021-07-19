# 文件操作:文本文件（本质为二进制文件）和二进制文件
# 文件基本操作:打开（open（））、读取（read()）、写入（write()）、关闭（close）
# 格式：file = open("文件名",'打开方式（#'r'默认只读；'w'文件覆盖；无文件则新建；‘a'文件末尾追加，无文件新建）', encoding:'utf-8（#编码方式）')
#1.打开文件
file = open( "love.txt" , 'r',encoding = 'utf-8')
# 操作文件
text = file.read()
print(text)
print(type(text))
# 关闭文件
file.close()
