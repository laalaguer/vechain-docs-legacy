Smart contract development best practice
=========================================

VeChainThor Solidity The Right Way
-----------------------------------


Motivation
-----------

As you may know, EVM is also the runtime environment for smart contracts in VeChainThor. So this guide is built upon and inspired by a number of articles and talks by the Ethereum community. These practices are certainly not unique to programming and development in VeChainThor.

Our goal here is to make you a better—more effective, more knowledgeable, more practical—solidity developer in VeChainThor.

General Philosophy
-------------------

+ **Keep Simple**: Complexity increases the likelihood of errors.
+ **Security First**: The security of a smart contract is always a top priority.
+ **Revert As Far As Possible**: Do not use `return false` when a condition is not met.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   best-practice/recommendations.md 
   best-practice/design-patterns.md 
   best-practice/security.md
   best-practice/resources.md