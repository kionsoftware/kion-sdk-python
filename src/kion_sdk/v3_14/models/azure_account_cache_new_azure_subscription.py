from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.subscription_csp_billing_info import SubscriptionCSPBillingInfo
  from ..models.subscription_ea_billing_info import SubscriptionEABillingInfo
  from ..models.subscription_mca_billing_info import SubscriptionMCABillingInfo





T = TypeVar("T", bound="AzureAccountCacheNewAzureSubscription")



@_attrs_define
class AzureAccountCacheNewAzureSubscription:
    """ AzureAccountCacheNewAzureSubscription defines a payload for creating a new Azure Subscription.

        Attributes:
            account_name (str): Name of the account as it appears in the application Example: My New Account.
            name (str): Name of the subscription as it appears in azure Example: Some New Subscription.
            payer_id (int | None): ID of the application payer the new account and subscription will be created under
                Example: 1.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            csp (SubscriptionCSPBillingInfo | Unset):
            ea (SubscriptionEABillingInfo | Unset):
            mca (SubscriptionMCABillingInfo | Unset):
            parent_management_group_id (str | Unset): Optional parent management group id. If provided, the subscription
                will be created under the provided management group.
                If not provided, the subscription will be created at the root level Example: aaaaaaaa-bbbb-
                cccc-1111-222222222222.
     """

    account_name: str
    name: str
    payer_id: int | None
    account_alias: str | Unset = UNSET
    csp: SubscriptionCSPBillingInfo | Unset = UNSET
    ea: SubscriptionEABillingInfo | Unset = UNSET
    mca: SubscriptionMCABillingInfo | Unset = UNSET
    parent_management_group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_csp_billing_info import SubscriptionCSPBillingInfo
        from ..models.subscription_ea_billing_info import SubscriptionEABillingInfo
        from ..models.subscription_mca_billing_info import SubscriptionMCABillingInfo
        account_name = self.account_name

        name = self.name

        payer_id: int | None
        payer_id = self.payer_id

        account_alias = self.account_alias

        csp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.csp, Unset):
            csp = self.csp.to_dict()

        ea: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ea, Unset):
            ea = self.ea.to_dict()

        mca: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mca, Unset):
            mca = self.mca.to_dict()

        parent_management_group_id = self.parent_management_group_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_name": account_name,
            "name": name,
            "payer_id": payer_id,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if csp is not UNSET:
            field_dict["csp"] = csp
        if ea is not UNSET:
            field_dict["ea"] = ea
        if mca is not UNSET:
            field_dict["mca"] = mca
        if parent_management_group_id is not UNSET:
            field_dict["parent_management_group_id"] = parent_management_group_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_csp_billing_info import SubscriptionCSPBillingInfo
        from ..models.subscription_ea_billing_info import SubscriptionEABillingInfo
        from ..models.subscription_mca_billing_info import SubscriptionMCABillingInfo
        d = dict(src_dict)
        account_name = d.pop("account_name")

        name = d.pop("name")

        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        account_alias = d.pop("account_alias", UNSET)

        _csp = d.pop("csp", UNSET)
        csp: SubscriptionCSPBillingInfo | Unset
        if isinstance(_csp,  Unset):
            csp = UNSET
        else:
            csp = SubscriptionCSPBillingInfo.from_dict(_csp)




        _ea = d.pop("ea", UNSET)
        ea: SubscriptionEABillingInfo | Unset
        if isinstance(_ea,  Unset):
            ea = UNSET
        else:
            ea = SubscriptionEABillingInfo.from_dict(_ea)




        _mca = d.pop("mca", UNSET)
        mca: SubscriptionMCABillingInfo | Unset
        if isinstance(_mca,  Unset):
            mca = UNSET
        else:
            mca = SubscriptionMCABillingInfo.from_dict(_mca)




        parent_management_group_id = d.pop("parent_management_group_id", UNSET)

        azure_account_cache_new_azure_subscription = cls(
            account_name=account_name,
            name=name,
            payer_id=payer_id,
            account_alias=account_alias,
            csp=csp,
            ea=ea,
            mca=mca,
            parent_management_group_id=parent_management_group_id,
        )


        azure_account_cache_new_azure_subscription.additional_properties = d
        return azure_account_cache_new_azure_subscription

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
