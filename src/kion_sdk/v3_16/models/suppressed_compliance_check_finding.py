from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SuppressedComplianceCheckFinding")



@_attrs_define
class SuppressedComplianceCheckFinding:
    """ SuppressedComplianceCheckFinding defines a Suppressed Compliance Check Finding.

        Attributes:
            account_id (int | None | Unset): Account ID of the Suppressed Compliance Check Scan Finding in the application.
                Example: 1.
            compliance_check_id (int | None | Unset): Compliance Check ID of the Suppressed Compliance Check Scan Finding in
                the application. Example: 1.
            compliance_standard_cloud_rule_id (int | None | Unset): Compliance Standard Cloud Rule ID of the Suppressed
                Compliance Check Scan Finding in the application. Example: 1.
            compliance_standard_resource_policy_id (int | None | Unset): Compliance Standard Resource Policy ID of the
                Suppressed Compliance Check Scan Finding in the application. Example: 1.
            created_at (str | Unset): Date when the finding was made. Example: 2019-02-12T22:57:10+0000.
            id (int | Unset): ID of the suppressed check scan finding in the application. Example: 1.
            resource_name (str | Unset): ResourceName for the Compliance Check Scan Finding in the application. Example:
                vol-xxxxxxxxxxxxxxxxx.
            resource_type (str | Unset): ResourceType for the Compliance Check Scan Finding in the application. Example:
                EC2.
            suppression_timeout_at (str | Unset): Date when the finding will be automatically unsuppressed. Example:
                2019-02-12T22:57:10+0000.
            user_id (int | None | Unset): User ID of the Suppressed Compliance Check Scan Finding in the application.
                Example: 1.
     """

    account_id: int | None | Unset = UNSET
    compliance_check_id: int | None | Unset = UNSET
    compliance_standard_cloud_rule_id: int | None | Unset = UNSET
    compliance_standard_resource_policy_id: int | None | Unset = UNSET
    created_at: str | Unset = UNSET
    id: int | Unset = UNSET
    resource_name: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    suppression_timeout_at: str | Unset = UNSET
    user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
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

        compliance_standard_cloud_rule_id: int | None | Unset
        if isinstance(self.compliance_standard_cloud_rule_id, Unset):
            compliance_standard_cloud_rule_id = UNSET
        else:
            compliance_standard_cloud_rule_id = self.compliance_standard_cloud_rule_id

        compliance_standard_resource_policy_id: int | None | Unset
        if isinstance(self.compliance_standard_resource_policy_id, Unset):
            compliance_standard_resource_policy_id = UNSET
        else:
            compliance_standard_resource_policy_id = self.compliance_standard_resource_policy_id

        created_at = self.created_at

        id = self.id

        resource_name = self.resource_name

        resource_type = self.resource_type

        suppression_timeout_at = self.suppression_timeout_at

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if compliance_check_id is not UNSET:
            field_dict["compliance_check_id"] = compliance_check_id
        if compliance_standard_cloud_rule_id is not UNSET:
            field_dict["compliance_standard_cloud_rule_id"] = compliance_standard_cloud_rule_id
        if compliance_standard_resource_policy_id is not UNSET:
            field_dict["compliance_standard_resource_policy_id"] = compliance_standard_resource_policy_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if suppression_timeout_at is not UNSET:
            field_dict["suppression_timeout_at"] = suppression_timeout_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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


        def _parse_compliance_standard_cloud_rule_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_standard_cloud_rule_id = _parse_compliance_standard_cloud_rule_id(d.pop("compliance_standard_cloud_rule_id", UNSET))


        def _parse_compliance_standard_resource_policy_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_standard_resource_policy_id = _parse_compliance_standard_resource_policy_id(d.pop("compliance_standard_resource_policy_id", UNSET))


        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        resource_name = d.pop("resource_name", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        suppression_timeout_at = d.pop("suppression_timeout_at", UNSET)

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        suppressed_compliance_check_finding = cls(
            account_id=account_id,
            compliance_check_id=compliance_check_id,
            compliance_standard_cloud_rule_id=compliance_standard_cloud_rule_id,
            compliance_standard_resource_policy_id=compliance_standard_resource_policy_id,
            created_at=created_at,
            id=id,
            resource_name=resource_name,
            resource_type=resource_type,
            suppression_timeout_at=suppression_timeout_at,
            user_id=user_id,
        )


        suppressed_compliance_check_finding.additional_properties = d
        return suppressed_compliance_check_finding

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
