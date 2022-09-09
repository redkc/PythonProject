# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2022/9/9 20:34
# @Author : redkc02
# @File : 中国大学排名.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import bs4

ulist1=[]

def getHTMLText(url):#获取URL信息，输出内容
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return""

def fillUnivList(ulist,html):#将html页面放到ulist列表中(核心)
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#如果tr标签的类型不是bs4库中定义的tag类型，则过滤掉
            a = tr('a')
            tds = tr('td')#将所有的td标签存为一个列表类型
            ulist.append([tds[0].text.strip(), a[0].string.strip(), tds[4].text.strip()])#11.17更新后代码
			#原来代码ulist.append([tds[0].string.strip(),a[0].string.strip(),tds[4].string.strip()])

def printUnivList(ulist1,num):#打印出ulist列表的信息，num表示希望将列表中的多少个元素打印出来
    #格式化输出
    tplt = "{0:^10}\t{1:{3}^12}\t{2:^10}"
    # 0、1、2为槽,{3}表示若宽度不够,使用format的3号位置处的chr(12288)(中文空格)进行填充
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist1[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288)))
    print()
    print("共有记录"+str(num)+"条")

def main():
    uinfo = [] #将大学信息放到列表中
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,10)

main()