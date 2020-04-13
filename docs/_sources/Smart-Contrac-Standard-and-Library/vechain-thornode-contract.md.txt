# VeChainThor Node token contract
Contracts for VeChainThor Node Token on the VeChainThor blockchain.
[block:api-header]
{
  "title": "Project Construct"
}
[/block]
The project includes the following files:
[block:code]
{
  "codes": [
    {
      "code": "   ├── SupportsInterface.sol\n    ├── ThunderFactory.sol\n    ├── TokenAuction.sol\n    ├── XAccessControl.sol\n    ├── XOwnership.sol\n    ├── auction\n    │       ├── ClockAuction.sol\n    │       └── ClockAuctionBase.sol\n    └── utility\n            ├── Ownable.sol\n            ├── Pausable.sol\n            ├── SafeMath.sol\n            ├── Strings.sol\n            └── interfaces\n                    ├── IERC165.sol\n                    ├── IVIP181.sol\n                    └── IVIP181Basic.sol",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Contracts Overview"
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eed8e62-ContracOverview.png",
        "ContracOverview.png",
        627,
        374,
        "#dfebf8"
      ]
    }
  ]
}
[/block]
The smart contracts are split into modules.

* [`XAccessControl`](https://github.com/vechain/ThorNode-contracts/blob/master/contracts/XAccessControl.sol) - Defines the organizational permission and black lists.
* [`ThunderFactory`](https://github.com/vechain/ThorNode-contracts/blob/master/contracts/ThunderFactory.sol) - Defines the `Token` struct and storage, it's the core contract
* [`XOwnership`](https://github.com/vechain/ThorNode-contracts/blob/master/contracts/XOwnership.sol) - Implements VIP181 and defines ownership and transfer rights
* [`TokenAuction`](https://github.com/vechain/ThorNode-contracts/blob/master/contracts/TokenAuction.sol) - Calls auction contract and Implements token auction
* [`ClockAuction`](https://github.com/vechain/ThorNode-contracts/blob/master/contracts/auction/ClockAuction.sol) - Implements token auction logic
* [`ClockAuctionBase`](https://github.com/vechain/ThorNode-contracts/blob/master/contracts/auction/ClockAuction.sol) - Defines internal variables, functions for token auction
[block:api-header]
{
  "title": "TokenAuction.sol"
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a4801f4-TokenAuction.png",
        "TokenAuction.png",
        960,
        1199,
        "#eeeff4"
      ]
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "ClockAuction.sol"
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b363b5e-ClockAuction.png",
        "ClockAuction.png",
        1069,
        659,
        "#eef0f5"
      ]
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Contract Address"
}
[/block]
+ TokenAuction: `0xb81E9C5f9644Dec9e5e3Cac86b4461A222072302`
+ ClockAuction: `0xE28cE32d637eb93cBDa105f87FBB829E9ef8540B`
[block:api-header]
{
  "title": "API"
}
[/block]
## getMetadata
[block:code]
{
  "codes": [
    {
      "code": " function getMetadata(uint256 _tokenId) public view \n                returns(\n                        address owner,\n                        uint8 level,\n                        bool isOnUpgrade,\n                        bool isOnAuction,\n                        uint64 lastTransferTime,\n                        uint64 createdAt,\n                        uint64 updatedAt\n                )\n",
      "language": "text"
    }
  ]
}
[/block]
Get the information about the given token.

Params:

+ _tokenId: token id

Return:

+ owner: the address that owns token
+ level: the level of the token
+ isOnUpgrade: return true when the token is upgrading
+ isOnAuction: return true when the token is on auction
+ lastTransferTime: the timestamp that the token 
+ createdAt: when the token is genearted
+ updatedAt: when the token data is updated


## applyUpgrade
[block:code]
{
  "codes": [
    {
      "code": "   function applyUpgrade(strengthLevel _toLvl)",
      "language": "text"
    }
  ]
}
[/block]
Apply for upgrading your node token.

Params:

+ _toLvl: the next level index. Notice that a normal node token cannot upgrade to X node token.
[block:parameters]
{
  "data": {
    "h-0": "Level Index",
    "h-1": "Level Name",
    "0-0": "1",
    "1-0": "2",
    "2-0": "3",
    "3-0": "4",
    "4-0": "5",
    "5-0": "6",
    "6-0": "7",
    "0-1": "VeChainThor Strength Node",
    "1-1": "VeChainThor Thunder Node",
    "2-1": "VeChainThor Mjolnir Node",
    "3-1": "VeChainThor X Node",
    "4-1": "VeChainThor Strength X Node",
    "5-1": "VeChainThor Thunder X Node",
    "6-1": "VeChainThor Mjolnir X Node"
  },
  "cols": 2,
  "rows": 7
}
[/block]
## cancelUpgrade
[block:code]
{
  "codes": [
    {
      "code": "function cancelUpgrade(uint256 _tokenId)",
      "language": "text"
    }
  ]
}
[/block]
Cancel the application of upgrading node token.

Params:

+ _tokenId: the id of the token

## getTokenParams
[block:code]
{
  "codes": [
    {
      "code": "function getTokenParams(strengthLevel _level) public view\n            returns(\n                    uint256 minBalance,\n                    uint64 ripeDays,\n                    uint64 rewardRatio,\n                    uint64 rewardRatioX\n            )",
      "language": "text"
    }
  ]
}
[/block]

Get Node Level parameters

Return:

+ minBalance: the minimum VET balance needed
+ ripeDays: the days of being the level
+ rewardRatio: reward ratio for normal node token
+ rewardRatioX: reward ratio for X node token


## idToOwner
[block:code]
{
  "codes": [
    {
      "code": "    function idToOwner(uint256 _tokenId) public view\n            returns (address)",
      "language": "text"
    }
  ]
}
[/block]
Get the owner of the given node token.

Params:

+ _tokenId: the id of node token

Return: the owner of the token


## ownerToId
[block:code]
{
  "codes": [
    {
      "code": "    function ownerToId(address _owner) public view\n            returns (uint256)",
      "language": "text"
    }
  ]
}
[/block]
Get the node token id of the given address owns.

Params:

+ _owner: the address that owns token

Return: the node token id of the given address owns


## createSaleAuction
[block:code]
{
  "codes": [
    {
      "code": "        function createSaleAuction(\n                uint256 _tokenId,\n                uint128 _startingPrice,\n                uint128 _endingPrice,\n                uint64 _duration\n        ) public",
      "language": "text"
    }
  ]
}
[/block]
Create an public auction.

Params:

+ _tokenId: the id of token
+ _startingPrice: starting price
+ _endingPrice: ending price
+ _duration: the duration of the auction from 2 hours to 7 days

## createDirectionalSaleAuction
[block:code]
{
  "codes": [
    {
      "code": "\n        function createDirectionalSaleAuction(\n                uint256 _tokenId,\n                uint128 _price,\n                uint64 _duration,\n                address _toAddress\n        ) public",
      "language": "text"
    }
  ]
}
[/block]
reate a directional auction.

Params:

+ _tokenId: the id of token
+ _price: the selling price
+ _duration: the duration of the auction from 2 hours to 7 days
+ _toAddress: the receiver address
  

## bid
[block:code]
{
  "codes": [
    {
      "code": "    function bid(uint256 _tokenId) public payable",
      "language": "text"
    }
  ]
}
[/block]
Purchase or bid an auction.

Params:

+ _tokenId: the id of token


## cancelAuction
[block:code]
{
  "codes": [
    {
      "code": " function cancelAuction(uint256 _tokenId) public",
      "language": "text"
    }
  ]
}
[/block]
Cancel the auction.

Params:

+ _tokenId: the id of token


## addAuctionWhiteList
[block:code]
{
  "codes": [
    {
      "code": "     function addAuctionWhiteList(uint256 _tokenId, address _address) public\n",
      "language": "text"
    }
  ]
}
[/block]
Add an address to whitelist.

Params:

+ _tokenId: the id of token
+ _address: the target address

## removeAuctionWhiteList
[block:code]
{
  "codes": [
    {
      "code": " function removeAuctionWhiteList(uint256 _tokenId, address _address) public",
      "language": "text"
    }
  ]
}
[/block]
Remove an address from whitelist.

Params:

+ _tokenId: the id of token
+ _address: the target address

[block:api-header]
{
  "title": "Audit Report"
}
[/block]
Security audit performed by [SlowMist Team](https://github.com/slowmist/Knowledge-Base/tree/master/open-report/VeChainThorNodeToken-Smart-Contract-Security-Audit-Report.md).

[block:api-header]
{
  "title": "License"
}
[/block]
It is licensed under the [GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.html), also included in [LICENSE](https://github.com/vechain/ThorNode-contracts/blob/master/LICENSE) file in repository.