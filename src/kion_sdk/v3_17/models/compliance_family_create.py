from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceFamilyCreate")



@_attrs_define
class ComplianceFamilyCreate:
    """ 
        Attributes:
            compliance_program_id (int | None): ComplianceProgramID of the compliance family. Example: 1.
            name (str): Name of the compliance family in the application. Example: New Compliance Family.
            description (str | Unset): Description for the compliance family in the application. Example: This is a new
                compliance family..
     """

    compliance_program_id: int | None
    name: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        compliance_program_id: int | None
        compliance_program_id = self.compliance_program_id

        name = self.name

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "compliance_program_id": compliance_program_id,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_compliance_program_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        compliance_program_id = _parse_compliance_program_id(d.pop("compliance_program_id"))


        name = d.pop("name")

        description = d.pop("description", UNSET)

        compliance_family_create = cls(
            compliance_program_id=compliance_program_id,
            name=name,
            description=description,
        )


        compliance_family_create.additional_properties = d
        return compliance_family_create

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
