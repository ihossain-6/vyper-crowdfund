from web3 import Web3

def test_initialization(crowdfund, owner):
    deadline = 1683009675
    assert crowdfund.get_owner() == owner
    assert crowdfund.get_deadline() == deadline
    
def test_fund(crowdfund, funder):
    value = Web3.to_wei(1,"ether")
    crowdfund.fund(sender = funder, value = value)
    assert crowdfund.get_funders(funder) == value
    assert crowdfund.get_amount() == value
    
def test_withdraw(crowdfund, owner):    
    crowdfund.withdraw(sender = owner)
    assert crowdfund.get_amount() == 0