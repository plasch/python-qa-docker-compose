import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://localhost:8080",
        help="Test server url"
    )


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption("--url")
