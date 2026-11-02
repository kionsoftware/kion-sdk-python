from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomBrandingConfig")



@_attrs_define
class CustomBrandingConfig:
    """ CustomBrandingConfig represents the system settings for custom branding options

        Attributes:
            custom_favicon (str | Unset): The favicon that appears in the browser tab
            custom_favicon_name (str | Unset): The filename of the custom favicon Example: favicon.png.
            custom_nav_logo (str | Unset): This logo will appear in the application nav bar
            custom_nav_logo_name (str | Unset): The filename of the custom nav logo Example: nav_logo.png.
            login_bg_color (str | Unset): Login screen background color Example: #000000.
            login_logo (str | Unset): This logo will appear on the login screen and in the application header.
            login_logo_name (str | Unset): The filename of the custom logo Example: login_logo.png.
            login_text_color (str | Unset): Login screen text color Example: #FFFFFF.
            product_name (str | Unset): Custom product name Example: Product Name.
            side_nav_accent_color (str | Unset): Left navigation accent color Example: #61D7AC.
            side_nav_bg_color (str | Unset): Left navigation background color Example: #101C21.
            side_nav_text_color (str | Unset): Left navigation text color Example: #CFD2D3.
     """

    custom_favicon: str | Unset = UNSET
    custom_favicon_name: str | Unset = UNSET
    custom_nav_logo: str | Unset = UNSET
    custom_nav_logo_name: str | Unset = UNSET
    login_bg_color: str | Unset = UNSET
    login_logo: str | Unset = UNSET
    login_logo_name: str | Unset = UNSET
    login_text_color: str | Unset = UNSET
    product_name: str | Unset = UNSET
    side_nav_accent_color: str | Unset = UNSET
    side_nav_bg_color: str | Unset = UNSET
    side_nav_text_color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        custom_favicon = self.custom_favicon

        custom_favicon_name = self.custom_favicon_name

        custom_nav_logo = self.custom_nav_logo

        custom_nav_logo_name = self.custom_nav_logo_name

        login_bg_color = self.login_bg_color

        login_logo = self.login_logo

        login_logo_name = self.login_logo_name

        login_text_color = self.login_text_color

        product_name = self.product_name

        side_nav_accent_color = self.side_nav_accent_color

        side_nav_bg_color = self.side_nav_bg_color

        side_nav_text_color = self.side_nav_text_color


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if custom_favicon is not UNSET:
            field_dict["custom_favicon"] = custom_favicon
        if custom_favicon_name is not UNSET:
            field_dict["custom_favicon_name"] = custom_favicon_name
        if custom_nav_logo is not UNSET:
            field_dict["custom_nav_logo"] = custom_nav_logo
        if custom_nav_logo_name is not UNSET:
            field_dict["custom_nav_logo_name"] = custom_nav_logo_name
        if login_bg_color is not UNSET:
            field_dict["login_bg_color"] = login_bg_color
        if login_logo is not UNSET:
            field_dict["login_logo"] = login_logo
        if login_logo_name is not UNSET:
            field_dict["login_logo_name"] = login_logo_name
        if login_text_color is not UNSET:
            field_dict["login_text_color"] = login_text_color
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if side_nav_accent_color is not UNSET:
            field_dict["side_nav_accent_color"] = side_nav_accent_color
        if side_nav_bg_color is not UNSET:
            field_dict["side_nav_bg_color"] = side_nav_bg_color
        if side_nav_text_color is not UNSET:
            field_dict["side_nav_text_color"] = side_nav_text_color

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_favicon = d.pop("custom_favicon", UNSET)

        custom_favicon_name = d.pop("custom_favicon_name", UNSET)

        custom_nav_logo = d.pop("custom_nav_logo", UNSET)

        custom_nav_logo_name = d.pop("custom_nav_logo_name", UNSET)

        login_bg_color = d.pop("login_bg_color", UNSET)

        login_logo = d.pop("login_logo", UNSET)

        login_logo_name = d.pop("login_logo_name", UNSET)

        login_text_color = d.pop("login_text_color", UNSET)

        product_name = d.pop("product_name", UNSET)

        side_nav_accent_color = d.pop("side_nav_accent_color", UNSET)

        side_nav_bg_color = d.pop("side_nav_bg_color", UNSET)

        side_nav_text_color = d.pop("side_nav_text_color", UNSET)

        custom_branding_config = cls(
            custom_favicon=custom_favicon,
            custom_favicon_name=custom_favicon_name,
            custom_nav_logo=custom_nav_logo,
            custom_nav_logo_name=custom_nav_logo_name,
            login_bg_color=login_bg_color,
            login_logo=login_logo,
            login_logo_name=login_logo_name,
            login_text_color=login_text_color,
            product_name=product_name,
            side_nav_accent_color=side_nav_accent_color,
            side_nav_bg_color=side_nav_bg_color,
            side_nav_text_color=side_nav_text_color,
        )


        custom_branding_config.additional_properties = d
        return custom_branding_config

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
