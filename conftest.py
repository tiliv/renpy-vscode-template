import logging

import pytest

log = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def setup():
    """Perform setup and teardown."""
    log.info("Performing setup...")

    log.info("Starting tests...")
    yield

    log.info("Performing teardown...")
