import pytest


class TestClass:

    def test_validate_user(self):
        # arrange
        user = "test"
        password = "test"

        # act

        # assert
        assert(user and password != None)

    if __name__ == '__main__':
        TestClass.test_validate_user()
