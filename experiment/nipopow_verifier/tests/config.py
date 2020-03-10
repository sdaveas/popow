"""
Contains information in the context of nipopow verifier
"""

import json

genesis = b"\xf3\x0cF\xbe\xc5B\xa3t9\x95.\x0f\xfe\x0ea\r\xbb\xcd\xad\x97\xee\xd9\xba\x94U\xdc\x90\x05\xcbW\xfcR"

profiler = "/home/stelios/Projects/solidity-gas-profiler/profile.js"

errors = {
    "merkle": "Merkle verification failed",
    "stack": "Stack length <= 0",
    "branch": "Branch length too big",
    "merkle_index": "Merkle index too big",
    "genesis": "Invalid genesis",
}


def extract_message_from_error(err):
    """
    Returns the error message of the exception generated by failed require
    """

    data = json.loads(str(err.value).replace("'", '"'))["data"]
    data_l = list(data.keys())
    return data[data_l[0]]["reason"]