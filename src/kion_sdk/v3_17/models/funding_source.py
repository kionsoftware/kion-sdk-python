from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FundingSource")



@_attrs_define
class FundingSource:
    """ FundingSource defines a funding source.

        Attributes:
            amount (float | Unset): Amount of the funding source.
            description (str | Unset): Description for the funding source in the application. Example: Internal research and
                development funding for the 2019 financial year..
            end_datecode (str | Unset): The month this funding source stops being usable - this is exclusive of the date
                returned (YYYY-MM). Example: 2019-12.
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the funding source in the application. Example: 2019 IRAD funding.
            ou_id (int | None | Unset): The ID of the OU the funding source was assigned to at creation. When allocations
                mode is off, this field is not populated. Example: 1.
            start_datecode (str | Unset): The month this funding source starts being usable (YYYY-MM). Example: 2019-01.
     """

    amount: float | Unset = UNSET
    description: str | Unset = UNSET
    end_datecode: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    start_datecode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        description = self.description

        end_datecode = self.end_datecode

        id = self.id

        name = self.name

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        description = d.pop("description", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        funding_source = cls(
            amount=amount,
            description=description,
            end_datecode=end_datecode,
            id=id,
            name=name,
            ou_id=ou_id,
            start_datecode=start_datecode,
        )


        funding_source.additional_properties = d
        return funding_source

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
