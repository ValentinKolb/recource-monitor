import abc
from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class ResourceStatus:
    reachable: bool
    status_msg: str


@dataclass
class BaseResource(metaclass=abc.ABCMeta):
    img: str
    title: str
    address: str
    status: Optional[ResourceStatus] = field(default=None)


class PingResource(BaseResource):
    pass


class HTTPResource(BaseResource):
    pass
