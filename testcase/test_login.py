import time

import pytest

class TestLogin:
    age=18

    # @pytest.mark.run(order=1)
    def test_09_baili(self):
        # time.sleep(2)
        print('百里')

    def test_08_xingyao(self):
        # assert 1==2
        # time.sleep(2)
        print('星耀')

    @pytest.mark.run(order=1)
    @pytest.mark.skipif(age>=18,reason="成年")
    def test_03_zhiliao(self):
        # assert 1==2
        # time.sleep(2)
        print('知了')

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @pytest.mark.skip(reason="跳")
    def test_06_weiwei(self):
        # time.sleep(2)
        print('微微')

    @pytest.mark.run(order=2)
    @pytest.mark.usermanage
    def test_05_huahua(self):
        # time.sleep(2)
        print('花花')
