from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceCheckCreate")



@_attrs_define
class ComplianceCheckCreate:
    """ ComplianceCheckCreate defines a Compliance Check creation.

        Attributes:
            cloud_provider_id (int | None): CloudProviderID for the Compliance Check in the application. Must be "2" for
                Azure Policy checks.
                1 - AWS.
                2 - Microsoft. Example: 1.
            compliance_check_type_id (int | None): ComplianceCheckTypeID for the Compliance Check in the application.
                1 - External. These checks are not triggered by cloudtamer.io, but rather can display findings from checks run
                outside of cloudtamer.io.
                2 - Cloud Custodian. These checks are run by cloudtamer.io using Cloud Custodian.
                3 - Azure Policy. These checks are scraped from Azure's policy reporting engine and apply Azure Policies to
                accounts. Example: 1.
            name (str): Name of the Compliance Check in the application. Example: NIST 800-53.
            azure_policy_id (int | None | Unset): AzurePolicyID refers to the ID of the Azure Policy in cloudtamer.io which
                will be deployed and scraped to determine
                compliance status of Azure resources. Should only be provided for Azure Policy checks. Example: 1.
            body (str | Unset): TODO: add a valid example here
                Body of the Compliance Check defining what actions will be run.
            compliance_control_ids (list[int] | None | Unset): List of Compliance Control IDs to which this Compliance Check
                is linked. Example: [1, 2].
            compliance_standard_id (int | None | Unset): ComplianceStandardID is an optional field for which compliance
                standard the created check should be associated with. Example: 1.
            created_by_user_id (int | None | Unset): CreatedByUserID refers to the User in the application who created the
                Compliance Check. Will be the requesting User's ID if not specified. Example: 1.
            description (str | Unset): Description for the Compliance Check in the application. Example: The NIST SP 800-53
                provides a catalog of controls that support the development of secure and resilient federal information
                systems..
            frequency_minutes (int | Unset): FrequencyMinutes defines how often the check will be run. Is required if check
                type is Cloud Custodian or Azure Policy. Example: 60.
            frequency_type_id (int | None | Unset): FrequencyTypeID refers to the duration type of the frequency it will be
                checked. Is required if check type is Cloud Custodian or Azure Policy.
                2 - minutes
                3 - hours
                4 - days Example: 2.
            is_all_regions (bool | None | Unset): IsAllRegions determines if the check should be applied to all regions
                applied on the system
            is_auto_archived (bool | None | Unset): IsAutoArchived defines whether existing findings should be archived
                before new findings are reported. Example: True.
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the Compliance Check. Is
                required if no owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the Compliance Check. Is required if no
                owner group IDs are listed. Example: [1, 2].
            regions (list[str] | None | Unset): List of the AWS regions where the compliance check applies. Required when
                check type id is cloud custodian. Example: ['us-east-1'].
            severity_type_id (int | None | Unset): SeverityTypeID for the severity level of the compliance check
                1 - Informational.
                2 - Low.
                3 - Medium (Default).
                4 - High. Default: 3. Example: 2.
     """

    cloud_provider_id: int | None
    compliance_check_type_id: int | None
    name: str
    azure_policy_id: int | None | Unset = UNSET
    body: str | Unset = UNSET
    compliance_control_ids: list[int] | None | Unset = UNSET
    compliance_standard_id: int | None | Unset = UNSET
    created_by_user_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    frequency_minutes: int | Unset = UNSET
    frequency_type_id: int | None | Unset = UNSET
    is_all_regions: bool | None | Unset = UNSET
    is_auto_archived: bool | None | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    regions: list[str] | None | Unset = UNSET
    severity_type_id: int | None | Unset = 3
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cloud_provider_id: int | None
        cloud_provider_id = self.cloud_provider_id

        compliance_check_type_id: int | None
        compliance_check_type_id = self.compliance_check_type_id

        name = self.name

        azure_policy_id: int | None | Unset
        if isinstance(self.azure_policy_id, Unset):
            azure_policy_id = UNSET
        else:
            azure_policy_id = self.azure_policy_id

        body = self.body

        compliance_control_ids: list[int] | None | Unset
        if isinstance(self.compliance_control_ids, Unset):
            compliance_control_ids = UNSET
        elif isinstance(self.compliance_control_ids, list):
            compliance_control_ids = self.compliance_control_ids


        else:
            compliance_control_ids = self.compliance_control_ids

        compliance_standard_id: int | None | Unset
        if isinstance(self.compliance_standard_id, Unset):
            compliance_standard_id = UNSET
        else:
            compliance_standard_id = self.compliance_standard_id

        created_by_user_id: int | None | Unset
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

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

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids

        regions: list[str] | None | Unset
        if isinstance(self.regions, Unset):
            regions = UNSET
        elif isinstance(self.regions, list):
            regions = self.regions


        else:
            regions = self.regions

        severity_type_id: int | None | Unset
        if isinstance(self.severity_type_id, Unset):
            severity_type_id = UNSET
        else:
            severity_type_id = self.severity_type_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cloud_provider_id": cloud_provider_id,
            "compliance_check_type_id": compliance_check_type_id,
            "name": name,
        })
        if azure_policy_id is not UNSET:
            field_dict["azure_policy_id"] = azure_policy_id
        if body is not UNSET:
            field_dict["body"] = body
        if compliance_control_ids is not UNSET:
            field_dict["compliance_control_ids"] = compliance_control_ids
        if compliance_standard_id is not UNSET:
            field_dict["compliance_standard_id"] = compliance_standard_id
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
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
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if regions is not UNSET:
            field_dict["regions"] = regions
        if severity_type_id is not UNSET:
            field_dict["severity_type_id"] = severity_type_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cloud_provider_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cloud_provider_id = _parse_cloud_provider_id(d.pop("cloud_provider_id"))


        def _parse_compliance_check_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        compliance_check_type_id = _parse_compliance_check_type_id(d.pop("compliance_check_type_id"))


        name = d.pop("name")

        def _parse_azure_policy_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        azure_policy_id = _parse_azure_policy_id(d.pop("azure_policy_id", UNSET))


        body = d.pop("body", UNSET)

        def _parse_compliance_control_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_control_ids_type_0 = cast(list[int], data)

                return compliance_control_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        compliance_control_ids = _parse_compliance_control_ids(d.pop("compliance_control_ids", UNSET))


        def _parse_compliance_standard_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_standard_id = _parse_compliance_standard_id(d.pop("compliance_standard_id", UNSET))


        def _parse_created_by_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id", UNSET))


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


        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        def _parse_regions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                regions_type_0 = cast(list[str], data)

                return regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        regions = _parse_regions(d.pop("regions", UNSET))


        def _parse_severity_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        severity_type_id = _parse_severity_type_id(d.pop("severity_type_id", UNSET))


        compliance_check_create = cls(
            cloud_provider_id=cloud_provider_id,
            compliance_check_type_id=compliance_check_type_id,
            name=name,
            azure_policy_id=azure_policy_id,
            body=body,
            compliance_control_ids=compliance_control_ids,
            compliance_standard_id=compliance_standard_id,
            created_by_user_id=created_by_user_id,
            description=description,
            frequency_minutes=frequency_minutes,
            frequency_type_id=frequency_type_id,
            is_all_regions=is_all_regions,
            is_auto_archived=is_auto_archived,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            regions=regions,
            severity_type_id=severity_type_id,
        )


        compliance_check_create.additional_properties = d
        return compliance_check_create

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
