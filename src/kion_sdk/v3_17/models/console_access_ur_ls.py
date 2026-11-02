from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConsoleAccessURLs")



@_attrs_define
class ConsoleAccessURLs:
    """ ConsoleAccessURLs defines the three URL variation types for console federation.

        Attributes:
            fabric_specific_url (str | Unset): Fabric-specific URL - region-aware URL for commercial vs government Example:
                https://us-east-1.signin.aws.amazon.com/federation?Action=login&Issuer=....
            federation_url (str | Unset): Plain federation URL - direct AWS federation URL Example:
                https://signin.aws.amazon.com/federation?Action=login&Issuer=....
            logout_redirect_url (str | Unset): Logout+redirect URL - full logout URL with redirect query parameter Example:
                https://us-east-1.signin.aws.amazon.com/logout?logout_uri=....
     """

    fabric_specific_url: str | Unset = UNSET
    federation_url: str | Unset = UNSET
    logout_redirect_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fabric_specific_url = self.fabric_specific_url

        federation_url = self.federation_url

        logout_redirect_url = self.logout_redirect_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fabric_specific_url is not UNSET:
            field_dict["fabric_specific_url"] = fabric_specific_url
        if federation_url is not UNSET:
            field_dict["federation_url"] = federation_url
        if logout_redirect_url is not UNSET:
            field_dict["logout_redirect_url"] = logout_redirect_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fabric_specific_url = d.pop("fabric_specific_url", UNSET)

        federation_url = d.pop("federation_url", UNSET)

        logout_redirect_url = d.pop("logout_redirect_url", UNSET)

        console_access_ur_ls = cls(
            fabric_specific_url=fabric_specific_url,
            federation_url=federation_url,
            logout_redirect_url=logout_redirect_url,
        )


        console_access_ur_ls.additional_properties = d
        return console_access_ur_ls

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
