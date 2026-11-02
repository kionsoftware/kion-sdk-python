from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.app_role_permission import AppRolePermission





T = TypeVar("T", bound="PermissionSchemeCreate")



@_attrs_define
class PermissionSchemeCreate:
    """ PermissionSchemeCreate defines a permission scheme creation.

        Attributes:
            name (str): Name of the permission scheme in the application. Example: IRAD project permission scheme.
            type_ (str): Specifies the type of policy. Options are: global, ou, project, or funding_source. Example:
                project.
            roles (list[AppRolePermission] | None | Unset):
     """

    name: str
    type_: str
    roles: list[AppRolePermission] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.app_role_permission import AppRolePermission
        name = self.name

        type_ = self.type_

        roles: list[dict[str, Any]] | None | Unset
        if isinstance(self.roles, Unset):
            roles = UNSET
        elif isinstance(self.roles, list):
            roles = []
            for roles_type_0_item_data in self.roles:
                roles_type_0_item = roles_type_0_item_data.to_dict()
                roles.append(roles_type_0_item)


        else:
            roles = self.roles


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "type": type_,
        })
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_role_permission import AppRolePermission
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_roles(data: object) -> list[AppRolePermission] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = []
                _roles_type_0 = data
                for roles_type_0_item_data in (_roles_type_0):
                    roles_type_0_item = AppRolePermission.from_dict(roles_type_0_item_data)



                    roles_type_0.append(roles_type_0_item)

                return roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AppRolePermission] | None | Unset, data)

        roles = _parse_roles(d.pop("roles", UNSET))


        permission_scheme_create = cls(
            name=name,
            type_=type_,
            roles=roles,
        )


        permission_scheme_create.additional_properties = d
        return permission_scheme_create

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
