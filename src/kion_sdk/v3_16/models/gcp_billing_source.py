from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.gcp_billing_account_with_start import GCPBillingAccountWithStart





T = TypeVar("T", bound="GCPBillingSource")



@_attrs_define
class GCPBillingSource:
    """ GCPBillingSource defines a billing source used for testing and creation.

        Attributes:
            account_type_id (int | None): The Account Type ID is the corresponding billing source account's type.
                15 - Google Cloud Example: 15.
            gcp_billing_account_create (GCPBillingAccountWithStart): GCPBillingAccountWithStart contains fields describing a
                billing account in GCP
     """

    account_type_id: int | None
    gcp_billing_account_create: GCPBillingAccountWithStart
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_billing_account_with_start import GCPBillingAccountWithStart
        account_type_id: int | None
        account_type_id = self.account_type_id

        gcp_billing_account_create = self.gcp_billing_account_create.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_type_id": account_type_id,
            "gcp_billing_account_create": gcp_billing_account_create,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_billing_account_with_start import GCPBillingAccountWithStart
        d = dict(src_dict)
        def _parse_account_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id"))


        gcp_billing_account_create = GCPBillingAccountWithStart.from_dict(d.pop("gcp_billing_account_create"))




        gcp_billing_source = cls(
            account_type_id=account_type_id,
            gcp_billing_account_create=gcp_billing_account_create,
        )


        gcp_billing_source.additional_properties = d
        return gcp_billing_source

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
