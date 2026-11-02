from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_check_scan_data import ComplianceCheckScanData





T = TypeVar("T", bound="ComplianceCheckScanCreate")



@_attrs_define
class ComplianceCheckScanCreate:
    """ ComplianceCheckScanCreate defines a Compliance Check Scan Array Creation.

        Attributes:
            account_number (str): AccountNumber for the Check Scan in the application. Example: 1.
            compliance_check_id (int | None): ComplianceCheckID of a compliance check in the application. Example: 1.
            resource_name (str): ResourceName for the Compliance Check Scan Finding in the application. Example: vol-
                xxxxxxxxxxxxxxxxx.
            resource_type (str): ResourceType for the Compliance Check Scan Finding in the application. Example: EC2.
            scan_started_at (float): ScanStartedAt for the Check Scan in the application in Epoch. Example: 1584126884.
            compliance_check_scan_group_id (int | None | Unset): ComplianceCheckScanGroupID for the Check Scan in the
                application Example: 1.
            data_json (ComplianceCheckScanData | Unset): ComplianceCheckScanData defines Compliance Check Scan Finding Data.
            region (str | Unset): Region for the Check Scan in the application. Example: us-east-1.
            resource_group_name (str | Unset): ResourceGroupName that is within the subscription ID (AccountNumber). Only
                applicable and required for Azure Accounts that is a resource group. Example: resource-group-name.
            scan_finished_at (float | Unset): ScanFinishedAt for the Check Scan in the application in Epoch. Example:
                1584126887.
     """

    account_number: str
    compliance_check_id: int | None
    resource_name: str
    resource_type: str
    scan_started_at: float
    compliance_check_scan_group_id: int | None | Unset = UNSET
    data_json: ComplianceCheckScanData | Unset = UNSET
    region: str | Unset = UNSET
    resource_group_name: str | Unset = UNSET
    scan_finished_at: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check_scan_data import ComplianceCheckScanData
        account_number = self.account_number

        compliance_check_id: int | None
        compliance_check_id = self.compliance_check_id

        resource_name = self.resource_name

        resource_type = self.resource_type

        scan_started_at = self.scan_started_at

        compliance_check_scan_group_id: int | None | Unset
        if isinstance(self.compliance_check_scan_group_id, Unset):
            compliance_check_scan_group_id = UNSET
        else:
            compliance_check_scan_group_id = self.compliance_check_scan_group_id

        data_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_json, Unset):
            data_json = self.data_json.to_dict()

        region = self.region

        resource_group_name = self.resource_group_name

        scan_finished_at = self.scan_finished_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_number": account_number,
            "compliance_check_id": compliance_check_id,
            "resource_name": resource_name,
            "resource_type": resource_type,
            "scan_started_at": scan_started_at,
        })
        if compliance_check_scan_group_id is not UNSET:
            field_dict["compliance_check_scan_group_id"] = compliance_check_scan_group_id
        if data_json is not UNSET:
            field_dict["data_json"] = data_json
        if region is not UNSET:
            field_dict["region"] = region
        if resource_group_name is not UNSET:
            field_dict["resource_group_name"] = resource_group_name
        if scan_finished_at is not UNSET:
            field_dict["scan_finished_at"] = scan_finished_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check_scan_data import ComplianceCheckScanData
        d = dict(src_dict)
        account_number = d.pop("account_number")

        def _parse_compliance_check_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        compliance_check_id = _parse_compliance_check_id(d.pop("compliance_check_id"))


        resource_name = d.pop("resource_name")

        resource_type = d.pop("resource_type")

        scan_started_at = d.pop("scan_started_at")

        def _parse_compliance_check_scan_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_check_scan_group_id = _parse_compliance_check_scan_group_id(d.pop("compliance_check_scan_group_id", UNSET))


        _data_json = d.pop("data_json", UNSET)
        data_json: ComplianceCheckScanData | Unset
        if isinstance(_data_json,  Unset):
            data_json = UNSET
        else:
            data_json = ComplianceCheckScanData.from_dict(_data_json)




        region = d.pop("region", UNSET)

        resource_group_name = d.pop("resource_group_name", UNSET)

        scan_finished_at = d.pop("scan_finished_at", UNSET)

        compliance_check_scan_create = cls(
            account_number=account_number,
            compliance_check_id=compliance_check_id,
            resource_name=resource_name,
            resource_type=resource_type,
            scan_started_at=scan_started_at,
            compliance_check_scan_group_id=compliance_check_scan_group_id,
            data_json=data_json,
            region=region,
            resource_group_name=resource_group_name,
            scan_finished_at=scan_finished_at,
        )


        compliance_check_scan_create.additional_properties = d
        return compliance_check_scan_create

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
