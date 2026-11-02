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





T = TypeVar("T", bound="GCPBillingSourceCreateGcpBillingAccountCreate")



@_attrs_define
class GCPBillingSourceCreateGcpBillingAccountCreate:
    """ 
        Attributes:
            big_query_export (GCPBigQueryExport | Unset): GCPBigQueryExport describes information about where billing data
                is exported in BigQuery
            billing_start_date (int | Unset):
            gcp_id (str | Unset):
            name (str | Unset):
            service_account_id (int | Unset):
     """

    big_query_export: GCPBigQueryExport | Unset = UNSET
    billing_start_date: int | Unset = UNSET
    gcp_id: str | Unset = UNSET
    name: str | Unset = UNSET
    service_account_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_big_query_export import GCPBigQueryExport
        big_query_export: dict[str, Any] | Unset = UNSET
        if not isinstance(self.big_query_export, Unset):
            big_query_export = self.big_query_export.to_dict()

        billing_start_date = self.billing_start_date

        gcp_id = self.gcp_id

        name = self.name

        service_account_id = self.service_account_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if big_query_export is not UNSET:
            field_dict["big_query_export"] = big_query_export
        if billing_start_date is not UNSET:
            field_dict["billing_start_date"] = billing_start_date
        if gcp_id is not UNSET:
            field_dict["gcp_id"] = gcp_id
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




        billing_start_date = d.pop("billing_start_date", UNSET)

        gcp_id = d.pop("gcp_id", UNSET)

        name = d.pop("name", UNSET)

        service_account_id = d.pop("service_account_id", UNSET)

        gcp_billing_source_create_gcp_billing_account_create = cls(
            big_query_export=big_query_export,
            billing_start_date=billing_start_date,
            gcp_id=gcp_id,
            name=name,
            service_account_id=service_account_id,
        )


        gcp_billing_source_create_gcp_billing_account_create.additional_properties = d
        return gcp_billing_source_create_gcp_billing_account_create

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
