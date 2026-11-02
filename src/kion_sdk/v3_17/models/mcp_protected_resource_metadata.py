from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MCPProtectedResourceMetadata")



@_attrs_define
class MCPProtectedResourceMetadata:
    """ MCPProtectedResourceMetadata is OAuth protected resource metadata for the MCP endpoint.

        Attributes:
            authorization_servers (list[str] | None | Unset): OAuth authorization server issuer URLs.
            bearer_methods_supported (list[str] | None | Unset): Supported bearer token presentation methods.
            resource (str | Unset): Canonical protected resource URL.
            scopes_supported (list[str] | None | Unset): OAuth scopes the client may request when accessing this resource.
     """

    authorization_servers: list[str] | None | Unset = UNSET
    bearer_methods_supported: list[str] | None | Unset = UNSET
    resource: str | Unset = UNSET
    scopes_supported: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        authorization_servers: list[str] | None | Unset
        if isinstance(self.authorization_servers, Unset):
            authorization_servers = UNSET
        elif isinstance(self.authorization_servers, list):
            authorization_servers = self.authorization_servers


        else:
            authorization_servers = self.authorization_servers

        bearer_methods_supported: list[str] | None | Unset
        if isinstance(self.bearer_methods_supported, Unset):
            bearer_methods_supported = UNSET
        elif isinstance(self.bearer_methods_supported, list):
            bearer_methods_supported = self.bearer_methods_supported


        else:
            bearer_methods_supported = self.bearer_methods_supported

        resource = self.resource

        scopes_supported: list[str] | None | Unset
        if isinstance(self.scopes_supported, Unset):
            scopes_supported = UNSET
        elif isinstance(self.scopes_supported, list):
            scopes_supported = self.scopes_supported


        else:
            scopes_supported = self.scopes_supported


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if authorization_servers is not UNSET:
            field_dict["authorization_servers"] = authorization_servers
        if bearer_methods_supported is not UNSET:
            field_dict["bearer_methods_supported"] = bearer_methods_supported
        if resource is not UNSET:
            field_dict["resource"] = resource
        if scopes_supported is not UNSET:
            field_dict["scopes_supported"] = scopes_supported

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_authorization_servers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authorization_servers_type_0 = cast(list[str], data)

                return authorization_servers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        authorization_servers = _parse_authorization_servers(d.pop("authorization_servers", UNSET))


        def _parse_bearer_methods_supported(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bearer_methods_supported_type_0 = cast(list[str], data)

                return bearer_methods_supported_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        bearer_methods_supported = _parse_bearer_methods_supported(d.pop("bearer_methods_supported", UNSET))


        resource = d.pop("resource", UNSET)

        def _parse_scopes_supported(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_supported_type_0 = cast(list[str], data)

                return scopes_supported_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scopes_supported = _parse_scopes_supported(d.pop("scopes_supported", UNSET))


        mcp_protected_resource_metadata = cls(
            authorization_servers=authorization_servers,
            bearer_methods_supported=bearer_methods_supported,
            resource=resource,
            scopes_supported=scopes_supported,
        )


        mcp_protected_resource_metadata.additional_properties = d
        return mcp_protected_resource_metadata

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
