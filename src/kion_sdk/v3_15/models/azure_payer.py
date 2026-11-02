from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzurePayer")



@_attrs_define
class AzurePayer:
    """ AzurePayer defines the contents of an Azure payer.

        Attributes:
            app_id (str | Unset): Application ID. Example: 12345.
            azure_csp_id (int | None | Unset): ID of Azure CSP. Example: 1.
            billing_start_date (str | Unset): Payer start date. Example: 2020-01.
            customer_id (str | Unset): Customer ID. Example: 12345-abcd-1234-abcd-12345abcdef.
            domain (str | Unset): CSP Domain. Example: csp.domain.com.
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the CSP. Example: My Master Payer.
            primary_management_group_azure_id (str | Unset): Primary management group ID. Example: abc123.
     """

    app_id: str | Unset = UNSET
    azure_csp_id: int | None | Unset = UNSET
    billing_start_date: str | Unset = UNSET
    customer_id: str | Unset = UNSET
    domain: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    primary_management_group_azure_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        azure_csp_id: int | None | Unset
        if isinstance(self.azure_csp_id, Unset):
            azure_csp_id = UNSET
        else:
            azure_csp_id = self.azure_csp_id

        billing_start_date = self.billing_start_date

        customer_id = self.customer_id

        domain = self.domain

        id = self.id

        name = self.name

        primary_management_group_azure_id = self.primary_management_group_azure_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if azure_csp_id is not UNSET:
            field_dict["azure_csp_id"] = azure_csp_id
        if billing_start_date is not UNSET:
            field_dict["billing_start_date"] = billing_start_date
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if primary_management_group_azure_id is not UNSET:
            field_dict["primary_management_group_azure_id"] = primary_management_group_azure_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        def _parse_azure_csp_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        azure_csp_id = _parse_azure_csp_id(d.pop("azure_csp_id", UNSET))


        billing_start_date = d.pop("billing_start_date", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        domain = d.pop("domain", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        primary_management_group_azure_id = d.pop("primary_management_group_azure_id", UNSET)

        azure_payer = cls(
            app_id=app_id,
            azure_csp_id=azure_csp_id,
            billing_start_date=billing_start_date,
            customer_id=customer_id,
            domain=domain,
            id=id,
            name=name,
            primary_management_group_azure_id=primary_management_group_azure_id,
        )


        azure_payer.additional_properties = d
        return azure_payer

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
