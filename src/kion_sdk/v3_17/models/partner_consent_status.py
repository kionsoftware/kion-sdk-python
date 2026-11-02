from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PartnerConsentStatus")



@_attrs_define
class PartnerConsentStatus:
    """ PartnerConsentStatus contains a number and human-readable string stating the partner consent status of an Azure CSP.

        Attributes:
            consent_status (int | Unset): AzureCSPStatus represents the partner consent state of an Azure CSP
            human_readable_status (str | Unset):
     """

    consent_status: int | Unset = UNSET
    human_readable_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        consent_status = self.consent_status

        human_readable_status = self.human_readable_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if consent_status is not UNSET:
            field_dict["consent_status"] = consent_status
        if human_readable_status is not UNSET:
            field_dict["human_readable_status"] = human_readable_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consent_status = d.pop("consent_status", UNSET)

        human_readable_status = d.pop("human_readable_status", UNSET)

        partner_consent_status = cls(
            consent_status=consent_status,
            human_readable_status=human_readable_status,
        )


        partner_consent_status.additional_properties = d
        return partner_consent_status

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
