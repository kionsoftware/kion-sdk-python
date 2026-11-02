from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateLabel")



@_attrs_define
class CreateLabel:
    """ CreateLabel defines a new label

        Attributes:
            color (str): Hex value of the label color Example: #9fa4a6.
            key (str): Key of the label (first part of the label) Example: Department.
            value (str): Value of the label (second part of the label following the key) Example: Engineering.
            id (int | Unset): ID of the record in the application. Example: 1.
     """

    color: str
    key: str
    value: str
    id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        color = self.color

        key = self.key

        value = self.value

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "color": color,
            "key": key,
            "value": value,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color")

        key = d.pop("key")

        value = d.pop("value")

        id = d.pop("id", UNSET)

        create_label = cls(
            color=color,
            key=key,
            value=value,
            id=id,
        )


        create_label.additional_properties = d
        return create_label

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
