from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.google_cloud_project import GoogleCloudProject





T = TypeVar("T", bound="GCPBillingAccountProjectsDataBody")



@_attrs_define
class GCPBillingAccountProjectsDataBody:
    """ in:body

        Attributes:
            data (list[GoogleCloudProject] | Unset): The projects
            status (int | Unset): HTTP status code of the response Example: 200.
     """

    data: list[GoogleCloudProject] | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.google_cloud_project import GoogleCloudProject
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
        from ..models.google_cloud_project import GoogleCloudProject
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[GoogleCloudProject] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = GoogleCloudProject.from_dict(data_item_data)



                data.append(data_item)


        status = d.pop("status", UNSET)

        gcp_billing_account_projects_data_body = cls(
            data=data,
            status=status,
        )


        gcp_billing_account_projects_data_body.additional_properties = d
        return gcp_billing_account_projects_data_body

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
