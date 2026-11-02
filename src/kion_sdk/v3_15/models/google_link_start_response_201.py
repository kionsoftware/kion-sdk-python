from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.google_oauth_link import GoogleOauthLink





T = TypeVar("T", bound="GoogleLinkStartResponse201")



@_attrs_define
class GoogleLinkStartResponse201:
    """ 
        Attributes:
            data (GoogleOauthLink | Unset): GoogleOauthLink contains an OAuth URL which can be used for Google account
                linkage
            status (int | Unset): HTTP status code of the response Example: 200.
     """

    data: GoogleOauthLink | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.google_oauth_link import GoogleOauthLink
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_oauth_link import GoogleOauthLink
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: GoogleOauthLink | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = GoogleOauthLink.from_dict(_data)




        status = d.pop("status", UNSET)

        google_link_start_response_201 = cls(
            data=data,
            status=status,
        )


        google_link_start_response_201.additional_properties = d
        return google_link_start_response_201

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
