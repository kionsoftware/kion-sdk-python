from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_check_scan_finding import ComplianceCheckScanFinding





T = TypeVar("T", bound="ComplianceCheckScan")



@_attrs_define
class ComplianceCheckScan:
    """ ComplianceCheckScan defines a Compliance Check Scan.

        Attributes:
            account_id (int | None | Unset): AccountID for the Check Scan in the application. Example: 1.
            compliance_check_id (int | None | Unset): ComplianceCheckID of a compliance check in the application. Example:
                1.
            compliance_check_scan_group_id (int | None | Unset): ComplianceCheckScanGroupID for the Check Scan in the
                application. Example: 1.
            findings (list[ComplianceCheckScanFinding] | None | Unset): Findings defines the compliance check scan findings
            id (int | Unset): ID of the check scan in the application. Example: 1.
            region (str | Unset): Region for the Check Scan in the application. Example: us-east-1.
            scan_finished_at (str | Unset): ScanFinishedAt for the Check Scan in the application in Epoch. Example:
                1584126887.
            scan_started_at (str | Unset): ScanStartedAt for the Check Scan in the application in Epoch. Example:
                1584126884.
     """

    account_id: int | None | Unset = UNSET
    compliance_check_id: int | None | Unset = UNSET
    compliance_check_scan_group_id: int | None | Unset = UNSET
    findings: list[ComplianceCheckScanFinding] | None | Unset = UNSET
    id: int | Unset = UNSET
    region: str | Unset = UNSET
    scan_finished_at: str | Unset = UNSET
    scan_started_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check_scan_finding import ComplianceCheckScanFinding
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        compliance_check_id: int | None | Unset
        if isinstance(self.compliance_check_id, Unset):
            compliance_check_id = UNSET
        else:
            compliance_check_id = self.compliance_check_id

        compliance_check_scan_group_id: int | None | Unset
        if isinstance(self.compliance_check_scan_group_id, Unset):
            compliance_check_scan_group_id = UNSET
        else:
            compliance_check_scan_group_id = self.compliance_check_scan_group_id

        findings: list[dict[str, Any]] | None | Unset
        if isinstance(self.findings, Unset):
            findings = UNSET
        elif isinstance(self.findings, list):
            findings = []
            for findings_type_0_item_data in self.findings:
                findings_type_0_item = findings_type_0_item_data.to_dict()
                findings.append(findings_type_0_item)


        else:
            findings = self.findings

        id = self.id

        region = self.region

        scan_finished_at = self.scan_finished_at

        scan_started_at = self.scan_started_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if compliance_check_id is not UNSET:
            field_dict["compliance_check_id"] = compliance_check_id
        if compliance_check_scan_group_id is not UNSET:
            field_dict["compliance_check_scan_group_id"] = compliance_check_scan_group_id
        if findings is not UNSET:
            field_dict["findings"] = findings
        if id is not UNSET:
            field_dict["id"] = id
        if region is not UNSET:
            field_dict["region"] = region
        if scan_finished_at is not UNSET:
            field_dict["scan_finished_at"] = scan_finished_at
        if scan_started_at is not UNSET:
            field_dict["scan_started_at"] = scan_started_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check_scan_finding import ComplianceCheckScanFinding
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        def _parse_compliance_check_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_check_id = _parse_compliance_check_id(d.pop("compliance_check_id", UNSET))


        def _parse_compliance_check_scan_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_check_scan_group_id = _parse_compliance_check_scan_group_id(d.pop("compliance_check_scan_group_id", UNSET))


        def _parse_findings(data: object) -> list[ComplianceCheckScanFinding] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                findings_type_0 = []
                _findings_type_0 = data
                for findings_type_0_item_data in (_findings_type_0):
                    findings_type_0_item = ComplianceCheckScanFinding.from_dict(findings_type_0_item_data)



                    findings_type_0.append(findings_type_0_item)

                return findings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceCheckScanFinding] | None | Unset, data)

        findings = _parse_findings(d.pop("findings", UNSET))


        id = d.pop("id", UNSET)

        region = d.pop("region", UNSET)

        scan_finished_at = d.pop("scan_finished_at", UNSET)

        scan_started_at = d.pop("scan_started_at", UNSET)

        compliance_check_scan = cls(
            account_id=account_id,
            compliance_check_id=compliance_check_id,
            compliance_check_scan_group_id=compliance_check_scan_group_id,
            findings=findings,
            id=id,
            region=region,
            scan_finished_at=scan_finished_at,
            scan_started_at=scan_started_at,
        )


        compliance_check_scan.additional_properties = d
        return compliance_check_scan

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
