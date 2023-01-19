import os
import time

import pytest

if __name__ == '__main__':
    now = time.strftime("%Y_%m_%d_%H%M%S", time.localtime())
    path = "./Report/" + now + "/"
    pytest.main(["--alluredir=" + path])
    os.system("allure generate " + path + " -o allure-report/html/" + now)
