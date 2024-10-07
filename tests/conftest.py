import pytest

from pymafia import start_kolmafia


@pytest.fixture(scope="session", autouse=True)
def start_kolmafia_fixture():
    start_kolmafia()
    yield
