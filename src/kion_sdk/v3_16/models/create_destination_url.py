from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateDestinationURL")



@_attrs_define
class CreateDestinationURL:
    """ CreateDestinationURL defines an additional destination url to validate a saml idms against

        Attributes:
            destination_url (str | Unset): Additional destination URL to use for SAML validation for an IDMS Example:
                http://localhost:8400/callback.
     """

    destination_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        destination_url = self.destination_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if destination_url is not UNSET:
            field_dict["destination_url"] = destination_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_url = d.pop("destination_url", UNSET)

        create_destination_url = cls(
            destination_url=destination_url,
        )


        create_destination_url.additional_properties = d
        return create_destination_url

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
