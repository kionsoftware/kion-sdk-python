from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PaginationQuery")



@_attrs_define
class PaginationQuery:
    """ PaginationQuery represents an account in the system.

        Attributes:
            count (int | Unset): Number of results to return. Optional

                in: query Default: 10.
            page (int | Unset): Page number of results. Optional

                in: query Default: 1.
            sort_method (str | Unset): Specifies how to sort the data. Optional

                in: query Default: 'alphabetical'.
            sort_order (str | Unset): Specifies order of sorting. Allowed values are "ASC" and "DESC". Optional

                in: query Default: 'ASC'.
     """

    count: int | Unset = 10
    page: int | Unset = 1
    sort_method: str | Unset = 'alphabetical'
    sort_order: str | Unset = 'ASC'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        page = self.page

        sort_method = self.sort_method

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if page is not UNSET:
            field_dict["page"] = page
        if sort_method is not UNSET:
            field_dict["sort_method"] = sort_method
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        page = d.pop("page", UNSET)

        sort_method = d.pop("sort_method", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        pagination_query = cls(
            count=count,
            page=page,
            sort_method=sort_method,
            sort_order=sort_order,
        )


        pagination_query.additional_properties = d
        return pagination_query

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
