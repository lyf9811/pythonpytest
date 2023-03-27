import pytest

@pytest.fixture(scope="function")
def user_fixture():
    print("\n用户管理前置")
    yield
    print("\n用户管理后置")