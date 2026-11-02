from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AccountServiceSpend")



@_attrs_define
class AccountServiceSpend:
    """ AccountServiceSpend defines the spend for an account in a project for a specific service

        Attributes:
            account_number (str | Unset): AWS account number. Example: 121212121212.
            date_code (str | Unset): The date of the spending (YYYY-MM). Example: 2019-01.
            service (str | Unset): Service the spending is for Example: AmazonEC2.
            spend (float | Unset): The total amount spent for this service. Use of `total` is deprecated, use `spend`
                instead.
            total (float | Unset):
     """

    account_number: str | Unset = UNSET
    date_code: str | Unset = UNSET
    service: str | Unset = UNSET
    spend: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        date_code = self.date_code

        service = self.service

        spend = self.spend

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if date_code is not UNSET:
            field_dict["date_code"] = date_code
        if service is not UNSET:
            field_dict["service"] = service
        if spend is not UNSET:
            field_dict["spend"] = spend
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number = d.pop("account_number", UNSET)

        date_code = d.pop("date_code", UNSET)

        service = d.pop("service", UNSET)

        spend = d.pop("spend", UNSET)

        total = d.pop("total", UNSET)

        account_service_spend = cls(
            account_number=account_number,
            date_code=date_code,
            service=service,
            spend=spend,
            total=total,
        )


        account_service_spend.additional_properties = d
        return account_service_spend

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
