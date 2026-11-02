from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ScopeCreate")



@_attrs_define
class ScopeCreate:
    """ AppRoleCreate defines a Scope creation.

        Attributes:
            name (str): Name of the role in the application. Example: GitHub Development.
            alias (str | Unset): Alias of the scope in the application. Example: GH-Dev.
            criteria (Any | Unset): Criteria for the scope, stored as raw JSON. Example: {'account_id': 1, 'tag':
                'repo:Prod'}.
            description (str | Unset): Description of the scope in the application. Example: This scope includes all
                resources related to development environments..
            end_datecode (int | Unset): End datecode for the scope (YYYYMM format), if applicable. Example: 202512.
            project_id (int | None | Unset): ID of the project associated with this scope. Example: 42.
            start_datecode (int | Unset): Start datecode for the scope (YYYYMM format). Example: 202501.
     """

    name: str
    alias: str | Unset = UNSET
    criteria: Any | Unset = UNSET
    description: str | Unset = UNSET
    end_datecode: int | Unset = UNSET
    project_id: int | None | Unset = UNSET
    start_datecode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        alias = self.alias

        criteria = self.criteria

        description = self.description

        end_datecode = self.end_datecode

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if description is not UNSET:
            field_dict["description"] = description
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        alias = d.pop("alias", UNSET)

        criteria = d.pop("criteria", UNSET)

        description = d.pop("description", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        scope_create = cls(
            name=name,
            alias=alias,
            criteria=criteria,
            description=description,
            end_datecode=end_datecode,
            project_id=project_id,
            start_datecode=start_datecode,
        )


        scope_create.additional_properties = d
        return scope_create

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
