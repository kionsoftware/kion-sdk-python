from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PaginationQuery")



@_attrs_define
class PaginationQuery:
    """ PaginationQuery represents an account in the system.

        Attributes:
            augmented (bool | None | Unset): Options are: true, false.

                in: query
            count (int | Unset): Options are: 0-N.

                in: query Default: 10.
            page (int | Unset): Options are: 0-N.

                in: query Default: 1.
            sort_method (str | Unset): Options are: alphabetical, date.

                in: query
            sort_order (str | Unset): Options are: ASC, DESC.

                in: query
     """

    augmented: bool | None | Unset = UNSET
    count: int | Unset = 10
    page: int | Unset = 1
    sort_method: str | Unset = UNSET
    sort_order: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        augmented: bool | None | Unset
        if isinstance(self.augmented, Unset):
            augmented = UNSET
        else:
            augmented = self.augmented

        count = self.count

        page = self.page

        sort_method = self.sort_method

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if augmented is not UNSET:
            field_dict["augmented"] = augmented
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
        def _parse_augmented(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        augmented = _parse_augmented(d.pop("augmented", UNSET))


        count = d.pop("count", UNSET)

        page = d.pop("page", UNSET)

        sort_method = d.pop("sort_method", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        pagination_query = cls(
            augmented=augmented,
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
