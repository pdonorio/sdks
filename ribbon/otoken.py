#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By: Steven (steven@ribbon.finance)
# Created Date: 04/04/2022
# version ='0.1.0'
# ---------------------------------------------------------------------------
""" Module to call oToken contract """
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from erc20 import ERC20Contract

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
DEFAULT_ABI_LOCATION = 'abis/oToken.json'

# ---------------------------------------------------------------------------
# oToken Contract
# ---------------------------------------------------------------------------
class oTokenContract(ERC20Contract):
  """
  Object to create connection to the an oToken contract

  Args:
      chain (str): The chain the contract is deployed in
      address (str): Contract address
      abi (dict): Contract ABI location
  """
  def __init__(
    self, 
    address: str,
    chain: str,
    abi: dict=DEFAULT_ABI_LOCATION
  ):
    super().__init__(address, chain, abi)

  def get_otoken_details(self) -> dict:
    """
    Method to validate bid

    Args:

    Returns:
        response (dict): Dictionary oToken details
    """
    details = self.contract.functions.getOtokenDetails().call()

    return {
      'collateralAsset': details[0], 
      'underlyingAsset': details[1], 
      'strikeAsset': details[2], 
      'strikePrice': details[3], 
      'expiryTimestamp': details[4], 
      'isPut': details[5]
    }