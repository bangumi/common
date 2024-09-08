from pathlib import Path

import msgspec


class Platform(msgspec.Struct):
    id: int
    type: str
    type_cn: str
    sortKeys: tuple[str, ...] = ()


PlatformConfig = dict[int, dict[int, Platform]]


PLATFORM_CONFIG: PlatformConfig = msgspec.json.decode(
    Path(__file__, "../platform.json").resolve().read_bytes(), type=PlatformConfig
)
