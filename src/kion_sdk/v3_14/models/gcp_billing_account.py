from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gcp_big_query_export import GCPBigQueryExport





T = TypeVar("T", bound="GCPBillingAccount")



@_attrs_define
class GCPBillingAccount:
    """ GCPBillingAccount contains fields describing a billing account in GCP

        Attributes:
            big_query_export (GCPBigQueryExport | Unset): GCPBigQueryExport describes information about where billing data
                is exported in BigQuery
            gcp_id (str | Unset): The GCP ID of the billing account Example: 55EE55_55EE55_55EE55.
            id (int | Unset): The ID of the billing account in cloudtamer.io Example: 1.
            is_reseller (bool | None | Unset): Indicates if the Billing Account belongs to a reseller
            name (str | Unset): The name of the GCP billing account Example: My billing account.
            service_account_id (int | None | Unset): The ID of the service account used for authentication against GCP
                Example: 1.
     """

    big_query_export: GCPBigQueryExport | Unset = UNSET
    gcp_id: str | Unset = UNSET
    id: int | Unset = UNSET
    is_reseller: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    service_account_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_big_query_export import GCPBigQueryExport
        big_query_export: dict[str, Any] | Unset = UNSET
        if not isinstance(self.big_query_export, Unset):
            big_query_export = self.big_query_export.to_dict()

        gcp_id = self.gcp_id

        id = self.id

        is_reseller: bool | None | Unset
        if isinstance(self.is_reseller, Unset):
            is_reseller = UNSET
        else:
            is_reseller = self.is_reseller

        name = self.name

        service_account_id: int | None | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if big_query_export is not UNSET:
            field_dict["big_query_export"] = big_query_export
        if gcp_id is not UNSET:
            field_dict["gcp_id"] = gcp_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_reseller is not UNSET:
            field_dict["is_reseller"] = is_reseller
        if name is not UNSET:
            field_dict["name"] = name
        if service_account_id is not UNSET:
            field_dict["service_account_id"] = service_account_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_big_query_export import GCPBigQueryExport
        d = dict(src_dict)
        _big_query_export = d.pop("big_query_export", UNSET)
        big_query_export: GCPBigQueryExport | Unset
        if isinstance(_big_query_export,  Unset):
            big_query_export = UNSET
        else:
            big_query_export = GCPBigQueryExport.from_dict(_big_query_export)




        gcp_id = d.pop("gcp_id", UNSET)

        id = d.pop("id", UNSET)

        def _parse_is_reseller(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_reseller = _parse_is_reseller(d.pop("is_reseller", UNSET))


        name = d.pop("name", UNSET)

        def _parse_service_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("service_account_id", UNSET))


        gcp_billing_account = cls(
            big_query_export=big_query_export,
            gcp_id=gcp_id,
            id=id,
            is_reseller=is_reseller,
            name=name,
            service_account_id=service_account_id,
        )


        gcp_billing_account.additional_properties = d
        return gcp_billing_account

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
