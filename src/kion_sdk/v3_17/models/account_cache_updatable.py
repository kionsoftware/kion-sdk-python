from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountCacheUpdatable")



@_attrs_define
class AccountCacheUpdatable:
    """ AccountCacheUpdatable defines a cached account update.

        Attributes:
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_email (str | Unset): Email of the account in the application. Example: jdoe@example.com.
            account_name (str | Unset): Name of the cached account in the application. Example: Tech Project 2.
            include_linked_account_spend (bool | None | Unset): When true, the application will include spend from the
                linked govcloud account.
            linked_role (str | Unset): Name of the AWS Organizations service role. AWS recommends:
                OrganizationAccountAccessRole. Example: OrganizationAccountAccessRole.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
     """

    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    account_name: str | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    linked_role: str | Unset = UNSET
    skip_access_checking: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_alias = self.account_alias

        account_email = self.account_email

        account_name = self.account_name

        include_linked_account_spend: bool | None | Unset
        if isinstance(self.include_linked_account_spend, Unset):
            include_linked_account_spend = UNSET
        else:
            include_linked_account_spend = self.include_linked_account_spend

        linked_role = self.linked_role

        skip_access_checking: bool | None | Unset
        if isinstance(self.skip_access_checking, Unset):
            skip_access_checking = UNSET
        else:
            skip_access_checking = self.skip_access_checking


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if account_email is not UNSET:
            field_dict["account_email"] = account_email
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if include_linked_account_spend is not UNSET:
            field_dict["include_linked_account_spend"] = include_linked_account_spend
        if linked_role is not UNSET:
            field_dict["linked_role"] = linked_role
        if skip_access_checking is not UNSET:
            field_dict["skip_access_checking"] = skip_access_checking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_alias = d.pop("account_alias", UNSET)

        account_email = d.pop("account_email", UNSET)

        account_name = d.pop("account_name", UNSET)

        def _parse_include_linked_account_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_linked_account_spend = _parse_include_linked_account_spend(d.pop("include_linked_account_spend", UNSET))


        linked_role = d.pop("linked_role", UNSET)

        def _parse_skip_access_checking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_access_checking = _parse_skip_access_checking(d.pop("skip_access_checking", UNSET))


        account_cache_updatable = cls(
            account_alias=account_alias,
            account_email=account_email,
            account_name=account_name,
            include_linked_account_spend=include_linked_account_spend,
            linked_role=linked_role,
            skip_access_checking=skip_access_checking,
        )


        account_cache_updatable.additional_properties = d
        return account_cache_updatable

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
