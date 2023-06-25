import re
import cx_Oracle
import openpyxl
#==========================================================================
 # 解析DELETE语句并获取表名和WHERE子句
def parse_delete_query(query):
    table_name = re.findall(r'DELETE\s+FROM\s+(\w+)\s+', query)[0]
    where_clause = re.findall(r'\s+WHERE\s+(.+)', query)[0]
    return table_name, where_clause
 # 使用DESCRIBE语句获取表的列名和类型
def get_table_columns(table_name, cursor):
    cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")
    return [col[0] for col in cursor.description]
 # 根据表名和WHERE子句生成SELECT语句的SELECT子句和WHERE子句
def generate_select_query(table_name, where_clause, table_columns):
    where_clause = re.sub(r'(\w+)\s*=', r'\1 IN', where_clause)
    select_clause = ', '.join(table_columns)
    return f"SELECT {select_clause} FROM {table_name} WHERE {where_clause}"


#============================================================================
# 解析INSERT语句并获取表名和插入的列名和值
def parse_insert_query(query):
    table_name = re.findall(r'INSERT\s+INTO\s+(\w+)\s+', query)[0]
    columns = re.findall(r'\((.+)\)', query)[0].split(',')
    values = re.findall(r'VALUES\s*\((.+)\)', query)[0].split(',')
    return table_name, columns, values

# 根据表名和插入的列名和值生成SELECT语句的WHERE子句
def generate_where_clause(columns, values):
    where_clause = []
    for i in range(len(columns)):
        where_clause.append(f"{columns[i].strip()} = {values[i].strip()}")
    return ' AND '.join(where_clause)

# 根据表名和WHERE子句生成SELECT语句的SELECT子句和WHERE子句
def generate_select_query(table_name, where_clause):
    return f"SELECT * FROM {table_name} WHERE {where_clause}"
#======================================================================================
# 解析UPDATE语句并获取表名、SET子句和WHERE子句
def parse_update_query(query):
    table_name = re.findall(r'UPDATE\s+(\w+)\s+', query)[0]
    set_clause = re.findall(r'\s+SET\s+(.+)\s+WHERE', query)[0]
    where_clause = re.findall(r'\s+WHERE\s+(.+)', query)[0]
    return table_name, set_clause, where_clause

# 根据SET子句生成列名和新值的字典
def generate_set_dict(set_clause):
    set_dict = {}
    set_list = set_clause.split(',')
    for item in set_list:
        col, val = item.split('=')
        set_dict[col.strip()] = val.strip()
    return set_dict

# 根据WHERE子句生成SELECT语句的WHERE子句
def generate_where_clause(where_clause):
    where_clause = re.sub(r'(\w+)\s*=', r'\1 IN', where_clause)
    return where_clause

# 根据表名、SET子句和WHERE子句生成SELECT语句的SELECT子句和WHERE子句
def generate_select_query(table_name, set_dict, where_clause):
    select_clause = ', '.join(set_dict.keys())
    where_clause = generate_where_clause(where_clause)
    return f"SELECT {select_clause} FROM {table_name} WHERE {where_clause}"
#==================================================================================
###########################################################################################
 # 解析INSERT语句并获取表名和插入的列名和值
def parse_insert_query(query):
    table_name = re.findall(r'INSERT\s+INTO\s+(\w+)\s+', query)[0]
    columns_clause, values_clause = re.findall(r'\((.+)\)\s+VALUES\s+\((.+)\)', query)[0]
    columns = [col.strip() for col in columns_clause.split(',')]
    values = [val.strip() for val in values_clause.split(',')]
    return table_name, columns, values
 # 使用DESCRIBE语句获取表的列名和类型
def get_table_columns(table_name, cursor):
    cursor.execute(f"DESCRIBE {table_name}")
    return [col[0] for col in cursor.fetchall()]
 # 根据表名和列名生成SELECT语句的SELECT子句和WHERE子句
def generate_select_query(table_name, columns, values, table_columns):
    where_clause = ' AND '.join([f"{col} = {format_col_val(val, table_columns[col])}" for col, val in zip(columns, values)])
    select_clause = ', '.join(table_columns)
    return f"SELECT {select_clause} FROM {table_name} WHERE {where_clause}"
 # 将INSERT语句中的值转换为相应的类型，并将其添加到WHERE子句中
