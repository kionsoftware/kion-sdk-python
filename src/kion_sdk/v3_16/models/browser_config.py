from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BrowserConfig")



@_attrs_define
class BrowserConfig:
    """ BrowserConfig represents the system settings for browser warning banners

        Attributes:
            browser_warning_banner (bool | None | Unset): Indicates whether the browser warning banner for unsupported
                browsers is displayed or not Example: True.
     """

    browser_warning_banner: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        browser_warning_banner: bool | None | Unset
        if isinstance(self.browser_warning_banner, Unset):
            browser_warning_banner = UNSET
        else:
            browser_warning_banner = self.browser_warning_banner


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if browser_warning_banner is not UNSET:
            field_dict["browser_warning_banner"] = browser_warning_banner

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_browser_warning_banner(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        browser_warning_banner = _parse_browser_warning_banner(d.pop("browser_warning_banner", UNSET))


        browser_config = cls(
            browser_warning_banner=browser_warning_banner,
        )


        browser_config.additional_properties = d
        return browser_config

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
