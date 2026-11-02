from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CustomBillingSourceTestResults")



@_attrs_define
class CustomBillingSourceTestResults:
    """ CustomBillingSourceTestResults defines the results of a custom billing source test.

        Attributes:
            can_access_account (bool | None | Unset): When true, Kion is able to connect to the account where the custom
                billing reports are held. Example: True.
            can_access_storage (bool | None | Unset): When true, Kion is able to access the storage location for the custom
                billing reports. Example: True.
            newest_timestamp (datetime.datetime | Unset): The date and time of the most recently created report for this
                custom billing source. Example: 2019-12-19T11:59:25+0000.
            oldest_month (datetime.datetime | Unset): The first month with a report for this custom billing source. Example:
                2019-01.
            report_count (int | Unset): The number of reports found for this custom billing source. Example: 10.
            test_summary (str | Unset): Text summary of any issues discovered during the test. Example: Kion is unable to
                connect to the custom billing source account..
     """

    can_access_account: bool | None | Unset = UNSET
    can_access_storage: bool | None | Unset = UNSET
    newest_timestamp: datetime.datetime | Unset = UNSET
    oldest_month: datetime.datetime | Unset = UNSET
    report_count: int | Unset = UNSET
    test_summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_access_account: bool | None | Unset
        if isinstance(self.can_access_account, Unset):
            can_access_account = UNSET
        else:
            can_access_account = self.can_access_account

        can_access_storage: bool | None | Unset
        if isinstance(self.can_access_storage, Unset):
            can_access_storage = UNSET
        else:
            can_access_storage = self.can_access_storage

        newest_timestamp: str | Unset = UNSET
        if not isinstance(self.newest_timestamp, Unset):
            newest_timestamp = self.newest_timestamp.isoformat()

        oldest_month: str | Unset = UNSET
        if not isinstance(self.oldest_month, Unset):
            oldest_month = self.oldest_month.isoformat()

        report_count = self.report_count

        test_summary = self.test_summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_access_account is not UNSET:
            field_dict["can_access_account"] = can_access_account
        if can_access_storage is not UNSET:
            field_dict["can_access_storage"] = can_access_storage
        if newest_timestamp is not UNSET:
            field_dict["newest_timestamp"] = newest_timestamp
        if oldest_month is not UNSET:
            field_dict["oldest_month"] = oldest_month
        if report_count is not UNSET:
            field_dict["report_count"] = report_count
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


        def _parse_can_access_storage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_access_storage = _parse_can_access_storage(d.pop("can_access_storage", UNSET))


        _newest_timestamp = d.pop("newest_timestamp", UNSET)
        newest_timestamp: datetime.datetime | Unset
        if isinstance(_newest_timestamp,  Unset):
            newest_timestamp = UNSET
        else:
            newest_timestamp = datetime.datetime.fromisoformat(_newest_timestamp)




        _oldest_month = d.pop("oldest_month", UNSET)
        oldest_month: datetime.datetime | Unset
        if isinstance(_oldest_month,  Unset):
            oldest_month = UNSET
        else:
            oldest_month = datetime.datetime.fromisoformat(_oldest_month)




        report_count = d.pop("report_count", UNSET)

        test_summary = d.pop("test_summary", UNSET)

        custom_billing_source_test_results = cls(
            can_access_account=can_access_account,
            can_access_storage=can_access_storage,
            newest_timestamp=newest_timestamp,
            oldest_month=oldest_month,
            report_count=report_count,
            test_summary=test_summary,
        )


        custom_billing_source_test_results.additional_properties = d
        return custom_billing_source_test_results

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
