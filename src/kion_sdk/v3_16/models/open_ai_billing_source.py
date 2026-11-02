from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OpenAIBillingSource")



@_attrs_define
class OpenAIBillingSource:
    """ OpenAIBillingSource defines an OpenAI billing source.

        Attributes:
            admin_api_key (str | Unset):
            billing_start_date (str | Unset):
            id (int | Unset):
            name (str | Unset):
     """

    admin_api_key: str | Unset = UNSET
    billing_start_date: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        admin_api_key = self.admin_api_key

        billing_start_date = self.billing_start_date

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if admin_api_key is not UNSET:
            field_dict["admin_api_key"] = admin_api_key
        if billing_start_date is not UNSET:
            field_dict["billing_start_date"] = billing_start_date
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_api_key = d.pop("admin_api_key", UNSET)

        billing_start_date = d.pop("billing_start_date", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        open_ai_billing_source = cls(
            admin_api_key=admin_api_key,
            billing_start_date=billing_start_date,
            id=id,
            name=name,
        )


        open_ai_billing_source.additional_properties = d
        return open_ai_billing_source

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
