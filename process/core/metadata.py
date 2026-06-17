from collections.abc import Mapping
from dataclasses import dataclass, field, fields
from typing import Any

_METADATA_KEY = "_PROCESS_VARIABLE_STATIC_METADATA"


@dataclass(kw_only=True, slots=True)
class PROCESSVariableMetadata:
    name: str
    short_description: str | None = None
    symbol: str | None = None
    units: str | None


def process_variable_field(
    *,
    default: Any,
    short_description: str | None = None,
    symbol: str | None = None,
    units: str | None = None,
    metadata: Mapping[Any, Any] | None = None,
    **kwargs,
):
    metadata = {
        _METADATA_KEY: PROCESSVariableMetadata(
            name="", short_description=short_description, symbol=symbol, units=units
        ),
        **(metadata or {}),
    }
    return field(default=default, metadata=metadata, **kwargs)


_NO_METADATA = object()


class PROCESSModelData:
    metadata: dict[str, PROCESSVariableMetadata]

    def __post_init__(self):
        self.metadata = {}
        for f in fields(self):
            metadata = f.metadata.get(_METADATA_KEY, _NO_METADATA)

            if metadata is _NO_METADATA:
                continue

            metadata.name = f.name
            self.metadata[f.name] = metadata
