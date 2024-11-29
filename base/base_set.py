from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class BaseSet:

    def __init__(self):
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 打开浏览器
        self.driver.get('https://item.jd.com/10055931096628.html#crumb-wrap')
        # 打开浏览器页面

    # 定位元素的关键字
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    # 设置值的关键字
    def send_Mykeys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 实现属性的点击效果
    def click(self, loc):
        self.locator_element(loc).click()

    # 清除属性(文本框)中的内容
    def value_clear(self, loc, ):
        self.locator_element(loc).clear()

    # 进入框架
    def goto_frame(self, frame_name):
        self.driver.switch_to.frame(frame_name)

    # 出框架
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 下拉框
    def pull_down(self, loc, value):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)
        # sel.select_by_index("3")
        # 下拉框的选中，value中的值是显示几个下拉框，index中的是下标第几个下拉框

    # 页面等待时间
    def page_wait(self, long):
        self.driver.implicitly_wait(long)

    # 获取文本的值
    def get_value(self, loc):
        return self.locator_element(loc).text

    # 向页面提交文件
    def post_file(self, loc, file):
        self.locator_element(loc).find_element(file)

    # 查找页面元素，判断他是否为空，如果为空，则返回信息，不为空则进行相应的操作，以下代码为点击操作
    def judge_list_isnull(self,loc):
        del_button_list = self.locator_element(loc)
        if len(del_button_list) > 0:
            del_button_list[0].click()
        else:
            print("无数据")
        # find_elements是查询所有的元素转化为一个列表，通过判断语句来增强代码的健壮性

    # 弹窗处理
    def alert_approach(self):
        ale = self.driver.switch_to.alert
        ale.accept()
    # 处理弹窗。alert(只有确定)、confirm(有确定有取消)、prompt(有确定取消还能输入)
