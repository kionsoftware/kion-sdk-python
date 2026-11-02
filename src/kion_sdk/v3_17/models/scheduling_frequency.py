from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="SchedulingFrequency")



@_attrs_define
class SchedulingFrequency:
    """ 
        Attributes:
            validate_scheduling (bool | None | Unset):
            day_of_month (int | Unset): Day of month on which report should be sent. Only used for monthly frequency.
                Default: 1. Example: 1.
            day_of_quarter (int | Unset): Day of quarter on which report should be sent. Only used for quarterly frequency.
                Valid values: 1 for first day of quarter, 2 for last day of quarter. Default: 1. Example: 1.
            days_of_week (list[int] | None | Unset): Days of week on which the report should be sent. Only used for daily
                and weekly frequency.
                Valid values are 0 for Sunday through 6 for Saturday. Example: [2, 4, 6].
            end_date (datetime.datetime | Unset): Ending timestamp for when to stop the report schedule. Continues
                indefinitely if omitted. Example: 2025-10-20T14:48:00Z.
            frequency_type (int | Unset): Period type of the scheduling.
                Valid values: 0 for daily, 1 for weekly, 2 for monthly, 3 for quarterly. Example: 1.
            hour (int | Unset): Hour at which the report should be sent. Uses 24 hour clock.
                Values that are out of range will be adjusted to the nearest valid hour. Example: 12.
            minute (int | Unset): Minute at which the report should be sent.
                Values that are out of range will be adjusted to the nearest valid minute.

                30
            start_date (datetime.datetime | Unset): Starting timestamp for when to begin the report schedule. Defaults to
                current date if not provided. Example: 2025-10-10T14:48:00Z.
            time_zone_identifier (str | Unset): Timezone identifier for the time at which the report should be sent.
                Uses IANA time zone identifiers. Default: 'GMT'. Example: America/New_York.
            weekly_recurrence (int | Unset): Weekly recurrence schedule, e.g. repeat every x weeks. Only used for weekly
                frequency. Default: 1. Example: 1.
     """

    validate_scheduling: bool | None | Unset = UNSET
    day_of_month: int | Unset = 1
    day_of_quarter: int | Unset = 1
    days_of_week: list[int] | None | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    frequency_type: int | Unset = UNSET
    hour: int | Unset = UNSET
    minute: int | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    time_zone_identifier: str | Unset = 'GMT'
    weekly_recurrence: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        validate_scheduling: bool | None | Unset
        if isinstance(self.validate_scheduling, Unset):
            validate_scheduling = UNSET
        else:
            validate_scheduling = self.validate_scheduling

        day_of_month = self.day_of_month

        day_of_quarter = self.day_of_quarter

        days_of_week: list[int] | None | Unset
        if isinstance(self.days_of_week, Unset):
            days_of_week = UNSET
        elif isinstance(self.days_of_week, list):
            days_of_week = self.days_of_week


        else:
            days_of_week = self.days_of_week

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        frequency_type = self.frequency_type

        hour = self.hour

        minute = self.minute

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        time_zone_identifier = self.time_zone_identifier

        weekly_recurrence = self.weekly_recurrence


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if validate_scheduling is not UNSET:
            field_dict["ValidateScheduling"] = validate_scheduling
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if day_of_quarter is not UNSET:
            field_dict["day_of_quarter"] = day_of_quarter
        if days_of_week is not UNSET:
            field_dict["days_of_week"] = days_of_week
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if frequency_type is not UNSET:
            field_dict["frequency_type"] = frequency_type
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if time_zone_identifier is not UNSET:
            field_dict["time_zone_identifier"] = time_zone_identifier
        if weekly_recurrence is not UNSET:
            field_dict["weekly_recurrence"] = weekly_recurrence

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_validate_scheduling(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        validate_scheduling = _parse_validate_scheduling(d.pop("ValidateScheduling", UNSET))


        day_of_month = d.pop("day_of_month", UNSET)

        day_of_quarter = d.pop("day_of_quarter", UNSET)

        def _parse_days_of_week(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_of_week_type_0 = cast(list[int], data)

                return days_of_week_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        days_of_week = _parse_days_of_week(d.pop("days_of_week", UNSET))


        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.datetime.fromisoformat(_end_date)




        frequency_type = d.pop("frequency_type", UNSET)

        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.datetime.fromisoformat(_start_date)




        time_zone_identifier = d.pop("time_zone_identifier", UNSET)

        weekly_recurrence = d.pop("weekly_recurrence", UNSET)

        scheduling_frequency = cls(
            validate_scheduling=validate_scheduling,
            day_of_month=day_of_month,
            day_of_quarter=day_of_quarter,
            days_of_week=days_of_week,
            end_date=end_date,
            frequency_type=frequency_type,
            hour=hour,
            minute=minute,
            start_date=start_date,
            time_zone_identifier=time_zone_identifier,
            weekly_recurrence=weekly_recurrence,
        )


        scheduling_frequency.additional_properties = d
        return scheduling_frequency

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
