import logging

import typing
from typing import Any, Optional

from osmium import MergeInputReader
from osmium.replication.utils import Sequence, Timestamp

log: logging.Logger

OsmosisState = typing.NamedTuple('OsmosisState', [('sequence', Sequence), ('timestamp', Timestamp)])
DownloadResult = typing.NamedTuple('DownloadResult',
                                   [('id', Sequence), ('reader', MergeInputReader), ('newest', Sequence)])


class ReplicationServer:
    baseurl: str = ...
    diff_type: str = ...

    def __init__(self, url: str, diff_type: str = ...) -> None: ...

    def collect_diffs(self, start_id: Sequence, max_size: int = ...) -> DownloadResult: ...

    def apply_diffs(self, handler: Any, start_id: Sequence, max_size: int = ..., idx: str = ...,
                    simplify: bool = ...) -> Optional[Sequence]: ...

    def apply_diffs_to_file(self, infile: str, outfile: str, start_id: Sequence, max_size: int = ...,
                            set_replication_header: bool = ...) -> Optional[typing.Tuple[Sequence, Sequence]]: ...

    def timestamp_to_sequence(self, timestamp: Timestamp, balanced_search: bool = ...) -> Optional[Sequence]: ...

    def get_state_info(self, seq: Optional[Sequence] = ...) -> OsmosisState: ...

    def get_diff_block(self, seq: Sequence) -> bytes: ...

    def get_state_url(self, seq: Sequence) -> str: ...

    def get_diff_url(self, seq: Sequence) -> str: ...
