from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CloudtamerPartnerConsentLink")



@_attrs_define
class CloudtamerPartnerConsentLink:
    """ CloudtamerPartnerConsentLink contains a URL that can be visited on the frontend to provide access to a CSP's billing
    data

        Attributes:
            partner_consent_url (str | Unset):
     """

    partner_consent_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        partner_consent_url = self.partner_consent_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if partner_consent_url is not UNSET:
            field_dict["partner_consent_url"] = partner_consent_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partner_consent_url = d.pop("partner_consent_url", UNSET)

        cloudtamer_partner_consent_link = cls(
            partner_consent_url=partner_consent_url,
        )


        cloudtamer_partner_consent_link.additional_properties = d
        return cloudtamer_partner_consent_link

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
