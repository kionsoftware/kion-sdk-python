from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PermissionScheme")



@_attrs_define
class PermissionScheme:
    """ PermissionScheme defines a permission scheme.

        Attributes:
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the permission scheme in the application. Example: IRAD project permission scheme.
            system_managed (bool | None | Unset): True if this permission scheme came with and is updated by the
                application.
            type_ (str | Unset): Specifies the type of policy. Options are: global, ou, project, or funding_source. Example:
                project.
     """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    system_managed: bool | None | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        system_managed: bool | None | Unset
        if isinstance(self.system_managed, Unset):
            system_managed = UNSET
        else:
            system_managed = self.system_managed

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if system_managed is not UNSET:
            field_dict["system_managed"] = system_managed
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_system_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed = _parse_system_managed(d.pop("system_managed", UNSET))


        type_ = d.pop("type", UNSET)

        permission_scheme = cls(
            id=id,
            name=name,
            system_managed=system_managed,
            type_=type_,
        )


        permission_scheme.additional_properties = d
        return permission_scheme

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
