import yaml
import os
from Config.config import base_path


class PareseYaml:
    def __init__(self, file=base_path + "Config/keycaps.yaml"):
        if os.path.isfile(file):
            self.file = file
        else:
            raise FileNotFoundError('yaml文件不存在')

    @property
    def data(self):
        with open(file=self.file, mode="r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def replace_data(self, data):
        with open(file=self.file, mode="w", encoding="utf-8") as f:
            yaml.dump(data, f)

    def parse_yaml(self, key):
        """
        解析yaml文件，根据key读取value
        :param key: 多个单词使用.号分割
        :return: 值
        """
        data = self.data
        keys = key.split(".")
        for i in keys:
            data = data[i]
        return data

    def switch_yaml(self, data, keyn, valuen):
        """
        替换yaml文件,根据key替换value
        :param keyn: 需要替换value的key
        :param valuen: 需要替换的value
        :return:无返回
        """
        for key, values in data.items():
            if isinstance(values, list):
                self.get_list(values, keyn, valuen)
            elif isinstance(values, dict):
                self.switch_yaml(values, keyn, valuen)
            elif type(values) != list and key == keyn:
                data[key] = valuen
            else:
                pass
        self.replace_data(data)

    def get_list(self, values, keyn, valuen):
        result = values[0]
        if isinstance(result, list):
            self.get_list(values, keyn, valuen)
        else:
            self.switch_yaml(result, keyn, valuen)


if __name__ == '__main__':
    data = PareseYaml().data
    value = PareseYaml().switch_yaml(data, 'Admin-Auto-Token', 'a')
    print(value)
