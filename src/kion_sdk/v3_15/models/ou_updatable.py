from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OUUpdatable")



@_attrs_define
class OUUpdatable:
    """ OUUpdatable defines an OU update.

        Attributes:
            permission_scheme_id (int | None): ID of the permission scheme applied to the ou. Example: 2.
            description (str | Unset): Description for the OU in the application. Example: Internal research and development
                of cloud applications..
            name (str | Unset): Name of the OU in the application. Example: Research and Development.
     """

    permission_scheme_id: int | None
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        permission_scheme_id: int | None
        permission_scheme_id = self.permission_scheme_id

        description = self.description

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "permission_scheme_id": permission_scheme_id,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_permission_scheme_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        permission_scheme_id = _parse_permission_scheme_id(d.pop("permission_scheme_id"))


        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        ou_updatable = cls(
            permission_scheme_id=permission_scheme_id,
            description=description,
            name=name,
        )


        ou_updatable.additional_properties = d
        return ou_updatable

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
