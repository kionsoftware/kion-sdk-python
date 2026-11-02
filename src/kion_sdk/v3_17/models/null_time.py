from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="NullTime")



@_attrs_define
class NullTime:
    """ NullTime represents a time.Time that may be NULL.

        Attributes:
            time (datetime.datetime | Unset):
            valid (bool | None | Unset):
     """

    time: datetime.datetime | Unset = UNSET
    valid: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        valid: bool | None | Unset
        if isinstance(self.valid, Unset):
            valid = UNSET
        else:
            valid = self.valid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if time is not UNSET:
            field_dict["Time"] = time
        if valid is not UNSET:
            field_dict["Valid"] = valid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _time = d.pop("Time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)




        def _parse_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        valid = _parse_valid(d.pop("Valid", UNSET))


        null_time = cls(
            time=time,
            valid=valid,
        )


        null_time.additional_properties = d
        return null_time

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
