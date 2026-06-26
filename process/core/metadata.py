from collections.abc import Mapping
from dataclasses import dataclass, field, fields
from typing import Any

from process.core.exceptions import ProcessValueError

_METADATA_KEY = "_PROCESS_VARIABLE_STATIC_METADATA"

_MISSING = object()


@dataclass(kw_only=True, slots=True)
class PROCESSVariableMetadata:
    name: str
    short_description: str | None = None
    symbol: str | None = None
    units: str | None
    _index: int = _MISSING


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
    _metadata: dict[str, PROCESSVariableMetadata]

    def __post_init__(self):
        self._metadata = {}
        for i, f in enumerate(fields(self)):
            metadata = f.metadata.get(_METADATA_KEY, _NO_METADATA)

            if metadata is _NO_METADATA:
                continue

            metadata._index = i
            metadata.name = f.name
            self._metadata[f.name] = metadata

    def get_field(self, variable: int | str):
        if isinstance(variable, int):
            return fields(self)[variable]
        if isinstance(variable, str):
            for f in fields(self):
                if f.name == variable:
                    return f
            else:  # noqa: PLW0120
                error_msg = (
                    f"No field {variable} exists on dataclass {self.__class__.__name__}."
                )
                raise ProcessValueError(error_msg)
        else:
            error_msg = "'variable' must either be a string or integer."
            raise TypeError

    def get_formatted_outputs(self):
        outputs = []
        for var_name, var_metadata in self._metadata.items():
            value = getattr(self, var_name)
            variable_field = self.get_field(var_metadata._index)

            outputs.append((
                var_metadata.short_description,
                f"({var_name})",
                value,
                "OP " if value != variable_field.default else "",
            ))

        return outputs
