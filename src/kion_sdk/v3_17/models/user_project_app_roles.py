from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.app_role import AppRole
  from ..models.project import Project





T = TypeVar("T", bound="UserProjectAppRoles")



@_attrs_define
class UserProjectAppRoles:
    """ UserProjectAppRoles represents the app role a user has on a project.

        Attributes:
            app_roles (list[AppRole] | None | Unset):
            project (Project | Unset): Project defines a project.
     """

    app_roles: list[AppRole] | None | Unset = UNSET
    project: Project | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.app_role import AppRole
        from ..models.project import Project
        app_roles: list[dict[str, Any]] | None | Unset
        if isinstance(self.app_roles, Unset):
            app_roles = UNSET
        elif isinstance(self.app_roles, list):
            app_roles = []
            for app_roles_type_0_item_data in self.app_roles:
                app_roles_type_0_item = app_roles_type_0_item_data.to_dict()
                app_roles.append(app_roles_type_0_item)


        else:
            app_roles = self.app_roles

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if app_roles is not UNSET:
            field_dict["app_roles"] = app_roles
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_role import AppRole
        from ..models.project import Project
        d = dict(src_dict)
        def _parse_app_roles(data: object) -> list[AppRole] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                app_roles_type_0 = []
                _app_roles_type_0 = data
                for app_roles_type_0_item_data in (_app_roles_type_0):
                    app_roles_type_0_item = AppRole.from_dict(app_roles_type_0_item_data)



                    app_roles_type_0.append(app_roles_type_0_item)

                return app_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AppRole] | None | Unset, data)

        app_roles = _parse_app_roles(d.pop("app_roles", UNSET))


        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        user_project_app_roles = cls(
            app_roles=app_roles,
            project=project,
        )


        user_project_app_roles.additional_properties = d
        return user_project_app_roles

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
