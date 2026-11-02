from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UserCreate")



@_attrs_define
class UserCreate:
    """ UserCreate defines a user creation.

        Attributes:
            email (str): Email address of the user. Example: jdoe@example.com.
            first_name (str): First name of the user. Example: John.
            idms_id (int | None): ID of the IDMS where the user exists. Example: 1.
            last_name (str): Last name of the user. Example: Doe.
            username (str): Username of the user. Example: jdoe.
            mfa (int | Unset): The ID of the MFA type. Options: 1 is Webauthn (Yubikey), 2 is TOTP (Google Auth). Example:
                1.
            phone (str | Unset): Phone number of the user. Example: 123-555-4567.
            user_group_ids (list[int] | None | Unset): List of IDs of groups the user is in. Example: [1, 2].
     """

    email: str
    first_name: str
    idms_id: int | None
    last_name: str
    username: str
    mfa: int | Unset = UNSET
    phone: str | Unset = UNSET
    user_group_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        idms_id: int | None
        idms_id = self.idms_id

        last_name = self.last_name

        username = self.username

        mfa = self.mfa

        phone = self.phone

        user_group_ids: list[int] | None | Unset
        if isinstance(self.user_group_ids, Unset):
            user_group_ids = UNSET
        elif isinstance(self.user_group_ids, list):
            user_group_ids = self.user_group_ids


        else:
            user_group_ids = self.user_group_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "email": email,
            "first_name": first_name,
            "idms_id": idms_id,
            "last_name": last_name,
            "username": username,
        })
        if mfa is not UNSET:
            field_dict["mfa"] = mfa
        if phone is not UNSET:
            field_dict["phone"] = phone
        if user_group_ids is not UNSET:
            field_dict["user_group_ids"] = user_group_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        first_name = d.pop("first_name")

        def _parse_idms_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        idms_id = _parse_idms_id(d.pop("idms_id"))


        last_name = d.pop("last_name")

        username = d.pop("username")

        mfa = d.pop("mfa", UNSET)

        phone = d.pop("phone", UNSET)

        def _parse_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_group_ids_type_0 = cast(list[int], data)

                return user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_group_ids = _parse_user_group_ids(d.pop("user_group_ids", UNSET))


        user_create = cls(
            email=email,
            first_name=first_name,
            idms_id=idms_id,
            last_name=last_name,
            username=username,
            mfa=mfa,
            phone=phone,
            user_group_ids=user_group_ids,
        )


        user_create.additional_properties = d
        return user_create

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
