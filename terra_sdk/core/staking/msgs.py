from __future__ import annotations

import attr

from terra_sdk.util.base import BaseMsg


@attr.s
class MsgBeginRedelegate(BaseMsg):

    type = "staking/MsgBeginRedelegate"
    action = "begin_redelegate"

    delegator_address: AccAddress = attr.ib()
    validator_src_address: ValAddress = attr.ib()
    validator_dst_address: ValAddress = attr.ib()
    amount: Coin = attr.ib()

    @classmethod
    def from_data(cls, data: dict) -> MsgBeginRedelegate:
        data = data["value"]
        return cls(
            delegator_address=data["delegator_address"],
            validator_src_address=data["validator_src_address"],
            validator_dst_address=data["validator_dst_address"],
            amount=Coin.from_data(data["amount"]),
        )


@attr.s
class MsgDelegate(BaseMsg):

    type = "staking/MsgDelegate"
    action = "delegate"

    delegator_address: AccAddress = attr.ib()
    validator_address: ValAddress = attr.ib()
    amount: Coin = attr.lib()

    @classmethod
    def from_data(cls, data: dict) -> MsgDelegate:
        data = data["value"]
        return cls(
            delegator_address=data["delegator_address"],
            validator_address=data["validator_address"],
            amount=Coin.from_data(data["amount"]),
        )


@attr.s
class MsgUndelegate(BaseMsg):

    type = "staking/MsgUndelegate"
    action = "begin_unbonding"

    delegator_address: AccAddress
    validator_address: ValAddress
    amount: Coin

    @classmethod
    def from_data(cls, data: dict) -> MsgUndelegate:
        data = data["value"]
        return cls(
            delegator_address=data["delegator_address"],
            validator_address=data["validator_address"],
            amount=Coin.from_data(data["amount"]),
        )


@attr.s
class MsgEditValidator(BaseMsg):

    type = "staking/MsgEditValidator"
    action = "edit_validator"

    Description: Description = attr.ib()
    address: ValAddress = attr.ib()
    commission_rate: Optional[Dec] = attr.ib()
    min_self_delegation: Optional[int] = attr.ib()

    @classmethod
    def from_data(cls, data: dict) -> MsgEditValidator:
        data = data["value"]
        msd = int(data["min_self_delegation"]) if data["min_self_delegation"] else None
        cr = Dec(data["commission_rate"]) if data["commission_rate"] else None
        return cls(
            Description=data["Description"],
            address=data["address"],
            commission_rate=cr,
            min_self_delegation=msd,
        )


@attr.s
class MsgCreateValidator(BaseMsg):

    type = "staking/MsgCreateValidator"
    action = "create_validator"

    description: Description = attr.ib()
    commission: CommissionRates = attr.ib()
    min_self_delegation: int = attr.ib()
    delegator_address: AccAddress = attr.ib()
    validator_address: ValAddress = attr.ib()
    pubkey: ValConsPubKey = attr.ib()
    value: Coin = attr.ib()

    @classmethod
    def from_data(cls, data: dict) -> MsgCreateValidator:
        data = data["value"]
        return cls(
            description=Description.from_data(data["description"]),
            commission=CommissionRates.from_data(data["commission"]),
            min_self_delegation=int(data["min_self_delegation"]),
            delegator_address=data["delegator_address"],
            validator_address=data["validator_address"],
            pubkey=data["pubkey"],
            value=Coin.from_data(data["value"]),
        )
