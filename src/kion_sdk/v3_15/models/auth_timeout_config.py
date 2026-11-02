from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AuthTimeoutConfig")



@_attrs_define
class AuthTimeoutConfig:
    """ AuthTimeoutConfig represents the system settings for auth timeouts

        Attributes:
            default_timeout (int | Unset): The default timeout for authenticating Example: 10.
            refresh_timeout (int | Unset): The default timeout for authentication refreshes Example: 480.
     """

    default_timeout: int | Unset = UNSET
    refresh_timeout: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        default_timeout = self.default_timeout

        refresh_timeout = self.refresh_timeout


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if default_timeout is not UNSET:
            field_dict["default_timeout"] = default_timeout
        if refresh_timeout is not UNSET:
            field_dict["refresh_timeout"] = refresh_timeout

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_timeout = d.pop("default_timeout", UNSET)

        refresh_timeout = d.pop("refresh_timeout", UNSET)

        auth_timeout_config = cls(
            default_timeout=default_timeout,
            refresh_timeout=refresh_timeout,
        )


        auth_timeout_config.additional_properties = d
        return auth_timeout_config

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
