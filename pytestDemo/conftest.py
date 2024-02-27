import pytest

#it will execute after and before every test case
@pytest.fixture()
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


# @pytest.fixture(scope="class")
# def setup():
#     print("I will execute first")
#     yield
#     print("I will execute last")
# #it will execute after and before every class
