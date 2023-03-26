
import pytest

@pytest.fixture(scope="module",params=["成立","甄子丹","蔡依林"])
def my_fixture(request):
    print("\n这是前置的方法")
    yield request.param
    print("\n这是后置方法")


class TestMashang1:

    def test_01_baili(self):
        print("\n测试百里")

    def test_02_xingyao(self,my_fixture):
        print("\n测试星耀")
        print("-----"+str(my_fixture))

# class TestMashang2:
#
#     def test_03_weiwei(self):
#         print("\n测试微微")
#
#     def test_04_huahua(self):
#         print("\n测试花花")


