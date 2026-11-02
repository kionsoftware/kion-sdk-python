from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomMessagingConfig")



@_attrs_define
class CustomMessagingConfig:
    """ CustomMessagingConfig represents the system settings for custom messaging in the app

        Attributes:
            banner_bg_color (str | Unset): The background color for the application banner Example: #112233.
            banner_text (str | Unset): The application banner text. Appears above and below the content at all times
                Example: Company Name Cloud Resources.
            banner_text_color (str | Unset): The text color for the application banner Example: #FFFFFF.
            login_text (str | Unset): The text shown above the login fields Example: Login Page.
            modal_text (str | Unset): The text displayed in a modal as users log in Example: Some message that users must
                acknowledge.
     """

    banner_bg_color: str | Unset = UNSET
    banner_text: str | Unset = UNSET
    banner_text_color: str | Unset = UNSET
    login_text: str | Unset = UNSET
    modal_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        banner_bg_color = self.banner_bg_color

        banner_text = self.banner_text

        banner_text_color = self.banner_text_color

        login_text = self.login_text

        modal_text = self.modal_text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if banner_bg_color is not UNSET:
            field_dict["banner_bg_color"] = banner_bg_color
        if banner_text is not UNSET:
            field_dict["banner_text"] = banner_text
        if banner_text_color is not UNSET:
            field_dict["banner_text_color"] = banner_text_color
        if login_text is not UNSET:
            field_dict["login_text"] = login_text
        if modal_text is not UNSET:
            field_dict["modal_text"] = modal_text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        banner_bg_color = d.pop("banner_bg_color", UNSET)

        banner_text = d.pop("banner_text", UNSET)

        banner_text_color = d.pop("banner_text_color", UNSET)

        login_text = d.pop("login_text", UNSET)

        modal_text = d.pop("modal_text", UNSET)

        custom_messaging_config = cls(
            banner_bg_color=banner_bg_color,
            banner_text=banner_text,
            banner_text_color=banner_text_color,
            login_text=login_text,
            modal_text=modal_text,
        )


        custom_messaging_config.additional_properties = d
        return custom_messaging_config

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
