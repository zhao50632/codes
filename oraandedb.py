# 导入必要的库
import cx_Oracle
import csv
import psycopg2
from tkinter import *
from tkinter import filedialog

# 创建GUI界面
root = Tk()
root.title("Oracle & PostgreSQL查询工具")

# 创建Oracle SQL语句输入框
sql_input = Entry(root, width=50, borderwidth=5)
sql_input.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 创建Oracle连接信息输入框
oracle_label = Label(root, text="Oracle Connection:")
oracle_label.grid(row=0, column=0, padx=10, pady=10)

username_label = Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_input = Entry(root, width=20, borderwidth=5)
username_input.grid(row=1, column=1, padx=10, pady=10)

password_label = Label(root, text="Password:")
password_label.grid(row=1, column=2, padx=10, pady=10)
password_input = Entry(root, width=20, borderwidth=5, show="*")
password_input.grid(row=1, column=3, padx=10, pady=10)

service_label = Label(root, text="Service Name:")
service_label.grid(row=1, column=4, padx=10, pady=10)
service_input = Entry(root, width=20, borderwidth=5)
service_input.grid(row=1, column=5, padx=10, pady=10)

# 创建PostgreSQL SQL语句输入框
pg_sql_input = Entry(root, width=50, borderwidth=5)
pg_sql_input.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# 创建PostgreSQL连接信息输入框
pg_label = Label(root, text="PostgreSQL Connection:")
pg_label.grid(row=3, column=0, padx=10, pady=10)

pg_username_label = Label(root, text="Username:")
pg_username_label.grid(row=4, column=0, padx=10, pady=10)
pg_username_input = Entry(root, width=20, borderwidth=5)
pg_username_input.grid(row=4, column=1, padx=10, pady=10)

pg_password_label = Label(root, text="Password:")
pg_password_label.grid(row=4, column=2, padx=10, pady=10)
pg_password_input = Entry(root, width=20, borderwidth=5, show="*")
pg_password_input.grid(row=4, column=3, padx=10, pady=10)

pg_database_label = Label(root, text="Database Name:")
pg_database_label.grid(row=4, column=4, padx=10, pady=10)
pg_database_input = Entry(root, width=20, borderwidth=5)
pg_database_input.grid(row=4, column=5, padx=10, pady=10)

