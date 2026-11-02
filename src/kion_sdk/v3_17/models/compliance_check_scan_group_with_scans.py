from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_check_scan import ComplianceCheckScan
  from ..models.compliance_check_scan_group import ComplianceCheckScanGroup





T = TypeVar("T", bound="ComplianceCheckScanGroupWithScans")



@_attrs_define
class ComplianceCheckScanGroupWithScans:
    """ ComplianceCheckScanGroupWithScans defines a Compliance Check Scan Group with its scans

        Attributes:
            compliance_check_scan_group (ComplianceCheckScanGroup | Unset): ComplianceCheckScanGroup defines a Compliance
                Check Scan Group.
            compliance_check_scans (list[ComplianceCheckScan] | None | Unset): List of Compliance Check Scans within a
                group.
     """

    compliance_check_scan_group: ComplianceCheckScanGroup | Unset = UNSET
    compliance_check_scans: list[ComplianceCheckScan] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check_scan import ComplianceCheckScan
        from ..models.compliance_check_scan_group import ComplianceCheckScanGroup
        compliance_check_scan_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compliance_check_scan_group, Unset):
            compliance_check_scan_group = self.compliance_check_scan_group.to_dict()

        compliance_check_scans: list[dict[str, Any]] | None | Unset
        if isinstance(self.compliance_check_scans, Unset):
            compliance_check_scans = UNSET
        elif isinstance(self.compliance_check_scans, list):
            compliance_check_scans = []
            for compliance_check_scans_type_0_item_data in self.compliance_check_scans:
                compliance_check_scans_type_0_item = compliance_check_scans_type_0_item_data.to_dict()
                compliance_check_scans.append(compliance_check_scans_type_0_item)


        else:
            compliance_check_scans = self.compliance_check_scans


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if compliance_check_scan_group is not UNSET:
            field_dict["compliance_check_scan_group"] = compliance_check_scan_group
        if compliance_check_scans is not UNSET:
            field_dict["compliance_check_scans"] = compliance_check_scans

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check_scan import ComplianceCheckScan
        from ..models.compliance_check_scan_group import ComplianceCheckScanGroup
        d = dict(src_dict)
        _compliance_check_scan_group = d.pop("compliance_check_scan_group", UNSET)
        compliance_check_scan_group: ComplianceCheckScanGroup | Unset
        if isinstance(_compliance_check_scan_group,  Unset):
            compliance_check_scan_group = UNSET
        else:
            compliance_check_scan_group = ComplianceCheckScanGroup.from_dict(_compliance_check_scan_group)




        def _parse_compliance_check_scans(data: object) -> list[ComplianceCheckScan] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_check_scans_type_0 = []
                _compliance_check_scans_type_0 = data
                for compliance_check_scans_type_0_item_data in (_compliance_check_scans_type_0):
                    compliance_check_scans_type_0_item = ComplianceCheckScan.from_dict(compliance_check_scans_type_0_item_data)



                    compliance_check_scans_type_0.append(compliance_check_scans_type_0_item)

                return compliance_check_scans_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceCheckScan] | None | Unset, data)

        compliance_check_scans = _parse_compliance_check_scans(d.pop("compliance_check_scans", UNSET))


        compliance_check_scan_group_with_scans = cls(
            compliance_check_scan_group=compliance_check_scan_group,
            compliance_check_scans=compliance_check_scans,
        )


        compliance_check_scan_group_with_scans.additional_properties = d
        return compliance_check_scan_group_with_scans

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
