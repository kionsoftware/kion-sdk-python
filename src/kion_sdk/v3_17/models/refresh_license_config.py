from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="RefreshLicenseConfig")



@_attrs_define
class RefreshLicenseConfig:
    """ RefreshLicenseConfig contains a license key to be used to refresh an expired license.

        Attributes:
            license_key (str): The license key for the application Example: licenseKey.
     """

    license_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        license_key = self.license_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "license_key": license_key,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_key = d.pop("license_key")

        refresh_license_config = cls(
            license_key=license_key,
        )


        refresh_license_config.additional_properties = d
        return refresh_license_config

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
