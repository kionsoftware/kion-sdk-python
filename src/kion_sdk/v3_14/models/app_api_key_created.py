from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AppAPIKeyCreated")



@_attrs_define
class AppAPIKeyCreated:
    """ AppAPIKeyCreated defines an App API Key creation response.

        Attributes:
            id (int | Unset): ID of the record in the application. Example: 1.
            key (str | Unset): Secret key. Example: a_key_123.
     """

    id: int | Unset = UNSET
    key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        app_api_key_created = cls(
            id=id,
            key=key,
        )


        app_api_key_created.additional_properties = d
        return app_api_key_created

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
