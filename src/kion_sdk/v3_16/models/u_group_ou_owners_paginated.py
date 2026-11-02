from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pagination_query import PaginationQuery
  from ..models.u_group_ou_app_roles import UGroupOUAppRoles





T = TypeVar("T", bound="UGroupOUOwnersPaginated")



@_attrs_define
class UGroupOUOwnersPaginated:
    """ UGroupOUOwnersPaginated defines a paginated list of OUAppRoles.

        Attributes:
            items (list[UGroupOUAppRoles] | None | Unset):
            pagination (None | PaginationQuery | Unset):
            total (int | Unset):
     """

    items: list[UGroupOUAppRoles] | None | Unset = UNSET
    pagination: None | PaginationQuery | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pagination_query import PaginationQuery
        from ..models.u_group_ou_app_roles import UGroupOUAppRoles
        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for componentsschemas_u_group_ou_app_roles_list_item_data in self.items:
                componentsschemas_u_group_ou_app_roles_list_item = componentsschemas_u_group_ou_app_roles_list_item_data.to_dict()
                items.append(componentsschemas_u_group_ou_app_roles_list_item)


        else:
            items = self.items

        pagination: dict[str, Any] | None | Unset
        if isinstance(self.pagination, Unset):
            pagination = UNSET
        elif isinstance(self.pagination, PaginationQuery):
            pagination = self.pagination.to_dict()
        else:
            pagination = self.pagination

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_query import PaginationQuery
        from ..models.u_group_ou_app_roles import UGroupOUAppRoles
        d = dict(src_dict)
        def _parse_items(data: object) -> list[UGroupOUAppRoles] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_1 = []
                _items_type_1 = data
                for componentsschemas_u_group_ou_app_roles_list_item_data in (_items_type_1):
                    componentsschemas_u_group_ou_app_roles_list_item = UGroupOUAppRoles.from_dict(componentsschemas_u_group_ou_app_roles_list_item_data)



                    items_type_1.append(componentsschemas_u_group_ou_app_roles_list_item)

                return items_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroupOUAppRoles] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_pagination(data: object) -> None | PaginationQuery | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pagination_type_1 = PaginationQuery.from_dict(data)



                return pagination_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PaginationQuery | Unset, data)

        pagination = _parse_pagination(d.pop("pagination", UNSET))


        total = d.pop("total", UNSET)

        u_group_ou_owners_paginated = cls(
            items=items,
            pagination=pagination,
            total=total,
        )


        u_group_ou_owners_paginated.additional_properties = d
        return u_group_ou_owners_paginated

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
