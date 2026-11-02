from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ResourceListItem")



@_attrs_define
class ResourceListItem:
    """ 
        Attributes:
            account_name (str | Unset): Name of the account the resource exists under. Example: AccountName.
            account_number (str | Unset): AccountNumber the resource exists under. Example: 1234.
            cloud_provider_id (int | None | Unset): ID of the cloud provider in the application. Example: 1.
            deleted_at (None | str | Unset): Date when the resource was deleted. Example: 2019-02-12T22:57:10+0000.
            id (int | Unset): ID of the record in the application. Example: 1.
            mtd_cost (float | Unset): The cost of the resource over the current month. Example: 12.13.
            project_id (int | None | Unset): ID of project the resource exists under. Example: 1.
            project_name (str | Unset): Name of project the resource exists under. Example: ProjectName.
            range_cost (float | Unset): The cost of the resource over the selected active range. Example: 143.23.
            region (str | Unset): The region the resource exists in. Example: us-east-1.
            resource_created_at (str | Unset): Date when the resource was created. Example: 2019-02-12T22:57:10+0000.
            resource_id (str | Unset): ID of the resource for a cloud provider. Example: 1234.
            resource_name (str | Unset): Name of the resource. Example: ResourceName.
            resource_type (str | Unset): Name of the Resource Type. Example: TypeName.
            size (str | Unset): The size the resource. Example: t2.micro.
     """

    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    cloud_provider_id: int | None | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    id: int | Unset = UNSET
    mtd_cost: float | Unset = UNSET
    project_id: int | None | Unset = UNSET
    project_name: str | Unset = UNSET
    range_cost: float | Unset = UNSET
    region: str | Unset = UNSET
    resource_created_at: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    resource_name: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    size: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        account_number = self.account_number

        cloud_provider_id: int | None | Unset
        if isinstance(self.cloud_provider_id, Unset):
            cloud_provider_id = UNSET
        else:
            cloud_provider_id = self.cloud_provider_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        id = self.id

        mtd_cost = self.mtd_cost

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        project_name = self.project_name

        range_cost = self.range_cost

        region = self.region

        resource_created_at = self.resource_created_at

        resource_id = self.resource_id

        resource_name = self.resource_name

        resource_type = self.resource_type

        size = self.size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if cloud_provider_id is not UNSET:
            field_dict["cloud_provider_id"] = cloud_provider_id
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if id is not UNSET:
            field_dict["id"] = id
        if mtd_cost is not UNSET:
            field_dict["mtd_cost"] = mtd_cost
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if range_cost is not UNSET:
            field_dict["range_cost"] = range_cost
        if region is not UNSET:
            field_dict["region"] = region
        if resource_created_at is not UNSET:
            field_dict["resource_created_at"] = resource_created_at
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("account_name", UNSET)

        account_number = d.pop("account_number", UNSET)

        def _parse_cloud_provider_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_provider_id = _parse_cloud_provider_id(d.pop("cloud_provider_id", UNSET))


        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        id = d.pop("id", UNSET)

        mtd_cost = d.pop("mtd_cost", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        project_name = d.pop("project_name", UNSET)

        range_cost = d.pop("range_cost", UNSET)

        region = d.pop("region", UNSET)

        resource_created_at = d.pop("resource_created_at", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        resource_name = d.pop("resource_name", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        size = d.pop("size", UNSET)

        resource_list_item = cls(
            account_name=account_name,
            account_number=account_number,
            cloud_provider_id=cloud_provider_id,
            deleted_at=deleted_at,
            id=id,
            mtd_cost=mtd_cost,
            project_id=project_id,
            project_name=project_name,
            range_cost=range_cost,
            region=region,
            resource_created_at=resource_created_at,
            resource_id=resource_id,
            resource_name=resource_name,
            resource_type=resource_type,
            size=size,
        )


        resource_list_item.additional_properties = d
        return resource_list_item

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
