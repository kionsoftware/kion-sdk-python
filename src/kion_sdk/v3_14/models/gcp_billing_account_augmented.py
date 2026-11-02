from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gcp_billing_account import GCPBillingAccount
  from ..models.google_cloud_service_account_with_key import GoogleCloudServiceAccountWithKey





T = TypeVar("T", bound="GCPBillingAccountAugmented")



@_attrs_define
class GCPBillingAccountAugmented:
    """ GCPBillingAccountAugmented contains information about retrieving billing data from GCP

        Attributes:
            gcp_billing_account (GCPBillingAccount | Unset): GCPBillingAccount contains fields describing a billing account
                in GCP
            gcp_service_account (GoogleCloudServiceAccountWithKey | Unset): GoogleCloudServiceAccountWithKey defines a
                Google Cloud service account and its key in cloudtamer.io.
     """

    gcp_billing_account: GCPBillingAccount | Unset = UNSET
    gcp_service_account: GoogleCloudServiceAccountWithKey | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_billing_account import GCPBillingAccount
        from ..models.google_cloud_service_account_with_key import GoogleCloudServiceAccountWithKey
        gcp_billing_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_billing_account, Unset):
            gcp_billing_account = self.gcp_billing_account.to_dict()

        gcp_service_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_service_account, Unset):
            gcp_service_account = self.gcp_service_account.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gcp_billing_account is not UNSET:
            field_dict["gcp_billing_account"] = gcp_billing_account
        if gcp_service_account is not UNSET:
            field_dict["gcp_service_account"] = gcp_service_account

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_billing_account import GCPBillingAccount
        from ..models.google_cloud_service_account_with_key import GoogleCloudServiceAccountWithKey
        d = dict(src_dict)
        _gcp_billing_account = d.pop("gcp_billing_account", UNSET)
        gcp_billing_account: GCPBillingAccount | Unset
        if isinstance(_gcp_billing_account,  Unset):
            gcp_billing_account = UNSET
        else:
            gcp_billing_account = GCPBillingAccount.from_dict(_gcp_billing_account)




        _gcp_service_account = d.pop("gcp_service_account", UNSET)
        gcp_service_account: GoogleCloudServiceAccountWithKey | Unset
        if isinstance(_gcp_service_account,  Unset):
            gcp_service_account = UNSET
        else:
            gcp_service_account = GoogleCloudServiceAccountWithKey.from_dict(_gcp_service_account)




        gcp_billing_account_augmented = cls(
            gcp_billing_account=gcp_billing_account,
            gcp_service_account=gcp_service_account,
        )


        gcp_billing_account_augmented.additional_properties = d
        return gcp_billing_account_augmented

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
