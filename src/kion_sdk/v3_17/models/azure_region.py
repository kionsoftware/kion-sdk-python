from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzureRegion")



@_attrs_define
class AzureRegion:
    """ AzureRegion represents a cached Azure Region in the database

        Attributes:
            azure_name (str | Unset): The name of the Azure Region in Azure which is filled into ARM templates Example:
                eastus.
            created_at (str | Unset): Time when this Azure Region was first cached in cloudtamer.io Example:
                2019-02-12T22:57:10+0000.
            deleted_at (None | str | Unset): Time when this Azure Region was deleted in cloudtamer.io. May be null. Example:
                2019-02-12T22:57:10+0000.
            display_name (str | Unset): The human-readable name of the Azure Region from Azure. Example: East US.
            id (int | Unset): The ID cloudtamer.io refers to this Azure Region by Example: 1.
            updated_at (None | str | Unset): Time when this Azure Region was last refreshed in cloudtamer.io. May be null.
                Example: 2019-02-12T22:57:10+0000.
     """

    azure_name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: int | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        azure_name = self.azure_name

        created_at = self.created_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        display_name = self.display_name

        id = self.id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if azure_name is not UNSET:
            field_dict["azure_name"] = azure_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        azure_name = d.pop("azure_name", UNSET)

        created_at = d.pop("created_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        azure_region = cls(
            azure_name=azure_name,
            created_at=created_at,
            deleted_at=deleted_at,
            display_name=display_name,
            id=id,
            updated_at=updated_at,
        )


        azure_region.additional_properties = d
        return azure_region

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
