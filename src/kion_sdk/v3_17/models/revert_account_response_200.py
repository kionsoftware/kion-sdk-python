from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RevertAccountResponse200")



@_attrs_define
class RevertAccountResponse200:
    """ 
        Attributes:
            message (str | Unset): User-friendly message. Example: Resource updated successfully..
            record_id (int | Unset): ID of the cached account. Example: 100.
            status (int | Unset): HTTP status code. Example: 200.
     """

    message: str | Unset = UNSET
    record_id: int | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        record_id = self.record_id

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if record_id is not UNSET:
            field_dict["record_id"] = record_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        record_id = d.pop("record_id", UNSET)

        status = d.pop("status", UNSET)

        revert_account_response_200 = cls(
            message=message,
            record_id=record_id,
            status=status,
        )


        revert_account_response_200.additional_properties = d
        return revert_account_response_200

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
