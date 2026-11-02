from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomBillingSourceAWSConnectionUpdate")



@_attrs_define
class CustomBillingSourceAWSConnectionUpdate:
    """ 
        Attributes:
            account_number (str | Unset): The AWS Account Number that holds FOCUS financial data for the custom provider.
                Example: 123456789012.
            bucket_access_role (str | Unset): The role name that has access to the listed account number. Example:
                my_custom_role.
            storage_bucket (str | Unset): Storage bucket where the custom provider's financial data is stored. Example:
                custom-provider-financial-data.
            storage_prefix (str | Unset): Storage prefix inside the billing report bucket where the custom provider's
                financial data is stored. Example: report.
            storage_region (str | Unset): Storage region where the custom provider's financial data is stored. Example: us-
                east-1.
     """

    account_number: str | Unset = UNSET
    bucket_access_role: str | Unset = UNSET
    storage_bucket: str | Unset = UNSET
    storage_prefix: str | Unset = UNSET
    storage_region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        bucket_access_role = self.bucket_access_role

        storage_bucket = self.storage_bucket

        storage_prefix = self.storage_prefix

        storage_region = self.storage_region


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if bucket_access_role is not UNSET:
            field_dict["bucket_access_role"] = bucket_access_role
        if storage_bucket is not UNSET:
            field_dict["storage_bucket"] = storage_bucket
        if storage_prefix is not UNSET:
            field_dict["storage_prefix"] = storage_prefix
        if storage_region is not UNSET:
            field_dict["storage_region"] = storage_region

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number = d.pop("account_number", UNSET)

        bucket_access_role = d.pop("bucket_access_role", UNSET)

        storage_bucket = d.pop("storage_bucket", UNSET)

        storage_prefix = d.pop("storage_prefix", UNSET)

        storage_region = d.pop("storage_region", UNSET)

        custom_billing_source_aws_connection_update = cls(
            account_number=account_number,
            bucket_access_role=bucket_access_role,
            storage_bucket=storage_bucket,
            storage_prefix=storage_prefix,
            storage_region=storage_region,
        )


        custom_billing_source_aws_connection_update.additional_properties = d
        return custom_billing_source_aws_connection_update

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
