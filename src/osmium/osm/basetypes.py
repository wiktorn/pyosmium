import typing
from ..osm import _osm


OSMObjectIdType = typing.NewType('OSMObjectId', int)
UnsginedOSMObjectIdType = typing.NewType('UnsginedOSMObjectIdType', OSMObjectIdType)
UidType = typing.NewType('UserId', int)
VersionType = typing.NewType('VersionType', int)
ChangesetId = typing.NewType('ChangesetId', int)

LocationType = typing.Union[_osm.Location, typing.Tuple[float, float]]
NodeListType = typing.Union[_osm.WayNodeList, typing.List[_osm.NodeRef], typing.List[int]]
RelationMembersType = typing.Union[
    _osm.RelationMemberList,
    typing.List[_osm.RelationMember],
    typing.List[typing.Tuple[str, int, str]]
]
