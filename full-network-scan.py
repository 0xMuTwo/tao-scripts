import torch
import bittensor
import sys  # Import sys to access command-line arguments

# Check if an argument was provided (the first argument is always the script name, so we need at least 2)
if len(sys.argv) < 2:
    print("Usage: python3 network-scan.py <subnet_number>")
    sys.exit(1)  # Exit the script if no subnet number is provided

# Convert the argument to an integer
subnet_number = int(sys.argv[1])

metagraph = bittensor.metagraph(netuid=subnet_number, sync=True)

# Helper function to print the stats
def print_tensor_stats(tensor, name):
    print(f"--- {name} ---")
    print(f"Tensor: {tensor}")  # Displaying tensor directly might be verbose for large tensors
    max_val = torch.max(tensor)
    min_val = torch.min(tensor)
    avg_val = torch.mean(tensor)
    # Filter out zero values for a 'non-zero average'
    non_zero_vals = tensor[tensor.nonzero(as_tuple=True)]
    non_zero_avg = torch.mean(non_zero_vals) if non_zero_vals.nelement() > 0 else torch.tensor(0.0)
    print(f"Maximum {name}: {max_val.item()}")
    print(f"Minimum {name}: {min_val.item()}")
    print(f"Average {name}: {avg_val.item()}")
    print(f"Non-Zero Average {name}: {non_zero_avg.item()}\n")

# Access attributes from the metagraph
stakes = metagraph.S
dividends = metagraph.D
incentives = metagraph.I
emissions = metagraph.E

# Print statistics for each of these attributes
print_tensor_stats(stakes, "Stake")
print_tensor_stats(dividends, "Dividends (FOR VALIDATORS)")
print_tensor_stats(incentives, "Incentives (FOR MINERS)")
print_tensor_stats(emissions, "Emission")