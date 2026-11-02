from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DeleteUserCloudAccessRoleAliasRequest")



@_attrs_define
class DeleteUserCloudAccessRoleAliasRequest:
    """ DeleteUserCloudAccessRoleAliasRequest contains the parameters for deleting a user cloud access role alias.

        Attributes:
            alias_name (str): Name of the alias for deletion. Example: development-admin.
     """

    alias_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        alias_name = self.alias_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "alias_name": alias_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alias_name = d.pop("alias_name")

        delete_user_cloud_access_role_alias_request = cls(
            alias_name=alias_name,
        )


        delete_user_cloud_access_role_alias_request.additional_properties = d
        return delete_user_cloud_access_role_alias_request

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
