from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomWhiteLabelConfig")



@_attrs_define
class CustomWhiteLabelConfig:
    """ CustomWhiteLabelConfig represents the system settings for custom white labeling

        Attributes:
            custom_white_label_copyright_text (str | Unset): Custom copyright text to show in the application Example:
                Copyright (c) Company Name 2024.
            custom_white_label_product_text (str | Unset): Custom product text to show in the application Example: Product
                Name.
     """

    custom_white_label_copyright_text: str | Unset = UNSET
    custom_white_label_product_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        custom_white_label_copyright_text = self.custom_white_label_copyright_text

        custom_white_label_product_text = self.custom_white_label_product_text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if custom_white_label_copyright_text is not UNSET:
            field_dict["custom_white_label_copyright_text"] = custom_white_label_copyright_text
        if custom_white_label_product_text is not UNSET:
            field_dict["custom_white_label_product_text"] = custom_white_label_product_text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_white_label_copyright_text = d.pop("custom_white_label_copyright_text", UNSET)

        custom_white_label_product_text = d.pop("custom_white_label_product_text", UNSET)

        custom_white_label_config = cls(
            custom_white_label_copyright_text=custom_white_label_copyright_text,
            custom_white_label_product_text=custom_white_label_product_text,
        )


        custom_white_label_config.additional_properties = d
        return custom_white_label_config

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
