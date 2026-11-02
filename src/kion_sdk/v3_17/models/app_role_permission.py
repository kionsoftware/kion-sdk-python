from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AppRolePermission")



@_attrs_define
class AppRolePermission:
    """ AppRolePermission defines a permission role mapping.

        Attributes:
            permission_id (int | None): ID of the permission within the application that will be assigned to the role.
                Example: 1.
            role_id (int | None): ID of the role within the application that will have the specified permission. Example: 1.
     """

    permission_id: int | None
    role_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        permission_id: int | None
        permission_id = self.permission_id

        role_id: int | None
        role_id = self.role_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "permission_id": permission_id,
            "role_id": role_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_permission_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        permission_id = _parse_permission_id(d.pop("permission_id"))


        def _parse_role_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        role_id = _parse_role_id(d.pop("role_id"))


        app_role_permission = cls(
            permission_id=permission_id,
            role_id=role_id,
        )


        app_role_permission.additional_properties = d
        return app_role_permission

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
