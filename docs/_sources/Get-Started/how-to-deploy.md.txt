# How to deploy a smart contract
## Quick Start
Quick guide to deploying a smart contract to VeChainThor blockchain:
- - - -
Requires Connex (find out here [Compatible Clients](https://doc.vechainworld.io/docs/clients) or [What is Connex?](https://doc.vechainworld.io/docs/connex))

It's recommended to use [VeChain IDE](doc:develop-and-deploy-smart-contract-in-ide) via [Sync](doc:sdk) for the smart contract development. 

- - - -
Open VIDE in the Connex environment (visit [https://vechainstore.com/ide](https://vechainstore.com/ide))

A sample contract is available (ballot.sol), this contract is very basic. The goal is to quickly start to create and to interact with a smart contract on VeChainThor blockchain.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cf3d32d-VIDE_editor.png",
        "VIDE_editor.png",
        1897,
        936,
        "#e6e6e9"
      ],
      "caption": "VIDE: Solidity Editor"
    }
  ]
}
[/block]
**Compile contracts:** in the ``Compile tab`` click on ``Start to compile`` button

**Deploy contracts:** in the ``Run tab`` select the contract you want to deploy (eg Ballot), the constructor of Ballot contract needs a parameter is number of proposals (_numProposals: type uint8). Give any value and click on ``Deploy`` button

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/924f36e-VIDE_runtab.png",
        "VIDE_runtab.png",
        380,
        575,
        "#f6f5f7"
      ],
      "caption": "VIDE: Run tab"
    }
  ]
}
[/block]
**Running transactions:** in the ``Run tab`` after deploying a successful contract and confirmed, in the ``Deployed Contracts`` table will appear the ``Ballot`` contract and its address

**Interacting with an instance**

This new instance contains 4 actions which corresponds to the 4 functions (giveRightToVote, delegate, vote, winningProposal). Clicking on giveRightToVote, delegate or vote will create a new transaction.

**giveRightToVote:** Give $(toVoter) the right to vote on this ballot, may only be called by $(chairperson) is also the creator of the contract.

**delegate:** Delegate your vote to the voter $(to).

**vote:** Give a single vote to proposal $(toProposal).

Clicking on ``winningProposal`` will not execute a transaction (blue action), not modify the state (variable value) of this instance.
As ``winningProposal`` is constant you can see the return value just below the action.