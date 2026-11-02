from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OAuthGrant")



@_attrs_define
class OAuthGrant:
    """ OAuthGrant is the V3 API response model for an authorized grant.

        Attributes:
            client_id (str | Unset):
            client_name (str | Unset):
            created_by (int | Unset):
            description (str | Unset):
            grant_types (list[str] | None | Unset):
            granted_at (str | Unset):
            is_public (bool | None | Unset):
            last_used (str | Unset):
            owner_user_id (int | None | Unset):
            token_count (int | Unset):
     """

    client_id: str | Unset = UNSET
    client_name: str | Unset = UNSET
    created_by: int | Unset = UNSET
    description: str | Unset = UNSET
    grant_types: list[str] | None | Unset = UNSET
    granted_at: str | Unset = UNSET
    is_public: bool | None | Unset = UNSET
    last_used: str | Unset = UNSET
    owner_user_id: int | None | Unset = UNSET
    token_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_name = self.client_name

        created_by = self.created_by

        description = self.description

        grant_types: list[str] | None | Unset
        if isinstance(self.grant_types, Unset):
            grant_types = UNSET
        elif isinstance(self.grant_types, list):
            grant_types = self.grant_types


        else:
            grant_types = self.grant_types

        granted_at = self.granted_at

        is_public: bool | None | Unset
        if isinstance(self.is_public, Unset):
            is_public = UNSET
        else:
            is_public = self.is_public

        last_used = self.last_used

        owner_user_id: int | None | Unset
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = self.owner_user_id

        token_count = self.token_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_name is not UNSET:
            field_dict["client_name"] = client_name
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if grant_types is not UNSET:
            field_dict["grant_types"] = grant_types
        if granted_at is not UNSET:
            field_dict["granted_at"] = granted_at
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if token_count is not UNSET:
            field_dict["token_count"] = token_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id", UNSET)

        client_name = d.pop("client_name", UNSET)

        created_by = d.pop("created_by", UNSET)

        description = d.pop("description", UNSET)

        def _parse_grant_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                grant_types_type_0 = cast(list[str], data)

                return grant_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        grant_types = _parse_grant_types(d.pop("grant_types", UNSET))


        granted_at = d.pop("granted_at", UNSET)

        def _parse_is_public(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_public = _parse_is_public(d.pop("is_public", UNSET))


        last_used = d.pop("last_used", UNSET)

        def _parse_owner_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))


        token_count = d.pop("token_count", UNSET)

        o_auth_grant = cls(
            client_id=client_id,
            client_name=client_name,
            created_by=created_by,
            description=description,
            grant_types=grant_types,
            granted_at=granted_at,
            is_public=is_public,
            last_used=last_used,
            owner_user_id=owner_user_id,
            token_count=token_count,
        )


        o_auth_grant.additional_properties = d
        return o_auth_grant

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
