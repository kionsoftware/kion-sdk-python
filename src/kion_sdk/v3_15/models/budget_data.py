from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BudgetData")



@_attrs_define
class BudgetData:
    """ BudgetData defines a single entry in a budget.

        Attributes:
            amount (float | Unset): Amount of the budget entry in dollars.
            datecode (str | Unset): Year and month for the budget data entry. Example: 2022-01.
            funding_source_id (int | None | Unset): ID of funding source for the budget entry. This is optional. Example: 1.
            id (int | Unset): ID of the budget data object. Example: 1.
            priority (int | Unset): Priority order of the budget entry. Example: 1.
     """

    amount: float | Unset = UNSET
    datecode: str | Unset = UNSET
    funding_source_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        datecode = self.datecode

        funding_source_id: int | None | Unset
        if isinstance(self.funding_source_id, Unset):
            funding_source_id = UNSET
        else:
            funding_source_id = self.funding_source_id

        id = self.id

        priority = self.priority


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if datecode is not UNSET:
            field_dict["datecode"] = datecode
        if funding_source_id is not UNSET:
            field_dict["funding_source_id"] = funding_source_id
        if id is not UNSET:
            field_dict["id"] = id
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        datecode = d.pop("datecode", UNSET)

        def _parse_funding_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id", UNSET))


        id = d.pop("id", UNSET)

        priority = d.pop("priority", UNSET)

        budget_data = cls(
            amount=amount,
            datecode=datecode,
            funding_source_id=funding_source_id,
            id=id,
            priority=priority,
        )


        budget_data.additional_properties = d
        return budget_data

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
