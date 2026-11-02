from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OAuthClientUpdateRequest")



@_attrs_define
class OAuthClientUpdateRequest:
    """ OAuthClientUpdateRequest defines the body for updating an OAuth client.

        Attributes:
            allowed_scopes (list[str] | None | Unset): Kion product scopes this client may request. Supported values are
                "mcp" and "api".
                Omit this field to retain the current scopes. An empty list grants no Kion product access. Example: ['mcp',
                'api'].
            description (str | Unset): Description of the OAuth client. Example: Updated description.
            grant_types (list[str] | None | Unset): Allowed grant types. Example: ['authorization_code'].
            is_public (bool | None | Unset): Whether the client is public (no secret).
            name (str | Unset): Name of the OAuth client. Example: My Updated App.
            owner_user_id (int | None | Unset): Owner of the client. If omitted (and the caller has Manage OAuth Clients
                permission), the client becomes a global, unowned application. Callers
                with only Manage Own OAuth Clients permission may only set this to their
                own user ID. Example: 1.
            redirect_uris (list[str] | None | Unset): Allowed redirect URIs. Example: ['https://example.com/callback'].
            service_account_user_id (int | None | Unset): Service account user ID for client_credentials grant. Example: 1.
     """

    allowed_scopes: list[str] | None | Unset = UNSET
    description: str | Unset = UNSET
    grant_types: list[str] | None | Unset = UNSET
    is_public: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    owner_user_id: int | None | Unset = UNSET
    redirect_uris: list[str] | None | Unset = UNSET
    service_account_user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed_scopes: list[str] | None | Unset
        if isinstance(self.allowed_scopes, Unset):
            allowed_scopes = UNSET
        elif isinstance(self.allowed_scopes, list):
            allowed_scopes = self.allowed_scopes


        else:
            allowed_scopes = self.allowed_scopes

        description = self.description

        grant_types: list[str] | None | Unset
        if isinstance(self.grant_types, Unset):
            grant_types = UNSET
        elif isinstance(self.grant_types, list):
            grant_types = self.grant_types


        else:
            grant_types = self.grant_types

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

        service_account_user_id: int | None | Unset
        if isinstance(self.service_account_user_id, Unset):
            service_account_user_id = UNSET
        else:
            service_account_user_id = self.service_account_user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed_scopes is not UNSET:
            field_dict["allowed_scopes"] = allowed_scopes
        if description is not UNSET:
            field_dict["description"] = description
        if grant_types is not UNSET:
            field_dict["grant_types"] = grant_types
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris
        if service_account_user_id is not UNSET:
            field_dict["service_account_user_id"] = service_account_user_id

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


        def _parse_service_account_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        service_account_user_id = _parse_service_account_user_id(d.pop("service_account_user_id", UNSET))


        o_auth_client_update_request = cls(
            allowed_scopes=allowed_scopes,
            description=description,
            grant_types=grant_types,
            is_public=is_public,
            name=name,
            owner_user_id=owner_user_id,
            redirect_uris=redirect_uris,
            service_account_user_id=service_account_user_id,
        )


        o_auth_client_update_request.additional_properties = d
        return o_auth_client_update_request

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
