from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AccountCustomVariableCreateOrUpdate")



@_attrs_define
class AccountCustomVariableCreateOrUpdate:
    """ AccountCustomVariableCreateOrUpdate represents the fields necessary to create or update an account custom variable
    override.

        Attributes:
            value (Any | Unset): Value is the value of the account custom variable override. Example: Example Value.
     """

    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        account_custom_variable_create_or_update = cls(
            value=value,
        )


        account_custom_variable_create_or_update.additional_properties = d
        return account_custom_variable_create_or_update

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
