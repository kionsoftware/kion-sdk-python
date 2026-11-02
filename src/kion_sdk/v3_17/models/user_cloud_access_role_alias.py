from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="UserCloudAccessRoleAlias")



@_attrs_define
class UserCloudAccessRoleAlias:
    """ UserCloudAccessRoleAlias defines the state of a user cloud access role alias

        Attributes:
            access_type (str | Unset): AccessType represents how a cloud access role is used by the user
            alias_name (str | Unset): Name of the alias. Example: development-admin.
            created_at (datetime.datetime | Unset): Timestamp when the user cloud access role alias was created. Example:
                2023-04-15T14:32:10Z.
            id (int | Unset): Unique identifier for the user cloud access role alias. Example: 1.
            updated_at (datetime.datetime | None | Unset): Timestamp when the user cloud access role alias was last updated.
                Example: 2023-04-15T14:32:10Z.
            user_cloud_access_role_history_id (int | None | Unset): ID of the user cloud access role history. Example: 42.
     """

    access_type: str | Unset = UNSET
    alias_name: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    id: int | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    user_cloud_access_role_history_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_type = self.access_type

        alias_name = self.alias_name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        user_cloud_access_role_history_id: int | None | Unset
        if isinstance(self.user_cloud_access_role_history_id, Unset):
            user_cloud_access_role_history_id = UNSET
        else:
            user_cloud_access_role_history_id = self.user_cloud_access_role_history_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_type is not UNSET:
            field_dict["access_type"] = access_type
        if alias_name is not UNSET:
            field_dict["alias_name"] = alias_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_cloud_access_role_history_id is not UNSET:
            field_dict["user_cloud_access_role_history_id"] = user_cloud_access_role_history_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_type = d.pop("access_type", UNSET)

        alias_name = d.pop("alias_name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        id = d.pop("id", UNSET)

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_user_cloud_access_role_history_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_cloud_access_role_history_id = _parse_user_cloud_access_role_history_id(d.pop("user_cloud_access_role_history_id", UNSET))


        user_cloud_access_role_alias = cls(
            access_type=access_type,
            alias_name=alias_name,
            created_at=created_at,
            id=id,
            updated_at=updated_at,
            user_cloud_access_role_history_id=user_cloud_access_role_history_id,
        )


        user_cloud_access_role_alias.additional_properties = d
        return user_cloud_access_role_alias

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
