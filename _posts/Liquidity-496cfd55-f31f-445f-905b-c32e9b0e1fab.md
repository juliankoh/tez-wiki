---
layout: post
title:  "Liquidity"
date:   2019-01-02 18:07:24
categories: jekyll update
---
# Liquidity

Liquidity is a high-level language to program Smart Contracts for Tezos. It is a fully typed functional language, it uses the syntax of OCaml, and strictly complies with Michelson security restrictions.

A formal-method framework for Liquidity is under development, to prove the correctness of smart-contracts written in Liquidity.

The Liquidity language provides the following features:

- Full coverage of the Michelson language: Anything that can be written in Michelson can be written in Liquidity,
- Local variables instead of stack manipulations: values can be stored in local variables.
- High-level types: types like sum-types and record-types can be defined and used in Liquidity programs.

Liquidity already covers 100% of the Michelson features, and contracts generated with Liquidity can be submitted on the current mainnet and zeronet.