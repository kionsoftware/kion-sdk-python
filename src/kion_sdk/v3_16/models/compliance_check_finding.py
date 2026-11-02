from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceCheckFinding")



@_attrs_define
class ComplianceCheckFinding:
    """ ComplianceCheckFinding defines a Compliance Check Finding.

        Attributes:
            account_id (int | None | Unset): AccountID for the finding in the application. Example: 1.
            compliance_check_id (int | None | Unset): ComplianceCheckID of the related compliance check in the application.
                Example: 1.
            hash_identifier (int | Unset): Hash Identifier is used to reference a finding for a particular resource.
                Example: 3298734.
            id (int | Unset): ID of the check scan finding in the application. Example: 1.
            region (str | Unset): Region for the finding in the application. Example: us-east-1.
            resource_name (str | Unset): ResourceName for the Compliance Check Scan Finding in the application. Example:
                vol-xxxxxxxxxxxxxxxxx.
            resource_type (str | Unset): ResourceType for the Compliance Check Scan Finding in the application. Example:
                EC2.
     """

    account_id: int | None | Unset = UNSET
    compliance_check_id: int | None | Unset = UNSET
    hash_identifier: int | Unset = UNSET
    id: int | Unset = UNSET
    region: str | Unset = UNSET
    resource_name: str | Unset = UNSET
    resource_type: str | Unset = UNSET
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

        hash_identifier = self.hash_identifier

        id = self.id

        region = self.region

        resource_name = self.resource_name

        resource_type = self.resource_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if compliance_check_id is not UNSET:
            field_dict["compliance_check_id"] = compliance_check_id
        if hash_identifier is not UNSET:
            field_dict["hash_identifier"] = hash_identifier
        if id is not UNSET:
            field_dict["id"] = id
        if region is not UNSET:
            field_dict["region"] = region
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type

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


        hash_identifier = d.pop("hash_identifier", UNSET)

        id = d.pop("id", UNSET)

        region = d.pop("region", UNSET)

        resource_name = d.pop("resource_name", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        compliance_check_finding = cls(
            account_id=account_id,
            compliance_check_id=compliance_check_id,
            hash_identifier=hash_identifier,
            id=id,
            region=region,
            resource_name=resource_name,
            resource_type=resource_type,
        )


        compliance_check_finding.additional_properties = d
        return compliance_check_finding

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
