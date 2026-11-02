from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IDMSUpdatable")



@_attrs_define
class IDMSUpdatable:
    """ IDMSUpdatable defines an IDMS update.

        Attributes:
            idms_type_id (int | None | Unset): ID of the IDMS type in the application. 1 is Internal Directory, 2 is
                Active Directory, 3 is SAML. Example: 1.
            name (str | Unset): Name of the IDMS in the application. Example: Internal Directory.
            password_expiration (int | Unset): Number of days until a password reset dialog displays on login. Example: 90.
     """

    idms_type_id: int | None | Unset = UNSET
    name: str | Unset = UNSET
    password_expiration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        idms_type_id: int | None | Unset
        if isinstance(self.idms_type_id, Unset):
            idms_type_id = UNSET
        else:
            idms_type_id = self.idms_type_id

        name = self.name

        password_expiration = self.password_expiration


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if idms_type_id is not UNSET:
            field_dict["idms_type_id"] = idms_type_id
        if name is not UNSET:
            field_dict["name"] = name
        if password_expiration is not UNSET:
            field_dict["password_expiration"] = password_expiration

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_idms_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idms_type_id = _parse_idms_type_id(d.pop("idms_type_id", UNSET))


        name = d.pop("name", UNSET)

        password_expiration = d.pop("password_expiration", UNSET)

        idms_updatable = cls(
            idms_type_id=idms_type_id,
            name=name,
            password_expiration=password_expiration,
        )


        idms_updatable.additional_properties = d
        return idms_updatable

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
