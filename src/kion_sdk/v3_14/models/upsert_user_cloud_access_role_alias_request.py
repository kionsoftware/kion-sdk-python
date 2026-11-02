from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpsertUserCloudAccessRoleAliasRequest")



@_attrs_define
class UpsertUserCloudAccessRoleAliasRequest:
    """ UpsertUserCloudAccessRoleAliasRequest contains the parameters for creating or updating a user cloud access role
    alias.

        Attributes:
            access_type (str): AccessType represents how a cloud access role is used by the user
            account_number (str): Account number to bind alias to. Example: 12345.
            alias_name (str): Name of the alias. Example: development-admin.
            cloud_access_role_name (str | Unset): Name of cloud access role (OU or Project) for the alias Example:
                developer-role.
     """

    access_type: str
    account_number: str
    alias_name: str
    cloud_access_role_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_type = self.access_type

        account_number = self.account_number

        alias_name = self.alias_name

        cloud_access_role_name = self.cloud_access_role_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_type": access_type,
            "account_number": account_number,
            "alias_name": alias_name,
        })
        if cloud_access_role_name is not UNSET:
            field_dict["cloud_access_role_name"] = cloud_access_role_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_type = d.pop("access_type")

        account_number = d.pop("account_number")

        alias_name = d.pop("alias_name")

        cloud_access_role_name = d.pop("cloud_access_role_name", UNSET)

        upsert_user_cloud_access_role_alias_request = cls(
            access_type=access_type,
            account_number=account_number,
            alias_name=alias_name,
            cloud_access_role_name=cloud_access_role_name,
        )


        upsert_user_cloud_access_role_alias_request.additional_properties = d
        return upsert_user_cloud_access_role_alias_request

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
