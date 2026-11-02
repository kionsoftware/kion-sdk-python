from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ou_cloud_access_role import OUCloudAccessRole
  from ..models.project_cloud_access_role import ProjectCloudAccessRole





T = TypeVar("T", bound="CloudAccessRoles")



@_attrs_define
class CloudAccessRoles:
    """ CloudAccessRoles defines all local and inherited cloud access roles visible to a user.

        Attributes:
            ou_cloud_access_roles (list[OUCloudAccessRole] | None | Unset):
            project_cloud_access_roles (list[ProjectCloudAccessRole] | None | Unset):
     """

    ou_cloud_access_roles: list[OUCloudAccessRole] | None | Unset = UNSET
    project_cloud_access_roles: list[ProjectCloudAccessRole] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ou_cloud_access_role import OUCloudAccessRole
        from ..models.project_cloud_access_role import ProjectCloudAccessRole
        ou_cloud_access_roles: list[dict[str, Any]] | None | Unset
        if isinstance(self.ou_cloud_access_roles, Unset):
            ou_cloud_access_roles = UNSET
        elif isinstance(self.ou_cloud_access_roles, list):
            ou_cloud_access_roles = []
            for ou_cloud_access_roles_type_0_item_data in self.ou_cloud_access_roles:
                ou_cloud_access_roles_type_0_item = ou_cloud_access_roles_type_0_item_data.to_dict()
                ou_cloud_access_roles.append(ou_cloud_access_roles_type_0_item)


        else:
            ou_cloud_access_roles = self.ou_cloud_access_roles

        project_cloud_access_roles: list[dict[str, Any]] | None | Unset
        if isinstance(self.project_cloud_access_roles, Unset):
            project_cloud_access_roles = UNSET
        elif isinstance(self.project_cloud_access_roles, list):
            project_cloud_access_roles = []
            for project_cloud_access_roles_type_0_item_data in self.project_cloud_access_roles:
                project_cloud_access_roles_type_0_item = project_cloud_access_roles_type_0_item_data.to_dict()
                project_cloud_access_roles.append(project_cloud_access_roles_type_0_item)


        else:
            project_cloud_access_roles = self.project_cloud_access_roles


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ou_cloud_access_roles is not UNSET:
            field_dict["ou_cloud_access_roles"] = ou_cloud_access_roles
        if project_cloud_access_roles is not UNSET:
            field_dict["project_cloud_access_roles"] = project_cloud_access_roles

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ou_cloud_access_role import OUCloudAccessRole
        from ..models.project_cloud_access_role import ProjectCloudAccessRole
        d = dict(src_dict)
        def _parse_ou_cloud_access_roles(data: object) -> list[OUCloudAccessRole] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ou_cloud_access_roles_type_0 = []
                _ou_cloud_access_roles_type_0 = data
                for ou_cloud_access_roles_type_0_item_data in (_ou_cloud_access_roles_type_0):
                    ou_cloud_access_roles_type_0_item = OUCloudAccessRole.from_dict(ou_cloud_access_roles_type_0_item_data)



                    ou_cloud_access_roles_type_0.append(ou_cloud_access_roles_type_0_item)

                return ou_cloud_access_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OUCloudAccessRole] | None | Unset, data)

        ou_cloud_access_roles = _parse_ou_cloud_access_roles(d.pop("ou_cloud_access_roles", UNSET))


        def _parse_project_cloud_access_roles(data: object) -> list[ProjectCloudAccessRole] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_cloud_access_roles_type_0 = []
                _project_cloud_access_roles_type_0 = data
                for project_cloud_access_roles_type_0_item_data in (_project_cloud_access_roles_type_0):
                    project_cloud_access_roles_type_0_item = ProjectCloudAccessRole.from_dict(project_cloud_access_roles_type_0_item_data)



                    project_cloud_access_roles_type_0.append(project_cloud_access_roles_type_0_item)

                return project_cloud_access_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProjectCloudAccessRole] | None | Unset, data)

        project_cloud_access_roles = _parse_project_cloud_access_roles(d.pop("project_cloud_access_roles", UNSET))


        cloud_access_roles = cls(
            ou_cloud_access_roles=ou_cloud_access_roles,
            project_cloud_access_roles=project_cloud_access_roles,
        )


        cloud_access_roles.additional_properties = d
        return cloud_access_roles

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
