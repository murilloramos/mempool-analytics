import requests # This library allow us to talk to websites and make HTTPS requests, we need this to talk with Bitcoin because Bitcoin data lives on the network
import time # This library gives us access to time-related functions, basically it is used for timers
MEMPOOL_URL = "https://mempool.space/api/mempool" # API call stored on constant, this URL endpoint will return how many transactions are waiting and how full the mempool is, basically a waiting room for transactions
FEES_URL = "https://mempool.space/api/v1/fees/recommended" # API call stored on a constant, this URL endpol will return recommend fees in sat/vByte based on current network congestion

def fetch_mempool():
    return requests.get(MEMPOOL_URL).json() # HTTP GET request converting into a Python dictionary with .json()

def fetch_fees():
    return requests.get(FEES_URL).json() # HTTP GET request converting into a Python dictionary with .json()

while True: # This while True is telling the program to monitor Bitcoin forever
    mempool = fetch_mempool() # Here we are calling the function previously defined and storing the results in variables
    fees = fetch_fees() # Same thing as line 13

    print("\n MEMPOOL STATUS HERE!")
    print(f"Transactions: {mempool['count']}") # Here we are accessing the dictionary key "count"
    print(f"Size (in vBytes): {mempool['vsize']}") # Here we are accessing the dictionary key "vsize"

    print("\n RECOMMENDED FEES (in sat/vB)")
    for k, v in fees.items(): # Here we will loop through each fee tier
        print(f"{k}: {v}")

    time.sleep(30) # Here we will pause the execution for 30 seconds then the loop will start again
    