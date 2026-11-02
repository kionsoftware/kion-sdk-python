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





T = TypeVar("T", bound="ComplianceCheckScanFindingCreate")



@_attrs_define
class ComplianceCheckScanFindingCreate:
    """ ComplianceCheckScanFindingCreate defines a Compliance Check Scan Finding creation.

        Attributes:
            data_json (ComplianceCheckScanData | Unset): ComplianceCheckScanData defines Compliance Check Scan Finding Data.
            region (str | Unset): Region is for the region where the resource is deployed.
                Only applicable and required for azure when running a scan on an azure compliance check. Example: eastus.
            resource_name (str | Unset): ResourceName for the Compliance Check Scan Finding in the application. Example:
                vol-xxxxxxxxxxxxxxxxx.
            resource_type (str | Unset): ResourceType for the Compliance Check Scan Finding in the application. Example:
                EC2.
     """

    data_json: ComplianceCheckScanData | Unset = UNSET
    region: str | Unset = UNSET
    resource_name: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check_scan_data import ComplianceCheckScanData
        data_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_json, Unset):
            data_json = self.data_json.to_dict()

        region = self.region

        resource_name = self.resource_name

        resource_type = self.resource_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_json is not UNSET:
            field_dict["data_json"] = data_json
        if region is not UNSET:
            field_dict["region"] = region
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check_scan_data import ComplianceCheckScanData
        d = dict(src_dict)
        _data_json = d.pop("data_json", UNSET)
        data_json: ComplianceCheckScanData | Unset
        if isinstance(_data_json,  Unset):
            data_json = UNSET
        else:
            data_json = ComplianceCheckScanData.from_dict(_data_json)




        region = d.pop("region", UNSET)

        resource_name = d.pop("resource_name", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        compliance_check_scan_finding_create = cls(
            data_json=data_json,
            region=region,
            resource_name=resource_name,
            resource_type=resource_type,
        )


        compliance_check_scan_finding_create.additional_properties = d
        return compliance_check_scan_finding_create

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
