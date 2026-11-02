from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.funding_source import FundingSource





T = TypeVar("T", bound="OUFunding")



@_attrs_define
class OUFunding:
    """ OUFunding defines the funding for an ou.

        Attributes:
            allocated_in (float | Unset): The amount of money from this funding source allocated to this OU.
            allocated_out (float | Unset): The amount of money already allocated down to lower OUs.
            available (float | Unset): The amount of money in the OU not currently spent or planned.
            funding_source (FundingSource | Unset): FundingSource defines a funding source.
            planned (float | Unset): The amount of money already planned for the projects in this OU.
            spend (float | Unset): The amount of money already spent by projects in this OU. Use of `spent` is deprecated,
                use `spend` instead.
            spent (float | Unset):
     """

    allocated_in: float | Unset = UNSET
    allocated_out: float | Unset = UNSET
    available: float | Unset = UNSET
    funding_source: FundingSource | Unset = UNSET
    planned: float | Unset = UNSET
    spend: float | Unset = UNSET
    spent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.funding_source import FundingSource
        allocated_in = self.allocated_in

        allocated_out = self.allocated_out

        available = self.available

        funding_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funding_source, Unset):
            funding_source = self.funding_source.to_dict()

        planned = self.planned

        spend = self.spend

        spent = self.spent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allocated_in is not UNSET:
            field_dict["allocated_in"] = allocated_in
        if allocated_out is not UNSET:
            field_dict["allocated_out"] = allocated_out
        if available is not UNSET:
            field_dict["available"] = available
        if funding_source is not UNSET:
            field_dict["funding_source"] = funding_source
        if planned is not UNSET:
            field_dict["planned"] = planned
        if spend is not UNSET:
            field_dict["spend"] = spend
        if spent is not UNSET:
            field_dict["spent"] = spent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.funding_source import FundingSource
        d = dict(src_dict)
        allocated_in = d.pop("allocated_in", UNSET)

        allocated_out = d.pop("allocated_out", UNSET)

        available = d.pop("available", UNSET)

        _funding_source = d.pop("funding_source", UNSET)
        funding_source: FundingSource | Unset
        if isinstance(_funding_source,  Unset):
            funding_source = UNSET
        else:
            funding_source = FundingSource.from_dict(_funding_source)




        planned = d.pop("planned", UNSET)

        spend = d.pop("spend", UNSET)

        spent = d.pop("spent", UNSET)

        ou_funding = cls(
            allocated_in=allocated_in,
            allocated_out=allocated_out,
            available=available,
            funding_source=funding_source,
            planned=planned,
            spend=spend,
            spent=spent,
        )


        ou_funding.additional_properties = d
        return ou_funding

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
