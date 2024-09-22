from pathlib import Path

import msgspec
import yaml


class Platform(msgspec.Struct):
    id: int
    type: str
    type_cn: str
    sort_keys: tuple[str, ...] = ()


subject_platforms = yaml.safe_load(
    Path(__file__, "../subject_platforms.yml").resolve().read_bytes()
)

PlatformConfig = dict[int, dict[int, Platform]]
SortKeys = msgspec.convert(subject_platforms['sort_keys'], dict[int, tuple[str, ...]])

PLATFORM_CONFIG: PlatformConfig = msgspec.convert(
    {key: value for key, value in subject_platforms['platforms'].items() if isinstance(key, int)},
    type=PlatformConfig
)
