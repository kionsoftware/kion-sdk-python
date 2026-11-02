from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ScopeCriteriaRecord")



@_attrs_define
class ScopeCriteriaRecord:
    """ ScopeCriteriaRecord represents a versioned criteria entry for a scope.

        Attributes:
            created_at (datetime.datetime | Unset): When the criteria record was created.
            criteria (Any | Unset): Criteria for this period, stored as raw JSON.
            criteria_error (str | Unset): Criteria error message, if the criteria could not be parsed properly.
            end_month (int | Unset): End month for this criteria period (YYYYMM format), if applicable.
            id (int | Unset): ID of the criteria record.
            scope_id (int | None | Unset): Scope ID this criteria belongs to.
            start_month (int | Unset): Start month for this criteria period (YYYYMM format).
     """

    created_at: datetime.datetime | Unset = UNSET
    criteria: Any | Unset = UNSET
    criteria_error: str | Unset = UNSET
    end_month: int | Unset = UNSET
    id: int | Unset = UNSET
    scope_id: int | None | Unset = UNSET
    start_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        criteria = self.criteria

        criteria_error = self.criteria_error

        end_month = self.end_month

        id = self.id

        scope_id: int | None | Unset
        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = self.scope_id

        start_month = self.start_month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if criteria_error is not UNSET:
            field_dict["criteria_error"] = criteria_error
        if end_month is not UNSET:
            field_dict["end_month"] = end_month
        if id is not UNSET:
            field_dict["id"] = id
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if start_month is not UNSET:
            field_dict["start_month"] = start_month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        criteria = d.pop("criteria", UNSET)

        criteria_error = d.pop("criteria_error", UNSET)

        end_month = d.pop("end_month", UNSET)

        id = d.pop("id", UNSET)

        def _parse_scope_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scope_id = _parse_scope_id(d.pop("scope_id", UNSET))


        start_month = d.pop("start_month", UNSET)

        scope_criteria_record = cls(
            created_at=created_at,
            criteria=criteria,
            criteria_error=criteria_error,
            end_month=end_month,
            id=id,
            scope_id=scope_id,
            start_month=start_month,
        )


        scope_criteria_record.additional_properties = d
        return scope_criteria_record

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
