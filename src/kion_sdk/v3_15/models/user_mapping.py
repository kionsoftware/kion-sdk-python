from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UserMapping")



@_attrs_define
class UserMapping:
    """ UserMapping stores the information needed to map users to roles in a permission scheme.

        Attributes:
            app_role_id (int | None): App role the user will be assigned to. Example: 1.
            user_groups_ids (list[int] | None | Unset): User groups being assigned to the specified role. Example: [1, 2].
            user_ids (list[int] | None | Unset): Users being assigned to the specified role. Example: [1, 2].
     """

    app_role_id: int | None
    user_groups_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        app_role_id: int | None
        app_role_id = self.app_role_id

        user_groups_ids: list[int] | None | Unset
        if isinstance(self.user_groups_ids, Unset):
            user_groups_ids = UNSET
        elif isinstance(self.user_groups_ids, list):
            user_groups_ids = self.user_groups_ids


        else:
            user_groups_ids = self.user_groups_ids

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
            "app_role_id": app_role_id,
        })
        if user_groups_ids is not UNSET:
            field_dict["user_groups_ids"] = user_groups_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_app_role_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        app_role_id = _parse_app_role_id(d.pop("app_role_id"))


        def _parse_user_groups_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_groups_ids_type_0 = cast(list[int], data)

                return user_groups_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_groups_ids = _parse_user_groups_ids(d.pop("user_groups_ids", UNSET))


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


        user_mapping = cls(
            app_role_id=app_role_id,
            user_groups_ids=user_groups_ids,
            user_ids=user_ids,
        )


        user_mapping.additional_properties = d
        return user_mapping

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
