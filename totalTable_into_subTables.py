'''
脚本说明：
此脚本将按照某一列（示例：科室）筛选出来的行写入对应的新建子表格中,即将总表按照某一列分成子表,并对子表统一命名。
让子表保存在输入表格路径的下面。
'''
import pandas as pd
import os
from datetime import datetime

def process_table(input_file):
    # 读取原始表格
    df = pd.read_excel(input_file)

    # 获取科室列表
    departments = df['科室'].unique()

    # 获取当前日期
    today = datetime.today().strftime('%m%d')

    # 获取输入文件所在目录
    input_folder = os.path.dirname(input_file)
    # 创建文件夹（如果不存在）
    output_folder = os.path.join(input_folder, today + "-新增端口")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 按科室生成新表格并保存
    for department in departments:
        department_df = df[df['科室'] == department]
        output_file = f"附件1：{today}新增端口-{department}.xlsx"
        output_path = os.path.join(output_folder, output_file)
        department_df.to_excel(output_path, index=False)

if __name__ == "__main__":
    input_file = "xxxx .xlsx"  # 替换成你的原始Excel文件路径
    process_table(input_file)
