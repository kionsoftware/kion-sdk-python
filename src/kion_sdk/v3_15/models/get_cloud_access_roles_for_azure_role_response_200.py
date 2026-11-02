from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloud_access_roles import CloudAccessRoles





T = TypeVar("T", bound="GetCloudAccessRolesForAzureRoleResponse200")



@_attrs_define
class GetCloudAccessRolesForAzureRoleResponse200:
    """ 
        Attributes:
            data (CloudAccessRoles | Unset): CloudAccessRoles defines all local and inherited cloud access roles visible to
                a user.
            status (int | Unset): HTTP status code. Example: 200.
     """

    data: CloudAccessRoles | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_access_roles import CloudAccessRoles
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
        from ..models.cloud_access_roles import CloudAccessRoles
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: CloudAccessRoles | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = CloudAccessRoles.from_dict(_data)




        status = d.pop("status", UNSET)

        get_cloud_access_roles_for_azure_role_response_200 = cls(
            data=data,
            status=status,
        )


        get_cloud_access_roles_for_azure_role_response_200.additional_properties = d
        return get_cloud_access_roles_for_azure_role_response_200

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
