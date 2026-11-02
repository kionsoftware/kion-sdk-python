from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AWSBillingSourceCreateWithValidation")



@_attrs_define
class AWSBillingSourceCreateWithValidation:
    """ AWSBillingSourceCreateWithValidation defines a billing source used for testing and creation with validation

        Attributes:
            account_type_id (int | None): The Account Type ID is the corresponding billing source account's type.
                1 - AWS Commercial
                2 - Govcloud
                4 - AWS C2S
                5 - AWS SC2S Example: 1.
            aws_account_number (str): AWS Account Number of the master billing account Example: 121212121212.
            billing_start_date (str): Start date of billing source (YYYY-MM). Example: 2019-01.
            linked_role (str): Enter the name of an existing IAM role that has full administrator permissions. If you do not
                have a custom role, we suggest using Amazon's default OrganizationAccountAccessRole. The role you enter here
                will be prefilled as the linked role when creating or importing new accounts under this billing source. Example:
                OrganizationAccountAccessRole.
            name (str): Name of the billing source. Example: My Master Payer.
            account_creation (bool | None | Unset): When true, cloudtamer is able to automatically create accounts in this
                billing source.
            billing_bucket_account_number (str | Unset): AWS Account Number of the s3 bucket holding the billing reports
                Example: 121212121212.
            billing_region (str | Unset): Region of the s3 bucket holding billing reports (both CUR and DBR reports)
                Example: us-east-1.
            billing_report_type (str | Unset): Specify the available billing report types for this Billing Source.
                Available options are:
                "none" - Do not use any proprietary billing report
                "cur" - Use the AWS Cost and Usage Report
                "dbrrt" - Use the AWS Detailed Billing Report with Resources and Tags
                If omitted, "cur" is assumed. Example: "cur".
            bucket_access_role (str | Unset): Alternate role for accessing the billing buckets (optional). Example: my-
                custom-role.
            cur_bucket (str | Unset): Name of the bucket containing the cost and usage reports. Required if not using only
                DBR Example: cloudtamer-121212121212-hourly.
            cur_bucket_region (str | Unset): Region of the bucket containing the cost and usage reports. Required if not
                using only DBR Example: us-east-1.
            cur_name (str | Unset): Name of the cost and usage report. Required if not using only DBR Example:
                cloudtamer-121212121212-hourly.
            cur_prefix (str | Unset): Report prefix for the cost and usage reports. Required if not using only DBR Example:
                report.
            focus_billing_bucket_account_number (str | Unset): AWS Account Number of the s3 bucket holding the FOCUS reports
                Example: 121212121212.
            focus_billing_report_bucket (str | Unset): Name of the bucket containing the FOCUS reports Example:
                cloudtamer-121212121212-focus.
            focus_billing_report_bucket_region (str | Unset): Region of the bucket containing the FOCUS reports Example: us-
                east-1.
            focus_billing_report_name (str | Unset): Name of the FOCUS billing report Example:
                cloudtamer-121212121212-focus.
            focus_billing_report_prefix (str | Unset): Prefix for the FOCUS billing reports Example: focus.
            focus_bucket_access_role (str | Unset): Alternate role for accessing the focus billing buckets (optional).
                Example: my-custom-role.
            key_id (str | Unset): The AWS Access Key used to access the billing s3 bucket Example: AKIA1234567890123456.
            key_secret (str | Unset): The AWS Secret Access Key used to access the billing s3 bucket Example:
                ABCabcdAB1ABcABCDEFabcdeABaAbA1a1abCdA1a.
            mr_bucket (str | Unset): Name of the bucket containing the monthly reports (detailed billing reports). Only
                required when Only CUR is false Example: cloudtamer-121212121212-hourly.
            only_dbr (bool | None | Unset): DEPRECATED: Use billing_report_type to specify your billing report type
                Only use the Detailed Billing Report and Detailed Billing Report With Resources And Tags for financial reports.
                Example: True.
            skip_validation (bool | None | Unset): When true, will skip validating the connection to the billing source
            use_focus_reports (bool | None | Unset): Use FOCUS Reports - If true, cloudtamer will use FOCUS reports for this
                billing source Example: True.
     """

    account_type_id: int | None
    aws_account_number: str
    billing_start_date: str
    linked_role: str
    name: str
    account_creation: bool | None | Unset = UNSET
    billing_bucket_account_number: str | Unset = UNSET
    billing_region: str | Unset = UNSET
    billing_report_type: str | Unset = UNSET
    bucket_access_role: str | Unset = UNSET
    cur_bucket: str | Unset = UNSET
    cur_bucket_region: str | Unset = UNSET
    cur_name: str | Unset = UNSET
    cur_prefix: str | Unset = UNSET
    focus_billing_bucket_account_number: str | Unset = UNSET
    focus_billing_report_bucket: str | Unset = UNSET
    focus_billing_report_bucket_region: str | Unset = UNSET
    focus_billing_report_name: str | Unset = UNSET
    focus_billing_report_prefix: str | Unset = UNSET
    focus_bucket_access_role: str | Unset = UNSET
    key_id: str | Unset = UNSET
    key_secret: str | Unset = UNSET
    mr_bucket: str | Unset = UNSET
    only_dbr: bool | None | Unset = UNSET
    skip_validation: bool | None | Unset = UNSET
    use_focus_reports: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_type_id: int | None
        account_type_id = self.account_type_id

        aws_account_number = self.aws_account_number

        billing_start_date = self.billing_start_date

        linked_role = self.linked_role

        name = self.name

        account_creation: bool | None | Unset
        if isinstance(self.account_creation, Unset):
            account_creation = UNSET
        else:
            account_creation = self.account_creation

        billing_bucket_account_number = self.billing_bucket_account_number

        billing_region = self.billing_region

        billing_report_type = self.billing_report_type

        bucket_access_role = self.bucket_access_role

        cur_bucket = self.cur_bucket

        cur_bucket_region = self.cur_bucket_region

        cur_name = self.cur_name

        cur_prefix = self.cur_prefix

        focus_billing_bucket_account_number = self.focus_billing_bucket_account_number

        focus_billing_report_bucket = self.focus_billing_report_bucket

        focus_billing_report_bucket_region = self.focus_billing_report_bucket_region

        focus_billing_report_name = self.focus_billing_report_name

        focus_billing_report_prefix = self.focus_billing_report_prefix

        focus_bucket_access_role = self.focus_bucket_access_role

        key_id = self.key_id

        key_secret = self.key_secret

        mr_bucket = self.mr_bucket

        only_dbr: bool | None | Unset
        if isinstance(self.only_dbr, Unset):
            only_dbr = UNSET
        else:
            only_dbr = self.only_dbr

        skip_validation: bool | None | Unset
        if isinstance(self.skip_validation, Unset):
            skip_validation = UNSET
        else:
            skip_validation = self.skip_validation

        use_focus_reports: bool | None | Unset
        if isinstance(self.use_focus_reports, Unset):
            use_focus_reports = UNSET
        else:
            use_focus_reports = self.use_focus_reports


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_type_id": account_type_id,
            "aws_account_number": aws_account_number,
            "billing_start_date": billing_start_date,
            "linked_role": linked_role,
            "name": name,
        })
        if account_creation is not UNSET:
            field_dict["account_creation"] = account_creation
        if billing_bucket_account_number is not UNSET:
            field_dict["billing_bucket_account_number"] = billing_bucket_account_number
        if billing_region is not UNSET:
            field_dict["billing_region"] = billing_region
        if billing_report_type is not UNSET:
            field_dict["billing_report_type"] = billing_report_type
        if bucket_access_role is not UNSET:
            field_dict["bucket_access_role"] = bucket_access_role
        if cur_bucket is not UNSET:
            field_dict["cur_bucket"] = cur_bucket
        if cur_bucket_region is not UNSET:
            field_dict["cur_bucket_region"] = cur_bucket_region
        if cur_name is not UNSET:
            field_dict["cur_name"] = cur_name
        if cur_prefix is not UNSET:
            field_dict["cur_prefix"] = cur_prefix
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
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if key_secret is not UNSET:
            field_dict["key_secret"] = key_secret
        if mr_bucket is not UNSET:
            field_dict["mr_bucket"] = mr_bucket
        if only_dbr is not UNSET:
            field_dict["only_dbr"] = only_dbr
        if skip_validation is not UNSET:
            field_dict["skip_validation"] = skip_validation
        if use_focus_reports is not UNSET:
            field_dict["use_focus_reports"] = use_focus_reports

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id"))


        aws_account_number = d.pop("aws_account_number")

        billing_start_date = d.pop("billing_start_date")

        linked_role = d.pop("linked_role")

        name = d.pop("name")

        def _parse_account_creation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        account_creation = _parse_account_creation(d.pop("account_creation", UNSET))


        billing_bucket_account_number = d.pop("billing_bucket_account_number", UNSET)

        billing_region = d.pop("billing_region", UNSET)

        billing_report_type = d.pop("billing_report_type", UNSET)

        bucket_access_role = d.pop("bucket_access_role", UNSET)

        cur_bucket = d.pop("cur_bucket", UNSET)

        cur_bucket_region = d.pop("cur_bucket_region", UNSET)

        cur_name = d.pop("cur_name", UNSET)

        cur_prefix = d.pop("cur_prefix", UNSET)

        focus_billing_bucket_account_number = d.pop("focus_billing_bucket_account_number", UNSET)

        focus_billing_report_bucket = d.pop("focus_billing_report_bucket", UNSET)

        focus_billing_report_bucket_region = d.pop("focus_billing_report_bucket_region", UNSET)

        focus_billing_report_name = d.pop("focus_billing_report_name", UNSET)

        focus_billing_report_prefix = d.pop("focus_billing_report_prefix", UNSET)

        focus_bucket_access_role = d.pop("focus_bucket_access_role", UNSET)

        key_id = d.pop("key_id", UNSET)

        key_secret = d.pop("key_secret", UNSET)

        mr_bucket = d.pop("mr_bucket", UNSET)

        def _parse_only_dbr(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        only_dbr = _parse_only_dbr(d.pop("only_dbr", UNSET))


        def _parse_skip_validation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_validation = _parse_skip_validation(d.pop("skip_validation", UNSET))


        def _parse_use_focus_reports(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_focus_reports = _parse_use_focus_reports(d.pop("use_focus_reports", UNSET))


        aws_billing_source_create_with_validation = cls(
            account_type_id=account_type_id,
            aws_account_number=aws_account_number,
            billing_start_date=billing_start_date,
            linked_role=linked_role,
            name=name,
            account_creation=account_creation,
            billing_bucket_account_number=billing_bucket_account_number,
            billing_region=billing_region,
            billing_report_type=billing_report_type,
            bucket_access_role=bucket_access_role,
            cur_bucket=cur_bucket,
            cur_bucket_region=cur_bucket_region,
            cur_name=cur_name,
            cur_prefix=cur_prefix,
            focus_billing_bucket_account_number=focus_billing_bucket_account_number,
            focus_billing_report_bucket=focus_billing_report_bucket,
            focus_billing_report_bucket_region=focus_billing_report_bucket_region,
            focus_billing_report_name=focus_billing_report_name,
            focus_billing_report_prefix=focus_billing_report_prefix,
            focus_bucket_access_role=focus_bucket_access_role,
            key_id=key_id,
            key_secret=key_secret,
            mr_bucket=mr_bucket,
            only_dbr=only_dbr,
            skip_validation=skip_validation,
            use_focus_reports=use_focus_reports,
        )


        aws_billing_source_create_with_validation.additional_properties = d
        return aws_billing_source_create_with_validation

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