def format_col_val(col_val, col_type):
    if col_type.startswith('int'):
        return int(col_val)
    elif col_type.startswith('float'):
        return float(col_val)
    else:
        return f"'{col_val}'"
 # 将SELECT语句的SELECT子句和WHERE子句组合在一起，生成最终的SELECT语句
def generate_select_query_from_insert_query(query, cursor):
    table_name, columns, values = parse_insert_query(query)
    table_columns = get_table_columns(table_name, cursor)
    formatted_values = [format_col_val(val, table_columns[col]) for col, val in zip(columns, values)]
    select_query = generate_select_query(table_name, columns, formatted_values, table_columns)
    return select_query


# 解析UPDATE语句并获取表名和更新的列名和值
def parse_update_query(query):
    table_name = re.findall(r'UPDATE\s+(\w+)\s+SET', query)[0]
    set_clause = re.findall(r'SET\s+(.+)\s+WHERE', query)[0]
    col_name, col_val = set_clause.split('=')
    col_name = col_name.strip()
    col_val = col_val.strip()
    return table_name, col_name, col_val

# 使用DESCRIBE语句获取表的列名和类型
def get_table_columns(table_name, cursor):
    cursor.execute(f"DESCRIBE {table_name}")
    return [col[0] for col in cursor.fetchall()]

# 根据表名和列名生成SELECT语句的SELECT子句和WHERE子句
def generate_select_query(table_name, col_name, col_val, columns):
    where_clause = f"{col_name} = {col_val}"
    select_clause = ', '.join(columns)
    return f"SELECT {select_clause} FROM {table_name} WHERE {where_clause}"

# 将UPDATE语句中的值转换为相应的类型，并将其添加到WHERE子句中
def format_col_val(col_val, col_type):
    if col_type.startswith('int'):
        return int(col_val)
    elif col_type.startswith('float'):
        return float(col_val)
    else:
        return f"'{col_val}'"

# 将SELECT语句的SELECT子句和WHERE子句组合在一起，生成最终的SELECT语句
def generate_select_query_from_update_query(query, cursor):
    table_name, col_name, col_val = parse_update_query(query)
    columns = get_table_columns(table_name, cursor)
    col_type = [col[1] for col in cursor.description if col[0] == col_name][0]
    formatted_col_val = format_col_val(col_val, col_type)
    select_query = generate_select_query(table_name, col_name, formatted_col_val, columns)
    return select_query
##########################################################################################################

 # 将查询结果写入Excel文件
def write_to_excel(result, file_name):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.append([col[0] for col in result.description])
    for row in result.fetchall():
        worksheet.append(row)
    workbook.save(file_name)
 # 连接Oracle数据库
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLCDB')
connection = cx_Oracle.connect(user='yourusername', password='yourpassword', dsn=dsn_tns)
 # 创建游标对象
cursor = connection.cursor()
 # 执行DELETE语句
delete_query = "DELETE FROM customers WHERE age > 30"
cursor.execute(delete_query)
 # 提交更改
connection.commit()
 # 根据DELETE语句生成对应的SELECT语句
table_name, where_clause = parse_delete_query(delete_query)
table_columns = get_table_columns(table_name, cursor)
select_query = generate_select_query(table_name, where_clause, table_columns)

# 根据INSERT语句生成对应的SELECT语句
table_name, columns, values = parse_insert_query(insert_query)
where_clause = generate_where_clause(columns, values)
select_query = generate_select_query(table_name, where_clause)

# 根据UPDATE语句生成对应的SELECT语句
table_name, set_clause, where_clause = parse_update_query(update_query)
set_dict = generate_set_dict(set_clause)
select_query = generate_select_query(table_name, set_dict, where_clause)

 # 执行SELECT语句并将结果写入Excel文件
cursor.execute(select_query)
result = cursor
write_to_excel(result, 'customers.xlsx')
 # 关闭游标和连接
cursor.close()
connection.close()
