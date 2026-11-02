from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.google_cloud_service_account_with_key import GoogleCloudServiceAccountWithKey





T = TypeVar("T", bound="PostServiceAccountJSONResponse200")



@_attrs_define
class PostServiceAccountJSONResponse200:
    """ 
        Attributes:
            data (GoogleCloudServiceAccountWithKey | Unset): GoogleCloudServiceAccountWithKey defines a Google Cloud service
                account and its key in cloudtamer.io.
            status (int | Unset): HTTP status code of the response Example: 200.
     """

    data: GoogleCloudServiceAccountWithKey | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.google_cloud_service_account_with_key import GoogleCloudServiceAccountWithKey
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_cloud_service_account_with_key import GoogleCloudServiceAccountWithKey
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: GoogleCloudServiceAccountWithKey | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = GoogleCloudServiceAccountWithKey.from_dict(_data)




        status = d.pop("status", UNSET)

        post_service_account_json_response_200 = cls(
            data=data,
            status=status,
        )


        post_service_account_json_response_200.additional_properties = d
        return post_service_account_json_response_200

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
