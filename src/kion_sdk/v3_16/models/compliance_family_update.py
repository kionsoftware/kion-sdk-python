from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceFamilyUpdate")



@_attrs_define
class ComplianceFamilyUpdate:
    """ ComplianceFamilyUpdate defines the fields that can be updated for a compliance family.

        Attributes:
            compliance_program_id (int | None | Unset): ComplianceProgramID of the compliance family. Example: 2.
            description (str | Unset): Description for the compliance family in the application. Example: This is an updated
                compliance family..
            name (str | Unset): Name of the compliance family in the application. Example: Updated Compliance Family.
     """

    compliance_program_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        compliance_program_id: int | None | Unset
        if isinstance(self.compliance_program_id, Unset):
            compliance_program_id = UNSET
        else:
            compliance_program_id = self.compliance_program_id

        description = self.description

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if compliance_program_id is not UNSET:
            field_dict["compliance_program_id"] = compliance_program_id
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_compliance_program_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_program_id = _parse_compliance_program_id(d.pop("compliance_program_id", UNSET))


        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        compliance_family_update = cls(
            compliance_program_id=compliance_program_id,
            description=description,
            name=name,
        )


        compliance_family_update.additional_properties = d
        return compliance_family_update

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
