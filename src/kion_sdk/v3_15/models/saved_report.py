from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.saved_report_scheduling import SavedReportScheduling





T = TypeVar("T", bound="SavedReport")



@_attrs_define
class SavedReport:
    """ 
        Attributes:
            created_at (datetime.datetime | Unset): Timestamp for when the saved report was created Example:
                2025-10-20T14:48:00Z.
            created_by (int | Unset): User ID of the saved report creator. Example: 1.
            date_range (str | Unset): Date range covered by the spend report.
            deduct_credits (bool | None | Unset): If credits are deducted in the saved report. Example: True.
            deduct_refunds (bool | None | Unset): If refunds are deducted in the saved report. Example: True.
            dimension (str | Unset): Group on which the saved report is dimensioned. The report can also have no dimension.
                Example: service.
            excluded_ugroups (list[int] | None | Unset): List of user group IDs to exclude from sharing. Only used when
                is_global is true. Example: [1, 2, 3].
            excluded_users (list[int] | None | Unset): List of user IDs to exclude from sharing. Only used when is_global is
                true. Example: [1, 2, 3].
            forecasting_enabled (bool | None | Unset): If forecasting is enabled for the saved report and the report
                includes future data. Example: True.
            id (int | Unset): Saved report ID. Example: 1.
            is_global (bool | None | Unset): Whether the report should be shared globally as opposed to with specific users
                or user groups.
                Required. If omitted, is_global will be set to false. Example: True.
            report_name (str | Unset): Saved report name. Example: Spend by Service.
            scheduling (SavedReportScheduling | Unset):
            spend_type (str | Unset): Spend type in the saved report. Values include billed, list, amortized, or amortized
                and attributed Example: billed.
            time_granularity (str | Unset): Time granularity for the saved report. Can be daily or monthly. Example:
                monthly.
            ugroup_ids (list[int] | None | Unset): List of user group IDs with whom the report should be shared. Only used
                when is_global is false. Example: [1, 2, 3].
            updated_at (datetime.datetime | None | Unset): Timestamp for the last update to the saved report. Null if the
                report has never been updated. Example: 2025-10-20T14:48:00Z.
            user_ids (list[int] | None | Unset): List of user IDs with whom the report should be shared. Only used when
                is_global is false. Example: [1, 2, 3].
     """

    created_at: datetime.datetime | Unset = UNSET
    created_by: int | Unset = UNSET
    date_range: str | Unset = UNSET
    deduct_credits: bool | None | Unset = UNSET
    deduct_refunds: bool | None | Unset = UNSET
    dimension: str | Unset = UNSET
    excluded_ugroups: list[int] | None | Unset = UNSET
    excluded_users: list[int] | None | Unset = UNSET
    forecasting_enabled: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    is_global: bool | None | Unset = UNSET
    report_name: str | Unset = UNSET
    scheduling: SavedReportScheduling | Unset = UNSET
    spend_type: str | Unset = UNSET
    time_granularity: str | Unset = UNSET
    ugroup_ids: list[int] | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.saved_report_scheduling import SavedReportScheduling
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        date_range = self.date_range

        deduct_credits: bool | None | Unset
        if isinstance(self.deduct_credits, Unset):
            deduct_credits = UNSET
        else:
            deduct_credits = self.deduct_credits

        deduct_refunds: bool | None | Unset
        if isinstance(self.deduct_refunds, Unset):
            deduct_refunds = UNSET
        else:
            deduct_refunds = self.deduct_refunds

        dimension = self.dimension

        excluded_ugroups: list[int] | None | Unset
        if isinstance(self.excluded_ugroups, Unset):
            excluded_ugroups = UNSET
        elif isinstance(self.excluded_ugroups, list):
            excluded_ugroups = self.excluded_ugroups


        else:
            excluded_ugroups = self.excluded_ugroups

        excluded_users: list[int] | None | Unset
        if isinstance(self.excluded_users, Unset):
            excluded_users = UNSET
        elif isinstance(self.excluded_users, list):
            excluded_users = self.excluded_users


        else:
            excluded_users = self.excluded_users

        forecasting_enabled: bool | None | Unset
        if isinstance(self.forecasting_enabled, Unset):
            forecasting_enabled = UNSET
        else:
            forecasting_enabled = self.forecasting_enabled

        id = self.id

        is_global: bool | None | Unset
        if isinstance(self.is_global, Unset):
            is_global = UNSET
        else:
            is_global = self.is_global

        report_name = self.report_name

        scheduling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduling, Unset):
            scheduling = self.scheduling.to_dict()

        spend_type = self.spend_type

        time_granularity = self.time_granularity

        ugroup_ids: list[int] | None | Unset
        if isinstance(self.ugroup_ids, Unset):
            ugroup_ids = UNSET
        elif isinstance(self.ugroup_ids, list):
            ugroup_ids = self.ugroup_ids


        else:
            ugroup_ids = self.ugroup_ids

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        user_ids: list[int] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids


        else:
            user_ids = self.user_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if date_range is not UNSET:
            field_dict["date_range"] = date_range
        if deduct_credits is not UNSET:
            field_dict["deduct_credits"] = deduct_credits
        if deduct_refunds is not UNSET:
            field_dict["deduct_refunds"] = deduct_refunds
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if excluded_ugroups is not UNSET:
            field_dict["excluded_ugroups"] = excluded_ugroups
        if excluded_users is not UNSET:
            field_dict["excluded_users"] = excluded_users
        if forecasting_enabled is not UNSET:
            field_dict["forecasting_enabled"] = forecasting_enabled
        if id is not UNSET:
            field_dict["id"] = id
        if is_global is not UNSET:
            field_dict["is_global"] = is_global
        if report_name is not UNSET:
            field_dict["report_name"] = report_name
        if scheduling is not UNSET:
            field_dict["scheduling"] = scheduling
        if spend_type is not UNSET:
            field_dict["spend_type"] = spend_type
        if time_granularity is not UNSET:
            field_dict["time_granularity"] = time_granularity
        if ugroup_ids is not UNSET:
            field_dict["ugroup_ids"] = ugroup_ids
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.saved_report_scheduling import SavedReportScheduling
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        created_by = d.pop("created_by", UNSET)

        date_range = d.pop("date_range", UNSET)

        def _parse_deduct_credits(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deduct_credits = _parse_deduct_credits(d.pop("deduct_credits", UNSET))


        def _parse_deduct_refunds(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deduct_refunds = _parse_deduct_refunds(d.pop("deduct_refunds", UNSET))


        dimension = d.pop("dimension", UNSET)

        def _parse_excluded_ugroups(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_ugroups_type_0 = cast(list[int], data)

                return excluded_ugroups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        excluded_ugroups = _parse_excluded_ugroups(d.pop("excluded_ugroups", UNSET))


        def _parse_excluded_users(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_users_type_0 = cast(list[int], data)

                return excluded_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        excluded_users = _parse_excluded_users(d.pop("excluded_users", UNSET))


        def _parse_forecasting_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        forecasting_enabled = _parse_forecasting_enabled(d.pop("forecasting_enabled", UNSET))


        id = d.pop("id", UNSET)

        def _parse_is_global(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_global = _parse_is_global(d.pop("is_global", UNSET))


        report_name = d.pop("report_name", UNSET)

        _scheduling = d.pop("scheduling", UNSET)
        scheduling: SavedReportScheduling | Unset
        if isinstance(_scheduling,  Unset):
            scheduling = UNSET
        else:
            scheduling = SavedReportScheduling.from_dict(_scheduling)




        spend_type = d.pop("spend_type", UNSET)

        time_granularity = d.pop("time_granularity", UNSET)

        def _parse_ugroup_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ugroup_ids_type_0 = cast(list[int], data)

                return ugroup_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        ugroup_ids = _parse_ugroup_ids(d.pop("ugroup_ids", UNSET))


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


        def _parse_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[int], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))


        saved_report = cls(
            created_at=created_at,
            created_by=created_by,
            date_range=date_range,
            deduct_credits=deduct_credits,
            deduct_refunds=deduct_refunds,
            dimension=dimension,
            excluded_ugroups=excluded_ugroups,
            excluded_users=excluded_users,
            forecasting_enabled=forecasting_enabled,
            id=id,
            is_global=is_global,
            report_name=report_name,
            scheduling=scheduling,
            spend_type=spend_type,
            time_granularity=time_granularity,
            ugroup_ids=ugroup_ids,
            updated_at=updated_at,
            user_ids=user_ids,
        )


        saved_report.additional_properties = d
        return saved_report

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
