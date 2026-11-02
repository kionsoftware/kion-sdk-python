from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SpendPlanV4Patch")



@_attrs_define
class SpendPlanV4Patch:
    """ SpendPlanV4Patch defines a spend plan PATCH record.

        Attributes:
            funding_source_id (int | None): ID of the funding source the money is coming from. Example: 1.
            amount (float | Unset): Amount of funding from the funding source.
            end_datecode (str | Unset): The month this funding source stops being usable (YYYY-MM). Example: 2019-12.
            start_datecode (str | Unset): The month this funding source starts being usable (YYYY-MM). Example: 2019-01.
     """

    funding_source_id: int | None
    amount: float | Unset = UNSET
    end_datecode: str | Unset = UNSET
    start_datecode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        funding_source_id: int | None
        funding_source_id = self.funding_source_id

        amount = self.amount

        end_datecode = self.end_datecode

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "funding_source_id": funding_source_id,
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_funding_source_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id"))


        amount = d.pop("amount", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        start_datecode = d.pop("start_datecode", UNSET)

        spend_plan_v4_patch = cls(
            funding_source_id=funding_source_id,
            amount=amount,
            end_datecode=end_datecode,
            start_datecode=start_datecode,
        )


        spend_plan_v4_patch.additional_properties = d
        return spend_plan_v4_patch

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
