# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/types/block.proto, tendermint/types/canonical.proto, tendermint/types/events.proto, tendermint/types/evidence.proto, tendermint/types/params.proto, tendermint/types/types.proto, tendermint/types/validator.proto
# plugin: python-betterproto
import builtins
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class BlockIdFlag(betterproto.Enum):
    """BlockIdFlag indicates which BlcokID the signature is for"""

    BLOCK_ID_FLAG_UNKNOWN = 0
    BLOCK_ID_FLAG_ABSENT = 1
    BLOCK_ID_FLAG_COMMIT = 2
    BLOCK_ID_FLAG_NIL = 3


class SignedMsgType(betterproto.Enum):
    """SignedMsgType is a type of signed message in the consensus."""

    SIGNED_MSG_TYPE_UNKNOWN = 0
    # Votes
    SIGNED_MSG_TYPE_PREVOTE = 1
    SIGNED_MSG_TYPE_PRECOMMIT = 2
    # Proposals
    SIGNED_MSG_TYPE_PROPOSAL = 32


@dataclass(eq=False, repr=False)
class ValidatorSet(betterproto.Message):
    validators: List["Validator"] = betterproto.message_field(1)
    proposer: "Validator" = betterproto.message_field(2)
    total_voting_power: int = betterproto.int64_field(3)


@dataclass(eq=False, repr=False)
class Validator(betterproto.Message):
    address: bytes = betterproto.bytes_field(1)
    pub_key: "_crypto__.PublicKey" = betterproto.message_field(2)
    voting_power: int = betterproto.int64_field(3)
    proposer_priority: int = betterproto.int64_field(4)


@dataclass(eq=False, repr=False)
class SimpleValidator(betterproto.Message):
    pub_key: "_crypto__.PublicKey" = betterproto.message_field(1)
    voting_power: int = betterproto.int64_field(2)


@dataclass(eq=False, repr=False)
class PartSetHeader(betterproto.Message):
    """PartsetHeader"""

    total: int = betterproto.uint32_field(1)
    hash: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class Part(betterproto.Message):
    index: int = betterproto.uint32_field(1)
    bytes: builtins.bytes = betterproto.bytes_field(2)
    proof: "_crypto__.Proof" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class BlockId(betterproto.Message):
    """BlockID"""

    hash: bytes = betterproto.bytes_field(1)
    part_set_header: "PartSetHeader" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Header(betterproto.Message):
    """Header defines the structure of a Tendermint block header."""

    # basic block info
    version: "_version__.Consensus" = betterproto.message_field(1)
    chain_id: str = betterproto.string_field(2)
    height: int = betterproto.int64_field(3)
    time: datetime = betterproto.message_field(4)
    # prev block info
    last_block_id: "BlockId" = betterproto.message_field(5)
    # hashes of block data
    last_commit_hash: bytes = betterproto.bytes_field(6)
    data_hash: bytes = betterproto.bytes_field(7)
    # hashes from the app output from the prev block
    validators_hash: bytes = betterproto.bytes_field(8)
    next_validators_hash: bytes = betterproto.bytes_field(9)
    consensus_hash: bytes = betterproto.bytes_field(10)
    app_hash: bytes = betterproto.bytes_field(11)
    last_results_hash: bytes = betterproto.bytes_field(12)
    # consensus info
    evidence_hash: bytes = betterproto.bytes_field(13)
    proposer_address: bytes = betterproto.bytes_field(14)


@dataclass(eq=False, repr=False)
class Data(betterproto.Message):
    """Data contains the set of transactions included in the block"""

    # Txs that will be applied by state @ block.Height+1. NOTE: not all txs here
    # are valid.  We're just agreeing on the order first. This means that
    # block.AppHash does not include these txs.
    txs: List[bytes] = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class Vote(betterproto.Message):
    """
    Vote represents a prevote, precommit, or commit vote from validators for
    consensus.
    """

    type: "SignedMsgType" = betterproto.enum_field(1)
    height: int = betterproto.int64_field(2)
    round: int = betterproto.int32_field(3)
    block_id: "BlockId" = betterproto.message_field(4)
    timestamp: datetime = betterproto.message_field(5)
    validator_address: bytes = betterproto.bytes_field(6)
    validator_index: int = betterproto.int32_field(7)
    signature: bytes = betterproto.bytes_field(8)


