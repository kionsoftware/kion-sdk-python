from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="LinkAccount")



@_attrs_define
class LinkAccount:
    """ LinkAccount is used to link an account to CT.

        Attributes:
            account_email (str | Unset): Email registered with AWS for the account. Example: test@example.com.
            account_name (str | Unset): Name of the account in the application. Example: Tech Project 1.
            account_number (str | Unset): AWS account number. Example: 121212121212.
            account_type_id (int | None | Unset): The AccountTypeID is the corresponding account's type. Example: 1.
            linked_account_number (str | Unset): Linked AWS account number. Example: 121212121212.
     """

    account_email: str | Unset = UNSET
    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    account_type_id: int | None | Unset = UNSET
    linked_account_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_email = self.account_email

        account_name = self.account_name

        account_number = self.account_number

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        linked_account_number = self.linked_account_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_email is not UNSET:
            field_dict["account_email"] = account_email
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if linked_account_number is not UNSET:
            field_dict["linked_account_number"] = linked_account_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_email = d.pop("account_email", UNSET)

        account_name = d.pop("account_name", UNSET)

        account_number = d.pop("account_number", UNSET)

        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        linked_account_number = d.pop("linked_account_number", UNSET)

        link_account = cls(
            account_email=account_email,
            account_name=account_name,
            account_number=account_number,
            account_type_id=account_type_id,
            linked_account_number=linked_account_number,
        )


        link_account.additional_properties = d
        return link_account

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
