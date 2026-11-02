from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="CloudProviderEnabled")



@_attrs_define
class CloudProviderEnabled:
    """ CloudProviderEnabled .

        Attributes:
            is_enabled (bool | None): True if the cloud provider should be enabled. False if not enabled. Example: True.
     """

    is_enabled: bool | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_enabled: bool | None
        is_enabled = self.is_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "is_enabled": is_enabled,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_is_enabled(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_enabled = _parse_is_enabled(d.pop("is_enabled"))


        cloud_provider_enabled = cls(
            is_enabled=is_enabled,
        )


        cloud_provider_enabled.additional_properties = d
        return cloud_provider_enabled

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
