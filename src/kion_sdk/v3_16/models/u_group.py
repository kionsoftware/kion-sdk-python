from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UGroup")



@_attrs_define
class UGroup:
    """ UGroup defines a user group.

        Attributes:
            created_at (str | Unset): Date when the user was created in the application. Example: 2019-02-12T22:57:10+0000.
            description (str | Unset): Description for the user group in the application. Example: This group contains the
                users on the development team..
            enabled (bool | None | Unset): Enabled state of the group. Example: True.
            id (int | Unset): ID of the record in the application. Example: 1.
            idms_id (int | None | Unset): ID of the IDMS where the user group is located. Example: 1.
            name (str | Unset): Name of the user group in the application. Example: development-team.
     """

    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    idms_id: int | None | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        id = self.id

        idms_id: int | None | Unset
        if isinstance(self.idms_id, Unset):
            idms_id = UNSET
        else:
            idms_id = self.idms_id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if idms_id is not UNSET:
            field_dict["idms_id"] = idms_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        id = d.pop("id", UNSET)

        def _parse_idms_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idms_id = _parse_idms_id(d.pop("idms_id", UNSET))


        name = d.pop("name", UNSET)

        u_group = cls(
            created_at=created_at,
            description=description,
            enabled=enabled,
            id=id,
            idms_id=idms_id,
            name=name,
        )


        u_group.additional_properties = d
        return u_group

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
