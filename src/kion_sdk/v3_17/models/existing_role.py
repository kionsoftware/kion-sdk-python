from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ExistingRole")



@_attrs_define
class ExistingRole:
    """ ExistingRole maps a role that already exists in AWS to CT

        Attributes:
            account_ids (list[int] | None | Unset):
            role_arn (str | Unset):
            role_name (str | Unset):
     """

    account_ids: list[int] | None | Unset = UNSET
    role_arn: str | Unset = UNSET
    role_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_ids: list[int] | None | Unset
        if isinstance(self.account_ids, Unset):
            account_ids = UNSET
        elif isinstance(self.account_ids, list):
            account_ids = self.account_ids


        else:
            account_ids = self.account_ids

        role_arn = self.role_arn

        role_name = self.role_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_ids is not UNSET:
            field_dict["account_ids"] = account_ids
        if role_arn is not UNSET:
            field_dict["role_arn"] = role_arn
        if role_name is not UNSET:
            field_dict["role_name"] = role_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = cast(list[int], data)

                return account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        account_ids = _parse_account_ids(d.pop("account_ids", UNSET))


        role_arn = d.pop("role_arn", UNSET)

        role_name = d.pop("role_name", UNSET)

        existing_role = cls(
            account_ids=account_ids,
            role_arn=role_arn,
            role_name=role_name,
        )


        existing_role.additional_properties = d
        return existing_role

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
