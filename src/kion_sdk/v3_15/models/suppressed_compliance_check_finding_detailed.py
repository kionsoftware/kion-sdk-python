from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.suppressed_compliance_check_finding import SuppressedComplianceCheckFinding





T = TypeVar("T", bound="SuppressedComplianceCheckFindingDetailed")



@_attrs_define
class SuppressedComplianceCheckFindingDetailed:
    """ SuppressedComplianceCheckFindingDetailed defines a Compliance Check Scan Finding that has been suppressed.

        Attributes:
            account_name (str | Unset): Name of the account in the application. Example: Tech Project 1.
            account_number (str | Unset): AWS account number. Example: 121212121212.
            check_id (int | None | Unset): ID of the compliance check in the application. Example: 1.
            check_name (str | Unset): Name of the check in the application. Example: public-s3.
            finding_created_at (str | Unset): Date when the finding was made. Example: 2019-02-12T22:57:10+0000.
            hash_identifier (int | Unset): Hash Identifier is used to reference a finding for a particular resource.
                Example: 3298734.
            parent_ou_id (int | None | Unset): ID of the parent OU in the application. Example: 1.
            parent_ou_name (str | Unset): Name of the parent OU in the application. Example: Tech Project 1.
            project_id (int | None | Unset): ID of the project in the application. Example: 1.
            project_name (str | Unset): Name of the Project in the application. Example: Tech Project 1.
            region (str | Unset): Region where the finding was made. Example: us-east-1.
            severity_type_id (int | None | Unset): Severity type of the finding in the application Example: 4.
            standard_id (int | None | Unset): ID of the compliance standard in the application. Example: 1.
            standard_name (str | Unset): Name of the standard in the application. Example: No Public Resources.
            suppressed_finding (SuppressedComplianceCheckFinding | Unset): SuppressedComplianceCheckFinding defines a
                Suppressed Compliance Check Finding.
     """

    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    check_id: int | None | Unset = UNSET
    check_name: str | Unset = UNSET
    finding_created_at: str | Unset = UNSET
    hash_identifier: int | Unset = UNSET
    parent_ou_id: int | None | Unset = UNSET
    parent_ou_name: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    project_name: str | Unset = UNSET
    region: str | Unset = UNSET
    severity_type_id: int | None | Unset = UNSET
    standard_id: int | None | Unset = UNSET
    standard_name: str | Unset = UNSET
    suppressed_finding: SuppressedComplianceCheckFinding | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.suppressed_compliance_check_finding import SuppressedComplianceCheckFinding
        account_name = self.account_name

        account_number = self.account_number

        check_id: int | None | Unset
        if isinstance(self.check_id, Unset):
            check_id = UNSET
        else:
            check_id = self.check_id

        check_name = self.check_name

        finding_created_at = self.finding_created_at

        hash_identifier = self.hash_identifier

        parent_ou_id: int | None | Unset
        if isinstance(self.parent_ou_id, Unset):
            parent_ou_id = UNSET
        else:
            parent_ou_id = self.parent_ou_id

        parent_ou_name = self.parent_ou_name

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        project_name = self.project_name

        region = self.region

        severity_type_id: int | None | Unset
        if isinstance(self.severity_type_id, Unset):
            severity_type_id = UNSET
        else:
            severity_type_id = self.severity_type_id

        standard_id: int | None | Unset
        if isinstance(self.standard_id, Unset):
            standard_id = UNSET
        else:
            standard_id = self.standard_id

        standard_name = self.standard_name

        suppressed_finding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suppressed_finding, Unset):
            suppressed_finding = self.suppressed_finding.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if check_id is not UNSET:
            field_dict["check_id"] = check_id
        if check_name is not UNSET:
            field_dict["check_name"] = check_name
        if finding_created_at is not UNSET:
            field_dict["finding_created_at"] = finding_created_at
        if hash_identifier is not UNSET:
            field_dict["hash_identifier"] = hash_identifier
        if parent_ou_id is not UNSET:
            field_dict["parent_ou_id"] = parent_ou_id
        if parent_ou_name is not UNSET:
            field_dict["parent_ou_name"] = parent_ou_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if region is not UNSET:
            field_dict["region"] = region
        if severity_type_id is not UNSET:
            field_dict["severity_type_id"] = severity_type_id
        if standard_id is not UNSET:
            field_dict["standard_id"] = standard_id
        if standard_name is not UNSET:
            field_dict["standard_name"] = standard_name
        if suppressed_finding is not UNSET:
            field_dict["suppressed_finding"] = suppressed_finding

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.suppressed_compliance_check_finding import SuppressedComplianceCheckFinding
        d = dict(src_dict)
        account_name = d.pop("account_name", UNSET)

        account_number = d.pop("account_number", UNSET)

        def _parse_check_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        check_id = _parse_check_id(d.pop("check_id", UNSET))


        check_name = d.pop("check_name", UNSET)

        finding_created_at = d.pop("finding_created_at", UNSET)

        hash_identifier = d.pop("hash_identifier", UNSET)

        def _parse_parent_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_ou_id = _parse_parent_ou_id(d.pop("parent_ou_id", UNSET))


        parent_ou_name = d.pop("parent_ou_name", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        project_name = d.pop("project_name", UNSET)

        region = d.pop("region", UNSET)

        def _parse_severity_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        severity_type_id = _parse_severity_type_id(d.pop("severity_type_id", UNSET))


        def _parse_standard_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        standard_id = _parse_standard_id(d.pop("standard_id", UNSET))


        standard_name = d.pop("standard_name", UNSET)

        _suppressed_finding = d.pop("suppressed_finding", UNSET)
        suppressed_finding: SuppressedComplianceCheckFinding | Unset
        if isinstance(_suppressed_finding,  Unset):
            suppressed_finding = UNSET
        else:
            suppressed_finding = SuppressedComplianceCheckFinding.from_dict(_suppressed_finding)




        suppressed_compliance_check_finding_detailed = cls(
            account_name=account_name,
            account_number=account_number,
            check_id=check_id,
            check_name=check_name,
            finding_created_at=finding_created_at,
            hash_identifier=hash_identifier,
            parent_ou_id=parent_ou_id,
            parent_ou_name=parent_ou_name,
            project_id=project_id,
            project_name=project_name,
            region=region,
            severity_type_id=severity_type_id,
            standard_id=standard_id,
            standard_name=standard_name,
            suppressed_finding=suppressed_finding,
        )


        suppressed_compliance_check_finding_detailed.additional_properties = d
        return suppressed_compliance_check_finding_detailed

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
