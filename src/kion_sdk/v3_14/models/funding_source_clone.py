from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FundingSourceClone")



@_attrs_define
class FundingSourceClone:
    """ FundingSourceClone defines the structure used for cloning an existing funding source.

        Attributes:
            amount (float): Amount of the funding source.
            name (str): Name of the funding source in the application. Example: 2019 IRAD funding.
            permission_scheme_id (int | None): ID of the permission scheme applied to the funding source. Example: 4.
            start_datecode (str): The month this funding source starts being usable (YYYY-MM). Example: 2019-01.
            description (str | Unset): Description for the funding source in the application. Example: Internal research and
                development funding for the 2019 financial year..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the funding source. Is required
                if no owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the funding source. Is required if no
                owner group IDs are listed. Example: [1, 2].
     """

    amount: float
    name: str
    permission_scheme_id: int | None
    start_datecode: str
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        name = self.name

        permission_scheme_id: int | None
        permission_scheme_id = self.permission_scheme_id

        start_datecode = self.start_datecode

        description = self.description

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "amount": amount,
            "name": name,
            "permission_scheme_id": permission_scheme_id,
            "start_datecode": start_datecode,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        name = d.pop("name")

        def _parse_permission_scheme_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        permission_scheme_id = _parse_permission_scheme_id(d.pop("permission_scheme_id"))


        start_datecode = d.pop("start_datecode")

        description = d.pop("description", UNSET)

        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        funding_source_clone = cls(
            amount=amount,
            name=name,
            permission_scheme_id=permission_scheme_id,
            start_datecode=start_datecode,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
        )


        funding_source_clone.additional_properties = d
        return funding_source_clone

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
