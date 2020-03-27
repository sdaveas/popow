pragma solidity ^0.6.2;
pragma experimental ABIEncoderV2;


/*

# Gas usage of each function for different `N`s

| N | send array[N] | hash N |
|--:|--------------:|-------:|
| 10|        31,420 |  40,255|
|100|        98,110 | 206,124|
|200|       172,545 | 390,757|
|300|       247,343 | 575,754|
|400|       322,480 | 761,090|
|500|       397,969 | 946,778|

Note: A chain with 500K blocks creates proof with ~200 blocks
*/

contract send_vs_hash {
    function send_and_hash_array(bytes32[] memory array)
        public
        pure
        returns (bytes32)
    {
        return sha256(abi.encodePacked(array));
    }

    function hash_times(uint256 times) public pure returns (bytes32) {
        bytes32 res = bytes32(0);
        for (uint256 i = 0; i < times; i++) {
            res = sha256(abi.encodePacked(res));
        }
        return res;
    }
}
