from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GoogleOauthLink")



@_attrs_define
class GoogleOauthLink:
    """ GoogleOauthLink contains an OAuth URL which can be used for Google account linkage

        Attributes:
            oauth_url (str | Unset): The Google Login URL to redirect a user to begin linking a Google account. Example:
                https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount.
     """

    oauth_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        oauth_url = self.oauth_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if oauth_url is not UNSET:
            field_dict["oauth_url"] = oauth_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oauth_url = d.pop("oauth_url", UNSET)

        google_oauth_link = cls(
            oauth_url=oauth_url,
        )


        google_oauth_link.additional_properties = d
        return google_oauth_link

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
