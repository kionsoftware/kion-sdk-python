from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GCPOrganization")



@_attrs_define
class GCPOrganization:
    """ GCPOrganization represents an organization in google cloud

        Attributes:
            display_name (str | Unset): DisplayName is the user-friendly name for an organization Example: mycompany.net.
            id (str | Unset): ID is the numeric identifier for the organization Example: 1026377682360.
            name (str | Unset): ResourceName is the fully qualified gcp resource identifier for the organization Example:
                organizations/1026377682360.
     """

    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        gcp_organization = cls(
            display_name=display_name,
            id=id,
            name=name,
        )


        gcp_organization.additional_properties = d
        return gcp_organization

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
