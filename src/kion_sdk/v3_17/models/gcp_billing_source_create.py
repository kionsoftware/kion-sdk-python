from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gcp_billing_source_create_gcp_billing_account_create import GCPBillingSourceCreateGcpBillingAccountCreate





T = TypeVar("T", bound="GCPBillingSourceCreate")



@_attrs_define
class GCPBillingSourceCreate:
    """ GCPBillingSourceCreate defines a billing source used for testing and creation.

        Attributes:
            account_type_id (int | None | Unset):
            gcp_billing_account_create (GCPBillingSourceCreateGcpBillingAccountCreate | Unset):
     """

    account_type_id: int | None | Unset = UNSET
    gcp_billing_account_create: GCPBillingSourceCreateGcpBillingAccountCreate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_billing_source_create_gcp_billing_account_create import GCPBillingSourceCreateGcpBillingAccountCreate
        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        gcp_billing_account_create: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_billing_account_create, Unset):
            gcp_billing_account_create = self.gcp_billing_account_create.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if gcp_billing_account_create is not UNSET:
            field_dict["gcp_billing_account_create"] = gcp_billing_account_create

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_billing_source_create_gcp_billing_account_create import GCPBillingSourceCreateGcpBillingAccountCreate
        d = dict(src_dict)
        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        _gcp_billing_account_create = d.pop("gcp_billing_account_create", UNSET)
        gcp_billing_account_create: GCPBillingSourceCreateGcpBillingAccountCreate | Unset
        if isinstance(_gcp_billing_account_create,  Unset):
            gcp_billing_account_create = UNSET
        else:
            gcp_billing_account_create = GCPBillingSourceCreateGcpBillingAccountCreate.from_dict(_gcp_billing_account_create)




        gcp_billing_source_create = cls(
            account_type_id=account_type_id,
            gcp_billing_account_create=gcp_billing_account_create,
        )


        gcp_billing_source_create.additional_properties = d
        return gcp_billing_source_create

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
