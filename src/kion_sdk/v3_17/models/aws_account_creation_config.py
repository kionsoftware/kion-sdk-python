from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AWSAccountCreationConfig")



@_attrs_define
class AWSAccountCreationConfig:
    """ AWSAccountCreationConfig represents the system settings for creating AWS accounts

        Attributes:
            account_placeholder_email (str | Unset): The placeholder email for AWS accounts Example: test@test.com.
            include_linked_account_spend (bool | None | Unset): Indicates whether linked account spend should be enabled or
                not
     """

    account_placeholder_email: str | Unset = UNSET
    include_linked_account_spend: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_placeholder_email = self.account_placeholder_email

        include_linked_account_spend: bool | None | Unset
        if isinstance(self.include_linked_account_spend, Unset):
            include_linked_account_spend = UNSET
        else:
            include_linked_account_spend = self.include_linked_account_spend


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_placeholder_email is not UNSET:
            field_dict["account_placeholder_email"] = account_placeholder_email
        if include_linked_account_spend is not UNSET:
            field_dict["include_linked_account_spend"] = include_linked_account_spend

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_placeholder_email = d.pop("account_placeholder_email", UNSET)

        def _parse_include_linked_account_spend(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_linked_account_spend = _parse_include_linked_account_spend(d.pop("include_linked_account_spend", UNSET))


        aws_account_creation_config = cls(
            account_placeholder_email=account_placeholder_email,
            include_linked_account_spend=include_linked_account_spend,
        )


        aws_account_creation_config.additional_properties = d
        return aws_account_creation_config

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
