from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzureAccountCacheCreate")



@_attrs_define
class AzureAccountCacheCreate:
    """ AzureAccountCacheCreate defines the object to create an azure cached account.

        Attributes:
            account_name (str): Name of the subscription in the application. Example: My Azure Subscription.
            payer_id (int | None): ID of the payer (aka Azure Tenant) where this subscription can be found Example: 1.
            subscription_uuid (str): Azure Subscription UUID. Example: 00000000-1111-2222-3333-444444444444.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_email (str | Unset): Root email of the account if created inside the application, otherwise it will be
                an empty string. Example: jdoe@example.com.
            account_type_id (int | None | Unset): The Account Type ID is the corresponding account's type.
                3 - Azure CSP Standard
                6 - Azure EA
                7 - Azure EA Government
                8 - Azure CSP Standard Resource Group
                9 - Azure EA Resource Group
                10 - Azure EA Government Resource Group
                11 - Azure CSP Government
                12 - Azure CSP Government Resource Group
                Will default to 3 if not given. Example: 3.
            resource_group_name (str | Unset): Azure Resource Group Name. Example: My-Resource-group.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
     """

    account_name: str
    payer_id: int | None
    subscription_uuid: str
    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    account_type_id: int | None | Unset = UNSET
    resource_group_name: str | Unset = UNSET
    skip_access_checking: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        payer_id: int | None
        payer_id = self.payer_id

        subscription_uuid = self.subscription_uuid

        account_alias = self.account_alias

        account_email = self.account_email

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        resource_group_name = self.resource_group_name

        skip_access_checking: bool | None | Unset
        if isinstance(self.skip_access_checking, Unset):
            skip_access_checking = UNSET
        else:
            skip_access_checking = self.skip_access_checking


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_name": account_name,
            "payer_id": payer_id,
            "subscription_uuid": subscription_uuid,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if account_email is not UNSET:
            field_dict["account_email"] = account_email
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if resource_group_name is not UNSET:
            field_dict["resource_group_name"] = resource_group_name
        if skip_access_checking is not UNSET:
            field_dict["skip_access_checking"] = skip_access_checking

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


        subscription_uuid = d.pop("subscription_uuid")

        account_alias = d.pop("account_alias", UNSET)

        account_email = d.pop("account_email", UNSET)

        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        resource_group_name = d.pop("resource_group_name", UNSET)

        def _parse_skip_access_checking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_access_checking = _parse_skip_access_checking(d.pop("skip_access_checking", UNSET))


        azure_account_cache_create = cls(
            account_name=account_name,
            payer_id=payer_id,
            subscription_uuid=subscription_uuid,
            account_alias=account_alias,
            account_email=account_email,
            account_type_id=account_type_id,
            resource_group_name=resource_group_name,
            skip_access_checking=skip_access_checking,
        )


        azure_account_cache_create.additional_properties = d
        return azure_account_cache_create

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
