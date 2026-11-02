from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TagValue")



@_attrs_define
class TagValue:
    """ TagValue defines a value for a tag value.

        Attributes:
            name (str | Unset):
            tag_id (int | None | Unset):
            tag_key_id (int | None | Unset):
     """

    name: str | Unset = UNSET
    tag_id: int | None | Unset = UNSET
    tag_key_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tag_id: int | None | Unset
        if isinstance(self.tag_id, Unset):
            tag_id = UNSET
        else:
            tag_id = self.tag_id

        tag_key_id: int | None | Unset
        if isinstance(self.tag_key_id, Unset):
            tag_key_id = UNSET
        else:
            tag_key_id = self.tag_key_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if tag_id is not UNSET:
            field_dict["tag_id"] = tag_id
        if tag_key_id is not UNSET:
            field_dict["tag_key_id"] = tag_key_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_tag_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tag_id = _parse_tag_id(d.pop("tag_id", UNSET))


        def _parse_tag_key_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tag_key_id = _parse_tag_key_id(d.pop("tag_key_id", UNSET))


        tag_value = cls(
            name=name,
            tag_id=tag_id,
            tag_key_id=tag_key_id,
        )


        tag_value.additional_properties = d
        return tag_value

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
