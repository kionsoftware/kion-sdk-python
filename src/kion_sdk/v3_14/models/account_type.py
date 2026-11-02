from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AccountType")



@_attrs_define
class AccountType:
    """ AccountType defines account type structure.

        Attributes:
            account_name (str | Unset): Name of the account type. Example: AWS Commercial.
            account_type_description (str | Unset): Name of the account type. Example: Standard AWS account.
            id (int | Unset): ID of the account type. Example: 1.
     """

    account_name: str | Unset = UNSET
    account_type_description: str | Unset = UNSET
    id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        account_type_description = self.account_type_description

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_type_description is not UNSET:
            field_dict["account_type_description"] = account_type_description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("account_name", UNSET)

        account_type_description = d.pop("account_type_description", UNSET)

        id = d.pop("id", UNSET)

        account_type = cls(
            account_name=account_name,
            account_type_description=account_type_description,
            id=id,
        )


        account_type.additional_properties = d
        return account_type

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
