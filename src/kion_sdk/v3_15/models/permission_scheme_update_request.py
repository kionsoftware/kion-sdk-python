from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.app_role_array_permission import AppRoleArrayPermission
  from ..models.permission_scheme_to_update import PermissionSchemeToUpdate





T = TypeVar("T", bound="PermissionSchemeUpdateRequest")



@_attrs_define
class PermissionSchemeUpdateRequest:
    """ 
        Attributes:
            app_policy (PermissionSchemeToUpdate | Unset): PermissionSchemeToUpdate defines a permission scheme for update.
            permission_roles (list[AppRoleArrayPermission] | None | Unset):
     """

    app_policy: PermissionSchemeToUpdate | Unset = UNSET
    permission_roles: list[AppRoleArrayPermission] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.app_role_array_permission import AppRoleArrayPermission
        from ..models.permission_scheme_to_update import PermissionSchemeToUpdate
        app_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_policy, Unset):
            app_policy = self.app_policy.to_dict()

        permission_roles: list[dict[str, Any]] | None | Unset
        if isinstance(self.permission_roles, Unset):
            permission_roles = UNSET
        elif isinstance(self.permission_roles, list):
            permission_roles = []
            for permission_roles_type_0_item_data in self.permission_roles:
                permission_roles_type_0_item = permission_roles_type_0_item_data.to_dict()
                permission_roles.append(permission_roles_type_0_item)


        else:
            permission_roles = self.permission_roles


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if app_policy is not UNSET:
            field_dict["app_policy"] = app_policy
        if permission_roles is not UNSET:
            field_dict["permission_roles"] = permission_roles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_role_array_permission import AppRoleArrayPermission
        from ..models.permission_scheme_to_update import PermissionSchemeToUpdate
        d = dict(src_dict)
        _app_policy = d.pop("app_policy", UNSET)
        app_policy: PermissionSchemeToUpdate | Unset
        if isinstance(_app_policy,  Unset):
            app_policy = UNSET
        else:
            app_policy = PermissionSchemeToUpdate.from_dict(_app_policy)




        def _parse_permission_roles(data: object) -> list[AppRoleArrayPermission] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permission_roles_type_0 = []
                _permission_roles_type_0 = data
                for permission_roles_type_0_item_data in (_permission_roles_type_0):
                    permission_roles_type_0_item = AppRoleArrayPermission.from_dict(permission_roles_type_0_item_data)



                    permission_roles_type_0.append(permission_roles_type_0_item)

                return permission_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AppRoleArrayPermission] | None | Unset, data)

        permission_roles = _parse_permission_roles(d.pop("permission_roles", UNSET))


        permission_scheme_update_request = cls(
            app_policy=app_policy,
            permission_roles=permission_roles,
        )


        permission_scheme_update_request.additional_properties = d
        return permission_scheme_update_request

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
