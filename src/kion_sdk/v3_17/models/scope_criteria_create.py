from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ScopeCriteriaCreate")



@_attrs_define
class ScopeCriteriaCreate:
    """ ScopeCriteriaCreate defines a Scope Criteria creation payload.

        Attributes:
            criteria (Any | Unset): Criteria for the scope, stored as raw JSON. Example: {'account_id': 1, 'tag':
                'repo:Prod'}.
            end_month (int | Unset): End month for the scope (YYYYMM format). Example: 202501.
            start_month (int | Unset): Start month for the scope (YYYYMM format). Example: 202501.
     """

    criteria: Any | Unset = UNSET
    end_month: int | Unset = UNSET
    start_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        criteria = self.criteria

        end_month = self.end_month

        start_month = self.start_month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if end_month is not UNSET:
            field_dict["end_month"] = end_month
        if start_month is not UNSET:
            field_dict["start_month"] = start_month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        criteria = d.pop("criteria", UNSET)

        end_month = d.pop("end_month", UNSET)

        start_month = d.pop("start_month", UNSET)

        scope_criteria_create = cls(
            criteria=criteria,
            end_month=end_month,
            start_month=start_month,
        )


        scope_criteria_create.additional_properties = d
        return scope_criteria_create

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
