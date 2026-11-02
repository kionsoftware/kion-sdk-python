from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AWSBillingSourceTestResults")



@_attrs_define
class AWSBillingSourceTestResults:
    """ AWSBillingSourceTestResults defines the results of a billing source test.

        Attributes:
            can_access_account (bool | None | Unset): When true, cloudtamer is able to connect to the account where the
                billing reports are held. Example: True.
            can_access_cur_bucket (bool | None | Unset): When true, cloudtamer is able to access the cost and usage report
                bucket. Example: True.
            can_access_focus_account (bool | None | Unset): When true, cloudtamer is able to access the FOCUS account.
                Example: True.
            can_access_focus_bucket (bool | None | Unset): When true, cloudtamer is able to access the cost and usage report
                bucket. Example: True.
            can_access_mr_bucket (bool | None | Unset): When true, cloudtamer is able to access the monthly report bucket.
                Example: True.
            cost_and_usage_report_count (int | Unset): The number of cost and usage reports found for this billing source.
                Example: 10.
            dbrrt_report_count (int | Unset): The number of Detailed Billing Report with Resources and Tags reports found
                for this billing source. Example: 10.
            focus_report_count (int | Unset): The number of FOCUS reports found for this billing source. Example: 10.
            focus_test_summary (str | Unset): Text summary of any issues discovered during the FOCUS test. Example:
                Cloudtamer is unable to connect to the FOCUS account..
            newest_cur_timestamp (str | Unset): The date and time the most recent cost and usage report was created.
                Example: 2019-12-19T06:35:31+0000.
            newest_dbrrt_timestamp (str | Unset): The date and time of the most recently created Detailed Billing Report
                with Resources and Tags. Example: 2019-12-19T11:59:25+0000.
            newest_focus_timestamp (str | Unset): The date and time the most recent FOCUS report was created. Example:
                2019-12-19T06:35:31+0000.
            oldest_cur_month (str | Unset): The first month with a cost and usage report. Example: 2019-01.
            oldest_dbrrt_month (str | Unset): The first month with a Detailed Billing Report with Resources and Tags.
                Example: 2019-01.
            oldest_focus_month (str | Unset): The first month with a FOCUS report. Example: 2019-01.
            test_summary (str | Unset): Text summary of any issues discovered during the test. Example: Cloudtamer is unable
                to connect to the aws account..
     """

    can_access_account: bool | None | Unset = UNSET
    can_access_cur_bucket: bool | None | Unset = UNSET
    can_access_focus_account: bool | None | Unset = UNSET
    can_access_focus_bucket: bool | None | Unset = UNSET
    can_access_mr_bucket: bool | None | Unset = UNSET
    cost_and_usage_report_count: int | Unset = UNSET
    dbrrt_report_count: int | Unset = UNSET
    focus_report_count: int | Unset = UNSET
    focus_test_summary: str | Unset = UNSET
    newest_cur_timestamp: str | Unset = UNSET
    newest_dbrrt_timestamp: str | Unset = UNSET
    newest_focus_timestamp: str | Unset = UNSET
    oldest_cur_month: str | Unset = UNSET
    oldest_dbrrt_month: str | Unset = UNSET
    oldest_focus_month: str | Unset = UNSET
    test_summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_access_account: bool | None | Unset
        if isinstance(self.can_access_account, Unset):
            can_access_account = UNSET
        else:
            can_access_account = self.can_access_account

        can_access_cur_bucket: bool | None | Unset
        if isinstance(self.can_access_cur_bucket, Unset):
            can_access_cur_bucket = UNSET
        else:
            can_access_cur_bucket = self.can_access_cur_bucket

        can_access_focus_account: bool | None | Unset
        if isinstance(self.can_access_focus_account, Unset):
            can_access_focus_account = UNSET
        else:
            can_access_focus_account = self.can_access_focus_account

        can_access_focus_bucket: bool | None | Unset
        if isinstance(self.can_access_focus_bucket, Unset):
            can_access_focus_bucket = UNSET
        else:
            can_access_focus_bucket = self.can_access_focus_bucket

        can_access_mr_bucket: bool | None | Unset
        if isinstance(self.can_access_mr_bucket, Unset):
            can_access_mr_bucket = UNSET
        else:
            can_access_mr_bucket = self.can_access_mr_bucket

        cost_and_usage_report_count = self.cost_and_usage_report_count

        dbrrt_report_count = self.dbrrt_report_count

        focus_report_count = self.focus_report_count

        focus_test_summary = self.focus_test_summary

        newest_cur_timestamp = self.newest_cur_timestamp

        newest_dbrrt_timestamp = self.newest_dbrrt_timestamp

        newest_focus_timestamp = self.newest_focus_timestamp

        oldest_cur_month = self.oldest_cur_month

        oldest_dbrrt_month = self.oldest_dbrrt_month

        oldest_focus_month = self.oldest_focus_month

        test_summary = self.test_summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_access_account is not UNSET:
            field_dict["can_access_account"] = can_access_account
        if can_access_cur_bucket is not UNSET:
            field_dict["can_access_cur_bucket"] = can_access_cur_bucket
        if can_access_focus_account is not UNSET:
            field_dict["can_access_focus_account"] = can_access_focus_account
        if can_access_focus_bucket is not UNSET:
            field_dict["can_access_focus_bucket"] = can_access_focus_bucket
        if can_access_mr_bucket is not UNSET:
            field_dict["can_access_mr_bucket"] = can_access_mr_bucket
        if cost_and_usage_report_count is not UNSET:
            field_dict["cost_and_usage_report_count"] = cost_and_usage_report_count
        if dbrrt_report_count is not UNSET:
            field_dict["dbrrt_report_count"] = dbrrt_report_count
        if focus_report_count is not UNSET:
            field_dict["focus_report_count"] = focus_report_count
        if focus_test_summary is not UNSET:
            field_dict["focus_test_summary"] = focus_test_summary
        if newest_cur_timestamp is not UNSET:
            field_dict["newest_cur_timestamp"] = newest_cur_timestamp
        if newest_dbrrt_timestamp is not UNSET:
            field_dict["newest_dbrrt_timestamp"] = newest_dbrrt_timestamp
        if newest_focus_timestamp is not UNSET:
            field_dict["newest_focus_timestamp"] = newest_focus_timestamp
        if oldest_cur_month is not UNSET:
            field_dict["oldest_cur_month"] = oldest_cur_month
        if oldest_dbrrt_month is not UNSET:
            field_dict["oldest_dbrrt_month"] = oldest_dbrrt_month
        if oldest_focus_month is not UNSET:
            field_dict["oldest_focus_month"] = oldest_focus_month
        if test_summary is not UNSET:
            field_dict["test_summary"] = test_summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_can_access_account(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_access_account = _parse_can_access_account(d.pop("can_access_account", UNSET))


        def _parse_can_access_cur_bucket(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_access_cur_bucket = _parse_can_access_cur_bucket(d.pop("can_access_cur_bucket", UNSET))


        def _parse_can_access_focus_account(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_access_focus_account = _parse_can_access_focus_account(d.pop("can_access_focus_account", UNSET))


        def _parse_can_access_focus_bucket(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_access_focus_bucket = _parse_can_access_focus_bucket(d.pop("can_access_focus_bucket", UNSET))


        def _parse_can_access_mr_bucket(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_access_mr_bucket = _parse_can_access_mr_bucket(d.pop("can_access_mr_bucket", UNSET))


        cost_and_usage_report_count = d.pop("cost_and_usage_report_count", UNSET)

        dbrrt_report_count = d.pop("dbrrt_report_count", UNSET)

        focus_report_count = d.pop("focus_report_count", UNSET)

        focus_test_summary = d.pop("focus_test_summary", UNSET)

        newest_cur_timestamp = d.pop("newest_cur_timestamp", UNSET)

        newest_dbrrt_timestamp = d.pop("newest_dbrrt_timestamp", UNSET)

        newest_focus_timestamp = d.pop("newest_focus_timestamp", UNSET)

        oldest_cur_month = d.pop("oldest_cur_month", UNSET)

        oldest_dbrrt_month = d.pop("oldest_dbrrt_month", UNSET)

        oldest_focus_month = d.pop("oldest_focus_month", UNSET)

        test_summary = d.pop("test_summary", UNSET)

        aws_billing_source_test_results = cls(
            can_access_account=can_access_account,
            can_access_cur_bucket=can_access_cur_bucket,
            can_access_focus_account=can_access_focus_account,
            can_access_focus_bucket=can_access_focus_bucket,
            can_access_mr_bucket=can_access_mr_bucket,
            cost_and_usage_report_count=cost_and_usage_report_count,
            dbrrt_report_count=dbrrt_report_count,
            focus_report_count=focus_report_count,
            focus_test_summary=focus_test_summary,
            newest_cur_timestamp=newest_cur_timestamp,
            newest_dbrrt_timestamp=newest_dbrrt_timestamp,
            newest_focus_timestamp=newest_focus_timestamp,
            oldest_cur_month=oldest_cur_month,
            oldest_dbrrt_month=oldest_dbrrt_month,
            oldest_focus_month=oldest_focus_month,
            test_summary=test_summary,
        )


        aws_billing_source_test_results.additional_properties = d
        return aws_billing_source_test_results

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
