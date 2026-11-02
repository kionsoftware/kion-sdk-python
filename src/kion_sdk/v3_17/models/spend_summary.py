from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SpendSummary")



@_attrs_define
class SpendSummary:
    """ SpendSummary defines spending on a project, account, and funding source.

        Attributes:
            account_id (int | None | Unset): Account ID. Example: 1.
            amount (float | Unset):
            funding_source_id (int | None | Unset): Funding source ID. Example: 1.
            project_id (int | None | Unset): Project ID. Example: 1.
            spend (float | Unset): Spend amount.
     """

    account_id: int | None | Unset = UNSET
    amount: float | Unset = UNSET
    funding_source_id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    spend: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        amount = self.amount

        funding_source_id: int | None | Unset
        if isinstance(self.funding_source_id, Unset):
            funding_source_id = UNSET
        else:
            funding_source_id = self.funding_source_id

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        spend = self.spend


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if funding_source_id is not UNSET:
            field_dict["funding_source_id"] = funding_source_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
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


        amount = d.pop("amount", UNSET)

        def _parse_funding_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id", UNSET))


        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        spend = d.pop("spend", UNSET)

        spend_summary = cls(
            account_id=account_id,
            amount=amount,
            funding_source_id=funding_source_id,
            project_id=project_id,
            spend=spend,
        )


        spend_summary.additional_properties = d
        return spend_summary

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
