from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="DiagnosticBillingReport")



@_attrs_define
class DiagnosticBillingReport:
    """ DiagnosticBillingReport defines a billing report diagnostic record.

        Attributes:
            attempt_counter (int | Unset): Number of processing attempts for this report. Example: 2.
            billing_source_id (int | None | Unset): Billing source ID associated with this report. Example: 7.
            created_at (datetime.datetime | Unset): Timestamp when this diagnostic record was created. Example:
                2025-02-01T12:00:00Z.
            deleted_at (datetime.datetime | None | Unset): Timestamp when this diagnostic record was deleted, if applicable.
                Example: 2025-02-01T13:00:00Z.
            export_identifier (str | Unset): Export identifier used to detect updated source data. Example:
                export-202501-001.
            export_time (datetime.datetime | Unset): Timestamp when the billing export was generated. Example:
                2025-01-31T00:00:00Z.
            id (int | Unset): ID of the diagnostic billing report record. Example: 42.
            is_focus (bool | None | Unset): Indicates whether this report came from a FOCUS export. Example: True.
            month (int | Unset): Month for this billing report in YYYYMM format. Example: 202501.
            processed_at (datetime.datetime | Unset): Timestamp when this report was processed. Example:
                2025-02-01T12:30:00Z.
            should_process (bool | None | Unset): Indicates whether this report should be processed. Example: True.
            status (str | Unset): Current processing status (processed, queued, pending, deleted, failed, error). Example:
                processed.
            time_granularity_id (int | None | Unset): Time granularity identifier (1=monthly, 2=daily, 3=hourly). Example:
                1.
            updated_at (datetime.datetime | None | Unset): Timestamp when this diagnostic record was last updated. Example:
                2025-02-01T12:45:00Z.
     """

    attempt_counter: int | Unset = UNSET
    billing_source_id: int | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    export_identifier: str | Unset = UNSET
    export_time: datetime.datetime | Unset = UNSET
    id: int | Unset = UNSET
    is_focus: bool | None | Unset = UNSET
    month: int | Unset = UNSET
    processed_at: datetime.datetime | Unset = UNSET
    should_process: bool | None | Unset = UNSET
    status: str | Unset = UNSET
    time_granularity_id: int | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attempt_counter = self.attempt_counter

        billing_source_id: int | None | Unset
        if isinstance(self.billing_source_id, Unset):
            billing_source_id = UNSET
        else:
            billing_source_id = self.billing_source_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        export_identifier = self.export_identifier

        export_time: str | Unset = UNSET
        if not isinstance(self.export_time, Unset):
            export_time = self.export_time.isoformat()

        id = self.id

        is_focus: bool | None | Unset
        if isinstance(self.is_focus, Unset):
            is_focus = UNSET
        else:
            is_focus = self.is_focus

        month = self.month

        processed_at: str | Unset = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        should_process: bool | None | Unset
        if isinstance(self.should_process, Unset):
            should_process = UNSET
        else:
            should_process = self.should_process

        status = self.status

        time_granularity_id: int | None | Unset
        if isinstance(self.time_granularity_id, Unset):
            time_granularity_id = UNSET
        else:
            time_granularity_id = self.time_granularity_id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attempt_counter is not UNSET:
            field_dict["attempt_counter"] = attempt_counter
        if billing_source_id is not UNSET:
            field_dict["billing_source_id"] = billing_source_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if export_identifier is not UNSET:
            field_dict["export_identifier"] = export_identifier
        if export_time is not UNSET:
            field_dict["export_time"] = export_time
        if id is not UNSET:
            field_dict["id"] = id
        if is_focus is not UNSET:
            field_dict["is_focus"] = is_focus
        if month is not UNSET:
            field_dict["month"] = month
        if processed_at is not UNSET:
            field_dict["processed_at"] = processed_at
        if should_process is not UNSET:
            field_dict["should_process"] = should_process
        if status is not UNSET:
            field_dict["status"] = status
        if time_granularity_id is not UNSET:
            field_dict["time_granularity_id"] = time_granularity_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt_counter = d.pop("attempt_counter", UNSET)

        def _parse_billing_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        billing_source_id = _parse_billing_source_id(d.pop("billing_source_id", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)



                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        export_identifier = d.pop("export_identifier", UNSET)

        _export_time = d.pop("export_time", UNSET)
        export_time: datetime.datetime | Unset
        if isinstance(_export_time,  Unset):
            export_time = UNSET
        else:
            export_time = datetime.datetime.fromisoformat(_export_time)




        id = d.pop("id", UNSET)

        def _parse_is_focus(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_focus = _parse_is_focus(d.pop("is_focus", UNSET))


        month = d.pop("month", UNSET)

        _processed_at = d.pop("processed_at", UNSET)
        processed_at: datetime.datetime | Unset
        if isinstance(_processed_at,  Unset):
            processed_at = UNSET
        else:
            processed_at = datetime.datetime.fromisoformat(_processed_at)




        def _parse_should_process(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        should_process = _parse_should_process(d.pop("should_process", UNSET))


        status = d.pop("status", UNSET)

        def _parse_time_granularity_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_granularity_id = _parse_time_granularity_id(d.pop("time_granularity_id", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        diagnostic_billing_report = cls(
            attempt_counter=attempt_counter,
            billing_source_id=billing_source_id,
            created_at=created_at,
            deleted_at=deleted_at,
            export_identifier=export_identifier,
            export_time=export_time,
            id=id,
            is_focus=is_focus,
            month=month,
            processed_at=processed_at,
            should_process=should_process,
            status=status,
            time_granularity_id=time_granularity_id,
            updated_at=updated_at,
        )


        diagnostic_billing_report.additional_properties = d
        return diagnostic_billing_report

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
