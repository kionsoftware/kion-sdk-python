from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.string_base_filter import StringBaseFilter





T = TypeVar("T", bound="SpendReportQueryFilterTags")



@_attrs_define
class SpendReportQueryFilterTags:
    """ Filtering by tags

        Example:
            {'resourcetags/aws:createdby': {'is_exclusive': False, 'values': []}}

     """

    additional_properties: dict[str, StringBaseFilter] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.string_base_filter import StringBaseFilter
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.string_base_filter import StringBaseFilter
        d = dict(src_dict)
        spend_report_query_filter_tags = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = StringBaseFilter.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        spend_report_query_filter_tags.additional_properties = additional_properties
        return spend_report_query_filter_tags

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> StringBaseFilter:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: StringBaseFilter) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
