'''
脚本说明：由于工作中有大量要收集整理的文件，即使通知同事将命名格式统一，但收集的文件命名总是乱七八糟，编号，部门等填写上有很多错误，命名格式也不统一，
此脚本用来统一文件命名格式，一键解决大量文件命名格式的问题；希望该脚本能给你提供一个思路，针对你个人问题，只需你稍稍动脑修改一下，就能解决掉你一个一个的命名文件到手酸眼花的烦恼。
使用说明：输入文件所在目录即可
'''
import os
import re
# 定义部门名称列表
departments = [
    "互联网部",
    "监控部",
    "网络部"
]


def rename_files(directory):
    # 获取目录中的所有文件
    files = os.listdir(directory)
    print(files)
    # 定义正则表达式模式
    pattern_number = re.compile(r'\((\d+)\)|（(\d+)）')
    pattern_branch = re.compile("|".join(map(re.escape, departments)))
    # 遍历所有文件
    for filename in files:
        # 检查文件是否为文件而不是目录
        if os.path.isfile(os.path.join(directory, filename)):
            # 使用正则表达式匹配文件名
            match_number = pattern_number.search(filename)
            match_branch = pattern_branch.search(filename)
            # print(match_number.group(1))
            # print(match_branch.group(0))

            if match_number:
                number = match_number.group(1)  # 获取编号信息
                branch = match_branch.group(0)  # 获取部门信息

                # 构建新的文件名
                new_filename = f"整改通知单-网站-2024({number})号-{branch}.docx"

                # 构建新的文件路径
                new_file_path = os.path.join(directory, new_filename)

                # 重命名文件
                os.rename(os.path.join(directory, filename), new_file_path)
                print(f"文件重命名成功: {filename} -> {new_filename}")
# # 指定目录
directory = "your/path"
#
# # 调用函数重命名文件
rename_files(directory)



