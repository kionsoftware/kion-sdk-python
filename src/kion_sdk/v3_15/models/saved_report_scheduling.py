from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scheduling_frequency import SchedulingFrequency





T = TypeVar("T", bound="SavedReportScheduling")



@_attrs_define
class SavedReportScheduling:
    """ 
        Attributes:
            external_emails (list[str] | None | Unset): List of external email addresses to include when sending the report.
                Should not include user emails from shared users. Example: ['user@testmail.com'].
            saved_report_scheduled_frequency (SchedulingFrequency | Unset):
            scheduled (bool | None | Unset): Whether the saved report should be scheduled.
                All other properties will be ignored if set to false. Example: True.
            scheduled_email_message (str | Unset): Custom message for sent report email. Will use default message if
                excluded. Example: EmailMessage.
            scheduled_email_subject (str | Unset): Custom subject for sent report email. Will use default subject if
                excluded. Example: EmailSubject.
            scheduled_file_orientation (int | Unset): Page orientation for emailed reports. Only used for PDFs.
                Valid values: 1 for portrait, 2 for landscape.
                Defaults to portrait if not provided. Example: 1.
            scheduled_file_types (list[int] | None | Unset): Selected file types to send. Can select multiple file types.
                Valid values: 0 for CSV, 1 for PDF. Example: [0, 1].
     """

    external_emails: list[str] | None | Unset = UNSET
    saved_report_scheduled_frequency: SchedulingFrequency | Unset = UNSET
    scheduled: bool | None | Unset = UNSET
    scheduled_email_message: str | Unset = UNSET
    scheduled_email_subject: str | Unset = UNSET
    scheduled_file_orientation: int | Unset = UNSET
    scheduled_file_types: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.scheduling_frequency import SchedulingFrequency
        external_emails: list[str] | None | Unset
        if isinstance(self.external_emails, Unset):
            external_emails = UNSET
        elif isinstance(self.external_emails, list):
            external_emails = self.external_emails


        else:
            external_emails = self.external_emails

        saved_report_scheduled_frequency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saved_report_scheduled_frequency, Unset):
            saved_report_scheduled_frequency = self.saved_report_scheduled_frequency.to_dict()

        scheduled: bool | None | Unset
        if isinstance(self.scheduled, Unset):
            scheduled = UNSET
        else:
            scheduled = self.scheduled

        scheduled_email_message = self.scheduled_email_message

        scheduled_email_subject = self.scheduled_email_subject

        scheduled_file_orientation = self.scheduled_file_orientation

        scheduled_file_types: list[int] | None | Unset
        if isinstance(self.scheduled_file_types, Unset):
            scheduled_file_types = UNSET
        elif isinstance(self.scheduled_file_types, list):
            scheduled_file_types = self.scheduled_file_types


        else:
            scheduled_file_types = self.scheduled_file_types


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if external_emails is not UNSET:
            field_dict["external_emails"] = external_emails
        if saved_report_scheduled_frequency is not UNSET:
            field_dict["saved_report_scheduled_frequency"] = saved_report_scheduled_frequency
        if scheduled is not UNSET:
            field_dict["scheduled"] = scheduled
        if scheduled_email_message is not UNSET:
            field_dict["scheduled_email_message"] = scheduled_email_message
        if scheduled_email_subject is not UNSET:
            field_dict["scheduled_email_subject"] = scheduled_email_subject
        if scheduled_file_orientation is not UNSET:
            field_dict["scheduled_file_orientation"] = scheduled_file_orientation
        if scheduled_file_types is not UNSET:
            field_dict["scheduled_file_types"] = scheduled_file_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scheduling_frequency import SchedulingFrequency
        d = dict(src_dict)
        def _parse_external_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_emails_type_0 = cast(list[str], data)

                return external_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_emails = _parse_external_emails(d.pop("external_emails", UNSET))


        _saved_report_scheduled_frequency = d.pop("saved_report_scheduled_frequency", UNSET)
        saved_report_scheduled_frequency: SchedulingFrequency | Unset
        if isinstance(_saved_report_scheduled_frequency,  Unset):
            saved_report_scheduled_frequency = UNSET
        else:
            saved_report_scheduled_frequency = SchedulingFrequency.from_dict(_saved_report_scheduled_frequency)




        def _parse_scheduled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        scheduled = _parse_scheduled(d.pop("scheduled", UNSET))


        scheduled_email_message = d.pop("scheduled_email_message", UNSET)

        scheduled_email_subject = d.pop("scheduled_email_subject", UNSET)

        scheduled_file_orientation = d.pop("scheduled_file_orientation", UNSET)

        def _parse_scheduled_file_types(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scheduled_file_types_type_0 = cast(list[int], data)

                return scheduled_file_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        scheduled_file_types = _parse_scheduled_file_types(d.pop("scheduled_file_types", UNSET))


        saved_report_scheduling = cls(
            external_emails=external_emails,
            saved_report_scheduled_frequency=saved_report_scheduled_frequency,
            scheduled=scheduled,
            scheduled_email_message=scheduled_email_message,
            scheduled_email_subject=scheduled_email_subject,
            scheduled_file_orientation=scheduled_file_orientation,
            scheduled_file_types=scheduled_file_types,
        )


        saved_report_scheduling.additional_properties = d
        return saved_report_scheduling

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
