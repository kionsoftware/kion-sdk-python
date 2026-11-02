from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AWSAccountCacheCreate")



@_attrs_define
class AWSAccountCacheCreate:
    """ AWSAccountCacheCreate defines the object to create a cached account.

        Attributes:
            account_name (str): Name of the account in the AWS console. Example: Tech Project 1.
            account_number (str): AWS account number. Example: 121212121212.
            account_type_id (int | None): The Account Type ID is the corresponding account's type.
                1 - AWS Commercial
                2 - Govcloud
                4 - AWS C2S
                5 - AWS SC2S Example: 1.
            payer_id (int | None): ID of the payer where the application can find the billing data for the account. Example:
                1.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_email (str | Unset): Root email of the account if created inside the application, otherwise it will be
                an empty string. Example: jdoe@example.com.
            include_linked_account_spend (bool | None | Unset): When true, the application will include linked account spend
                from linked govcloud or commercial accounts. Default is true.
            key_id (str | Unset): AWS Key ID of the access key. Example: ABCDEFGHIJKLMNOPQRSTUVWXYZ.
            key_secret (str | Unset): AWS Key Secret (will be redacted for security purposes).
            linked_account_number (str | Unset): Empty string for Commercial AWS accounts or Azure CSP Standard, but will
                have a value for GovCloud accounts. Example: OrganizationAccountAccessRole.
            linked_role (str | Unset): Name of the AWS Organizations service role. Default as well as what AWS recommends
                is: OrganizationAccountAccessRole. Example: OrganizationAccountAccessRole.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
     """

    account_name: str
    account_number: str
    account_type_id: int | None
    payer_id: int | None
    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    key_id: str | Unset = UNSET
    key_secret: str | Unset = UNSET
    linked_account_number: str | Unset = UNSET
    linked_role: str | Unset = UNSET
    skip_access_checking: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        account_number = self.account_number

        account_type_id: int | None
        account_type_id = self.account_type_id

        payer_id: int | None
        payer_id = self.payer_id

        account_alias = self.account_alias

        account_email = self.account_email

        include_linked_account_spend: bool | None | Unset
        if isinstance(self.include_linked_account_spend, Unset):
            include_linked_account_spend = UNSET
        else:
            include_linked_account_spend = self.include_linked_account_spend

        key_id = self.key_id

        key_secret = self.key_secret

        linked_account_number = self.linked_account_number

        linked_role = self.linked_role

        skip_access_checking: bool | None | Unset
        if isinstance(self.skip_access_checking, Unset):
            skip_access_checking = UNSET
        else:
            skip_access_checking = self.skip_access_checking


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_name": account_name,
            "account_number": account_number,
            "account_type_id": account_type_id,
            "payer_id": payer_id,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if account_email is not UNSET:
            field_dict["account_email"] = account_email
        if include_linked_account_spend is not UNSET:
            field_dict["include_linked_account_spend"] = include_linked_account_spend
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if key_secret is not UNSET:
            field_dict["key_secret"] = key_secret
        if linked_account_number is not UNSET:
            field_dict["linked_account_number"] = linked_account_number
        if linked_role is not UNSET:
            field_dict["linked_role"] = linked_role
        if skip_access_checking is not UNSET:
            field_dict["skip_access_checking"] = skip_access_checking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("account_name")

        account_number = d.pop("account_number")

        def _parse_account_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id"))


        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        account_alias = d.pop("account_alias", UNSET)

        account_email = d.pop("account_email", UNSET)

        def _parse_include_linked_account_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_linked_account_spend = _parse_include_linked_account_spend(d.pop("include_linked_account_spend", UNSET))


        key_id = d.pop("key_id", UNSET)

        key_secret = d.pop("key_secret", UNSET)

        linked_account_number = d.pop("linked_account_number", UNSET)

        linked_role = d.pop("linked_role", UNSET)

        def _parse_skip_access_checking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_access_checking = _parse_skip_access_checking(d.pop("skip_access_checking", UNSET))


        aws_account_cache_create = cls(
            account_name=account_name,
            account_number=account_number,
            account_type_id=account_type_id,
            payer_id=payer_id,
            account_alias=account_alias,
            account_email=account_email,
            include_linked_account_spend=include_linked_account_spend,
            key_id=key_id,
            key_secret=key_secret,
            linked_account_number=linked_account_number,
            linked_role=linked_role,
            skip_access_checking=skip_access_checking,
        )


        aws_account_cache_create.additional_properties = d
        return aws_account_cache_create

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
