from openpyxl import load_workbook
from Config.config import base_path


def parse_xlsx(filename, sheet_name="Sheet1"):
    """
    读取excel表格中的全部数据
    :param filename:读取的文件路径
    :param sheet_name: 读取的具体的sheet页
    :return: 元组, 具体的业务数据
    """
    excel = load_workbook(filename)
    excel_data_list = []
    for value in excel[sheet_name].values:
        if value[0] > 1:
            excel_data_list.append(value[1:])
    excel.close()
    return excel_data_list


if __name__ == '__main__':
    excel_data = parse_xlsx(base_path + "")
    print(excel_data)
