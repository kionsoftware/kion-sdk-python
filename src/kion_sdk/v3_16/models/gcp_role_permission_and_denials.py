from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPRolePermissionAndDenials")



@_attrs_define
class GCPRolePermissionAndDenials:
    """ GCPRolePermissionAndDenials defines a list of permissions and denials to validate

        Attributes:
            role_denials (list[str] | None | Unset): List of GCP Permissions to remove when applying this role. Wildcards
                are supported.
                Is required if no permissions are provided. Example: ['iam.roles.get', 'resourcemanager.*'].
            role_permissions (list[str] | None | Unset): List of GCP Permissions to assign the role. Is required if no
                denials are provided. Example: ['iam.roles.get', 'iam.roles.list'].
     """

    role_denials: list[str] | None | Unset = UNSET
    role_permissions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        role_denials: list[str] | None | Unset
        if isinstance(self.role_denials, Unset):
            role_denials = UNSET
        elif isinstance(self.role_denials, list):
            role_denials = self.role_denials


        else:
            role_denials = self.role_denials

        role_permissions: list[str] | None | Unset
        if isinstance(self.role_permissions, Unset):
            role_permissions = UNSET
        elif isinstance(self.role_permissions, list):
            role_permissions = self.role_permissions


        else:
            role_permissions = self.role_permissions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if role_denials is not UNSET:
            field_dict["role_denials"] = role_denials
        if role_permissions is not UNSET:
            field_dict["role_permissions"] = role_permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_role_denials(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_denials_type_0 = cast(list[str], data)

                return role_denials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        role_denials = _parse_role_denials(d.pop("role_denials", UNSET))


        def _parse_role_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_permissions_type_0 = cast(list[str], data)

                return role_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        role_permissions = _parse_role_permissions(d.pop("role_permissions", UNSET))


        gcp_role_permission_and_denials = cls(
            role_denials=role_denials,
            role_permissions=role_permissions,
        )


        gcp_role_permission_and_denials.additional_properties = d
        return gcp_role_permission_and_denials

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
