from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.budget_data_create import BudgetDataCreate





T = TypeVar("T", bound="BudgetUpdate")



@_attrs_define
class BudgetUpdate:
    """ BudgetUpdate is used to update an existing project budget or OU threshold.

        Attributes:
            amount (int | Unset): Total amount for the budget. This is required if data is not specified. Example: 1000.
            data (list[BudgetDataCreate] | None | Unset): Month to month budget amounts. If not specified, these values are
                generated based on
                amount, start_datecode, end_datecode, and funding_source_ids.
            end_datecode (str | Unset): Year and month the budget ends. This is an exclusive date. Example: 2022-01.
            funding_source_ids (list[int] | None | Unset): Optional funding source IDs to use when data is not specified.
                This value is ignored is data is specified. Example: [1, 2].
            start_datecode (str | Unset): Year and month the budget starts. Example: 2022-01.
     """

    amount: int | Unset = UNSET
    data: list[BudgetDataCreate] | None | Unset = UNSET
    end_datecode: str | Unset = UNSET
    funding_source_ids: list[int] | None | Unset = UNSET
    start_datecode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.budget_data_create import BudgetDataCreate
        amount = self.amount

        data: list[dict[str, Any]] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)


        else:
            data = self.data

        end_datecode = self.end_datecode

        funding_source_ids: list[int] | None | Unset
        if isinstance(self.funding_source_ids, Unset):
            funding_source_ids = UNSET
        elif isinstance(self.funding_source_ids, list):
            funding_source_ids = self.funding_source_ids


        else:
            funding_source_ids = self.funding_source_ids

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if data is not UNSET:
            field_dict["data"] = data
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if funding_source_ids is not UNSET:
            field_dict["funding_source_ids"] = funding_source_ids
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_data_create import BudgetDataCreate
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        def _parse_data(data: object) -> list[BudgetDataCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in (_data_type_0):
                    data_type_0_item = BudgetDataCreate.from_dict(data_type_0_item_data)



                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BudgetDataCreate] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        end_datecode = d.pop("end_datecode", UNSET)

        def _parse_funding_source_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                funding_source_ids_type_0 = cast(list[int], data)

                return funding_source_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        funding_source_ids = _parse_funding_source_ids(d.pop("funding_source_ids", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        budget_update = cls(
            amount=amount,
            data=data,
            end_datecode=end_datecode,
            funding_source_ids=funding_source_ids,
            start_datecode=start_datecode,
        )


        budget_update.additional_properties = d
        return budget_update

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
