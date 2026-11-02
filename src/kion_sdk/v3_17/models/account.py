from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Account")



@_attrs_define
class Account:
    """ Account defines an account.

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
            created_at (str | Unset): Date when the AWS account was added to the application. Example:
                2019-02-12T22:57:10+0000.
            deleted_at (None | str | Unset): Date when the record was deleted or will be an empty string. Example:
                2019-02-12T22:57:10+0000.
            id (int | Unset): ID of the record in the application. Example: 1.
            include_linked_account_spend (bool | None | Unset): When true, the application will keep will include spend from
                the linked govcloud account.
            linked_account_number (str | Unset): Empty string for Commercial AWS accounts or Azure CSP Standard, but will
                have a value for GovCloud accounts. Example: 121212121212.
            linked_role (str | Unset): Name of the AWS Organizations service role. AWS recommends:
                OrganizationAccountAccessRole. Example: OrganizationAccountAccessRole.
            payer_id (int | None | Unset): ID of the payer where the application can find the billing data for the account.
                Example: 1.
            project_id (int | None | Unset): ID of the project where the account is attached. Example: 1.
            service_external_id (str | Unset): The external ID used for automated internal actions using the service role
                for this account. Example: Service-3764894.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
            start_datecode (str | Unset): Date when the AWS account will starting submitting payments against a funding
                source (YYYY-MM). Example: 2019-02.
            use_org_account_info (bool | None | Unset): When true, the application will keep the account name and email
                address in cloudtamer in sync with the account name and email address as set in AWS Organization. Default is
                false.
     """

    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    account_type_id: int | None | Unset = UNSET
    car_external_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    id: int | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    linked_account_number: str | Unset = UNSET
    linked_role: str | Unset = UNSET
    payer_id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    service_external_id: str | Unset = UNSET
    skip_access_checking: bool | None | Unset = UNSET
    start_datecode: str | Unset = UNSET
    use_org_account_info: bool | None | Unset = UNSET
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

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        id = self.id

        include_linked_account_spend: bool | None | Unset
        if isinstance(self.include_linked_account_spend, Unset):
            include_linked_account_spend = UNSET
        else:
            include_linked_account_spend = self.include_linked_account_spend

        linked_account_number = self.linked_account_number

        linked_role = self.linked_role

        payer_id: int | None | Unset
        if isinstance(self.payer_id, Unset):
            payer_id = UNSET
        else:
            payer_id = self.payer_id

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        service_external_id = self.service_external_id

        skip_access_checking: bool | None | Unset
        if isinstance(self.skip_access_checking, Unset):
            skip_access_checking = UNSET
        else:
            skip_access_checking = self.skip_access_checking

        start_datecode = self.start_datecode

        use_org_account_info: bool | None | Unset
        if isinstance(self.use_org_account_info, Unset):
            use_org_account_info = UNSET
        else:
            use_org_account_info = self.use_org_account_info


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
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if id is not UNSET:
            field_dict["id"] = id
        if include_linked_account_spend is not UNSET:
            field_dict["include_linked_account_spend"] = include_linked_account_spend
        if linked_account_number is not UNSET:
            field_dict["linked_account_number"] = linked_account_number
        if linked_role is not UNSET:
            field_dict["linked_role"] = linked_role
        if payer_id is not UNSET:
            field_dict["payer_id"] = payer_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if service_external_id is not UNSET:
            field_dict["service_external_id"] = service_external_id
        if skip_access_checking is not UNSET:
            field_dict["skip_access_checking"] = skip_access_checking
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode
        if use_org_account_info is not UNSET:
            field_dict["use_org_account_info"] = use_org_account_info

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

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        id = d.pop("id", UNSET)

        def _parse_include_linked_account_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_linked_account_spend = _parse_include_linked_account_spend(d.pop("include_linked_account_spend", UNSET))


        linked_account_number = d.pop("linked_account_number", UNSET)

        linked_role = d.pop("linked_role", UNSET)

        def _parse_payer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payer_id = _parse_payer_id(d.pop("payer_id", UNSET))


        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        service_external_id = d.pop("service_external_id", UNSET)

        def _parse_skip_access_checking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_access_checking = _parse_skip_access_checking(d.pop("skip_access_checking", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        def _parse_use_org_account_info(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_org_account_info = _parse_use_org_account_info(d.pop("use_org_account_info", UNSET))


        account = cls(
            account_alias=account_alias,
            account_email=account_email,
            account_name=account_name,
            account_number=account_number,
            account_type_id=account_type_id,
            car_external_id=car_external_id,
            created_at=created_at,
            deleted_at=deleted_at,
            id=id,
            include_linked_account_spend=include_linked_account_spend,
            linked_account_number=linked_account_number,
            linked_role=linked_role,
            payer_id=payer_id,
            project_id=project_id,
            service_external_id=service_external_id,
            skip_access_checking=skip_access_checking,
            start_datecode=start_datecode,
            use_org_account_info=use_org_account_info,
        )


        account.additional_properties = d
        return account

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
