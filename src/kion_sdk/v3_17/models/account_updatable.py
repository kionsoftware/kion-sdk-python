from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountUpdatable")



@_attrs_define
class AccountUpdatable:
    """ AccountUpdatable defines an account update.

        Attributes:
            account_alias (str | Unset): Alias of the account in the application. Example: TP2.
            account_email (str | Unset): Email of the account in the application. Example: jdoe@example.com.
            account_name (str | Unset): Name of the account in the application. Example: Tech Project 2.
            include_linked_account_spend (bool | None | Unset): When true, the application will include spend from the
                linked govcloud account.
            linked_role (str | Unset): Name of the AWS Organizations service role. AWS recommends:
                OrganizationAccountAccessRole. Example: OrganizationAccountAccessRole.
            reset_notification_time (bool | None | Unset): Flag to reset the scp notification time Example: True.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
            start_datecode (str | Unset): Date when the AWS account will start submitting payments against a funding source
                (YYYY-MM). Example: 2019-01.
            use_org_account_info (bool | None | Unset): When true, the application will keep the account name and email
                address in cloudtamer in sync with the account name and email address as set in AWS Organization. Default is
                false.
     """

    account_alias: str | Unset = UNSET
    account_email: str | Unset = UNSET
    account_name: str | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    linked_role: str | Unset = UNSET
    reset_notification_time: bool | None | Unset = UNSET
    skip_access_checking: bool | None | Unset = UNSET
    start_datecode: str | Unset = UNSET
    use_org_account_info: bool | None | Unset = UNSET
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

        reset_notification_time: bool | None | Unset
        if isinstance(self.reset_notification_time, Unset):
            reset_notification_time = UNSET
        else:
            reset_notification_time = self.reset_notification_time

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
        if include_linked_account_spend is not UNSET:
            field_dict["include_linked_account_spend"] = include_linked_account_spend
        if linked_role is not UNSET:
            field_dict["linked_role"] = linked_role
        if reset_notification_time is not UNSET:
            field_dict["reset_notification_time"] = reset_notification_time
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

        def _parse_include_linked_account_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_linked_account_spend = _parse_include_linked_account_spend(d.pop("include_linked_account_spend", UNSET))


        linked_role = d.pop("linked_role", UNSET)

        def _parse_reset_notification_time(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reset_notification_time = _parse_reset_notification_time(d.pop("reset_notification_time", UNSET))


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


        account_updatable = cls(
            account_alias=account_alias,
            account_email=account_email,
            account_name=account_name,
            include_linked_account_spend=include_linked_account_spend,
            linked_role=linked_role,
            reset_notification_time=reset_notification_time,
            skip_access_checking=skip_access_checking,
            start_datecode=start_datecode,
            use_org_account_info=use_org_account_info,
        )


        account_updatable.additional_properties = d
        return account_updatable

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
