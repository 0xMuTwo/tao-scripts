Simple Scripts to see how much money the top validators on Tao are making, and which are profitable to mine

Rank Subnets

```bash
btcli subnets list | awk 'NR>2 {print $0}' | sort -nrk 4 | tee -a ranked-subnets.txt && echo -e "\nUpdated on: $(date)" >> ranked-subnets.txt
```

btcli w balance --subtensor.network test
