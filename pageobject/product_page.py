from base.base_set import BaseSet
from selenium.webdriver.common.by import By


class ProductPage(BaseSet):
    # 页面元素
    exit_loc = (By.LINK_TEXT, "退出")
    click_loc = (By.LINK_TEXT, "点击的按钮名")
    file_loc = (By.NAME, "site")
    prise_site = (By.NAME, "price")
    list_loc = (By.XPATH, "定位的site")
    location_file_site = r"E://img"

    def page_operation(self):
        # 页面动作

        self.goto_frame("框架名")
        # 进入框架
        self.page_wait(10)
        # 等待加载，防止反应过快查找不到元素
        self.quit_frame()
        # 出框架，需要清楚知道是否有跨框架的操作
        self.click(self.click_loc)
        # 点击页面中的链接
        self.post_file(ProductPage.file_loc, ProductPage.location_file_site)
        # 在页面中上传文件
        self.value_clear(ProductPage.prise_site)
        # 清除输入框内的内容
        self.send_Mykeys(ProductPage.prise_site, "777")
        # 如果输入框内已经有数据，则clear后输入数据
        self.judge_list_isnull(ProductPage.list_loc)
        # 查询一整个页面list列表，并且判断元素是否存在，再进行操作
        self.alert_approach()
        # 处理弹窗。alert(只有确定)、confirm(有确定有取消)、prompt(有确定取消还能输入)


    # 断言
    def get_except_result(self):
        self.goto_frame("框架名")
        return self.get_value(ProductPage.exit_loc)
