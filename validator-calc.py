import bittensor as bt

subnet_number = 18

# Initialize the metagraph for a particular subnet
subnet = bt.metagraph(subnet_number)

# Update the metagraph to ensure it has the latest information
subnet.sync()

# Pair each UID with its stake into a list of (uid, stake) tuples
validators_with_stakes = [(uid, stake) for uid, stake in enumerate(subnet.S)]

# Sort the list of tuples by stake, in descending order (largest stake first)
sorted_validators = sorted(validators_with_stakes, key=lambda x: x[1], reverse=True)

# Prepare to write to a file
file_path = "validators_ranked_by_stake.txt"

with open(file_path, "w") as file:
    file.write(f"Current validators of subnet {subnet_number} sorted by their stakes:\n")
    rank = 1  # Initialize rank
    for uid, stake in sorted_validators:
        file.write(f"Rank: {rank}, UID: {uid}, Stake: {stake} tao\n")
        rank += 1  # Increment rank for the next validator

print(f"Output successfully written to {file_path}")