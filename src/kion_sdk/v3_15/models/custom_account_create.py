from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CustomAccountCreate")



@_attrs_define
class CustomAccountCreate:
    """ 
        Attributes:
            account_name (str): The name of the account as it will appear in the application. Example: My Custom account.
            account_number (str): The account number or identifier for the custom account. Example: 1234567890.
            payer_id (int | None): The ID of the payer to link the account to. Example: 1.
            project_id (int | None): The ID of the project to link the account to. Example: 1.
            start_datecode (str): The start date that the account's spend accrues against the linked project. Example:
                2019-01.
            account_alias (str | Unset): Alias of the account in the application. Example: CA1.
     """

    account_name: str
    account_number: str
    payer_id: int | None
    project_id: int | None
    start_datecode: str
    account_alias: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        account_number = self.account_number

        payer_id: int | None
        payer_id = self.payer_id

        project_id: int | None
        project_id = self.project_id

        start_datecode = self.start_datecode

        account_alias = self.account_alias


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_name": account_name,
            "account_number": account_number,
            "payer_id": payer_id,
            "project_id": project_id,
            "start_datecode": start_datecode,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("account_name")

        account_number = d.pop("account_number")

        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        def _parse_project_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        project_id = _parse_project_id(d.pop("project_id"))


        start_datecode = d.pop("start_datecode")

        account_alias = d.pop("account_alias", UNSET)

        custom_account_create = cls(
            account_name=account_name,
            account_number=account_number,
            payer_id=payer_id,
            project_id=project_id,
            start_datecode=start_datecode,
            account_alias=account_alias,
        )


        custom_account_create.additional_properties = d
        return custom_account_create

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
