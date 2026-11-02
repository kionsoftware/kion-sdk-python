from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RoleInfo")



@_attrs_define
class RoleInfo:
    """ RoleInfo defines a IAM role name and and account number.

        Attributes:
            iam_role_name (str): IAM role name. Example: ct-admin.
            account_alias (str | Unset): Account alias.
                Either account_number or account_alias must be provided. Example: TP1.
            account_number (str | Unset): AWS account number.
                Either account_number or account_alias must be provided. Example: 121212121212.
     """

    iam_role_name: str
    account_alias: str | Unset = UNSET
    account_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        iam_role_name = self.iam_role_name

        account_alias = self.account_alias

        account_number = self.account_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "iam_role_name": iam_role_name,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if account_number is not UNSET:
            field_dict["account_number"] = account_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        iam_role_name = d.pop("iam_role_name")

        account_alias = d.pop("account_alias", UNSET)

        account_number = d.pop("account_number", UNSET)

        role_info = cls(
            iam_role_name=iam_role_name,
            account_alias=account_alias,
            account_number=account_number,
        )


        role_info.additional_properties = d
        return role_info

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
