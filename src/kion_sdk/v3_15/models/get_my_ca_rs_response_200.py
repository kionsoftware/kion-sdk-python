from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.augmented_cloud_access_role import AugmentedCloudAccessRole





T = TypeVar("T", bound="GetMyCARsResponse200")



@_attrs_define
class GetMyCARsResponse200:
    """ 
        Attributes:
            data (list[AugmentedCloudAccessRole] | Unset): List of project cloud access roles.
            status (int | Unset): HTTP status code. Example: 200.
     """

    data: list[AugmentedCloudAccessRole] | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.augmented_cloud_access_role import AugmentedCloudAccessRole
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



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
        from ..models.augmented_cloud_access_role import AugmentedCloudAccessRole
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[AugmentedCloudAccessRole] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = AugmentedCloudAccessRole.from_dict(data_item_data)



                data.append(data_item)


        status = d.pop("status", UNSET)

        get_my_ca_rs_response_200 = cls(
            data=data,
            status=status,
        )


        get_my_ca_rs_response_200.additional_properties = d
        return get_my_ca_rs_response_200

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
