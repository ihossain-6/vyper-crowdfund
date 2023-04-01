# version ^0.3.3

funders: HashMap[address, uint256]
owner: address
deadline: uint256
amountRaised: uint256

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

@external 
def withdraw():
    assert msg.sender == self.owner, "You are not the owner"
    assert self.amountRaised > 0, "Not enough money to withdraw"
    send(msg.sender, self.balance)

@external 
@view 
def getOwner() -> address:
    return self.owner

@external 
@view
def getAmount() -> uint256:
    return self.amountRaised

@external
@view
def getDeadline() -> uint256:
    return self.deadline