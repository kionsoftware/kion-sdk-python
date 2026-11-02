from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OAuthClientCreated")



@_attrs_define
class OAuthClientCreated:
    """ OAuthClientCreated is the response for a newly created OAuth client, including the plaintext secret.

        Attributes:
            allowed_scopes (list[str] | None | Unset):
            created_at (str | Unset):
            created_by (int | Unset):
            description (str | Unset):
            grant_types (list[str] | None | Unset):
            id (str | Unset):
            is_dynamically_registered (bool | None | Unset): IsDynamicallyRegistered indicates that the client is managed
                with an RFC 7592 registration access token.
            is_public (bool | None | Unset):
            name (str | Unset):
            owner_user_id (int | None | Unset):
            redirect_uris (list[str] | None | Unset):
            secret (str | Unset):
            service_account_user_id (int | None | Unset):
            updated_at (None | str | Unset):
     """

    allowed_scopes: list[str] | None | Unset = UNSET
    created_at: str | Unset = UNSET
    created_by: int | Unset = UNSET
    description: str | Unset = UNSET
    grant_types: list[str] | None | Unset = UNSET
    id: str | Unset = UNSET
    is_dynamically_registered: bool | None | Unset = UNSET
    is_public: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    owner_user_id: int | None | Unset = UNSET
    redirect_uris: list[str] | None | Unset = UNSET
    secret: str | Unset = UNSET
    service_account_user_id: int | None | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed_scopes: list[str] | None | Unset
        if isinstance(self.allowed_scopes, Unset):
            allowed_scopes = UNSET
        elif isinstance(self.allowed_scopes, list):
            allowed_scopes = self.allowed_scopes


        else:
            allowed_scopes = self.allowed_scopes

        created_at = self.created_at

        created_by = self.created_by

        description = self.description

        grant_types: list[str] | None | Unset
        if isinstance(self.grant_types, Unset):
            grant_types = UNSET
        elif isinstance(self.grant_types, list):
            grant_types = self.grant_types


        else:
            grant_types = self.grant_types

        id = self.id

        is_dynamically_registered: bool | None | Unset
        if isinstance(self.is_dynamically_registered, Unset):
            is_dynamically_registered = UNSET
        else:
            is_dynamically_registered = self.is_dynamically_registered

        is_public: bool | None | Unset
        if isinstance(self.is_public, Unset):
            is_public = UNSET
        else:
            is_public = self.is_public

        name = self.name

        owner_user_id: int | None | Unset
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        else:
            owner_user_id = self.owner_user_id

        redirect_uris: list[str] | None | Unset
        if isinstance(self.redirect_uris, Unset):
            redirect_uris = UNSET
        elif isinstance(self.redirect_uris, list):
            redirect_uris = self.redirect_uris


        else:
            redirect_uris = self.redirect_uris

        secret = self.secret

        service_account_user_id: int | None | Unset
        if isinstance(self.service_account_user_id, Unset):
            service_account_user_id = UNSET
        else:
            service_account_user_id = self.service_account_user_id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed_scopes is not UNSET:
            field_dict["allowed_scopes"] = allowed_scopes
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if grant_types is not UNSET:
            field_dict["grant_types"] = grant_types
        if id is not UNSET:
            field_dict["id"] = id
        if is_dynamically_registered is not UNSET:
            field_dict["is_dynamically_registered"] = is_dynamically_registered
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris
        if secret is not UNSET:
            field_dict["secret"] = secret
        if service_account_user_id is not UNSET:
            field_dict["service_account_user_id"] = service_account_user_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_allowed_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_scopes_type_0 = cast(list[str], data)

                return allowed_scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_scopes = _parse_allowed_scopes(d.pop("allowed_scopes", UNSET))


        created_at = d.pop("created_at", UNSET)

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


        id = d.pop("id", UNSET)

        def _parse_is_dynamically_registered(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_dynamically_registered = _parse_is_dynamically_registered(d.pop("is_dynamically_registered", UNSET))


        def _parse_is_public(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_public = _parse_is_public(d.pop("is_public", UNSET))


        name = d.pop("name", UNSET)

        def _parse_owner_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))


        def _parse_redirect_uris(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                redirect_uris_type_0 = cast(list[str], data)

                return redirect_uris_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        redirect_uris = _parse_redirect_uris(d.pop("redirect_uris", UNSET))


        secret = d.pop("secret", UNSET)

        def _parse_service_account_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        service_account_user_id = _parse_service_account_user_id(d.pop("service_account_user_id", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        o_auth_client_created = cls(
            allowed_scopes=allowed_scopes,
            created_at=created_at,
            created_by=created_by,
            description=description,
            grant_types=grant_types,
            id=id,
            is_dynamically_registered=is_dynamically_registered,
            is_public=is_public,
            name=name,
            owner_user_id=owner_user_id,
            redirect_uris=redirect_uris,
            secret=secret,
            service_account_user_id=service_account_user_id,
            updated_at=updated_at,
        )


        o_auth_client_created.additional_properties = d
        return o_auth_client_created

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
