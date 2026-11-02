from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="HideIntegrationsStatus")



@_attrs_define
class HideIntegrationsStatus:
    """ HideIntegrationsStatus represents whether the integrations settings page should be hidden from users.

        Attributes:
            hide_integrations (bool | None | Unset): Indicates whether the integrations settings page should be hidden from
                users. Example: True.
     """

    hide_integrations: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hide_integrations: bool | None | Unset
        if isinstance(self.hide_integrations, Unset):
            hide_integrations = UNSET
        else:
            hide_integrations = self.hide_integrations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hide_integrations is not UNSET:
            field_dict["hide_integrations"] = hide_integrations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_hide_integrations(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hide_integrations = _parse_hide_integrations(d.pop("hide_integrations", UNSET))


        hide_integrations_status = cls(
            hide_integrations=hide_integrations,
        )


        hide_integrations_status.additional_properties = d
        return hide_integrations_status

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
