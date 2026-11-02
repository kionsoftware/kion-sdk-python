from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.subscription_csp_billing_info_billing_cycle import SubscriptionCSPBillingInfoBillingCycle
from ..types import UNSET, Unset






T = TypeVar("T", bound="SubscriptionCSPBillingInfo")



@_attrs_define
class SubscriptionCSPBillingInfo:
    """ 
        Attributes:
            billing_cycle (SubscriptionCSPBillingInfoBillingCycle | Unset): Optional azure CSP billing cycle
                If no value is provided, default value is monthly
                unknown Unknown  Enum initializer.
                monthly Monthly  Indicates that the partner will be charged monthly.
                annual Annual  Indicates that the partner will be charged annually.
                none None  Indicates that the partner will not be charged monthly. This value may be used for trial offers.
                one_time OneTime  Indicates that the partner will be charged one-time. This value does not apply to all
                products. Example: monthly.
            offer_id (str | Unset): Azure CSP offer id Example: MS-AZR-USGOV-1111P.
     """

    billing_cycle: SubscriptionCSPBillingInfoBillingCycle | Unset = UNSET
    offer_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        billing_cycle: str | Unset = UNSET
        if not isinstance(self.billing_cycle, Unset):
            billing_cycle = self.billing_cycle.value


        offer_id = self.offer_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_cycle is not UNSET:
            field_dict["billing_cycle"] = billing_cycle
        if offer_id is not UNSET:
            field_dict["offer_id"] = offer_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _billing_cycle = d.pop("billing_cycle", UNSET)
        billing_cycle: SubscriptionCSPBillingInfoBillingCycle | Unset
        if isinstance(_billing_cycle,  Unset):
            billing_cycle = UNSET
        else:
            billing_cycle = SubscriptionCSPBillingInfoBillingCycle(_billing_cycle)




        offer_id = d.pop("offer_id", UNSET)

        subscription_csp_billing_info = cls(
            billing_cycle=billing_cycle,
            offer_id=offer_id,
        )


        subscription_csp_billing_info.additional_properties = d
        return subscription_csp_billing_info

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
