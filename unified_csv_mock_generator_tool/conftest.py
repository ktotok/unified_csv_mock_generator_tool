import pytest

from unified_csv_mock_generator_tool.users.models import User
from unified_csv_mock_generator_tool.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()
