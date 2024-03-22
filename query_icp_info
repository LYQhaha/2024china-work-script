'''
此脚本用来使用icp.chinaz.com获取主办单位名称和域名 2024.3.22
注意：只能在国内网络环境下使用
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd


def query_icp_info(url):
    headers = {
        "Host": "icp.chinaz.com",
      #写上你自己的请求头
    }

    response = requests.get(url, headers=headers)

    print("响应状态码:", response.status_code)
    # print("响应内容:", response.text)

    # 假设response是您已经获取的响应对象，包含页面内容
    response_text = response.text

    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(response_text, 'html.parser')

    # 查找包含主办单位名称和域名的HTML标签
    name_tag = soup.find('a', id='companyName')
    domin_tag = soup.find('a', id='host')

    # 获取主办单位名称和域名
    if name_tag:
        company_name = name_tag.text.strip()
        print("主办单位名称:", company_name)
    else:
        company_name = '未找到主办单位名称'
        print(url+company_name)


    if domin_tag:
        domain = domin_tag.text.strip()
        print("域名:", domain)
    else:
        domain = "未找到域名"
        print(url+domain)
    return company_name,domain


if __name__ == "__main__":
    # 读取表格数据
    df = pd.read_excel("your_file.xlsx",sheet_name='Sheet1')  # 将"your_file.xlsx"替换为实际的文件路径

    # 确定URL列的名称，假设为"url"
    url_column_name = "网站网址"
    company_column_name = "主办单位名称"
    domain_column_name = "域名"


    # 逐行读取URL列，并输出
    for index, row in df.iterrows():
        Website_URL = row[url_column_name]
        # print("URL:", Website_URL)
        url = "https://icp.chinaz.com/" + Website_URL
        company_name,domain=query_icp_info(url)
        # 将获取到的主办单位名称和域名写入对应的列中
        df.loc[index, company_column_name] = company_name
        df.loc[index, domain_column_name] = domain

        # 将更新后的DataFrame保存回Excel文件
    df.to_excel("your_file.xlsx", index=False)

