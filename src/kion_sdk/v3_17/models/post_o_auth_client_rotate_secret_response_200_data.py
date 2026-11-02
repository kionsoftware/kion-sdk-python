from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostOAuthClientRotateSecretResponse200Data")



@_attrs_define
class PostOAuthClientRotateSecretResponse200Data:
    """ The new client secret.

        Example:
            new_secret_value

        Attributes:
            secret (str | Unset):
     """

    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        secret = self.secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("secret", UNSET)

        post_o_auth_client_rotate_secret_response_200_data = cls(
            secret=secret,
        )


        post_o_auth_client_rotate_secret_response_200_data.additional_properties = d
        return post_o_auth_client_rotate_secret_response_200_data

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
