from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.payer_organizational_unit import PayerOrganizationalUnit





T = TypeVar("T", bound="AWSAccountCacheNewAWSAccount")



@_attrs_define
class AWSAccountCacheNewAWSAccount:
    """ AWSAccountCacheNewAWSAccount defines a payload for creating a new AWS Account.

        Attributes:
            account_name (str): Name of the account in the application. Example: Tech Project 1.
            payer_id (int | None): ID of the payer where the application can find the billing data for the account. Example:
                1.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_email (str | Unset): Root email of the account if created inside the application, otherwise it will be
                an empty string. Note: If an account placeholder email (e.g. `jdoe+%s@example.com`) has been set, account_email
                MUST be empty. In this case, account_email will be set to the account placeholder email formatted with the
                account_name field (e.g. `jdoe+account_name@example.com`). Otherwise, account_email is required. Example:
                jdoe@example.com.
            account_type_id (int | None | Unset): AccountTypeID is used to specify the AWS Account Type being created. If
                not explicitly set, the partition that Kion is running in will be used.
                For AWS Commercial accounts, this value is 1.
                For AWS Government accounts, this value is 2.
                For AWS C2S accounts, this value is 4.
                For AWS SC2S accounts, this value is 5. Example: 1.
            commercial_account_name (str | Unset): Name of the Commercial Account in the application. If none is provided, a
                default value of
                "{Name} - Commercial" will be used instead. If include_linked_account_spend is set to true,
                this value will be ignored. Example: TechProject - Commercial.
            create_govcloud (bool | None | Unset): CreateGovcloud determines if this account should be created in govcloud.
                The default value is false.
            gov_account_name (str | Unset): Name of the GovCloud Account in the application.
                If no value is provided, "{Name} - GovCloud" will be used if create_govcloud is true Example: TechProject - GC.
            include_linked_account_spend (bool | None | Unset): When true, the application will include linked account spend
                from linked govcloud or commercial accounts. If a Govcloud account is created with include linked account spend
                set to false, cloudtamer.io will create both a commercial and govcloud account and add them both to the cache.
                Default is false.
            linked_role (str | Unset): Name of the AWS Organizations service role. Default as well as what AWS recommends
                is: OrganizationAccountAccessRole. Example: OrganizationAccountAccessRole.
            organizational_unit (PayerOrganizationalUnit | Unset): PayerOrganizationalUnit represents an organizational unit
                in an AWS payer's organization.
     """

    account_name: str
    payer_id: int | None
    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    account_type_id: int | None | Unset = UNSET
    commercial_account_name: str | Unset = UNSET
    create_govcloud: bool | None | Unset = UNSET
    gov_account_name: str | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    linked_role: str | Unset = UNSET
    organizational_unit: PayerOrganizationalUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.payer_organizational_unit import PayerOrganizationalUnit
        account_name = self.account_name

        payer_id: int | None
        payer_id = self.payer_id

        account_alias = self.account_alias

        account_email = self.account_email

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        commercial_account_name = self.commercial_account_name

        create_govcloud: bool | None | Unset
        if isinstance(self.create_govcloud, Unset):
            create_govcloud = UNSET
        else:
            create_govcloud = self.create_govcloud

        gov_account_name = self.gov_account_name

        include_linked_account_spend: bool | None | Unset
        if isinstance(self.include_linked_account_spend, Unset):
            include_linked_account_spend = UNSET
        else:
            include_linked_account_spend = self.include_linked_account_spend

        linked_role = self.linked_role

        organizational_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organizational_unit, Unset):
            organizational_unit = self.organizational_unit.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_name": account_name,
            "payer_id": payer_id,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if account_email is not UNSET:
            field_dict["account_email"] = account_email
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if commercial_account_name is not UNSET:
            field_dict["commercial_account_name"] = commercial_account_name
        if create_govcloud is not UNSET:
            field_dict["create_govcloud"] = create_govcloud
        if gov_account_name is not UNSET:
            field_dict["gov_account_name"] = gov_account_name
        if include_linked_account_spend is not UNSET:
            field_dict["include_linked_account_spend"] = include_linked_account_spend
        if linked_role is not UNSET:
            field_dict["linked_role"] = linked_role
        if organizational_unit is not UNSET:
            field_dict["organizational_unit"] = organizational_unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payer_organizational_unit import PayerOrganizationalUnit
        d = dict(src_dict)
        account_name = d.pop("account_name")

        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        account_alias = d.pop("account_alias", UNSET)

        account_email = d.pop("account_email", UNSET)

        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        commercial_account_name = d.pop("commercial_account_name", UNSET)

        def _parse_create_govcloud(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        create_govcloud = _parse_create_govcloud(d.pop("create_govcloud", UNSET))


        gov_account_name = d.pop("gov_account_name", UNSET)

        def _parse_include_linked_account_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_linked_account_spend = _parse_include_linked_account_spend(d.pop("include_linked_account_spend", UNSET))


        linked_role = d.pop("linked_role", UNSET)

        _organizational_unit = d.pop("organizational_unit", UNSET)
        organizational_unit: PayerOrganizationalUnit | Unset
        if isinstance(_organizational_unit,  Unset):
            organizational_unit = UNSET
        else:
            organizational_unit = PayerOrganizationalUnit.from_dict(_organizational_unit)




        aws_account_cache_new_aws_account = cls(
            account_name=account_name,
            payer_id=payer_id,
            account_alias=account_alias,
            account_email=account_email,
            account_type_id=account_type_id,
            commercial_account_name=commercial_account_name,
            create_govcloud=create_govcloud,
            gov_account_name=gov_account_name,
            include_linked_account_spend=include_linked_account_spend,
            linked_role=linked_role,
            organizational_unit=organizational_unit,
        )


        aws_account_cache_new_aws_account.additional_properties = d
        return aws_account_cache_new_aws_account

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
