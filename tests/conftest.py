import pytest

@pytest.fixture(scope='session')
def owner(accounts):
    return accounts[0]

@pytest.fixture(scope='session')
def funder(accounts):
    return accounts[1]

@pytest.fixture(scope='session')
def crowdfund(owner, project):
    return owner.deploy(project.crowdfund)