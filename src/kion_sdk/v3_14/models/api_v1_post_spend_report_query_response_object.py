from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ApiV1PostSpendReportQueryResponseObject")



@_attrs_define
class ApiV1PostSpendReportQueryResponseObject:
    """ 
        Attributes:
            account_id (int | None | Unset):
            account_label_label_key (str | Unset):
            account_name (str | Unset):
            account_number (str | Unset):
            attributed_spend (float | Unset):
            billed_spend (float | Unset):
            billing_source_id (int | None | Unset):
            billing_source_name (str | Unset):
            cloud_service_provider_id (int | None | Unset):
            cloud_service_provider_name (str | Unset):
            configured_spend (float | Unset):
            credit (float | Unset):
            list_spend (float | Unset):
            month (int | Unset):
            net_attributed_spend (float | Unset):
            net_billed_spend (float | Unset):
            net_list_spend (float | Unset):
            net_unattributed_spend (float | Unset):
            parent_ou_id (int | None | Unset):
            parent_ou_name (str | Unset):
            project_id (int | None | Unset):
            project_label_label_key (str | Unset):
            project_name (str | Unset):
            refund (float | Unset):
            resource (str | Unset):
            service (str | Unset):
            tag_tag_key (str | Unset):
            unadjusted_spend (float | Unset):
            unattributed_spend (float | Unset):
     """

    account_id: int | None | Unset = UNSET
    account_label_label_key: str | Unset = UNSET
    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    attributed_spend: float | Unset = UNSET
    billed_spend: float | Unset = UNSET
    billing_source_id: int | None | Unset = UNSET
    billing_source_name: str | Unset = UNSET
    cloud_service_provider_id: int | None | Unset = UNSET
    cloud_service_provider_name: str | Unset = UNSET
    configured_spend: float | Unset = UNSET
    credit: float | Unset = UNSET
    list_spend: float | Unset = UNSET
    month: int | Unset = UNSET
    net_attributed_spend: float | Unset = UNSET
    net_billed_spend: float | Unset = UNSET
    net_list_spend: float | Unset = UNSET
    net_unattributed_spend: float | Unset = UNSET
    parent_ou_id: int | None | Unset = UNSET
    parent_ou_name: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    project_label_label_key: str | Unset = UNSET
    project_name: str | Unset = UNSET
    refund: float | Unset = UNSET
    resource: str | Unset = UNSET
    service: str | Unset = UNSET
    tag_tag_key: str | Unset = UNSET
    unadjusted_spend: float | Unset = UNSET
    unattributed_spend: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_label_label_key = self.account_label_label_key

        account_name = self.account_name

        account_number = self.account_number

        attributed_spend = self.attributed_spend

        billed_spend = self.billed_spend

        billing_source_id: int | None | Unset
        if isinstance(self.billing_source_id, Unset):
            billing_source_id = UNSET
        else:
            billing_source_id = self.billing_source_id

        billing_source_name = self.billing_source_name

        cloud_service_provider_id: int | None | Unset
        if isinstance(self.cloud_service_provider_id, Unset):
            cloud_service_provider_id = UNSET
        else:
            cloud_service_provider_id = self.cloud_service_provider_id

        cloud_service_provider_name = self.cloud_service_provider_name

        configured_spend = self.configured_spend

        credit = self.credit

        list_spend = self.list_spend

        month = self.month

        net_attributed_spend = self.net_attributed_spend

        net_billed_spend = self.net_billed_spend

        net_list_spend = self.net_list_spend

        net_unattributed_spend = self.net_unattributed_spend

        parent_ou_id: int | None | Unset
        if isinstance(self.parent_ou_id, Unset):
            parent_ou_id = UNSET
        else:
            parent_ou_id = self.parent_ou_id

        parent_ou_name = self.parent_ou_name

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        project_label_label_key = self.project_label_label_key

        project_name = self.project_name

        refund = self.refund

        resource = self.resource

        service = self.service

        tag_tag_key = self.tag_tag_key

        unadjusted_spend = self.unadjusted_spend

        unattributed_spend = self.unattributed_spend


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_label_label_key is not UNSET:
            field_dict["account_label:<LABEL_KEY>"] = account_label_label_key
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if attributed_spend is not UNSET:
            field_dict["attributed_spend"] = attributed_spend
        if billed_spend is not UNSET:
            field_dict["billed_spend"] = billed_spend
        if billing_source_id is not UNSET:
            field_dict["billing_source_id"] = billing_source_id
        if billing_source_name is not UNSET:
            field_dict["billing_source_name"] = billing_source_name
        if cloud_service_provider_id is not UNSET:
            field_dict["cloud_service_provider_id"] = cloud_service_provider_id
        if cloud_service_provider_name is not UNSET:
            field_dict["cloud_service_provider_name"] = cloud_service_provider_name
        if configured_spend is not UNSET:
            field_dict["configured_spend"] = configured_spend
        if credit is not UNSET:
            field_dict["credit"] = credit
        if list_spend is not UNSET:
            field_dict["list_spend"] = list_spend
        if month is not UNSET:
            field_dict["month"] = month
        if net_attributed_spend is not UNSET:
            field_dict["net_attributed_spend"] = net_attributed_spend
        if net_billed_spend is not UNSET:
            field_dict["net_billed_spend"] = net_billed_spend
        if net_list_spend is not UNSET:
            field_dict["net_list_spend"] = net_list_spend
        if net_unattributed_spend is not UNSET:
            field_dict["net_unattributed_spend"] = net_unattributed_spend
        if parent_ou_id is not UNSET:
            field_dict["parent_ou_id"] = parent_ou_id
        if parent_ou_name is not UNSET:
            field_dict["parent_ou_name"] = parent_ou_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_label_label_key is not UNSET:
            field_dict["project_label:<LABEL_KEY>"] = project_label_label_key
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if refund is not UNSET:
            field_dict["refund"] = refund
        if resource is not UNSET:
            field_dict["resource"] = resource
        if service is not UNSET:
            field_dict["service"] = service
        if tag_tag_key is not UNSET:
            field_dict["tag:<TAG_KEY>"] = tag_tag_key
        if unadjusted_spend is not UNSET:
            field_dict["unadjusted_spend"] = unadjusted_spend
        if unattributed_spend is not UNSET:
            field_dict["unattributed_spend"] = unattributed_spend

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        account_label_label_key = d.pop("account_label:<LABEL_KEY>", UNSET)

        account_name = d.pop("account_name", UNSET)

        account_number = d.pop("account_number", UNSET)

        attributed_spend = d.pop("attributed_spend", UNSET)

        billed_spend = d.pop("billed_spend", UNSET)

        def _parse_billing_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        billing_source_id = _parse_billing_source_id(d.pop("billing_source_id", UNSET))


        billing_source_name = d.pop("billing_source_name", UNSET)

        def _parse_cloud_service_provider_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_service_provider_id = _parse_cloud_service_provider_id(d.pop("cloud_service_provider_id", UNSET))


        cloud_service_provider_name = d.pop("cloud_service_provider_name", UNSET)

        configured_spend = d.pop("configured_spend", UNSET)

        credit = d.pop("credit", UNSET)

        list_spend = d.pop("list_spend", UNSET)

        month = d.pop("month", UNSET)

        net_attributed_spend = d.pop("net_attributed_spend", UNSET)

        net_billed_spend = d.pop("net_billed_spend", UNSET)

        net_list_spend = d.pop("net_list_spend", UNSET)

        net_unattributed_spend = d.pop("net_unattributed_spend", UNSET)

        def _parse_parent_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_ou_id = _parse_parent_ou_id(d.pop("parent_ou_id", UNSET))


        parent_ou_name = d.pop("parent_ou_name", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        project_label_label_key = d.pop("project_label:<LABEL_KEY>", UNSET)

        project_name = d.pop("project_name", UNSET)

        refund = d.pop("refund", UNSET)

        resource = d.pop("resource", UNSET)

        service = d.pop("service", UNSET)

        tag_tag_key = d.pop("tag:<TAG_KEY>", UNSET)

        unadjusted_spend = d.pop("unadjusted_spend", UNSET)

        unattributed_spend = d.pop("unattributed_spend", UNSET)

        api_v1_post_spend_report_query_response_object = cls(
            account_id=account_id,
            account_label_label_key=account_label_label_key,
            account_name=account_name,
            account_number=account_number,
            attributed_spend=attributed_spend,
            billed_spend=billed_spend,
            billing_source_id=billing_source_id,
            billing_source_name=billing_source_name,
            cloud_service_provider_id=cloud_service_provider_id,
            cloud_service_provider_name=cloud_service_provider_name,
            configured_spend=configured_spend,
            credit=credit,
            list_spend=list_spend,
            month=month,
            net_attributed_spend=net_attributed_spend,
            net_billed_spend=net_billed_spend,
            net_list_spend=net_list_spend,
            net_unattributed_spend=net_unattributed_spend,
            parent_ou_id=parent_ou_id,
            parent_ou_name=parent_ou_name,
            project_id=project_id,
            project_label_label_key=project_label_label_key,
            project_name=project_name,
            refund=refund,
            resource=resource,
            service=service,
            tag_tag_key=tag_tag_key,
            unadjusted_spend=unadjusted_spend,
            unattributed_spend=unattributed_spend,
        )


        api_v1_post_spend_report_query_response_object.additional_properties = d
        return api_v1_post_spend_report_query_response_object

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
