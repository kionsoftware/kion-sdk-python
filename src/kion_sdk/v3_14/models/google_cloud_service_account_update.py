from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GoogleCloudServiceAccountUpdate")



@_attrs_define
class GoogleCloudServiceAccountUpdate:
    """ GoogleCloudServiceAccountUpdate defines updating a Google Cloud service account on cloudtamer.io.

        Attributes:
            description (str | Unset): Description is a brief description of the service account
            display_name (str | Unset): DisplayName is a human-friendly name for the service account
            enable_federation_support (bool | None | Unset): EnableFederationSupport represents if the service account will
                be used for federation
            name (str | Unset): Name is the kebab-case name for the service account
            oauth_client_id (str | Unset): OAuthClientID is the client id for an oauth client in the service account's
                project
            oauth_client_secret (str | Unset): OAuthClientSecret is the client secret for an oauth client in the service
                account's project
     """

    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    enable_federation_support: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    oauth_client_id: str | Unset = UNSET
    oauth_client_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        enable_federation_support: bool | None | Unset
        if isinstance(self.enable_federation_support, Unset):
            enable_federation_support = UNSET
        else:
            enable_federation_support = self.enable_federation_support

        name = self.name

        oauth_client_id = self.oauth_client_id

        oauth_client_secret = self.oauth_client_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enable_federation_support is not UNSET:
            field_dict["enable_federation_support"] = enable_federation_support
        if name is not UNSET:
            field_dict["name"] = name
        if oauth_client_id is not UNSET:
            field_dict["oauth_client_id"] = oauth_client_id
        if oauth_client_secret is not UNSET:
            field_dict["oauth_client_secret"] = oauth_client_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        def _parse_enable_federation_support(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_federation_support = _parse_enable_federation_support(d.pop("enable_federation_support", UNSET))


        name = d.pop("name", UNSET)

        oauth_client_id = d.pop("oauth_client_id", UNSET)

        oauth_client_secret = d.pop("oauth_client_secret", UNSET)

        google_cloud_service_account_update = cls(
            description=description,
            display_name=display_name,
            enable_federation_support=enable_federation_support,
            name=name,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
        )


        google_cloud_service_account_update.additional_properties = d
        return google_cloud_service_account_update

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
