import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开浏览器

    def test_example(self):
        self.driver.get('https://item.jd.com/10055931096628.html#crumb-wrap')
        # 打开浏览器页面

        self.driver.find_element(By.NAME, "loginname").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.XPATH, "//*[@id = 'loginsubmit']").click()
        # 登陆部分

        self.driver.implicitly_wait(10)
        # 等待加载，防止反应过快查找不到元素

        self.driver.switch_to.frame("框架名")
        # 如果页面有框架，那就得先进入框架再执行操作
        self.driver.switch_to.default_content()
        # 出框架，需要清楚知道是否有跨框架的操作

        self.driver.find_element(By.LINK_TEXT, "点击的按钮名").click()
        # 点击页面中的链接

        sel = Select(self.driver.find_element(By.NAME, "下拉框名称"))
        sel.select_by_value("3")
        sel.select_by_index("3")
        # 下拉框的选中，value中的值是显示几个下拉框，index中的是下标第几个下拉框

        # Day 2

        price = self.driver.find_element(By.NAME, "要定位的元素")
        price.clear()
        price.send_keys("需要重新输入的值")
        # 当输入框内已有值，需要先删除再重新进行输入

        self.driver.find_element(By.NAME, "文件上传site").send_keys(r"E:/img.png")
        self.driver.find_element(
            By.XPATH, "//*[@id='J_seckill']/div[1]/img").click()
        # 上传文件，需要先定位到需要上传的位置，后续将本地的文件路径选中并send

        del_button_list = self.driver.find_elements(
            By.XPATH, "//*[@id='需要删除的xpath site']")
        if len(del_button_list) > 0:
            del_button_list[0].click()
        else:
            print("值为空")
        # find_elements元素用于将查找到的元素整理成一个列表，并且在后续加入if判断增强代码的健壮性

    def tearDown(self):
        self.driver.quit()
        # 关闭浏览器
