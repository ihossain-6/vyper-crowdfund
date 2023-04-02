from ape import project, accounts, chain, config, networks
from scripts.helper_functions import get_account

def deploy_crowdfund():
    account = get_account()
    deadline = 1683009675
    crowdfund = account.deploy(project.Crowdfund, account, deadline)
    print(f"Crowdfund deployed to {crowdfund.address}")
    return crowdfund

def main():
    deploy_crowdfund()