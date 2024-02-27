import pytest


# @pytest.fixture()
# def setup():
#     print("I will execute first")
#
#
# def test_fixtureDemo(setup):
#     print("I will execute steps")"
from pytestDemo.conftest import setup


@pytest.mark.usefixture("setup")
class Testexapmle:

    def test_fixtureDemo(self):
        print("I will execute steps")

    def test_fixtureDemo1(self):
        print("I will execute steps1")

    def test_fixtureDemo2(self):
        print("I will execute steps2")