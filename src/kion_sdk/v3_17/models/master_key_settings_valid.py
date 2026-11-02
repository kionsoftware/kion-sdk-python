from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MasterKeySettingsValid")



@_attrs_define
class MasterKeySettingsValid:
    """ 
        Attributes:
            can_read (bool | None | Unset): Application can read the secret value Example: True.
            can_write (bool | None | Unset): Application can write to the secret Example: True.
            read_error (str | Unset): Why the application cannot read the secret value
            write_error (str | Unset): Why the application cannot write to the secret
     """

    can_read: bool | None | Unset = UNSET
    can_write: bool | None | Unset = UNSET
    read_error: str | Unset = UNSET
    write_error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_read: bool | None | Unset
        if isinstance(self.can_read, Unset):
            can_read = UNSET
        else:
            can_read = self.can_read

        can_write: bool | None | Unset
        if isinstance(self.can_write, Unset):
            can_write = UNSET
        else:
            can_write = self.can_write

        read_error = self.read_error

        write_error = self.write_error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_read is not UNSET:
            field_dict["canRead"] = can_read
        if can_write is not UNSET:
            field_dict["canWrite"] = can_write
        if read_error is not UNSET:
            field_dict["readError"] = read_error
        if write_error is not UNSET:
            field_dict["writeError"] = write_error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_can_read(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_read = _parse_can_read(d.pop("canRead", UNSET))


        def _parse_can_write(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_write = _parse_can_write(d.pop("canWrite", UNSET))


        read_error = d.pop("readError", UNSET)

        write_error = d.pop("writeError", UNSET)

        master_key_settings_valid = cls(
            can_read=can_read,
            can_write=can_write,
            read_error=read_error,
            write_error=write_error,
        )


        master_key_settings_valid.additional_properties = d
        return master_key_settings_valid

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
