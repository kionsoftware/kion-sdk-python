from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ScopeUpdate")



@_attrs_define
class ScopeUpdate:
    """ ScopeUpdate defines a Scope update.

        Attributes:
            alias (str | Unset): Alias of the scope in the application. Example: GH-Dev.
            description (str | Unset): Description of the scope in the application. Example: This scope includes all
                resources related to development environments..
            name (str | Unset): Name of the scope in the application. Example: GitHub Development.
            project_id (int | None | Unset): ID of the project to move this scope to. Example: 42.
     """

    alias: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        description = self.description

        name = self.name

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alias = d.pop("alias", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        scope_update = cls(
            alias=alias,
            description=description,
            name=name,
            project_id=project_id,
        )


        scope_update.additional_properties = d
        return scope_update

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
