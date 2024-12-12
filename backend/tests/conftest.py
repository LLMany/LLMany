import pytest
import os
import tempfile


@pytest.fixture
def temp_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_name = temp_file.name
    yield temp_file_name
    # Cleanup after test
    if os.path.exists(temp_file_name):
        os.remove(temp_file_name)
