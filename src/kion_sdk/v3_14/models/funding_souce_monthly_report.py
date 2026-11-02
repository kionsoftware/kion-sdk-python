from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FundingSouceMonthlyReport")



@_attrs_define
class FundingSouceMonthlyReport:
    """ FundingSouceMonthlyReport .

        Attributes:
            account_id (int | None | Unset): AccountID is id of the account associated to the report entry Example: 1.
            account_name (str | Unset): AccountName is name of the account associated to the report entry Example:
                CloudtamerAccount.
            account_number (str | Unset): AccountNumber is the account number of the account associated to the report entry.
                Example: 111222333444.
            cloud_provider (str | Unset): CloudProvider is the account's cloud provider associated with the report entry.
                Example: Amazon Web Services.
            datecode (int | Unset): Datecode is date of month of the funding source spend usage report entry Example:
                201901.
            funding_source_id (int | None | Unset): FundingSourceID is id of the funding source associated to the report
                entry Example: 1.
            funding_source_name (str | Unset): ProjectName is name of the project associated to the report entry Example:
                Tech Project 1.
            linked_account_number (str | Unset): LinkedAccountNumber is the linked account number of the account associated
                to the report entry. Example: 111222333444.
            project_id (int | None | Unset): ProjectID is id of the project associated to the report entry Example: 1.
            project_name (str | Unset): ProjectName is name of the project associated to the report entry Example: Tech
                Project 1.
            spend (float | Unset): Spend is amount spent for a particular month for the associated report entry
     """

    account_id: int | None | Unset = UNSET
    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    cloud_provider: str | Unset = UNSET
    datecode: int | Unset = UNSET
    funding_source_id: int | None | Unset = UNSET
    funding_source_name: str | Unset = UNSET
    linked_account_number: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    project_name: str | Unset = UNSET
    spend: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_name = self.account_name

        account_number = self.account_number

        cloud_provider = self.cloud_provider

        datecode = self.datecode

        funding_source_id: int | None | Unset
        if isinstance(self.funding_source_id, Unset):
            funding_source_id = UNSET
        else:
            funding_source_id = self.funding_source_id

        funding_source_name = self.funding_source_name

        linked_account_number = self.linked_account_number

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        project_name = self.project_name

        spend = self.spend


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
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if datecode is not UNSET:
            field_dict["datecode"] = datecode
        if funding_source_id is not UNSET:
            field_dict["funding_source_id"] = funding_source_id
        if funding_source_name is not UNSET:
            field_dict["funding_source_name"] = funding_source_name
        if linked_account_number is not UNSET:
            field_dict["linked_account_number"] = linked_account_number
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if spend is not UNSET:
            field_dict["spend"] = spend

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


        account_name = d.pop("account_name", UNSET)

        account_number = d.pop("account_number", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        datecode = d.pop("datecode", UNSET)

        def _parse_funding_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id", UNSET))


        funding_source_name = d.pop("funding_source_name", UNSET)

        linked_account_number = d.pop("linked_account_number", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        project_name = d.pop("project_name", UNSET)

        spend = d.pop("spend", UNSET)

        funding_souce_monthly_report = cls(
            account_id=account_id,
            account_name=account_name,
            account_number=account_number,
            cloud_provider=cloud_provider,
            datecode=datecode,
            funding_source_id=funding_source_id,
            funding_source_name=funding_source_name,
            linked_account_number=linked_account_number,
            project_id=project_id,
            project_name=project_name,
            spend=spend,
        )


        funding_souce_monthly_report.additional_properties = d
        return funding_souce_monthly_report

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
