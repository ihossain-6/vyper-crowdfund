from ape import networks, accounts, project, config, Contract

LOCAL_CHAIN_NAMES = ["local", "development"]

def get_account(index = None, id = None):
    if index:
        return accounts[index]
    if id:
        return accounts.load[id]
    if networks.active_provider.network.name in LOCAL_CHAIN_NAMES:
        return accounts.test_accounts[0]
    if networks.active_provider.chain_id == 31337:
        return accounts.load("local-default")
    return accounts.load("default")

def main():
    pass