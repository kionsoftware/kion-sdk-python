from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OUBaseFilter")



@_attrs_define
class OUBaseFilter:
    """ OUBaseFilter defines filtering on a set of OUs

        Attributes:
            include_descendants (bool | None | Unset): Include All OU Descendants Example: True.
            is_exclusive (bool | None | Unset): Is Exclusive

                If true, the filter will exclude the values specified from the results.
            values (list[int] | None | Unset): Values Example: [1, 2, 3].
     """

    include_descendants: bool | None | Unset = UNSET
    is_exclusive: bool | None | Unset = UNSET
    values: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        include_descendants: bool | None | Unset
        if isinstance(self.include_descendants, Unset):
            include_descendants = UNSET
        else:
            include_descendants = self.include_descendants

        is_exclusive: bool | None | Unset
        if isinstance(self.is_exclusive, Unset):
            is_exclusive = UNSET
        else:
            is_exclusive = self.is_exclusive

        values: list[int] | None | Unset
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
        if include_descendants is not UNSET:
            field_dict["include_descendants"] = include_descendants
        if is_exclusive is not UNSET:
            field_dict["is_exclusive"] = is_exclusive
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_include_descendants(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_descendants = _parse_include_descendants(d.pop("include_descendants", UNSET))


        def _parse_is_exclusive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_exclusive = _parse_is_exclusive(d.pop("is_exclusive", UNSET))


        def _parse_values(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[int], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))


        ou_base_filter = cls(
            include_descendants=include_descendants,
            is_exclusive=is_exclusive,
            values=values,
        )


        ou_base_filter.additional_properties = d
        return ou_base_filter

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
