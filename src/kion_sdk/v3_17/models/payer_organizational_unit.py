from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PayerOrganizationalUnit")



@_attrs_define
class PayerOrganizationalUnit:
    """ PayerOrganizationalUnit represents an organizational unit in an AWS payer's organization.

        Attributes:
            name (str | Unset): Name of the organizational unit in aws. Example: MyAWSOrg.
            org_unit_id (str | Unset): OUID is id of the aws organization Example: 1234567890.
     """

    name: str | Unset = UNSET
    org_unit_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        org_unit_id = self.org_unit_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if org_unit_id is not UNSET:
            field_dict["org_unit_id"] = org_unit_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        org_unit_id = d.pop("org_unit_id", UNSET)

        payer_organizational_unit = cls(
            name=name,
            org_unit_id=org_unit_id,
        )


        payer_organizational_unit.additional_properties = d
        return payer_organizational_unit

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
