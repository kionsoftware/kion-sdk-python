from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GoogleCloudServiceAccount")



@_attrs_define
class GoogleCloudServiceAccount:
    """ GoogleCloudServiceAccount defines a Google Cloud service account in cloudtamer.io.

        Attributes:
            created_at (datetime.datetime | Unset): CreatedAt represents when the service account was added to cloudtamer.io
            description (str | Unset): Description is a brief description of the service account
            disabled (bool | None | Unset): Disabled is true if the service account is disabled with GCP
            display_name (str | Unset): DisplayName is a human-friendly name for the service account
            email (str | Unset): Email is the google-designated email id for the service account
            enable_federation_support (bool | None | Unset): EnableFederationSupport represents if the service account will
                be used for federation
            gcp_project_id (str | Unset): GCPProjectID is the Google Cloud Project that the service account was created in
            id (int | Unset): ID is the cloudtamer.io internal ID for the service account
            name (str | Unset): Name is the kebab-case name for the service account
            oauth_client_id (str | Unset): OAuthClientID is the client id for an oauth client in the service account's
                project
            oauth_client_secret (str | Unset): OAuthClientSecret is the client secret for an oauth client in the service
                account's project
            unique_id (str | Unset): UniqueID is the client id used to authenticate in tandem with a key
     """

    created_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    disabled: bool | None | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    enable_federation_support: bool | None | Unset = UNSET
    gcp_project_id: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    oauth_client_id: str | Unset = UNSET
    oauth_client_secret: str | Unset = UNSET
    unique_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        disabled: bool | None | Unset
        if isinstance(self.disabled, Unset):
            disabled = UNSET
        else:
            disabled = self.disabled

        display_name = self.display_name

        email = self.email

        enable_federation_support: bool | None | Unset
        if isinstance(self.enable_federation_support, Unset):
            enable_federation_support = UNSET
        else:
            enable_federation_support = self.enable_federation_support

        gcp_project_id = self.gcp_project_id

        id = self.id

        name = self.name

        oauth_client_id = self.oauth_client_id

        oauth_client_secret = self.oauth_client_secret

        unique_id = self.unique_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if enable_federation_support is not UNSET:
            field_dict["enable_federation_support"] = enable_federation_support
        if gcp_project_id is not UNSET:
            field_dict["gcp_project_id"] = gcp_project_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if oauth_client_id is not UNSET:
            field_dict["oauth_client_id"] = oauth_client_id
        if oauth_client_secret is not UNSET:
            field_dict["oauth_client_secret"] = oauth_client_secret
        if unique_id is not UNSET:
            field_dict["unique_id"] = unique_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        description = d.pop("description", UNSET)

        def _parse_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        disabled = _parse_disabled(d.pop("disabled", UNSET))


        display_name = d.pop("display_name", UNSET)

        email = d.pop("email", UNSET)

        def _parse_enable_federation_support(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_federation_support = _parse_enable_federation_support(d.pop("enable_federation_support", UNSET))


        gcp_project_id = d.pop("gcp_project_id", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        oauth_client_id = d.pop("oauth_client_id", UNSET)

        oauth_client_secret = d.pop("oauth_client_secret", UNSET)

        unique_id = d.pop("unique_id", UNSET)

        google_cloud_service_account = cls(
            created_at=created_at,
            description=description,
            disabled=disabled,
            display_name=display_name,
            email=email,
            enable_federation_support=enable_federation_support,
            gcp_project_id=gcp_project_id,
            id=id,
            name=name,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
            unique_id=unique_id,
        )


        google_cloud_service_account.additional_properties = d
        return google_cloud_service_account

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
