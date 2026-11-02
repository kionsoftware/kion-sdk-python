from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectFundingCreate")



@_attrs_define
class ProjectFundingCreate:
    """ ProjectFundingCreate defines a funding source for a project.

        Attributes:
            amount (float | Unset): Amount of funding from the funding source.
            end_datecode (str | Unset): The month this funding source stops being usable - this is exclusive of the date
                returned (YYYY-MM). Example: 2019-12.
            funding_order (int | Unset): The priority of this funding for the project. Funding with order 1 will be drawn
                from first, then 2, 3, etc. Example: 1.
            funding_source_id (int | None | Unset): ID of the funding source the money is coming from. Example: 1.
            start_datecode (str | Unset): The month this funding source starts being usable (YYYY-MM). Example: 2019-01.
     """

    amount: float | Unset = UNSET
    end_datecode: str | Unset = UNSET
    funding_order: int | Unset = UNSET
    funding_source_id: int | None | Unset = UNSET
    start_datecode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        end_datecode = self.end_datecode

        funding_order = self.funding_order

        funding_source_id: int | None | Unset
        if isinstance(self.funding_source_id, Unset):
            funding_source_id = UNSET
        else:
            funding_source_id = self.funding_source_id

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if funding_order is not UNSET:
            field_dict["funding_order"] = funding_order
        if funding_source_id is not UNSET:
            field_dict["funding_source_id"] = funding_source_id
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        funding_order = d.pop("funding_order", UNSET)

        def _parse_funding_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        project_funding_create = cls(
            amount=amount,
            end_datecode=end_datecode,
            funding_order=funding_order,
            funding_source_id=funding_source_id,
            start_datecode=start_datecode,
        )


        project_funding_create.additional_properties = d
        return project_funding_create

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