# 创建执行按钮
def execute_sql():
  # 获取SQL语句
    sql = sql_input.get()
    pg_sql = pg_sql_input.get()

    # 获取Oracle连接信息
    oracle_username = username_input.get()
    oracle_password = password_input.get()
    oracle_service = service_input.get()

    # 获取PostgreSQL连接信息
    pg_username = pg_username_input.get()
    pg_password = pg_password_input.get()
    pg_database = pg_database_input.get()

     # 验证Oracle连接信息
    if not all([oracle_username, oracle_password, oracle_service]):
        messagebox.showerror("Oracle Error", "Please enter all Oracle connection information.")
        return
      
     try:
        # 连接Oracle数据库
        oracle_conn = cx_Oracle.connect(f'{oracle_username}/{oracle_password}@{oracle_service}')
        oracle_cursor = oracle_conn.cursor()

        # 执行Oracle SQL语句
        oracle_cursor.execute(sql)

        # 获取Oracle查询结果
        oracle_results = oracle_cursor.fetchall()

        # 导出Oracle查询结果到CSV文件
        oracle_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        if oracle_file_path:
            if os.path.exists(oracle_file_path):
                confirm = messagebox.askyesno("File Exists", "File already exists. Do you want to overwrite it?")
                if not confirm:
                    return
            with open(oracle_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(oracle_results)

        # 关闭Oracle数据库连接
        oracle_cursor.close()
        oracle_conn.close()

    except cx_Oracle.Error as error:
        messagebox.showerror("Oracle Error", error)
    
    # 验证PostgreSQL连接信息
    if not all([pg_username, pg_password, pg_database]):
        messagebox.showerror("PostgreSQL Error", "Please enter all PostgreSQL connection information.")
        return
      
      
      ####################################################
    # 获取Oracle SQL语句
    oracle_sql = sql_input.get()

    # 获取PostgreSQL SQL语句
    pg_sql = pg_sql_input.get()

    # 连接Oracle数据库
    oracle_conn = cx_Oracle.connect(username_input.get() + '/' + password_input.get() + '@' + service_input.get())

    # 执行Oracle SQL语句
    oracle_cursor = oracle_conn.cursor()
    oracle_cursor.execute(oracle_sql)

    # 获取Oracle查询结果
    oracle_results = oracle_cursor.fetchall()

    # 导出Oracle查询结果到CSV文件
    oracle_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    with open(oracle_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(oracle_results)

    # 关闭Oracle数据库连接
    oracle_cursor.close()
    oracle_conn.close()

    # 连接PostgreSQL数据库
    pg_conn = psycopg2.connect(user=pg_username_input.get(),
                               password=pg_password_input.get(),
                               host="localhost",
                               port="5432",
                               database=pg_database_input.get())

    # 执行PostgreSQL SQL语句
    pg_cursor = pg_conn.cursor()
    pg_cursor.execute(pg_sql)

    # 获取PostgreSQL查询结果
    pg_results = pg_cursor.fetchall()

    # 导出PostgreSQL查询结果到CSV文件
    pg_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    with open(pg_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(pg_results)

    # 关闭PostgreSQL数据库连接
    pg_cursor.close()
    pg_conn.close()

execute_button = Button(root, text="执行", command=execute_sql)
execute_button.grid(row=6, column=0, padx=10, pady=10)

# 创建退出按钮
exit_button = Button(root, text="退出", command=root.quit)
exit_button.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()



###########################################################
# 导入必要的库
import cx_Oracle
import csv
import psycopg2
from tkinter import *
from tkinter import filedialog

# 创建GUI界面
root = Tk()
root.title("Oracle & PostgreSQL查询工具")

# 创建标题
title_label = Label(root, text="Oracle & PostgreSQL查询工具", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# 创建Oracle SQL语句输入框
sql_input = Entry(root, width=70, borderwidth=5)
sql_input.grid(row=2, column=0, columnspan=6, padx=10, pady=10, sticky="w")

# 创建Oracle连接信息输入框
oracle_label = Label(root, text="Oracle Connection:", padx=10, pady=10)
oracle_label.grid(row=1, column=0, sticky="e")

username_label = Label(root, text="Username:", padx=10, pady=10)
username_label.grid(row=1, column=1, sticky="e")
username_input = Entry(root, width=20, borderwidth=5)
username_input.grid(row=1, column=2, sticky="w")

password_label = Label(root, text="Password:", padx=10, pady=10)
password_label.grid(row=1, column=3, sticky="e")
password_input = Entry(root, width=20, borderwidth=5, show="*")
password_input.grid(row=1, column=4, sticky="w")

service_label = Label(root, text="Service Name:", padx=10, pady=10)
service_label.grid(row=1, column=5, sticky="e")
service_input = Entry(root, width=20, borderwidth=5)
service_input.grid(row=1, column=6, sticky="w")

# 创建PostgreSQL SQL语句输入框
pg_sql_input = Entry(root, width=70, borderwidth=5)
pg_sql_input.grid(row=5, column=0, columnspan=6, padx=10, pady=10, sticky="w")

# 创建PostgreSQL连接信息输入框
pg_label = Label(root, text="PostgreSQL Connection:", padx=10, pady=10)
pg_label.grid(row=3, column=0, sticky="e")

pg_username_label = Label(root, text="Username:", padx=10, pady=10)
pg_username_label.grid(row=4, column=1, sticky="e")
pg_username_input = Entry(root, width=20, borderwidth=5)
pg_username_input.grid(row=4, column=2, sticky="w")

pg_password_label = Label(root, text="Password:", padx=10, pady=10)
pg_password_label.grid(row=4, column=3, sticky="e")
pg_password_input = Entry(root, width=20, borderwidth=5, show="*")
pg_password_input.grid(row=4, column=4, sticky="w")

pg_database_label = Label(root, text="Database Name:", padx=10, pady=10)
pg_database_label.grid(row=4, column=5, sticky="e")
pg_database_input = Entry(root, width=20, borderwidth=5)
pg_database_input.grid(row=4, column=6, sticky="w")

# 创建执行按钮
execute_button = Button(root, text="执行", command=execute_sql)
execute_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

# 创建退出按钮
exit_button = Button(root, text="退出", command=root.quit)
exit_button.grid(row=6, column=6, padx=10, pady=10, sticky="e")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)

root.mainloop()

def execute_sql():
    # 获取SQL语句
    sql = sql_input.get()
    pg_sql = pg_sql_input.get()

    # 获取Oracle连接信息
    oracle_username = username_input.get()
    oracle_password = password_input.get()
    oracle_service = service_input.get()

    # 获取PostgreSQL连接信息
    pg_username = pg_username_input.get()
    pg_password = pg_password_input.get()
    pg_database = pg_database_input.get()

    # 验证Oracle连接信息
    if not all([oracle_username, oracle_password, oracle_service]):
        messagebox.showerror("Oracle Error", "Please enter all Oracle connection information.")
        return

    try:
        # 连接Oracle数据库
        oracle_conn = cx_Oracle.connect(f'{oracle_username}/{oracle_password}@{oracle_service}')
        oracle_cursor = oracle_conn.cursor()

        # 执行Oracle SQL语句
        oracle_cursor.execute(sql)

        # 获取Oracle查询结果
        oracle_results = oracle_cursor.fetchall()

        # 导出Oracle查询结果到CSV文件
        oracle_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        if oracle_file_path:
            if os.path.exists(oracle_file_path):
                confirm = messagebox.askyesno("File Exists", "File already exists. Do you want to overwrite it?")
                if not confirm:
                    return
            with open(oracle_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(oracle_results)

        # 关闭Oracle数据库连接
        oracle_cursor.close()
        oracle_conn.close()

    except cx_Oracle.Error as error:
        messagebox.showerror("Oracle Error", error)

    # 验证PostgreSQL连接信息
    if not all([pg_username, pg_password, pg_database]):
        messagebox.showerror("PostgreSQL Error", "Please enter all PostgreSQL connection information.")
        return

    try:
        # 连接PostgreSQL数据库
        pg_conn = psycopg2.connect(user=pg_username, password=pg_password, host="localhost", port="5432", database=pg_database)
        pg_cursor = pg_conn.cursor()

        # 执行PostgreSQL SQL语句
        pg_cursor.execute(pg_sql)

        # 获取PostgreSQL查询结果
        pg_results = pg_cursor.fetchall()

        # 导出PostgreSQL查询结果到CSV文件
        pg_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        if pg_file_path:
            if os.path.exists(pg_file_path):
                confirm = messagebox.askyesno("File Exists",
