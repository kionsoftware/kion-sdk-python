from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MonthRange")



@_attrs_define
class MonthRange:
    """ MonthRange defines a range of months

        Attributes:
            end_month (int): End month Example: 202401.
            start_month (int): Start month Example: 202301.
     """

    end_month: int
    start_month: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_month = self.end_month

        start_month = self.start_month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "end_month": end_month,
            "start_month": start_month,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_month = d.pop("end_month")

        start_month = d.pop("start_month")

        month_range = cls(
            end_month=end_month,
            start_month=start_month,
        )


        month_range.additional_properties = d
        return month_range

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
