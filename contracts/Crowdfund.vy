# version ^0.3.3

funders: HashMap[address, uint256]
owner: address
deadline: uint256
amountRaised: uint256
amountLeft: uint256

event Funded:
    funder: indexed(address)
    value: uint256

@external
def __init__(_owner: address, _deadline: uint256):
    self.owner = _owner
    self.deadline = _deadline

@external
@payable
def fund():
    assert block.timestamp < self.deadline, "Deadline crossed"
    self.funders[msg.sender] += msg.value
    self.amountRaised += msg.value
    self.amountLeft += msg.value
    log Funded(msg.sender, msg.value)

@external 
def withdraw():
    assert msg.sender == self.owner, "You are not the owner"
    assert self.amountLeft > 0, "Not enough money to withdraw"
    self.amountLeft = 0
    send(msg.sender, self.balance)

@external 
@view 
def get_owner() -> address:
    return self.owner

@external 
@view
def get_amount() -> uint256:
    return self.amountRaised

@external
@view
def get_deadline() -> uint256:
    return self.deadline

@external
@view 
def get_funders(funder: address) -> uint256:
    return self.funders[funder]