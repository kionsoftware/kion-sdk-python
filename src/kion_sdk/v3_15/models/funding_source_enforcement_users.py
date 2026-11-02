from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FundingSourceEnforcementUsers")



@_attrs_define
class FundingSourceEnforcementUsers:
    """ FundingSourceEnforcementUsers .

        Attributes:
            user_group_ids (list[int] | None | Unset): List of user group IDs that will receive notifications from the
                enforcement. Example: [1].
            user_ids (list[int] | None | Unset): List of user IDs that will receive notifications from the enforcement.
                Example: [1].
     """

    user_group_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_group_ids: list[int] | None | Unset
        if isinstance(self.user_group_ids, Unset):
            user_group_ids = UNSET
        elif isinstance(self.user_group_ids, list):
            user_group_ids = self.user_group_ids


        else:
            user_group_ids = self.user_group_ids

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
        if user_group_ids is not UNSET:
            field_dict["user_group_ids"] = user_group_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_group_ids_type_0 = cast(list[int], data)

                return user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_group_ids = _parse_user_group_ids(d.pop("user_group_ids", UNSET))


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


        funding_source_enforcement_users = cls(
            user_group_ids=user_group_ids,
            user_ids=user_ids,
        )


        funding_source_enforcement_users.additional_properties = d
        return funding_source_enforcement_users

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
