from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CustomBillingSourceAzureConnection")



@_attrs_define
class CustomBillingSourceAzureConnection:
    """ CustomBillingSourceAzureConnection defines the Azure storage connection for a custom
    billing source. Provide either credentialed_billing_source_id (reuse an existing Azure
    billing source's tenant credentials) or the tenant credential fields, not both.

        Attributes:
            credentialed_billing_source_id (int | None | Unset): ID of an existing Azure billing source whose tenant
                credentials will be used to
                access the storage account. Example: 12.
            storage_container (str | Unset): Storage container where the custom provider's financial data is stored.
                Example: billing-data.
            storage_prefix (str | Unset): Storage prefix inside the container where the custom provider's financial data is
                stored. Example: reports.
            storage_primary_endpoint (str | Unset): Primary blob endpoint of the storage account that holds the custom
                provider's
                financial data. Example: https://mystorage.blob.core.windows.net/.
            tenant_app_id (str | Unset): App registration (client) ID when providing tenant credentials directly. Example:
                00000000-1111-2222-3333-444444444444.
            tenant_client_secret (str | Unset): Client secret for the app registration. When updating an existing billing
                source,
                leaving blank will leave existing secret as-is. Example: REDACTED.
            tenant_cloud_partition_id (int | None | Unset): Cloud partition of the tenant when providing tenant credentials
                directly.
                1 = commercial, 2 = government, 3 = secret, 4 = top secret. Example: 1.
            tenant_domain (str | Unset): Tenant domain when providing tenant credentials directly. Example:
                mycompany.onmicrosoft.com.
     """

    credentialed_billing_source_id: int | None | Unset = UNSET
    storage_container: str | Unset = UNSET
    storage_prefix: str | Unset = UNSET
    storage_primary_endpoint: str | Unset = UNSET
    tenant_app_id: str | Unset = UNSET
    tenant_client_secret: str | Unset = UNSET
    tenant_cloud_partition_id: int | None | Unset = UNSET
    tenant_domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        credentialed_billing_source_id: int | None | Unset
        if isinstance(self.credentialed_billing_source_id, Unset):
            credentialed_billing_source_id = UNSET
        else:
            credentialed_billing_source_id = self.credentialed_billing_source_id

        storage_container = self.storage_container

        storage_prefix = self.storage_prefix

        storage_primary_endpoint = self.storage_primary_endpoint

        tenant_app_id = self.tenant_app_id

        tenant_client_secret = self.tenant_client_secret

        tenant_cloud_partition_id: int | None | Unset
        if isinstance(self.tenant_cloud_partition_id, Unset):
            tenant_cloud_partition_id = UNSET
        else:
            tenant_cloud_partition_id = self.tenant_cloud_partition_id

        tenant_domain = self.tenant_domain


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if credentialed_billing_source_id is not UNSET:
            field_dict["credentialed_billing_source_id"] = credentialed_billing_source_id
        if storage_container is not UNSET:
            field_dict["storage_container"] = storage_container
        if storage_prefix is not UNSET:
            field_dict["storage_prefix"] = storage_prefix
        if storage_primary_endpoint is not UNSET:
            field_dict["storage_primary_endpoint"] = storage_primary_endpoint
        if tenant_app_id is not UNSET:
            field_dict["tenant_app_id"] = tenant_app_id
        if tenant_client_secret is not UNSET:
            field_dict["tenant_client_secret"] = tenant_client_secret
        if tenant_cloud_partition_id is not UNSET:
            field_dict["tenant_cloud_partition_id"] = tenant_cloud_partition_id
        if tenant_domain is not UNSET:
            field_dict["tenant_domain"] = tenant_domain

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_credentialed_billing_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credentialed_billing_source_id = _parse_credentialed_billing_source_id(d.pop("credentialed_billing_source_id", UNSET))


        storage_container = d.pop("storage_container", UNSET)

        storage_prefix = d.pop("storage_prefix", UNSET)

        storage_primary_endpoint = d.pop("storage_primary_endpoint", UNSET)

        tenant_app_id = d.pop("tenant_app_id", UNSET)

        tenant_client_secret = d.pop("tenant_client_secret", UNSET)

        def _parse_tenant_cloud_partition_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tenant_cloud_partition_id = _parse_tenant_cloud_partition_id(d.pop("tenant_cloud_partition_id", UNSET))


        tenant_domain = d.pop("tenant_domain", UNSET)

        custom_billing_source_azure_connection = cls(
            credentialed_billing_source_id=credentialed_billing_source_id,
            storage_container=storage_container,
            storage_prefix=storage_prefix,
            storage_primary_endpoint=storage_primary_endpoint,
            tenant_app_id=tenant_app_id,
            tenant_client_secret=tenant_client_secret,
            tenant_cloud_partition_id=tenant_cloud_partition_id,
            tenant_domain=tenant_domain,
        )


        custom_billing_source_azure_connection.additional_properties = d
        return custom_billing_source_azure_connection

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