@dataclass(eq=False, repr=False)
class Commit(betterproto.Message):
    """
    Commit contains the evidence that a block was committed by a set of
    validators.
    """

    height: int = betterproto.int64_field(1)
    round: int = betterproto.int32_field(2)
    block_id: "BlockId" = betterproto.message_field(3)
    signatures: List["CommitSig"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class CommitSig(betterproto.Message):
    """CommitSig is a part of the Vote included in a Commit."""

    block_id_flag: "BlockIdFlag" = betterproto.enum_field(1)
    validator_address: bytes = betterproto.bytes_field(2)
    timestamp: datetime = betterproto.message_field(3)
    signature: bytes = betterproto.bytes_field(4)


@dataclass(eq=False, repr=False)
class Proposal(betterproto.Message):
    type: "SignedMsgType" = betterproto.enum_field(1)
    height: int = betterproto.int64_field(2)
    round: int = betterproto.int32_field(3)
    pol_round: int = betterproto.int32_field(4)
    block_id: "BlockId" = betterproto.message_field(5)
    timestamp: datetime = betterproto.message_field(6)
    signature: bytes = betterproto.bytes_field(7)


@dataclass(eq=False, repr=False)
class SignedHeader(betterproto.Message):
    header: "Header" = betterproto.message_field(1)
    commit: "Commit" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class LightBlock(betterproto.Message):
    signed_header: "SignedHeader" = betterproto.message_field(1)
    validator_set: "ValidatorSet" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class BlockMeta(betterproto.Message):
    block_id: "BlockId" = betterproto.message_field(1)
    block_size: int = betterproto.int64_field(2)
    header: "Header" = betterproto.message_field(3)
    num_txs: int = betterproto.int64_field(4)


@dataclass(eq=False, repr=False)
class TxProof(betterproto.Message):
    """
    TxProof represents a Merkle proof of the presence of a transaction in the
    Merkle tree.
    """

    root_hash: bytes = betterproto.bytes_field(1)
    data: bytes = betterproto.bytes_field(2)
    proof: "_crypto__.Proof" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class ConsensusParams(betterproto.Message):
    """
    ConsensusParams contains consensus critical parameters that determine the
    validity of blocks.
    """

    block: "BlockParams" = betterproto.message_field(1)
    evidence: "EvidenceParams" = betterproto.message_field(2)
    validator: "ValidatorParams" = betterproto.message_field(3)
    version: "VersionParams" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class BlockParams(betterproto.Message):
    """BlockParams contains limits on the block size."""

    # Max block size, in bytes. Note: must be greater than 0
    max_bytes: int = betterproto.int64_field(1)
    # Max gas per block. Note: must be greater or equal to -1
    max_gas: int = betterproto.int64_field(2)
    # Minimum time increment between consecutive blocks (in milliseconds) If the
    # block header timestamp is ahead of the system clock, decrease this value.
    # Not exposed to the application.
    time_iota_ms: int = betterproto.int64_field(3)


@dataclass(eq=False, repr=False)
class EvidenceParams(betterproto.Message):
    """EvidenceParams determine how we handle evidence of malfeasance."""

    # Max age of evidence, in blocks. The basic formula for calculating this is:
    # MaxAgeDuration / {average block time}.
    max_age_num_blocks: int = betterproto.int64_field(1)
    # Max age of evidence, in time. It should correspond with an app's "unbonding
    # period" or other similar mechanism for handling [Nothing-At-Stake
    # attacks](https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQ#what-is-
    # the-nothing-at-stake-problem-and-how-can-it-be-fixed).
    max_age_duration: timedelta = betterproto.message_field(2)
    # This sets the maximum size of total evidence in bytes that can be committed
    # in a single block. and should fall comfortably under the max block bytes.
    # Default is 1048576 or 1MB
    max_bytes: int = betterproto.int64_field(3)


@dataclass(eq=False, repr=False)
class ValidatorParams(betterproto.Message):
    """
    ValidatorParams restrict the public key types validators can use. NOTE:
    uses ABCI pubkey naming, not Amino names.
    """

    pub_key_types: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class VersionParams(betterproto.Message):
    """VersionParams contains the ABCI application version."""

    app_version: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class HashedParams(betterproto.Message):
    """
    HashedParams is a subset of ConsensusParams. It is hashed into the
    Header.ConsensusHash.
    """

    block_max_bytes: int = betterproto.int64_field(1)
    block_max_gas: int = betterproto.int64_field(2)


@dataclass(eq=False, repr=False)
class Evidence(betterproto.Message):
    duplicate_vote_evidence: "DuplicateVoteEvidence" = betterproto.message_field(
        1, group="sum"
    )
    light_client_attack_evidence: "LightClientAttackEvidence" = (
        betterproto.message_field(2, group="sum")
    )


@dataclass(eq=False, repr=False)
class DuplicateVoteEvidence(betterproto.Message):
    """
    DuplicateVoteEvidence contains evidence of a validator signed two
    conflicting votes.
    """

    vote_a: "Vote" = betterproto.message_field(1)
    vote_b: "Vote" = betterproto.message_field(2)
    total_voting_power: int = betterproto.int64_field(3)
    validator_power: int = betterproto.int64_field(4)
    timestamp: datetime = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class LightClientAttackEvidence(betterproto.Message):
    """
    LightClientAttackEvidence contains evidence of a set of validators
    attempting to mislead a light client.
    """

    conflicting_block: "LightBlock" = betterproto.message_field(1)
    common_height: int = betterproto.int64_field(2)
    byzantine_validators: List["Validator"] = betterproto.message_field(3)
    total_voting_power: int = betterproto.int64_field(4)
    timestamp: datetime = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class EvidenceList(betterproto.Message):
    evidence: List["Evidence"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Block(betterproto.Message):
    header: "Header" = betterproto.message_field(1)
    data: "Data" = betterproto.message_field(2)
    evidence: "EvidenceList" = betterproto.message_field(3)
    last_commit: "Commit" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class EventDataRoundState(betterproto.Message):
    height: int = betterproto.int64_field(1)
    round: int = betterproto.int32_field(2)
    step: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CanonicalBlockId(betterproto.Message):
    hash: bytes = betterproto.bytes_field(1)
    part_set_header: "CanonicalPartSetHeader" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CanonicalPartSetHeader(betterproto.Message):
    total: int = betterproto.uint32_field(1)
    hash: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class CanonicalProposal(betterproto.Message):
    type: "SignedMsgType" = betterproto.enum_field(1)
    height: int = betterproto.sfixed64_field(2)
    round: int = betterproto.sfixed64_field(3)
    pol_round: int = betterproto.int64_field(4)
    block_id: "CanonicalBlockId" = betterproto.message_field(5)
    timestamp: datetime = betterproto.message_field(6)
    chain_id: str = betterproto.string_field(7)


@dataclass(eq=False, repr=False)
class CanonicalVote(betterproto.Message):
    type: "SignedMsgType" = betterproto.enum_field(1)
    height: int = betterproto.sfixed64_field(2)
    round: int = betterproto.sfixed64_field(3)
    block_id: "CanonicalBlockId" = betterproto.message_field(4)
    timestamp: datetime = betterproto.message_field(5)
    chain_id: str = betterproto.string_field(6)


from .. import crypto as _crypto__
from .. import version as _version__
