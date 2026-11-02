from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO






T = TypeVar("T", bound="PostServiceAccountJSONBody")



@_attrs_define
class PostServiceAccountJSONBody:
    """ 
        Attributes:
            description (str): Description is a brief description of the service account
            enable_federation_support (bool): EnableFederationSupport represents if the service account will be used for
                federation
            name (str): Name is the kebab-case name for the service account
            json (File | Unset): JSON is the json key file downloaded from the Google Cloud Console
            oauth_client_id (str | Unset): OAuthClientID is the client id for an oauth client in the service account's
                project
            oauth_client_secret (str | Unset): OAuthClientSecret is the client secret for an oauth client in the service
                account's project
     """

    description: str
    enable_federation_support: bool
    name: str
    json: File | Unset = UNSET
    oauth_client_id: str | Unset = UNSET
    oauth_client_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        enable_federation_support = self.enable_federation_support

        name = self.name

        json: FileTypes | Unset = UNSET
        if not isinstance(self.json, Unset):
            json = self.json.to_tuple()


        oauth_client_id = self.oauth_client_id

        oauth_client_secret = self.oauth_client_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "description": description,
            "enable_federation_support": enable_federation_support,
            "name": name,
        })
        if json is not UNSET:
            field_dict["json"] = json
        if oauth_client_id is not UNSET:
            field_dict["oauth_client_id"] = oauth_client_id
        if oauth_client_secret is not UNSET:
            field_dict["oauth_client_secret"] = oauth_client_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        enable_federation_support = d.pop("enable_federation_support")

        name = d.pop("name")

        _json = d.pop("json", UNSET)
        json: File | Unset
        if isinstance(_json,  Unset):
            json = UNSET
        else:
            json = File(
             payload = BytesIO(_json)
        )




        oauth_client_id = d.pop("oauth_client_id", UNSET)

        oauth_client_secret = d.pop("oauth_client_secret", UNSET)

        post_service_account_json_body = cls(
            description=description,
            enable_federation_support=enable_federation_support,
            name=name,
            json=json,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
        )


        post_service_account_json_body.additional_properties = d
        return post_service_account_json_body

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
