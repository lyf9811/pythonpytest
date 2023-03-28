import os
import pytest

if __name__ == '__main__':
    pytest.main()  #想多线程执行加,'=n=2'
    os.system('allure generate ./temp -o ./report --clean')
