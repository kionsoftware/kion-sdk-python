from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.null_time import NullTime





T = TypeVar("T", bound="GoogleCloudServiceAccountKeyUpdate")



@_attrs_define
class GoogleCloudServiceAccountKeyUpdate:
    """ GoogleCloudServiceAccountKeyUpdate defines updating a key attached to a google cloud service account

        Attributes:
            key_data (str | Unset): KeyData is the json data used to authenticate with the Google APIs
            key_origin (str | Unset): KeyOrigin indicates if the key pair is managed by Google Cloud or manually
            name (str | Unset): Name is the kebab-case name for the service account key
            valid_after_time (NullTime | Unset): NullTime represents a time.Time that may be NULL.
            valid_before_time (NullTime | Unset): NullTime represents a time.Time that may be NULL.
     """

    key_data: str | Unset = UNSET
    key_origin: str | Unset = UNSET
    name: str | Unset = UNSET
    valid_after_time: NullTime | Unset = UNSET
    valid_before_time: NullTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_time import NullTime
        key_data = self.key_data

        key_origin = self.key_origin

        name = self.name

        valid_after_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valid_after_time, Unset):
            valid_after_time = self.valid_after_time.to_dict()

        valid_before_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valid_before_time, Unset):
            valid_before_time = self.valid_before_time.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if key_data is not UNSET:
            field_dict["key_data"] = key_data
        if key_origin is not UNSET:
            field_dict["key_origin"] = key_origin
        if name is not UNSET:
            field_dict["name"] = name
        if valid_after_time is not UNSET:
            field_dict["valid_after_time"] = valid_after_time
        if valid_before_time is not UNSET:
            field_dict["valid_before_time"] = valid_before_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_time import NullTime
        d = dict(src_dict)
        key_data = d.pop("key_data", UNSET)

        key_origin = d.pop("key_origin", UNSET)

        name = d.pop("name", UNSET)

        _valid_after_time = d.pop("valid_after_time", UNSET)
        valid_after_time: NullTime | Unset
        if isinstance(_valid_after_time,  Unset):
            valid_after_time = UNSET
        else:
            valid_after_time = NullTime.from_dict(_valid_after_time)




        _valid_before_time = d.pop("valid_before_time", UNSET)
        valid_before_time: NullTime | Unset
        if isinstance(_valid_before_time,  Unset):
            valid_before_time = UNSET
        else:
            valid_before_time = NullTime.from_dict(_valid_before_time)




        google_cloud_service_account_key_update = cls(
            key_data=key_data,
            key_origin=key_origin,
            name=name,
            valid_after_time=valid_after_time,
            valid_before_time=valid_before_time,
        )


        google_cloud_service_account_key_update.additional_properties = d
        return google_cloud_service_account_key_update

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
