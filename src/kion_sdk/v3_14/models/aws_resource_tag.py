from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AWSResourceTag")



@_attrs_define
class AWSResourceTag:
    """ AWSResourceTag defines an AWS Resource Tag in the application.

        Attributes:
            id (int | Unset): ID of the record in the application. Example: 1.
            resource_key (str | Unset): ResourceKey is the resource tag's key. Example: aws_resource_key.
            resource_value (str | Unset): ResourceValue is the resource tag's value. Example: aws_resource_value.
     """

    id: int | Unset = UNSET
    resource_key: str | Unset = UNSET
    resource_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_key = self.resource_key

        resource_value = self.resource_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if resource_key is not UNSET:
            field_dict["resource_key"] = resource_key
        if resource_value is not UNSET:
            field_dict["resource_value"] = resource_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        resource_key = d.pop("resource_key", UNSET)

        resource_value = d.pop("resource_value", UNSET)

        aws_resource_tag = cls(
            id=id,
            resource_key=resource_key,
            resource_value=resource_value,
        )


        aws_resource_tag.additional_properties = d
        return aws_resource_tag

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
