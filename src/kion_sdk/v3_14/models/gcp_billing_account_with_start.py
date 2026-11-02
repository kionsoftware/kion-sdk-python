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





T = TypeVar("T", bound="GCPBillingAccountWithStart")



@_attrs_define
class GCPBillingAccountWithStart:
    """ GCPBillingAccountWithStart contains fields describing a billing account in GCP

        Attributes:
            big_query_export (GCPBigQueryExport): GCPBigQueryExport describes information about where billing data is
                exported in BigQuery
            billing_start_date (str): Start date of the billing source (YYYY-MM). Example: 2022-09.
            gcp_id (str): The GCP ID of the billing account Example: 55EE55_55EE55_55EE55.
            name (str): The name of the Google Cloud billing account Example: My billing account.
            service_account_id (int | None): The ID of the service account used for authentication against Google Cloud
                Example: 1.
            billing_account_attribution_account_id (int | None | Unset): The Account ID to attribute untracked charges to
                Example: 1.
            is_reseller (bool | None | Unset): Denotes if the billing account is that of a Parent Reseller Billing Account
            use_focus (bool | None | Unset): Use GCP FOCUS view Example: True.
            use_proprietary (bool | None | Unset): Use the GCP Proprietary Billing Table Example: True.
     """

    big_query_export: GCPBigQueryExport
    billing_start_date: str
    gcp_id: str
    name: str
    service_account_id: int | None
    billing_account_attribution_account_id: int | None | Unset = UNSET
    is_reseller: bool | None | Unset = UNSET
    use_focus: bool | None | Unset = UNSET
    use_proprietary: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_big_query_export import GCPBigQueryExport
        big_query_export = self.big_query_export.to_dict()

        billing_start_date = self.billing_start_date

        gcp_id = self.gcp_id

        name = self.name

        service_account_id: int | None
        service_account_id = self.service_account_id

        billing_account_attribution_account_id: int | None | Unset
        if isinstance(self.billing_account_attribution_account_id, Unset):
            billing_account_attribution_account_id = UNSET
        else:
            billing_account_attribution_account_id = self.billing_account_attribution_account_id

        is_reseller: bool | None | Unset
        if isinstance(self.is_reseller, Unset):
            is_reseller = UNSET
        else:
            is_reseller = self.is_reseller

        use_focus: bool | None | Unset
        if isinstance(self.use_focus, Unset):
            use_focus = UNSET
        else:
            use_focus = self.use_focus

        use_proprietary: bool | None | Unset
        if isinstance(self.use_proprietary, Unset):
            use_proprietary = UNSET
        else:
            use_proprietary = self.use_proprietary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "big_query_export": big_query_export,
            "billing_start_date": billing_start_date,
            "gcp_id": gcp_id,
            "name": name,
            "service_account_id": service_account_id,
        })
        if billing_account_attribution_account_id is not UNSET:
            field_dict["billing_account_attribution_account_id"] = billing_account_attribution_account_id
        if is_reseller is not UNSET:
            field_dict["is_reseller"] = is_reseller
        if use_focus is not UNSET:
            field_dict["use_focus"] = use_focus
        if use_proprietary is not UNSET:
            field_dict["use_proprietary"] = use_proprietary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_big_query_export import GCPBigQueryExport
        d = dict(src_dict)
        big_query_export = GCPBigQueryExport.from_dict(d.pop("big_query_export"))




        billing_start_date = d.pop("billing_start_date")

        gcp_id = d.pop("gcp_id")

        name = d.pop("name")

        def _parse_service_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        service_account_id = _parse_service_account_id(d.pop("service_account_id"))


        def _parse_billing_account_attribution_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        billing_account_attribution_account_id = _parse_billing_account_attribution_account_id(d.pop("billing_account_attribution_account_id", UNSET))


        def _parse_is_reseller(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_reseller = _parse_is_reseller(d.pop("is_reseller", UNSET))


        def _parse_use_focus(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_focus = _parse_use_focus(d.pop("use_focus", UNSET))


        def _parse_use_proprietary(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_proprietary = _parse_use_proprietary(d.pop("use_proprietary", UNSET))


        gcp_billing_account_with_start = cls(
            big_query_export=big_query_export,
            billing_start_date=billing_start_date,
            gcp_id=gcp_id,
            name=name,
            service_account_id=service_account_id,
            billing_account_attribution_account_id=billing_account_attribution_account_id,
            is_reseller=is_reseller,
            use_focus=use_focus,
            use_proprietary=use_proprietary,
        )


        gcp_billing_account_with_start.additional_properties = d
        return gcp_billing_account_with_start

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
