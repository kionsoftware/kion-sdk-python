from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OCIAccountCreate")



@_attrs_define
class OCIAccountCreate:
    """ OCIAccountCreate defines a the fields necessary to create an OCI account in the application

        Attributes:
            account_name (str): The name of the account as it will appear in the application. Example: My OCI account.
            payer_id (int | None): The ID of the payer to link the account to. Example: 1.
            project_id (int | None): The ID of the project to link the account to. Example: 1.
            start_datecode (str): The start date that the account's spend accrues against the linked project. Example:
                2019-01.
            tenancy_ocid (str): The tenancy OCID linked to the account. Example: ocid1.tenancy.oc1..aaaaaaaa.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_type_id (int | None | Unset): The type of the account being created.
                For OCI Commercial accounts (default), this value is 26.
                For OCI Government accounts, this value is 27.
                For OCI Federal accounts, this value is 28. Default: 26. Example: 26.
     """

    account_name: str
    payer_id: int | None
    project_id: int | None
    start_datecode: str
    tenancy_ocid: str
    account_alias: str | Unset = UNSET
    account_type_id: int | None | Unset = 26
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        payer_id: int | None
        payer_id = self.payer_id

        project_id: int | None
        project_id = self.project_id

        start_datecode = self.start_datecode

        tenancy_ocid = self.tenancy_ocid

        account_alias = self.account_alias

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_name": account_name,
            "payer_id": payer_id,
            "project_id": project_id,
            "start_datecode": start_datecode,
            "tenancy_ocid": tenancy_ocid,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("account_name")

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

        tenancy_ocid = d.pop("tenancy_ocid")

        account_alias = d.pop("account_alias", UNSET)

        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        oci_account_create = cls(
            account_name=account_name,
            payer_id=payer_id,
            project_id=project_id,
            start_datecode=start_datecode,
            tenancy_ocid=tenancy_ocid,
            account_alias=account_alias,
            account_type_id=account_type_id,
        )


        oci_account_create.additional_properties = d
        return oci_account_create

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
