from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ServiceWithProviderTypeID")



@_attrs_define
class ServiceWithProviderTypeID:
    """ ServiceWithProviderTypeID .

        Attributes:
            cloud_provider_type_id (int | None | Unset): The ID of the cloud provider type that this service belongs to. 1
                is AWS, 2 is Azure, 3 is Google Cloud, and 4 is OCI. Example: 1.
            id (int | Unset): ID of the service. Example: 1.
            name (str | Unset): Service name Example: EC2.
     """

    cloud_provider_type_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cloud_provider_type_id: int | None | Unset
        if isinstance(self.cloud_provider_type_id, Unset):
            cloud_provider_type_id = UNSET
        else:
            cloud_provider_type_id = self.cloud_provider_type_id

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cloud_provider_type_id is not UNSET:
            field_dict["cloud_provider_type_id"] = cloud_provider_type_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cloud_provider_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_provider_type_id = _parse_cloud_provider_type_id(d.pop("cloud_provider_type_id", UNSET))


        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        service_with_provider_type_id = cls(
            cloud_provider_type_id=cloud_provider_type_id,
            id=id,
            name=name,
        )


        service_with_provider_type_id.additional_properties = d
        return service_with_provider_type_id

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
