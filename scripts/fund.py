from ape import project, accounts, networks
from scripts.helper_functions import get_account
from web3 import Web3

def fund():
    account = get_account()
    deadline = 1683009675
    crowdfund = account.deploy(project.Crowdfund, account, deadline)
    value = Web3.to_wei(1,"ether")
    
    crowdfund.fund(sender = account, value = value)
    
    print("Funded......")
    
    balance = crowdfund.getAmount()
    
    print(f"The balance of the contract is {balance}")
    
def main():
    fund()