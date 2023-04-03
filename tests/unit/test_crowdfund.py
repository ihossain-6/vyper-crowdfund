from scripts.deploy_crowdfund import deploy_crowdfund
from scripts.helper_functions import get_account
from web3 import Web3
import pytest

def test_initialization():
    account = get_account
    crowdfund = deploy_crowdfund
    deadline = 1683009675
    assert crowdfund.get_owner() == account
    assert crowdfund.get_deadline() == deadline
    
def test_fund():
    account = get_account
    value = Web3.to_wei(1,"ether")
    crowdfund = deploy_crowdfund
    crowdfund.fund(sender = account, value = value)
    assert crowdfund.get_funders(account) == value
    assert crowdfund.get_amount() == value
    
def test_withdraw():
    account = get_account
    crowdfund = deploy_crowdfund
    crowdfund.withdraw(sender = account)
    assert crowdfund.get_amount() == 0