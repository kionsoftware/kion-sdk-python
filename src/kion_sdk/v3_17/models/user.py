from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ User defines a user.

        Attributes:
            created_at (str | Unset): Date when the user was created in the application. Example: 2019-02-12T22:57:10+0000.
            deleted_at (None | str | Unset): Date when the user was deleted from the application if the user is deleted, or
                null otherwise Example: 2019-02-12T22:57:10+0000.
            display_name (str | Unset): Display name of the user. Example: John Doe.
            email (str | Unset): Email address of the user. Example: jdoe@example.com.
            enabled (bool | None | Unset): True if the user is enabled and false if the user is disabled.
            first_name (str | Unset): First name of the user. Example: John.
            id (int | Unset): ID of the record in the application. Example: 1.
            idms_id (int | None | Unset): ID of the IDMS where the user exists. Example: 1.
            last_login (str | Unset): Date of the user's last login to the application. Example: 2019-02-12T22:57:10+0000.
            last_name (str | Unset): Last name of the user. Example: Doe.
            password_needs_update (bool | None | Unset): True means the user will be prompted to change their password on
                next login.
            phone (str | Unset): Phone number of the user. Example: 123-555-4567.
            username (str | Unset): Username of the user. Example: jdoe.
     """

    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    display_name: str | Unset = UNSET
    email: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    first_name: str | Unset = UNSET
    id: int | Unset = UNSET
    idms_id: int | None | Unset = UNSET
    last_login: str | Unset = UNSET
    last_name: str | Unset = UNSET
    password_needs_update: bool | None | Unset = UNSET
    phone: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        display_name = self.display_name

        email = self.email

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        first_name = self.first_name

        id = self.id

        idms_id: int | None | Unset
        if isinstance(self.idms_id, Unset):
            idms_id = UNSET
        else:
            idms_id = self.idms_id

        last_login = self.last_login

        last_name = self.last_name

        password_needs_update: bool | None | Unset
        if isinstance(self.password_needs_update, Unset):
            password_needs_update = UNSET
        else:
            password_needs_update = self.password_needs_update

        phone = self.phone

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if idms_id is not UNSET:
            field_dict["idms_id"] = idms_id
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if password_needs_update is not UNSET:
            field_dict["password_needs_update"] = password_needs_update
        if phone is not UNSET:
            field_dict["phone"] = phone
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        display_name = d.pop("display_name", UNSET)

        email = d.pop("email", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        def _parse_idms_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idms_id = _parse_idms_id(d.pop("idms_id", UNSET))


        last_login = d.pop("last_login", UNSET)

        last_name = d.pop("last_name", UNSET)

        def _parse_password_needs_update(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        password_needs_update = _parse_password_needs_update(d.pop("password_needs_update", UNSET))


        phone = d.pop("phone", UNSET)

        username = d.pop("username", UNSET)

        user = cls(
            created_at=created_at,
            deleted_at=deleted_at,
            display_name=display_name,
            email=email,
            enabled=enabled,
            first_name=first_name,
            id=id,
            idms_id=idms_id,
            last_login=last_login,
            last_name=last_name,
            password_needs_update=password_needs_update,
            phone=phone,
            username=username,
        )


        user.additional_properties = d
        return user

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
