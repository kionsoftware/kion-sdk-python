from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="StringBaseFilter")



@_attrs_define
class StringBaseFilter:
    """ StringBaseFilter defines filtering on a set of strings by including or excluding values

        Attributes:
            is_exclusive (bool | None | Unset): Is Exclusive

                If true, the filter will exclude the values specified from the results.
            values (list[str] | None | Unset): Values Example: ['val1', 'val2', 'val3'].
     """

    is_exclusive: bool | None | Unset = UNSET
    values: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_exclusive: bool | None | Unset
        if isinstance(self.is_exclusive, Unset):
            is_exclusive = UNSET
        else:
            is_exclusive = self.is_exclusive

        values: list[str] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = self.values


        else:
            values = self.values


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_exclusive is not UNSET:
            field_dict["is_exclusive"] = is_exclusive
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_is_exclusive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_exclusive = _parse_is_exclusive(d.pop("is_exclusive", UNSET))


        def _parse_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))


        string_base_filter = cls(
            is_exclusive=is_exclusive,
            values=values,
        )


        string_base_filter.additional_properties = d
        return string_base_filter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
