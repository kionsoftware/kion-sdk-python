from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UsageUnitConfig")



@_attrs_define
class UsageUnitConfig:
    """ UsageUnitConfig contains a usage unit key to be added to the application.

        Attributes:
            usage_unit_key (str): The usage unit key for the application Example: usageUnitKey.
     """

    usage_unit_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        usage_unit_key = self.usage_unit_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "usage_unit_key": usage_unit_key,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usage_unit_key = d.pop("usage_unit_key")

        usage_unit_config = cls(
            usage_unit_key=usage_unit_key,
        )


        usage_unit_config.additional_properties = d
        return usage_unit_config

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
