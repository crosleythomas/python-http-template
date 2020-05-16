import pytest

from app.app import *


class TestApp:

    def test_hello_world(self):
        resp = hello_world()
        assert(resp == "Hello, World!")
