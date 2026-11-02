from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceCheckScanGroup")



@_attrs_define
class ComplianceCheckScanGroup:
    """ ComplianceCheckScanGroup defines a Compliance Check Scan Group.

        Attributes:
            compliance_check_id (int | None | Unset): ComplianceCheckID of the Compliance Check in the application. Example:
                1.
            id (int | Unset): ID of the check scan group in the application. Example: 1.
     """

    compliance_check_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        compliance_check_id: int | None | Unset
        if isinstance(self.compliance_check_id, Unset):
            compliance_check_id = UNSET
        else:
            compliance_check_id = self.compliance_check_id

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if compliance_check_id is not UNSET:
            field_dict["compliance_check_id"] = compliance_check_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_compliance_check_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_check_id = _parse_compliance_check_id(d.pop("compliance_check_id", UNSET))


        id = d.pop("id", UNSET)

        compliance_check_scan_group = cls(
            compliance_check_id=compliance_check_id,
            id=id,
        )


        compliance_check_scan_group.additional_properties = d
        return compliance_check_scan_group

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
