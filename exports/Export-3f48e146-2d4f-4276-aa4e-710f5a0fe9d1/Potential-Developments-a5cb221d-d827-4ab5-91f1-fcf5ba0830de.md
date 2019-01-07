# Potential Developments

# Privacy-Preserving Transactions

Transactions in blockchains are public by default. A company would not want its past transactions to be a matter of public record, thus solutions to make transactions completely private are very important. To solve the problem of privacy-preserving transactions, there have been many competing solutions with different trade-offs and benefits.

## Non-interactive Zero Knowledge Proof

The usage of zero knowledge proofs with the zk-SNARK technique enables transactions to be broadcasted privately. How it works simplistically is that the commitments of each transaction are stored in the Merkle tree, which the recipients transact with using a zero knowledge proof. This technique leads to transactions that are private and concise but require a trusted setup. This trusted setup leads to 

## Ring Signatures

# Amendment Rules

## Constitutionalism

Constitutionalism refers to the adherence to a set of rules regarding protocol upgrades. These set of rules would create additional safeguards for the Tezos blockchain for protocol upgrades. One such rule could state that certain files (such as the one handling the generation of new tokens) are elevated to a privileged status. These files would then require a larger majority vote and a prolonged voting period to change.

A method to enforce constitutionalism is to have a proof checker embedded into the Tezos node. The proof checker works by employing a set of filters, where each filter ensures that some files are not modified or removed. By passing all the filters, it means that a protocol upgrade has not violated any of the rules stated in the constitution.

## Futarcy

Futarchy is a governance concept first proposed by [Robin Hanson](http://mason.gmu.edu/~rhanson/futarchy.html). The idea is that proposals and upgrades should be voted by the majority, however the choice of adopting the proposal/upgrade should be left to a betting market. An example would be, having a proposal that increases the block size of the Tezos blockchain to 1 MB, which is agreed upon by most stakeholders; the proposal is then voted upon by the market if the proposal is beneficial for the Tezos blockchain. There would only be 2 outcomes in this betting market, if an increased block size is beneficial for Tezos ("Yes" or "No"). These outcomes are reflected in the price of the token; the price of a Tez increasing represents "Yes" while the price of a Tez decreasing represents "No".

The market-making in those contracts can be subsidized by issuing coins to market makers in order to improve price discovery and liquidity. In the end, the amendment deemed most likely  by the market's price would be automatically adopted.