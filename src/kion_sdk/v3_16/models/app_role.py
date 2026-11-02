from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AppRole")



@_attrs_define
class AppRole:
    """ AppRole defines an App role metadata.

        Attributes:
            disabled (bool | None | Unset): Disabled whether the role has been disabled. Example: True.
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the role in the application. Example: GitHub Development.
            system_managed (bool | None | Unset): SystemManaged whether the role is managed by the system. Example: True.
     """

    disabled: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    system_managed: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        disabled: bool | None | Unset
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        id = self.id

        name = self.name

        system_managed: bool | None | Unset
        if isinstance(self.system_managed, Unset):
            system_managed = UNSET
        else:
            system_managed = self.system_managed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if system_managed is not UNSET:
            field_dict["system_managed"] = system_managed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))


        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_system_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed = _parse_system_managed(d.pop("system_managed", UNSET))


        app_role = cls(
            disabled=disabled,
            id=id,
            name=name,
            system_managed=system_managed,
        )


        app_role.additional_properties = d
        return app_role

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
