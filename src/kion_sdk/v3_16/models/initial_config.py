from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="InitialConfig")



@_attrs_define
class InitialConfig:
    """ InitialConfig contains the initial values needed to setup cloudtamer.

        Attributes:
            admin_password (str): Sets the admin password for the application Example: adminPassword.
            license_key (str): The license key for the application Example: licenseKey.
            usage_unit_keys (list[str] | None | Unset): Usage units for the application Example: ['usageUnits'].
     """

    admin_password: str
    license_key: str
    usage_unit_keys: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        admin_password = self.admin_password

        license_key = self.license_key

        usage_unit_keys: list[str] | None | Unset
        if isinstance(self.usage_unit_keys, Unset):
            usage_unit_keys = UNSET
        elif isinstance(self.usage_unit_keys, list):
            usage_unit_keys = self.usage_unit_keys


        else:
            usage_unit_keys = self.usage_unit_keys


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "admin_password": admin_password,
            "license_key": license_key,
        })
        if usage_unit_keys is not UNSET:
            field_dict["usage_unit_keys"] = usage_unit_keys

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_password = d.pop("admin_password")

        license_key = d.pop("license_key")

        def _parse_usage_unit_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                usage_unit_keys_type_0 = cast(list[str], data)

                return usage_unit_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        usage_unit_keys = _parse_usage_unit_keys(d.pop("usage_unit_keys", UNSET))


        initial_config = cls(
            admin_password=admin_password,
            license_key=license_key,
            usage_unit_keys=usage_unit_keys,
        )


        initial_config.additional_properties = d
        return initial_config

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
