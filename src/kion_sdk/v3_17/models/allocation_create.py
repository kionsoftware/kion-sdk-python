from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AllocationCreate")



@_attrs_define
class AllocationCreate:
    """ AllocationCreate defines the creation of an allocation of funds from one OU to another.

        Attributes:
            from_ou_id (int | None): The ID of the OU the money will be coming from. Example: 1.
            funding_source_id (int | None): The ID of the funding source where the money originally came from. Example: 1.
            to_ou_id (int | None): The ID of the OU the money will be going to. Example: 2.
            allocate_all_available_funds (bool | None | Unset): Whether all available funds should be allocated to the OU.
                If this is true, then amount will be ignored.
            amount (float | Unset): Amount of money being allocated from one OU to another.
            comments (str | Unset): Comments about the allocation. Example: Allocating new funds to be used for R&D..
     """

    from_ou_id: int | None
    funding_source_id: int | None
    to_ou_id: int | None
    allocate_all_available_funds: bool | None | Unset = UNSET
    amount: float | Unset = UNSET
    comments: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from_ou_id: int | None
        from_ou_id = self.from_ou_id

        funding_source_id: int | None
        funding_source_id = self.funding_source_id

        to_ou_id: int | None
        to_ou_id = self.to_ou_id

        allocate_all_available_funds: bool | None | Unset
        if isinstance(self.allocate_all_available_funds, Unset):
            allocate_all_available_funds = UNSET
        else:
            allocate_all_available_funds = self.allocate_all_available_funds

        amount = self.amount

        comments = self.comments


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "from_ou_id": from_ou_id,
            "funding_source_id": funding_source_id,
            "to_ou_id": to_ou_id,
        })
        if allocate_all_available_funds is not UNSET:
            field_dict["allocate_all_available_funds"] = allocate_all_available_funds
        if amount is not UNSET:
            field_dict["amount"] = amount
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_from_ou_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        from_ou_id = _parse_from_ou_id(d.pop("from_ou_id"))


        def _parse_funding_source_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id"))


        def _parse_to_ou_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        to_ou_id = _parse_to_ou_id(d.pop("to_ou_id"))


        def _parse_allocate_all_available_funds(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allocate_all_available_funds = _parse_allocate_all_available_funds(d.pop("allocate_all_available_funds", UNSET))


        amount = d.pop("amount", UNSET)

        comments = d.pop("comments", UNSET)

        allocation_create = cls(
            from_ou_id=from_ou_id,
            funding_source_id=funding_source_id,
            to_ou_id=to_ou_id,
            allocate_all_available_funds=allocate_all_available_funds,
            amount=amount,
            comments=comments,
        )


        allocation_create.additional_properties = d
        return allocation_create

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
