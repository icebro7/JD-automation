import os

import pytest


if __name__ == '__main__':

    pytest.main(['-vs','./testcase/test_case.py','--alluredir','./temp'])
    os.system('allure generate ./temp -o ./report --clean')
