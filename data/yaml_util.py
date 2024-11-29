import base64
import hashlib

import yaml


class YamlUtil:

    # 通过init方法把yaml文件传入到这个类
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_file(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            print(value, type(value))

    # 写入yaml文件
    def write_file(self):
        with open(self.yaml_file, encoding='utf-8', mode='w') as f:
            data = [{'text': [{'text01': 'aaa'}, {'text02': 'bbb'}]}]
            yaml.dump(data, f, allow_unicode=True)

    # md5加密
    def md5_encode(self, args):
        args = str(args).encode("utf-8")
        # 将输入的值转换为utf-8格式
        md5_value = hashlib.md5(args).hexdigest()
        # 进行hd5加密
        return md5_value

    def base64_encode(self,args):
        args = str(args).encode("utf-8")
        # 将输入的值转换为utf-8格式
        base64_value = base64.b64encode(args).decode(encoding="utf-8")
        # 进行base64加密
        return base64_value




if __name__ == '__main__':
    YamlUtil('test_api.yaml').write_file()
