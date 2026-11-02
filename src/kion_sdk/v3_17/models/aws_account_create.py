from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AWSAccountCreate")



@_attrs_define
class AWSAccountCreate:
    """ AWSAccountCreate defines an AWS account.

        Attributes:
            account_name (str): Name of the account in the application. Example: Tech Project 1.
            account_number (str): AWS account number. Example: 121212121212.
            payer_id (int | None): ID of the payer where the application can find the billing data for the account. Example:
                1.
            project_id (int | None): ID of the project where the account is attached. Example: 1.
            start_datecode (str): Date when the AWS account will start submitting payments against a funding source (YYYY-
                MM). Example: 2019-01.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_email (str | Unset): Root email of the account. Example: jdoe@example.com.
            account_type_id (int | None | Unset): The Account Type ID is the corresponding account's type.
                1 - AWS Commercial
                2 - Govcloud
                4 - AWS C2S
                5 - AWS SC2S
                Will default to 1 if not given. Example: 1.
            include_linked_account_spend (bool | None | Unset): When true, the application will keep will include spend from
                the linked govcloud account.
            linked_aws_account_number (str | Unset): Linked commercial AWS account number of this govcloud account. Example:
                123456789012.
            linked_role (str | Unset): Name of the AWS Organizations service role. Default as well as what AWS recommends
                is: OrganizationAccountAccessRole. Example: OrganizationAccountAccessRole.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
            use_org_account_info (bool | None | Unset): When true, the application will keep the account name and email
                address in cloudtamer in sync with the account name and email address as set in AWS Organization. Default is
                false.
     """

    account_name: str
    account_number: str
    payer_id: int | None
    project_id: int | None
    start_datecode: str
    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    account_type_id: int | None | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    linked_aws_account_number: str | Unset = UNSET
    linked_role: str | Unset = UNSET
    skip_access_checking: bool | None | Unset = UNSET
    use_org_account_info: bool | None | Unset = UNSET
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

        account_email = self.account_email

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        include_linked_account_spend: bool | None | Unset
        if isinstance(self.include_linked_account_spend, Unset):
            include_linked_account_spend = UNSET
        else:
            include_linked_account_spend = self.include_linked_account_spend

        linked_aws_account_number = self.linked_aws_account_number

        linked_role = self.linked_role

        skip_access_checking: bool | None | Unset
        if isinstance(self.skip_access_checking, Unset):
            skip_access_checking = UNSET
        else:
            skip_access_checking = self.skip_access_checking

        use_org_account_info: bool | None | Unset
        if isinstance(self.use_org_account_info, Unset):
            use_org_account_info = UNSET
        else:
            use_org_account_info = self.use_org_account_info


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
        if account_email is not UNSET:
            field_dict["account_email"] = account_email
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if include_linked_account_spend is not UNSET:
            field_dict["include_linked_account_spend"] = include_linked_account_spend
        if linked_aws_account_number is not UNSET:
            field_dict["linked_aws_account_number"] = linked_aws_account_number
        if linked_role is not UNSET:
            field_dict["linked_role"] = linked_role
        if skip_access_checking is not UNSET:
            field_dict["skip_access_checking"] = skip_access_checking
        if use_org_account_info is not UNSET:
            field_dict["use_org_account_info"] = use_org_account_info

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

        account_email = d.pop("account_email", UNSET)

        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        def _parse_include_linked_account_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_linked_account_spend = _parse_include_linked_account_spend(d.pop("include_linked_account_spend", UNSET))


        linked_aws_account_number = d.pop("linked_aws_account_number", UNSET)

        linked_role = d.pop("linked_role", UNSET)

        def _parse_skip_access_checking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_access_checking = _parse_skip_access_checking(d.pop("skip_access_checking", UNSET))


        def _parse_use_org_account_info(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_org_account_info = _parse_use_org_account_info(d.pop("use_org_account_info", UNSET))


        aws_account_create = cls(
            account_name=account_name,
            account_number=account_number,
            payer_id=payer_id,
            project_id=project_id,
            start_datecode=start_datecode,
            account_alias=account_alias,
            account_email=account_email,
            account_type_id=account_type_id,
            include_linked_account_spend=include_linked_account_spend,
            linked_aws_account_number=linked_aws_account_number,
            linked_role=linked_role,
            skip_access_checking=skip_access_checking,
            use_org_account_info=use_org_account_info,
        )


        aws_account_create.additional_properties = d
        return aws_account_create

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
