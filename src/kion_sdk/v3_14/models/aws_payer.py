from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AWSPayer")



@_attrs_define
class AWSPayer:
    """ AWSPayer defines the contents of an AWS payer.

        Attributes:
            account_number (str | Unset): AWS account number. Example: 121212121212.
            billing_bucket_account_number (str | Unset): Account number used to access S3 report bucket. Example:
                121212121212.
            billing_region (str | Unset): AWS billing region. Example: us-east-1.
            billing_report_bucket (str | Unset): S3 bucket containing monthly spend reports. Example:
                cloudtamer-12121212121212-hourly.
            billing_report_bucket_region (str | Unset): Region of the S3 bucket containing monthly spend reports. Example:
                us-east-1.
            billing_report_name (str | Unset): Name of billing reports stored in S3. Example:
                cloudtamer-12121212121212-hourly.
            billing_report_prefix (str | Unset): Prefix on billing reports. Example: report.
            billing_report_type (str | Unset): Specify the available billing report types for this Billing Source.
                Available options are:
                "none" - No proprietary billing report configured
                "cur" - Use the AWS Cost and Usage Report
                "dbrrt" - Use the AWS Detailed Billing Report with Resources and Tags
                If omitted, "cur" is assumed. Example: "cur".
            billing_start_date (str | Unset): Payer start date. Example: 2020-01.
            bucket_access_role (str | Unset): IAM role configured with trust policy. Example: service-role.
            detailed_billing_bucket (str | Unset): S3 buckets for detailed billing reports. Example: "my-billing-reports".
            focus_billing_bucket_account_number (str | Unset): Account number used to access S3 FOCUS report bucket.
                Example: 121212121212.
            focus_billing_report_bucket (str | Unset): S3 bucket containing FOCUS reports. Example:
                cloudtamer-12121212121212-focus.
            focus_billing_report_bucket_region (str | Unset): Region of the S3 bucket containing FOCUS reports. Example: us-
                east-1.
            focus_billing_report_name (str | Unset): Name of FOCUS billing reports stored in S3. Example:
                cloudtamer-12121212121212-focus.
            focus_billing_report_prefix (str | Unset): Prefix on FOCUS billing reports. Example: reports.
            focus_bucket_access_role (str | Unset): IAM role configured with trust policy for FOCUS reports. Example:
                service-role.
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the billing source. Example: My Master Payer.
            org_id (str | Unset): Organization ID. Example: 12345.
     """

    account_number: str | Unset = UNSET
    billing_bucket_account_number: str | Unset = UNSET
    billing_region: str | Unset = UNSET
    billing_report_bucket: str | Unset = UNSET
    billing_report_bucket_region: str | Unset = UNSET
    billing_report_name: str | Unset = UNSET
    billing_report_prefix: str | Unset = UNSET
    billing_report_type: str | Unset = UNSET
    billing_start_date: str | Unset = UNSET
    bucket_access_role: str | Unset = UNSET
    detailed_billing_bucket: str | Unset = UNSET
    focus_billing_bucket_account_number: str | Unset = UNSET
    focus_billing_report_bucket: str | Unset = UNSET
    focus_billing_report_bucket_region: str | Unset = UNSET
    focus_billing_report_name: str | Unset = UNSET
    focus_billing_report_prefix: str | Unset = UNSET
    focus_bucket_access_role: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    org_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        billing_bucket_account_number = self.billing_bucket_account_number

        billing_region = self.billing_region

        billing_report_bucket = self.billing_report_bucket

        billing_report_bucket_region = self.billing_report_bucket_region

        billing_report_name = self.billing_report_name

        billing_report_prefix = self.billing_report_prefix

        billing_report_type = self.billing_report_type

        billing_start_date = self.billing_start_date

        bucket_access_role = self.bucket_access_role

        detailed_billing_bucket = self.detailed_billing_bucket

        focus_billing_bucket_account_number = self.focus_billing_bucket_account_number

        focus_billing_report_bucket = self.focus_billing_report_bucket

        focus_billing_report_bucket_region = self.focus_billing_report_bucket_region

        focus_billing_report_name = self.focus_billing_report_name

        focus_billing_report_prefix = self.focus_billing_report_prefix

        focus_bucket_access_role = self.focus_bucket_access_role

        id = self.id

        name = self.name

        org_id = self.org_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if billing_bucket_account_number is not UNSET:
            field_dict["billing_bucket_account_number"] = billing_bucket_account_number
        if billing_region is not UNSET:
            field_dict["billing_region"] = billing_region
        if billing_report_bucket is not UNSET:
            field_dict["billing_report_bucket"] = billing_report_bucket
        if billing_report_bucket_region is not UNSET:
            field_dict["billing_report_bucket_region"] = billing_report_bucket_region
        if billing_report_name is not UNSET:
            field_dict["billing_report_name"] = billing_report_name
        if billing_report_prefix is not UNSET:
            field_dict["billing_report_prefix"] = billing_report_prefix
        if billing_report_type is not UNSET:
            field_dict["billing_report_type"] = billing_report_type
        if billing_start_date is not UNSET:
            field_dict["billing_start_date"] = billing_start_date
        if bucket_access_role is not UNSET:
            field_dict["bucket_access_role"] = bucket_access_role
        if detailed_billing_bucket is not UNSET:
            field_dict["detailed_billing_bucket"] = detailed_billing_bucket
        if focus_billing_bucket_account_number is not UNSET:
            field_dict["focus_billing_bucket_account_number"] = focus_billing_bucket_account_number
        if focus_billing_report_bucket is not UNSET:
            field_dict["focus_billing_report_bucket"] = focus_billing_report_bucket
        if focus_billing_report_bucket_region is not UNSET:
            field_dict["focus_billing_report_bucket_region"] = focus_billing_report_bucket_region
        if focus_billing_report_name is not UNSET:
            field_dict["focus_billing_report_name"] = focus_billing_report_name
        if focus_billing_report_prefix is not UNSET:
            field_dict["focus_billing_report_prefix"] = focus_billing_report_prefix
        if focus_bucket_access_role is not UNSET:
            field_dict["focus_bucket_access_role"] = focus_bucket_access_role
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_number = d.pop("account_number", UNSET)

        billing_bucket_account_number = d.pop("billing_bucket_account_number", UNSET)

        billing_region = d.pop("billing_region", UNSET)

        billing_report_bucket = d.pop("billing_report_bucket", UNSET)

        billing_report_bucket_region = d.pop("billing_report_bucket_region", UNSET)

        billing_report_name = d.pop("billing_report_name", UNSET)

        billing_report_prefix = d.pop("billing_report_prefix", UNSET)

        billing_report_type = d.pop("billing_report_type", UNSET)

        billing_start_date = d.pop("billing_start_date", UNSET)

        bucket_access_role = d.pop("bucket_access_role", UNSET)

        detailed_billing_bucket = d.pop("detailed_billing_bucket", UNSET)

        focus_billing_bucket_account_number = d.pop("focus_billing_bucket_account_number", UNSET)

        focus_billing_report_bucket = d.pop("focus_billing_report_bucket", UNSET)

        focus_billing_report_bucket_region = d.pop("focus_billing_report_bucket_region", UNSET)

        focus_billing_report_name = d.pop("focus_billing_report_name", UNSET)

        focus_billing_report_prefix = d.pop("focus_billing_report_prefix", UNSET)

        focus_bucket_access_role = d.pop("focus_bucket_access_role", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        org_id = d.pop("org_id", UNSET)

        aws_payer = cls(
            account_number=account_number,
            billing_bucket_account_number=billing_bucket_account_number,
            billing_region=billing_region,
            billing_report_bucket=billing_report_bucket,
            billing_report_bucket_region=billing_report_bucket_region,
            billing_report_name=billing_report_name,
            billing_report_prefix=billing_report_prefix,
            billing_report_type=billing_report_type,
            billing_start_date=billing_start_date,
            bucket_access_role=bucket_access_role,
            detailed_billing_bucket=detailed_billing_bucket,
            focus_billing_bucket_account_number=focus_billing_bucket_account_number,
            focus_billing_report_bucket=focus_billing_report_bucket,
            focus_billing_report_bucket_region=focus_billing_report_bucket_region,
            focus_billing_report_name=focus_billing_report_name,
            focus_billing_report_prefix=focus_billing_report_prefix,
            focus_bucket_access_role=focus_bucket_access_role,
            id=id,
            name=name,
            org_id=org_id,
        )


        aws_payer.additional_properties = d
        return aws_payer

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
