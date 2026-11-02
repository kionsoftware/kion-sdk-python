from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UserUpdatable")



@_attrs_define
class UserUpdatable:
    """ UserUpdatable defines a user update.

        Attributes:
            email (str | Unset): Email address of the user. Example: jdoe@example.com.
            enabled (bool | None | Unset): True if the user is enabled and false if the user is disabled. Example: True.
            first_name (str | Unset): First name of the user. Example: John.
            last_name (str | Unset): Last name of the user. Example: Doe.
            mfa (int | Unset): The ID of the MFA type. Options: 1 is Webauthn (Yubikey), 2 is TOTP (Google Auth). Example:
                1.
            phone (str | Unset): Phone number of the user. Example: 123-555-4567.
            username (str | Unset): Username of the user. Example: jdoe.
     """

    email: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    mfa: int | Unset = UNSET
    phone: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        first_name = self.first_name

        last_name = self.last_name

        mfa = self.mfa

        phone = self.phone

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if mfa is not UNSET:
            field_dict["mfa"] = mfa
        if phone is not UNSET:
            field_dict["phone"] = phone
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        mfa = d.pop("mfa", UNSET)

        phone = d.pop("phone", UNSET)

        username = d.pop("username", UNSET)

        user_updatable = cls(
            email=email,
            enabled=enabled,
            first_name=first_name,
            last_name=last_name,
            mfa=mfa,
            phone=phone,
            username=username,
        )


        user_updatable.additional_properties = d
        return user_updatable

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
