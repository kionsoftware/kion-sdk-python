from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceCheckUpdate")



@_attrs_define
class ComplianceCheckUpdate:
    """ ComplianceCheckUpdate defines a Compliance Check update.

        Attributes:
            regions (list[str] | None): List of the AWS regions where the compliance check applies Example: ['us-east-1'].
            azure_policy_id (int | None | Unset): AzurePolicyID refers to the ID of the Azure Policy that you want to change
                this check to. Set to 0
                to clear the policy ID. Example: 1.
            body (str | Unset): TODO: add a valid example here
                Body of the Compliance Check defining what actions will be run.
            cloud_provider_id (int | None | Unset): CloudProviderID for the Compliance Check in the application.
                1 - AWS.
                2 - Microsoft. Example: 1.
            compliance_check_type_id (int | None | Unset): ComplianceCheckTypeID for the Compliance Check in the
                application.
                1 - External. These checks are not triggered by cloudtamer.io, but rather can display findings from checks run
                outside of cloudtamer.io.
                2 - Cloud Custodian. These checks are run by cloudtamer.io using Cloud Custodian.
                3 - Azure Policy. These checks are scraped from Azure's policy reporting engine and apply Azure Policies to
                accounts. Example: 1.
            description (str | Unset): Description for the Compliance Check in the application. Example: The NIST SP 800-53
                provides a catalog of controls that support the development of secure and resilient federal information
                systems..
            frequency_minutes (int | Unset): FrequencyMinutes defines how often the check will be run. Example: 60.
            frequency_type_id (int | None | Unset): FrequencyTypeID refers to the duration type of the frequency it will be
                checked
                2 - minutes
                3 - hours
                4 - days Example: 2.
            is_all_regions (bool | None | Unset): IsAllRegions determines if the check should be applied to all regions
                applied on the system
            is_auto_archived (bool | None | Unset): IsAutoArchived defines whether existing findings should be archived
                before new findings are reported. Example: True.
            name (str | Unset): Name of the Compliance Check in the application. Example: NIST 800-53.
            severity_type_id (int | None | Unset): SeverityTypeID for the severity level of the compliance check
                1 - Informational.
                2 - Low.
                3 - Medium (Default).
                4 - High. Default: 3. Example: 2.
     """

    regions: list[str] | None
    azure_policy_id: int | None | Unset = UNSET
    body: str | Unset = UNSET
    cloud_provider_id: int | None | Unset = UNSET
    compliance_check_type_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    frequency_minutes: int | Unset = UNSET
    frequency_type_id: int | None | Unset = UNSET
    is_all_regions: bool | None | Unset = UNSET
    is_auto_archived: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    severity_type_id: int | None | Unset = 3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        regions: list[str] | None
        if isinstance(self.regions, list):
            regions = self.regions


        else:
            regions = self.regions

        azure_policy_id: int | None | Unset
        if isinstance(self.azure_policy_id, Unset):
            azure_policy_id = UNSET
        else:
            azure_policy_id = self.azure_policy_id

        body = self.body

        cloud_provider_id: int | None | Unset
        if isinstance(self.cloud_provider_id, Unset):
            cloud_provider_id = UNSET
        else:
            cloud_provider_id = self.cloud_provider_id

        compliance_check_type_id: int | None | Unset
        if isinstance(self.compliance_check_type_id, Unset):
            compliance_check_type_id = UNSET
        else:
            compliance_check_type_id = self.compliance_check_type_id

        description = self.description

        frequency_minutes = self.frequency_minutes

        frequency_type_id: int | None | Unset
        if isinstance(self.frequency_type_id, Unset):
            frequency_type_id = UNSET
        else:
            frequency_type_id = self.frequency_type_id

        is_all_regions: bool | None | Unset
        if isinstance(self.is_all_regions, Unset):
            is_all_regions = UNSET
        else:
            is_all_regions = self.is_all_regions

        is_auto_archived: bool | None | Unset
        if isinstance(self.is_auto_archived, Unset):
            is_auto_archived = UNSET
        else:
            is_auto_archived = self.is_auto_archived

        name = self.name

        severity_type_id: int | None | Unset
        if isinstance(self.severity_type_id, Unset):
            severity_type_id = UNSET
        else:
            severity_type_id = self.severity_type_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "regions": regions,
        })
        if azure_policy_id is not UNSET:
            field_dict["azure_policy_id"] = azure_policy_id
        if body is not UNSET:
            field_dict["body"] = body
        if cloud_provider_id is not UNSET:
            field_dict["cloud_provider_id"] = cloud_provider_id
        if compliance_check_type_id is not UNSET:
            field_dict["compliance_check_type_id"] = compliance_check_type_id
        if description is not UNSET:
            field_dict["description"] = description
        if frequency_minutes is not UNSET:
            field_dict["frequency_minutes"] = frequency_minutes
        if frequency_type_id is not UNSET:
            field_dict["frequency_type_id"] = frequency_type_id
        if is_all_regions is not UNSET:
            field_dict["is_all_regions"] = is_all_regions
        if is_auto_archived is not UNSET:
            field_dict["is_auto_archived"] = is_auto_archived
        if name is not UNSET:
            field_dict["name"] = name
        if severity_type_id is not UNSET:
            field_dict["severity_type_id"] = severity_type_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_regions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                regions_type_0 = cast(list[str], data)

                return regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        regions = _parse_regions(d.pop("regions"))


        def _parse_azure_policy_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        azure_policy_id = _parse_azure_policy_id(d.pop("azure_policy_id", UNSET))


        body = d.pop("body", UNSET)

        def _parse_cloud_provider_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_provider_id = _parse_cloud_provider_id(d.pop("cloud_provider_id", UNSET))


        def _parse_compliance_check_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_check_type_id = _parse_compliance_check_type_id(d.pop("compliance_check_type_id", UNSET))


        description = d.pop("description", UNSET)

        frequency_minutes = d.pop("frequency_minutes", UNSET)

        def _parse_frequency_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        frequency_type_id = _parse_frequency_type_id(d.pop("frequency_type_id", UNSET))


        def _parse_is_all_regions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_all_regions = _parse_is_all_regions(d.pop("is_all_regions", UNSET))


        def _parse_is_auto_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_auto_archived = _parse_is_auto_archived(d.pop("is_auto_archived", UNSET))


        name = d.pop("name", UNSET)

        def _parse_severity_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        severity_type_id = _parse_severity_type_id(d.pop("severity_type_id", UNSET))


        compliance_check_update = cls(
            regions=regions,
            azure_policy_id=azure_policy_id,
            body=body,
            cloud_provider_id=cloud_provider_id,
            compliance_check_type_id=compliance_check_type_id,
            description=description,
            frequency_minutes=frequency_minutes,
            frequency_type_id=frequency_type_id,
            is_all_regions=is_all_regions,
            is_auto_archived=is_auto_archived,
            name=name,
            severity_type_id=severity_type_id,
        )


        compliance_check_update.additional_properties = d
        return compliance_check_update

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
