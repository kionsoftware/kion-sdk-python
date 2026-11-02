from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AWSStackTag")



@_attrs_define
class AWSStackTag:
    """ AWSStackTag defines an AWSStackTag in an account managed by cloudtamer.io.

        Attributes:
            tag_key (str | Unset): Key of the stack tag. Example: department.
            tag_value (str | Unset): Value of the stack tag. Example: engineering.
     """

    tag_key: str | Unset = UNSET
    tag_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tag_key = self.tag_key

        tag_value = self.tag_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tag_key is not UNSET:
            field_dict["tag_key"] = tag_key
        if tag_value is not UNSET:
            field_dict["tag_value"] = tag_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_key = d.pop("tag_key", UNSET)

        tag_value = d.pop("tag_value", UNSET)

        aws_stack_tag = cls(
            tag_key=tag_key,
            tag_value=tag_value,
        )


        aws_stack_tag.additional_properties = d
        return aws_stack_tag

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
