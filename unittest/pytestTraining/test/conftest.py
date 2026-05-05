import pytest

@pytest.fixture(scope='function',autouse=True)
def setup_teardown():
    print('Starting.....')
    yield
    print('Ending......')
