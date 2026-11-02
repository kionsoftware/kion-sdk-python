from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SavedReportSharing")



@_attrs_define
class SavedReportSharing:
    """ 
        Attributes:
            excluded_ugroups (list[int] | None | Unset): List of user group IDs to exclude from sharing. Only used when
                is_global is true. Example: [1, 2, 3].
            excluded_users (list[int] | None | Unset): List of user IDs to exclude from sharing. Only used when is_global is
                true. Example: [1, 2, 3].
            is_global (bool | None | Unset): Whether the report should be shared globally as opposed to with specific users
                or user groups.
                Required. If omitted, is_global will be set to false. Example: True.
            ugroup_ids (list[int] | None | Unset): List of user group IDs with whom the report should be shared. Only used
                when is_global is false. Example: [1, 2, 3].
            user_ids (list[int] | None | Unset): List of user IDs with whom the report should be shared. Only used when
                is_global is false. Example: [1, 2, 3].
     """

    excluded_ugroups: list[int] | None | Unset = UNSET
    excluded_users: list[int] | None | Unset = UNSET
    is_global: bool | None | Unset = UNSET
    ugroup_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
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

        is_global: bool | None | Unset
        if isinstance(self.is_global, Unset):
            is_global = UNSET
        else:
            is_global = self.is_global

        ugroup_ids: list[int] | None | Unset
        if isinstance(self.ugroup_ids, Unset):
            ugroup_ids = UNSET
        elif isinstance(self.ugroup_ids, list):
            ugroup_ids = self.ugroup_ids


        else:
            ugroup_ids = self.ugroup_ids

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
        if excluded_ugroups is not UNSET:
            field_dict["excluded_ugroups"] = excluded_ugroups
        if excluded_users is not UNSET:
            field_dict["excluded_users"] = excluded_users
        if is_global is not UNSET:
            field_dict["is_global"] = is_global
        if ugroup_ids is not UNSET:
            field_dict["ugroup_ids"] = ugroup_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_is_global(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_global = _parse_is_global(d.pop("is_global", UNSET))


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


        saved_report_sharing = cls(
            excluded_ugroups=excluded_ugroups,
            excluded_users=excluded_users,
            is_global=is_global,
            ugroup_ids=ugroup_ids,
            user_ids=user_ids,
        )


        saved_report_sharing.additional_properties = d
        return saved_report_sharing

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
