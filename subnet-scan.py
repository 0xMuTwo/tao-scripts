import bittensor as bt

subnet_number = 8


subnet = bt.metagraph(subnet_number)

print (f'subnet {subnet_number} validator dividends', subnet.D )