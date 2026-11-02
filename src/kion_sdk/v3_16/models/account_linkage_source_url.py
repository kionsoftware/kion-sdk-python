from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AccountLinkageSourceURL")



@_attrs_define
class AccountLinkageSourceURL:
    """ AccountLinkageSourceURL contains a link to the URL the user should be redirected back to after completing the
    account linkage process.

        Attributes:
            source_url (str | Unset): The URL which account linkage should redirect back to after the OAuth flow is
                complete. Example: http://cloudtamer/project/1/.
     """

    source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source_url = self.source_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_url = d.pop("source_url", UNSET)

        account_linkage_source_url = cls(
            source_url=source_url,
        )


        account_linkage_source_url.additional_properties = d
        return account_linkage_source_url

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
