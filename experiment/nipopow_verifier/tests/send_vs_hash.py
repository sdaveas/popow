"""
Outputs the gas of calling a function with array[N] and a function that hashes N times
"""

import sys

sys.path.append("../tools/interface/")
import contract_interface

sys.path.append("../tests")
from config import profiler

contract_path = "./contracts/send_vs_hash.sol"
backend = "geth"
constructor_arguments = []


def call(function_name, function_args=[]):
    """
    Deploys the contract with contructor_arguments and runs a function with function_args
    """

    interface = contract_interface.ContractInterface(
        contract_path, backend=backend, constructor_arguments=constructor_arguments
    )
    my_contract = interface.get_contract()
    from_address = interface.w3.eth.accounts[0]
    function = my_contract.get_function_by_name(function_name)(*function_args)
    res = function.call({"from": from_address})
    tx_hash = function.transact({"from": from_address})
    receipt = interface.w3.eth.waitForTransactionReceipt(tx_hash)
    interface.run_gas_profiler(profiler, tx_hash, function_name + "_" + str(N))
    interface.end()
    return {"result": res, "gas": receipt["gasUsed"]}


N = 1
if len(sys.argv) >= 2:
    N = int(sys.argv[1])

array = [b"\xff"] * N

print("[Send]", call("send_and_hash_array", function_args=[array])["gas"])
print("[Hash]", call("hash_times", function_args=[N])["gas"])
