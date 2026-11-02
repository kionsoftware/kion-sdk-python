from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LogExport")



@_attrs_define
class LogExport:
    """ LogExport defines a Log Export.

        Attributes:
            from_ (str): The start datecode of the range for the request, expressed as YYYYMMDD
                after 1970-01-01 00:00:00 UTC. Events with a timestamp earlier than this
                time are not exported. Example: 20201019.
     """

    from_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "From": from_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("From")

        log_export = cls(
            from_=from_,
        )


        log_export.additional_properties = d
        return log_export

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
