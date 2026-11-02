from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FundingSourceFinancials")



@_attrs_define
class FundingSourceFinancials:
    """ FundingSourceFinancials defines financial data for a funding source.

        Attributes:
            amount (float | Unset): Amount of the funding source.
            amount_unspent (float | Unset): Amount unspent from the funding source. Equal to amount - spend.
            planned (float | Unset): Total amount planned from the funding source.
            planned_unspent (float | Unset): Amount that has been planned but not spent. Equal to planned - spend.
            spend (float | Unset): Total amount spent from the funding source. Use of `spent` is deprecated, use `spend`
                instead
            spent (float | Unset):
            unplanned (float | Unset): Amount unplanned from the funding source. Equal to amount - planned.
     """

    amount: float | Unset = UNSET
    amount_unspent: float | Unset = UNSET
    planned: float | Unset = UNSET
    planned_unspent: float | Unset = UNSET
    spend: float | Unset = UNSET
    spent: float | Unset = UNSET
    unplanned: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        amount_unspent = self.amount_unspent

        planned = self.planned

        planned_unspent = self.planned_unspent

        spend = self.spend

        spent = self.spent

        unplanned = self.unplanned


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_unspent is not UNSET:
            field_dict["amount_unspent"] = amount_unspent
        if planned is not UNSET:
            field_dict["planned"] = planned
        if planned_unspent is not UNSET:
            field_dict["planned_unspent"] = planned_unspent
        if spend is not UNSET:
            field_dict["spend"] = spend
        if spent is not UNSET:
            field_dict["spent"] = spent
        if unplanned is not UNSET:
            field_dict["unplanned"] = unplanned

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        amount_unspent = d.pop("amount_unspent", UNSET)

        planned = d.pop("planned", UNSET)

        planned_unspent = d.pop("planned_unspent", UNSET)

        spend = d.pop("spend", UNSET)

        spent = d.pop("spent", UNSET)

        unplanned = d.pop("unplanned", UNSET)

        funding_source_financials = cls(
            amount=amount,
            amount_unspent=amount_unspent,
            planned=planned,
            planned_unspent=planned_unspent,
            spend=spend,
            spent=spent,
            unplanned=unplanned,
        )


        funding_source_financials.additional_properties = d
        return funding_source_financials

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
