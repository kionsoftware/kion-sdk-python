from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AutomationPolicy")



@_attrs_define
class AutomationPolicy:
    """ AutomationPolicy defines an Automation Policy.

        Attributes:
            description (str | Unset): Description for the Automation Policy in the application. Example: This is an example
                automation policy..
            engine (int | Unset): Engine type for the Automation Policy. 0 = Kion, 1 = Cloud Custodian
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the Automation Policy in the application. Example: Example Automation Policy.
     """

    description: str | Unset = UNSET
    engine: int | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        engine = self.engine

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if engine is not UNSET:
            field_dict["engine"] = engine
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        engine = d.pop("engine", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        automation_policy = cls(
            description=description,
            engine=engine,
            id=id,
            name=name,
        )


        automation_policy.additional_properties = d
        return automation_policy

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
