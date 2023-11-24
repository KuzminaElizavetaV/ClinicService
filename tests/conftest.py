import os
import pytest
from sqlalchemy_utils import create_database, drop_database
from settings import settings


os.environ['TESTING'] = 'True'

TEST_DATABASE_URL = settings.TEST_DATABASE_URL


@pytest.fixture(scope="module")
def test_db():
    create_database(TEST_DATABASE_URL)

    try:
        yield TEST_DATABASE_URL
    finally:
        drop_database(TEST_DATABASE_URL)
