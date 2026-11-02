from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="IDMSCreate")



@_attrs_define
class IDMSCreate:
    """ IDMSCreate defines an identity management system creation.

        Attributes:
            idms_type_id (int | None): ID of the IDMS type in the application. 1 is Internal Directory, 2 is
                Active Directory, 3 is SAML. Example: 1.
            name (str): Name of the IDMS in the application. Example: Internal Directory.
            password_expiration (int): Number of days until a password reset dialog displays on login. Example: 90.
     """

    idms_type_id: int | None
    name: str
    password_expiration: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        idms_type_id: int | None
        idms_type_id = self.idms_type_id

        name = self.name

        password_expiration = self.password_expiration


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "idms_type_id": idms_type_id,
            "name": name,
            "password_expiration": password_expiration,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_idms_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        idms_type_id = _parse_idms_type_id(d.pop("idms_type_id"))


        name = d.pop("name")

        password_expiration = d.pop("password_expiration")

        idms_create = cls(
            idms_type_id=idms_type_id,
            name=name,
            password_expiration=password_expiration,
        )


        idms_create.additional_properties = d
        return idms_create

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
