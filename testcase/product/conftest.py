import pytest

@pytest.fixture(scope="function")
def product_fixture():
    print("\n商品管理前置")
    yield
    print("\n商品管理后置")