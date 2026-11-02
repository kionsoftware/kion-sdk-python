from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UGroupUpdatable")



@_attrs_define
class UGroupUpdatable:
    """ UGroupUpdatable defines a user group update.

        Attributes:
            description (str | Unset): Description for the user group in the application. Example: This group contains the
                users on the development team..
            idms_id (int | None | Unset): ID of the IDMS where the user group is located. Example: 1.
            name (str | Unset): Name of the user group in the application. Example: development-team.
     """

    description: str | Unset = UNSET
    idms_id: int | None | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

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
        if description is not UNSET:
            field_dict["description"] = description
        if idms_id is not UNSET:
            field_dict["idms_id"] = idms_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        def _parse_idms_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idms_id = _parse_idms_id(d.pop("idms_id", UNSET))


        name = d.pop("name", UNSET)

        u_group_updatable = cls(
            description=description,
            idms_id=idms_id,
            name=name,
        )


        u_group_updatable.additional_properties = d
        return u_group_updatable

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
