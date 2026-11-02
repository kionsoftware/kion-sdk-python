from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AppRoleArrayPermission")



@_attrs_define
class AppRoleArrayPermission:
    """ 
        Attributes:
            permission_id (int | None): ID of the permission within the application that will be assigned to the role.
                Example: 1.
            role_ids (list[int] | None): IDs of the role within the application that will have the specified permission.
                Example: [1, 2, 3].
     """

    permission_id: int | None
    role_ids: list[int] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        permission_id: int | None
        permission_id = self.permission_id

        role_ids: list[int] | None
        if isinstance(self.role_ids, list):
            role_ids = self.role_ids


        else:
            role_ids = self.role_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "permission_id": permission_id,
            "role_ids": role_ids,
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


        def _parse_role_ids(data: object) -> list[int] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_ids_type_0 = cast(list[int], data)

                return role_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None, data)

        role_ids = _parse_role_ids(d.pop("role_ids"))


        app_role_array_permission = cls(
            permission_id=permission_id,
            role_ids=role_ids,
        )


        app_role_array_permission.additional_properties = d
        return app_role_array_permission

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
