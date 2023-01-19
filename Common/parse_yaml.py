import yaml
from Config.config import base_path


def parse_yaml(key, filename=base_path + "Config/tms-data.yaml"):
    """
    解析yaml文件，根据key读取value
    :param key: 多个单词使用.号分割
    :param filename: 读取的文件路径
    :return: 值
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        keys = key.split(".")
        for i in keys:
            data = data[i]
        return data


if __name__ == '__main__':
    value = parse_yaml("case.login")
    print(value)
