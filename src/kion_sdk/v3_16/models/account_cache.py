from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountCache")



@_attrs_define
class AccountCache:
    """ AccountCache defines an account.

        Attributes:
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_email (str | Unset): Root email of the account if created inside the application, otherwise it will be
                an empty string. Example: jdoe@example.com.
            account_name (str | Unset): Name of the account in the application. Example: Tech Project 1.
            account_number (str | Unset): The cloud service provider account identifier.
                Either an AWS Account number, Azure Subscription ID or Google Cloud Project ID. Example: 121212121212.
            account_type_id (int | None | Unset): Will be: 1 for AWS Commercial, 2 for AWS GovCloud, 3 for Azure CSP
                Standard. Example: 1.
            car_external_id (str | Unset): The external ID used when assuming the cloud access role for this account.
                Example: CAR-9849055.
            created_at (str | Unset): Date when the account was added to the application. Example: 2019-02-12T22:57:10+0000.
            id (int | Unset): ID of the record in the application. Example: 1.
            include_linked_account_spend (bool | None | Unset): When true, the application will include linked account spend
                from linked govcloud or commercial accounts. Default is true.
            key_id (str | Unset): AWS Key ID of the access key. Example: ABCDEFGHIJKLMNOPQRSTUVWXYZ.
            key_secret (str | Unset): AWS Key Secret (will be redacted for security purposes).
            linked_account_number (str | Unset): Empty string for Commercial AWS accounts or Azure CSP Standard, but will
                have a value for GovCloud accounts. Example: OrganizationAccountAccessRole.
            linked_role (str | Unset): Name of the AWS Organizations service role. AWS recommends:
                OrganizationAccountAccessRole. Example: OrganizationAccountAccessRole.
            payer_id (int | None | Unset): ID of the payer where the application can find the billing data for the account.
                Example: 1.
            service_external_id (str | Unset): The external ID used for automated internal actions using the service role
                for this account. Example: Service-3764894.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
     """

    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    account_type_id: int | None | Unset = UNSET
    car_external_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    id: int | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    key_id: str | Unset = UNSET
    key_secret: str | Unset = UNSET
    linked_account_number: str | Unset = UNSET
    linked_role: str | Unset = UNSET
    payer_id: int | None | Unset = UNSET
    service_external_id: str | Unset = UNSET
    skip_access_checking: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_alias = self.account_alias

        account_email = self.account_email

        account_name = self.account_name

        account_number = self.account_number

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        car_external_id = self.car_external_id

        created_at = self.created_at

        id = self.id

        include_linked_account_spend: bool | None | Unset
        if isinstance(self.include_linked_account_spend, Unset):
            include_linked_account_spend = UNSET
        else:
            include_linked_account_spend = self.include_linked_account_spend

        key_id = self.key_id

        key_secret = self.key_secret

        linked_account_number = self.linked_account_number

        linked_role = self.linked_role

        payer_id: int | None | Unset
        if isinstance(self.payer_id, Unset):
            payer_id = UNSET
        else:
            payer_id = self.payer_id

        service_external_id = self.service_external_id

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
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if car_external_id is not UNSET:
            field_dict["car_external_id"] = car_external_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
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
        if payer_id is not UNSET:
            field_dict["payer_id"] = payer_id
        if service_external_id is not UNSET:
            field_dict["service_external_id"] = service_external_id
        if skip_access_checking is not UNSET:
            field_dict["skip_access_checking"] = skip_access_checking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_alias = d.pop("account_alias", UNSET)

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


        car_external_id = d.pop("car_external_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

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

        def _parse_payer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payer_id = _parse_payer_id(d.pop("payer_id", UNSET))


        service_external_id = d.pop("service_external_id", UNSET)

        def _parse_skip_access_checking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_access_checking = _parse_skip_access_checking(d.pop("skip_access_checking", UNSET))


        account_cache = cls(
            account_alias=account_alias,
            account_email=account_email,
            account_name=account_name,
            account_number=account_number,
            account_type_id=account_type_id,
            car_external_id=car_external_id,
            created_at=created_at,
            id=id,
            include_linked_account_spend=include_linked_account_spend,
            key_id=key_id,
            key_secret=key_secret,
            linked_account_number=linked_account_number,
            linked_role=linked_role,
            payer_id=payer_id,
            service_external_id=service_external_id,
            skip_access_checking=skip_access_checking,
        )


        account_cache.additional_properties = d
        return account_cache

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
