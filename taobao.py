# # -*- coding:utf-8 -*-
# # ICT Python 三期一阶段
# # @Time : 2022/9/9 20:02
# # @Author : redkc02
# # @File : taobao.py
# # @Software: PyCharm
#
#
import requests
import re
#

# 获得页面
def getHTMLText(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 '}
        cookies = {
            'cna': 'TLOhG6b8TQ0CAXF2BG2DpKLg',
            't': 'a8ef4ba3b52a106a8df781bae594f41f',
            '_tb_token_': '59338eeede78d',
            'xlly_s': '1',
            '_samesite_flag_': 'true',
            'cookie2': '118d21f7df01b9e54c2a10936bbaa9a1',
            'sgcookie': 'E100%2FbdBn9M9cZnozJGRmCGDp3pXXSOcJo%2FHtK9B6IbBYQX%2FLlLGVmk%2BRJctCtxq9ejTK27X3aDOZMy%2F103KUFLA826PrkSU4l2O6wJYykAZp98%3D',
            'unb': '387945031',
            'uc3': 'lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCv4Zr51lzbgFJgG4%3D&id2=UNiDSstiV3Rd&nk2=sG6ccCBG95A%3D',
            'csg': '8674c0f9',
            'lgc': '%5Cu5B87%5Cu4E4B%5Cu8D85%5Cu8D8A',
            'cancelledSubSites': 'empty',
            'cookie17': 'UNiDSstiV3Rd',
            'dnk': '%5Cu5B87%5Cu4E4B%5Cu8D85%5Cu8D8A',
            'skt': '9999c8f894055eac',
            'existShop': 'MTY2MjY5ODkwOQ%3D%3D',
            'uc4': 'nk4=0%40spaHu6f5U5hjLQg7mSJNrC4%2Fkw%3D%3D&id4=0%40Ug%2BcgxH9UqzhtXaFuYzbMOp2lV0%3D',
            'tracknick': '%5Cu5B87%5Cu4E4B%5Cu8D85%5Cu8D8A',
            '_cc_': 'WqG3DMC9EA%3D%3D',
            '_l_g_': 'Ug%3D%3D',
            'sg': '%E8%B6%8A1d',
            '_nk_': '%5Cu5B87%5Cu4E4B%5Cu8D85%5Cu8D8A',
            'cookie1': 'UIY9ebz%2Bt3z2IETC0aR0hlPJ79aHAklh5VapI9wG7hU%3D',
            'enc': 'X4l4RZRJvPlrdv27Bk%2BtOMOdEgSRN7W4ofvf93RByrlOocJHJ89FGmsbHvbG8ciVElMDnn53x7q6z9Q2tE8Uyg%3D%3D',
            'mt': 'ci=0_1',
            'thw': 'cn',
            '_m_h5_tk': '1081c36a6fd6a8cfa120578d95ee55ec_1662736485050',
            '_m_h5_tk_enc': 'b217cd3c72578248146051d0a5966e15',
            'uc1': 'existShop=false&cookie21=VT5L2FSpczFp&cookie14=UoeyDHXim6jVDw%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&pas=0',
            'isg': 'BOnp1ciCrgOLHJK2Pgcyobqq-JVDtt3oF3cZnIveS1APUglk0gRHuLZAEPbkSnUg',
            'l': 'eBQ4IyP7TPotOG_QBOfanurza77OSIRYYuPzaNbMiOCPO0CB5XgVW6kiqQL6C3GVh6VWR3oBkVYDBeYBqQAonxvtIosM_Ckmn',
            'tfstk': 'c1UCBbgMFpvQtRsZv01NLgM7eQ3Rw3BssMMLOOJPPb8EPx10kEkb_9rkI4l-1',
        }
        r = requests.get(url, timeout=30, headers=headers, params=params)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        # print(r.text[:1000])
        return r.text
    except:
        return ""


# 关键：解析每一个获得的页面
def parsePage(ilt, html):  # 结果的页表类型
    try:
        plt = re.findall(r'"view_price":"[\d.]*"', html)  # 获得商品价格和价格前对应的标识，保
        # 存在plt列表
        tlt = re.findall(r'"raw_title":".*?"', html)  # 获取商品本身的名字
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


# 输出商品信息
def printGoodlist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
def main():
    goods ="书包"
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):  # 对每一页进行单独的访问处理
        try:
            url = start_url + '&s=' + str(44 * i)  # 对URL中最后的s变量赋值形成每一商品页的URL
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodlist(infoList)


# if __name__ == "__main__":
main()

