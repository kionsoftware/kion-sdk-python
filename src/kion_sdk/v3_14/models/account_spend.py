from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountSpend")



@_attrs_define
class AccountSpend:
    """ AccountSpend defines the spend for an account.

        Attributes:
            account_id (int | None | Unset): Account ID. Example: 1.
            account_number (str | Unset): AWS account number. Example: 121212121212.
            account_type_id (int | None | Unset): Will be: 1 for AWS Commercial, 2 for AWS GovCloud, 3 for Azure CSP
                Standard. Example: 1.
            datecode (str | Unset): The date of the spending (YYYY-MM). Example: 2019-01.
            spend (float | Unset): The amount spent. Use of `total` is deprecated, use `spend` instead.
            total (float | Unset):
     """

    account_id: int | None | Unset = UNSET
    account_number: str | Unset = UNSET
    account_type_id: int | None | Unset = UNSET
    datecode: str | Unset = UNSET
    spend: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_number = self.account_number

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        datecode = self.datecode

        spend = self.spend

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if datecode is not UNSET:
            field_dict["datecode"] = datecode
        if spend is not UNSET:
            field_dict["spend"] = spend
        if total is not UNSET:
            field_dict["total"] = total

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


        account_number = d.pop("account_number", UNSET)

        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        datecode = d.pop("datecode", UNSET)

        spend = d.pop("spend", UNSET)

        total = d.pop("total", UNSET)

        account_spend = cls(
            account_id=account_id,
            account_number=account_number,
            account_type_id=account_type_id,
            datecode=datecode,
            spend=spend,
            total=total,
        )


        account_spend.additional_properties = d
        return account_spend

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
