from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AuthCreate")



@_attrs_define
class AuthCreate:
    """ AuthCreate defines a request to create an AuthToken.

        Attributes:
            idms (int | Unset): IDMS ID of the User requesting authentication. Example: 1.
            password (str | Unset): Password of the User requesting authentication. Example: password.
            username (str | Unset): Username of the User requesting authentication. Example: admin.
     """

    idms: int | Unset = UNSET
    password: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        idms = self.idms

        password = self.password

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if idms is not UNSET:
            field_dict["idms"] = idms
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idms = d.pop("idms", UNSET)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        auth_create = cls(
            idms=idms,
            password=password,
            username=username,
        )


        auth_create.additional_properties = d
        return auth_create

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
