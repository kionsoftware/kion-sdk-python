from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SystemDiagnosticsConfig")



@_attrs_define
class SystemDiagnosticsConfig:
    """ SystemDiagnosticsConfig represents the system settings for system diagnostics

        Attributes:
            autorefresh_enabled (bool | None | Unset): AutoRefresh enabled status Example: True.
            autorefresh_interval (str | Unset): Examples: "3 days", "12 hours", "4 weeks"
            notification_frequency (str | Unset): Examples: "3 days", "12 hours", "4 weeks"
     """

    autorefresh_enabled: bool | None | Unset = UNSET
    autorefresh_interval: str | Unset = UNSET
    notification_frequency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        autorefresh_enabled: bool | None | Unset
        if isinstance(self.autorefresh_enabled, Unset):
            autorefresh_enabled = UNSET
        else:
            autorefresh_enabled = self.autorefresh_enabled

        autorefresh_interval = self.autorefresh_interval

        notification_frequency = self.notification_frequency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if autorefresh_enabled is not UNSET:
            field_dict["autorefresh_enabled"] = autorefresh_enabled
        if autorefresh_interval is not UNSET:
            field_dict["autorefresh_interval"] = autorefresh_interval
        if notification_frequency is not UNSET:
            field_dict["notification_frequency"] = notification_frequency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_autorefresh_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        autorefresh_enabled = _parse_autorefresh_enabled(d.pop("autorefresh_enabled", UNSET))


        autorefresh_interval = d.pop("autorefresh_interval", UNSET)

        notification_frequency = d.pop("notification_frequency", UNSET)

        system_diagnostics_config = cls(
            autorefresh_enabled=autorefresh_enabled,
            autorefresh_interval=autorefresh_interval,
            notification_frequency=notification_frequency,
        )


        system_diagnostics_config.additional_properties = d
        return system_diagnostics_config

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
