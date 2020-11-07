#!/usr/bin/env python
# coding=utf-8
#!/usr/bin/env python
# coding=utf-8
import time

import pytest
from selenium import webdriver
import shelve

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLogin():
    def setup_method(self):
        # 复用当前浏览器不用新打开浏览器
        # 复用浏览器需要的前置步骤
        # 首先在windows上运行
        # C:/Users/huangpushuai/AppData/Local/Google/Chrome/Application/chrome --remote-debugging-port=9222
        # options=Options()
        # options.debugger_address='172.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=options)
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # def teardown_method(self):
    #     self.driver.quit()

    # @pytest.mark.skip()
    def test(self):
        self.driver.get('https://www.baidu.com/')

    # def test_cookies(self):
    #     # 服用浏览的cookies
    #     # cookies = self.driver.get_cookies()
    #     # print(cookies)
    #     # 测试的时候开发会提供特定的cookie使用
    #     cookies = [
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
    #          'value': '1688853424029239'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
    #          'value': 'TId_F7NO6zhxX93E1J0ajQ-SSg3uLPUgXe037mL21N4NnUoXqO90j-BQSVjbwwK8DnRic6p4KGHmDfzTigK7Ii6qp9hrESH38gfI9vhS_BaPktmcpbEic6lq00o57NxKFnnp4IMLXgpDMjo8ZXQL2YINMDZibGB9jQa3kpL0t-QZwAFk00rJuHBz_0zm9pNNcRE60lP2Id6vqdtb-P-AbmQ-h5Dpq4oHadY99LpSu-mcqsL5JtLDoCEebhOTIcyDlzRb4k7fsb9Mx1Vq3oPINg'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
    #          'value': '1688853424029239'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
    #          'value': '1970324977166075'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
    #          'value': 'r_0VfcCQYMYYrIM_ghZ9t2XHebm3znd0elVBafqL9J2nr98JEdVclvAM92GigVfm'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
    #          'value': 'a91079'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
    #          'value': '02790140'},
    #         {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'pt2gguin', 'path': '/',
    #          'secure': False, 'value': 'o1247432306'},
    #         {'domain': '.qq.com', 'expiry': 1666666572, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
    #          'value': 'GA1.2.1781432893.1603590554'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1635126551, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
    #          'path': '/', 'secure': False, 'value': '0'},
    #         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
    #          'secure': False, 'value': '1247432306'},
    #         {'domain': '.qq.com', 'expiry': 2147483396, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
    #          'value': 'db45e53e4fdec7b96a850ad52146f32121701812e2cb256196cb7ef9f46db187'},
    #         {'domain': '.work.weixin.qq.com', 'expiry': 1606186579, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
    #          'path': '/', 'secure': False, 'value': 'zh'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
    #          'value': '1'},
    #         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
    #          'value': 'direct'},
    #         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
    #          'secure': False, 'value': '385460890'},
    #         {'domain': '.qq.com', 'expiry': 1603680972, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
    #          'value': 'GA1.2.1765918150.1603590554'},
    #         {'domain': 'work.weixin.qq.com', 'expiry': 1603622087, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
    #          'secure': False, 'value': '3vu3i0a'},
    #         {'domain': '.qq.com', 'expiry': 1603594631, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
    #          'value': '1'},
    #         {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
    #          'secure': False, 'value': '5982712832'},
    #         {'domain': '.qq.com', 'expiry': 1833024034, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
    #          'secure': False, 'value': '8daff526b6ade97f'},
    #         {'domain': '.qq.com', 'expiry': 2147483482, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
    #          'value': '9i820LsPNa'}]
    #
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #     #     刷新当前页面
    #     self.driver.refresh()


    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        # 打开coolie数据库
        db = shelve.open('cookies')
        # 保存cookie
        # 保存cookie后关闭
        # db['cookies']=cookies
        # db.close()
        cookies=db['cookies']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            # add_cookies支持的是字典
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_item_title:nil-child(3)").click()
        # time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,".ww_fileImporter_fileContainer_uploadInputMask").send_keys('/c/Users/huangpushuai/Desktop/text.xlsx')
        file=self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_uploadInputMask').text()
        assert 'text.xlsx' == file