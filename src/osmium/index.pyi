import typing

from .osm import Location


class LocationTable:
    def clear(self) -> None: ...

    def get(self, id: int) -> Location: ...

    def set(self, id: int, loc: Location) -> None: ...

    def used_memory(self) -> int: ...


def create_map(map_type: str) -> LocationTable: ...


def map_types() -> typing.List[str]: ...
