import re
import openpyxl
 # 定义正则表达式来匹配SQL语句
sql_pattern = re.compile(r'\b(SELECT|UPDATE|INSERT|DELETE)\b.*?\b(;|$)', re.DOTALL)
 # 打开日志文件并读取内容
with open('logfile.log', 'r') as log_file:
    log_content = log_file.read()
 # 使用正则表达式查找所有的SQL语句
sql_list = sql_pattern.findall(log_content)
 # 创建Excel文件并添加表头
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(['SQL语句'])
 # 将每个SQL语句写入Excel文件中
for sql in sql_list:
    worksheet.append([sql[0].strip()])
 # 保存Excel文件
workbook.save('sql_queries.xlsx')
