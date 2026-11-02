from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubscriptionMCABillingInfo")



@_attrs_define
class SubscriptionMCABillingInfo:
    """ 
        Attributes:
            billing_account (str | Unset): Azure MCA billing account number Example:
                11111111-2222-5eb2-dab3-26a31fad392f:569ff21e-08bd-46a1-ac01-d4630b907506_2019-05-31.
            billing_profile (str | Unset): Azure MCA billing profile number Example: A3FE-DS4M-BG2-GPB.
            billing_profile_invoice (str | Unset): Azure MCA billing profile invoice section number Example: DUV2-JGGK-PJA-
                GPB.
     """

    billing_account: str | Unset = UNSET
    billing_profile: str | Unset = UNSET
    billing_profile_invoice: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        billing_account = self.billing_account

        billing_profile = self.billing_profile

        billing_profile_invoice = self.billing_profile_invoice


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_account is not UNSET:
            field_dict["billing_account"] = billing_account
        if billing_profile is not UNSET:
            field_dict["billing_profile"] = billing_profile
        if billing_profile_invoice is not UNSET:
            field_dict["billing_profile_invoice"] = billing_profile_invoice

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_account = d.pop("billing_account", UNSET)

        billing_profile = d.pop("billing_profile", UNSET)

        billing_profile_invoice = d.pop("billing_profile_invoice", UNSET)

        subscription_mca_billing_info = cls(
            billing_account=billing_account,
            billing_profile=billing_profile,
            billing_profile_invoice=billing_profile_invoice,
        )


        subscription_mca_billing_info.additional_properties = d
        return subscription_mca_billing_info

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
