from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AuthToken")



@_attrs_define
class AuthToken:
    """ AuthToken defines a user token.

        Attributes:
            expiry (str | Unset): Date when the token expires. Example: 2019-02-12T22:57:10+0000.
            token (str | Unset): A token string used to access the application. Example:
                abcdefghijklmnopqrstuvwxyz1234567890.
            user_id (int | None | Unset): User ID of the owner of the token. Example: 1.
     """

    expiry: str | Unset = UNSET
    token: str | Unset = UNSET
    user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        expiry = self.expiry

        token = self.token

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if token is not UNSET:
            field_dict["token"] = token
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expiry = d.pop("expiry", UNSET)

        token = d.pop("token", UNSET)

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        auth_token = cls(
            expiry=expiry,
            token=token,
            user_id=user_id,
        )


        auth_token.additional_properties = d
        return auth_token

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
