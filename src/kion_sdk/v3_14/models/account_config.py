from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountConfig")



@_attrs_define
class AccountConfig:
    """ AccountConfig represents the system settings for creating new accounts

        Attributes:
            account_cache_enabled (bool | None | Unset): Indicates whether the account cache is enabled or not Example:
                True.
            account_creation_enabled (bool | None | Unset): Indicates whether account creation is enabled or not
     """

    account_cache_enabled: bool | None | Unset = UNSET
    account_creation_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_cache_enabled: bool | None | Unset
        if isinstance(self.account_cache_enabled, Unset):
            account_cache_enabled = UNSET
        else:
            account_cache_enabled = self.account_cache_enabled

        account_creation_enabled: bool | None | Unset
        if isinstance(self.account_creation_enabled, Unset):
            account_creation_enabled = UNSET
        else:
            account_creation_enabled = self.account_creation_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_cache_enabled is not UNSET:
            field_dict["account_cache_enabled"] = account_cache_enabled
        if account_creation_enabled is not UNSET:
            field_dict["account_creation_enabled"] = account_creation_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_cache_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        account_cache_enabled = _parse_account_cache_enabled(d.pop("account_cache_enabled", UNSET))


        def _parse_account_creation_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        account_creation_enabled = _parse_account_creation_enabled(d.pop("account_creation_enabled", UNSET))


        account_config = cls(
            account_cache_enabled=account_cache_enabled,
            account_creation_enabled=account_creation_enabled,
        )


        account_config.additional_properties = d
        return account_config

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
