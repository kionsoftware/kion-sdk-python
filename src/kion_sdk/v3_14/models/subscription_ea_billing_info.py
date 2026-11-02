from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubscriptionEABillingInfo")



@_attrs_define
class SubscriptionEABillingInfo:
    """ 
        Attributes:
            account (str | Unset): Azure EA account number Example: 2222222.
            billing_account (str | Unset): Azure billing account number Example: 111111.
     """

    account: str | Unset = UNSET
    billing_account: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account = self.account

        billing_account = self.billing_account


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account is not UNSET:
            field_dict["account"] = account
        if billing_account is not UNSET:
            field_dict["billing_account"] = billing_account

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account", UNSET)

        billing_account = d.pop("billing_account", UNSET)

        subscription_ea_billing_info = cls(
            account=account,
            billing_account=billing_account,
        )


        subscription_ea_billing_info.additional_properties = d
        return subscription_ea_billing_info

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
