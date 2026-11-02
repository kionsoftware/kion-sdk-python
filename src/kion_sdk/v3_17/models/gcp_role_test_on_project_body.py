from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GCPRoleTestOnProjectBody")



@_attrs_define
class GCPRoleTestOnProjectBody:
    """ GCPRoleTestOnProjectBody defines the parameters needed to verify a set of IAM Permissions

        Attributes:
            role_permissions (list[str] | None): List of GCP Permissions to validate Example: ['iam.roles.get',
                'iam.roles.list'].
     """

    role_permissions: list[str] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        role_permissions: list[str] | None
        if isinstance(self.role_permissions, list):
            role_permissions = self.role_permissions


        else:
            role_permissions = self.role_permissions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "role_permissions": role_permissions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_role_permissions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_permissions_type_0 = cast(list[str], data)

                return role_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        role_permissions = _parse_role_permissions(d.pop("role_permissions"))


        gcp_role_test_on_project_body = cls(
            role_permissions=role_permissions,
        )


        gcp_role_test_on_project_body.additional_properties = d
        return gcp_role_test_on_project_body

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
