from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PermissionSchemeToUpdate")



@_attrs_define
class PermissionSchemeToUpdate:
    """ PermissionSchemeToUpdate defines a permission scheme for update.

        Attributes:
            id (int): ID of the record you are updating in the application. Example: 1.
            is_default (bool | None | Unset): True if this permission scheme came with and is updated by the application.
            name (str | Unset): Name of the permission scheme in the application. Example: IRAD project permission scheme.
            type_ (str | Unset): Specifies the type of policy. Options are: global, ou, project, or funding_source. Example:
                project.
     """

    id: int
    is_default: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_default: bool | None | Unset
        if isinstance(self.is_default, Unset):
            is_default = UNSET
        else:
            is_default = self.is_default

        name = self.name

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_is_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default = _parse_is_default(d.pop("is_default", UNSET))


        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        permission_scheme_to_update = cls(
            id=id,
            is_default=is_default,
            name=name,
            type_=type_,
        )


        permission_scheme_to_update.additional_properties = d
        return permission_scheme_to_update

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
