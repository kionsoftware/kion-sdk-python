from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GoogleCloudServiceAccountKeyCreate")



@_attrs_define
class GoogleCloudServiceAccountKeyCreate:
    """ GoogleCloudServiceAccountKeyCreate defines creating a key attached to a google cloud service account

        Attributes:
            key_data (str): KeyData is the json data used to authenticate with the Google APIs
            name (str): Name is the kebab-case name for the service account key
            key_origin (str | Unset): KeyOrigin indicates if the key pair is managed by Google Cloud or manually
     """

    key_data: str
    name: str
    key_origin: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key_data = self.key_data

        name = self.name

        key_origin = self.key_origin


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key_data": key_data,
            "name": name,
        })
        if key_origin is not UNSET:
            field_dict["key_origin"] = key_origin

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_data = d.pop("key_data")

        name = d.pop("name")

        key_origin = d.pop("key_origin", UNSET)

        google_cloud_service_account_key_create = cls(
            key_data=key_data,
            name=name,
            key_origin=key_origin,
        )


        google_cloud_service_account_key_create.additional_properties = d
        return google_cloud_service_account_key_create

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
