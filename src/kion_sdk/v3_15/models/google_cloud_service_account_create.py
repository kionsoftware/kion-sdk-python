from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GoogleCloudServiceAccountCreate")



@_attrs_define
class GoogleCloudServiceAccountCreate:
    """ GoogleCloudServiceAccountCreate defines adding a Google Cloud service account to cloudtamer.io.

        Attributes:
            email (str): Email is the google-designated email id for the service account
            enable_federation_support (bool | None): EnableFederationSupport represents if the service account will be used
                for federation
            gcp_project_id (str): GCPProjectID is the Google Cloud Project that the service account was created in
            name (str): Name is the kebab-case name for the service account
            unique_id (str): UniqueID is the client id used to authenticate in tandem with a key
            description (str | Unset): Description is a brief description of the service account
            disabled (bool | None | Unset): Disabled is true if the service account is disabled with GCP Default: False.
            display_name (str | Unset): DisplayName is a human-friendly name for the service account
            oauth_client_id (str | Unset): OAuthClientID is the client id for an oauth client in the service account's
                project
            oauth_client_secret (str | Unset): OAuthClientSecret is the client secret for an oauth client in the service
                account's project
     """

    email: str
    enable_federation_support: bool | None
    gcp_project_id: str
    name: str
    unique_id: str
    description: str | Unset = UNSET
    disabled: bool | None | Unset = False
    display_name: str | Unset = UNSET
    oauth_client_id: str | Unset = UNSET
    oauth_client_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        enable_federation_support: bool | None
        enable_federation_support = self.enable_federation_support

        gcp_project_id = self.gcp_project_id

        name = self.name

        unique_id = self.unique_id

        description = self.description

        disabled: bool | None | Unset
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        display_name = self.display_name

        oauth_client_id = self.oauth_client_id

        oauth_client_secret = self.oauth_client_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "email": email,
            "enable_federation_support": enable_federation_support,
            "gcp_project_id": gcp_project_id,
            "name": name,
            "unique_id": unique_id,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if oauth_client_id is not UNSET:
            field_dict["oauth_client_id"] = oauth_client_id
        if oauth_client_secret is not UNSET:
            field_dict["oauth_client_secret"] = oauth_client_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_enable_federation_support(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        enable_federation_support = _parse_enable_federation_support(d.pop("enable_federation_support"))


        gcp_project_id = d.pop("gcp_project_id")

        name = d.pop("name")

        unique_id = d.pop("unique_id")

        description = d.pop("description", UNSET)

        def _parse_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))


        display_name = d.pop("display_name", UNSET)

        oauth_client_id = d.pop("oauth_client_id", UNSET)

        oauth_client_secret = d.pop("oauth_client_secret", UNSET)

        google_cloud_service_account_create = cls(
            email=email,
            enable_federation_support=enable_federation_support,
            gcp_project_id=gcp_project_id,
            name=name,
            unique_id=unique_id,
            description=description,
            disabled=disabled,
            display_name=display_name,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
        )


        google_cloud_service_account_create.additional_properties = d
        return google_cloud_service_account_create

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
