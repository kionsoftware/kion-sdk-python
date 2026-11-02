from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_check_finding import ComplianceCheckFinding
  from ..models.compliance_check_finding_detailed_data_json import ComplianceCheckFindingDetailedDataJson





T = TypeVar("T", bound="ComplianceCheckFindingDetailed")



@_attrs_define
class ComplianceCheckFindingDetailed:
    """ ComplianceCheckFindingDetailed defines a Compliance Check Scan Finding and its associated region, account, and
    project.

        Attributes:
            account_id (int | None | Unset): ID of the account in the application. Example: 1.
            account_name (str | Unset): Name of the account in the application. Example: Tech Project 1.
            account_number (str | Unset): AWS account number. Example: 121212121212.
            archived_at (str | Unset): Date when the finding was archived. Example: 2019-02-12T22:57:10+0000.
            check_id (int | None | Unset): ID of the compliance check in the application. Example: 1.
            check_name (str | Unset): Name of the check in the application. Example: public-s3.
            created_at (str | Unset): Date when the finding was made. Example: 2019-02-12T22:57:10+0000.
            data_json (ComplianceCheckFindingDetailedDataJson | Unset): DataJSON for the Compliance Check Scan Finding in
                the application. Should look like: {"attachments":[{"AttachTime": "2017-10-15T04:17:22+00:00"}]}
            finding (ComplianceCheckFinding | Unset): ComplianceCheckFinding defines a Compliance Check Finding.
            parent_ou_id (int | None | Unset): ID of the parent OU in the application. Example: 1.
            parent_ou_name (str | Unset): Name of the parent OU in the application. Example: Tech Project 1.
            project_id (int | None | Unset): ID of the project in the application. Example: 1.
            project_name (str | Unset): Name of the Project in the application. Example: Tech Project 1.
            region (str | Unset): Region where the finding was made. Example: us-east-1.
            severity_type_id (int | None | Unset): Severity type of the finding in the application Example: 4.
            standard_id (int | None | Unset): ID of the compliance standard in the application.
                Will return 0 if not queried with a project_id Example: 1.
            standard_name (str | Unset): Name of the standard in the application.
                Will return blank if not queried with a project_id Example: No Public Resources.
     """

    account_id: int | None | Unset = UNSET
    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    archived_at: str | Unset = UNSET
    check_id: int | None | Unset = UNSET
    check_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    data_json: ComplianceCheckFindingDetailedDataJson | Unset = UNSET
    finding: ComplianceCheckFinding | Unset = UNSET
    parent_ou_id: int | None | Unset = UNSET
    parent_ou_name: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    project_name: str | Unset = UNSET
    region: str | Unset = UNSET
    severity_type_id: int | None | Unset = UNSET
    standard_id: int | None | Unset = UNSET
    standard_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check_finding import ComplianceCheckFinding
        from ..models.compliance_check_finding_detailed_data_json import ComplianceCheckFindingDetailedDataJson
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_name = self.account_name

        account_number = self.account_number

        archived_at = self.archived_at

        check_id: int | None | Unset
        if isinstance(self.check_id, Unset):
            check_id = UNSET
        else:
            check_id = self.check_id

        check_name = self.check_name

        created_at = self.created_at

        data_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_json, Unset):
            data_json = self.data_json.to_dict()

        finding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finding, Unset):
            finding = self.finding.to_dict()

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if check_id is not UNSET:
            field_dict["check_id"] = check_id
        if check_name is not UNSET:
            field_dict["check_name"] = check_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if data_json is not UNSET:
            field_dict["data_json"] = data_json
        if finding is not UNSET:
            field_dict["finding"] = finding
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check_finding import ComplianceCheckFinding
        from ..models.compliance_check_finding_detailed_data_json import ComplianceCheckFindingDetailedDataJson
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        account_name = d.pop("account_name", UNSET)

        account_number = d.pop("account_number", UNSET)

        archived_at = d.pop("archived_at", UNSET)

        def _parse_check_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        check_id = _parse_check_id(d.pop("check_id", UNSET))


        check_name = d.pop("check_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        _data_json = d.pop("data_json", UNSET)
        data_json: ComplianceCheckFindingDetailedDataJson | Unset
        if isinstance(_data_json,  Unset):
            data_json = UNSET
        else:
            data_json = ComplianceCheckFindingDetailedDataJson.from_dict(_data_json)




        _finding = d.pop("finding", UNSET)
        finding: ComplianceCheckFinding | Unset
        if isinstance(_finding,  Unset):
            finding = UNSET
        else:
            finding = ComplianceCheckFinding.from_dict(_finding)




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

        compliance_check_finding_detailed = cls(
            account_id=account_id,
            account_name=account_name,
            account_number=account_number,
            archived_at=archived_at,
            check_id=check_id,
            check_name=check_name,
            created_at=created_at,
            data_json=data_json,
            finding=finding,
            parent_ou_id=parent_ou_id,
            parent_ou_name=parent_ou_name,
            project_id=project_id,
            project_name=project_name,
            region=region,
            severity_type_id=severity_type_id,
            standard_id=standard_id,
            standard_name=standard_name,
        )


        compliance_check_finding_detailed.additional_properties = d
        return compliance_check_finding_detailed

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
