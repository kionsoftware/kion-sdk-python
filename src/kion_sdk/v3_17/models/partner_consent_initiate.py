from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PartnerConsentInitiate")



@_attrs_define
class PartnerConsentInitiate:
    """ PartnerConsentInitiate contains data about the web app registration and azure AD domain that should be used to
    authenticate the CSP service user

        Attributes:
            app_id (str | Unset):
            client_secret (str | Unset):
            domain (str | Unset):
     """

    app_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        client_secret = self.client_secret

        domain = self.domain


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        domain = d.pop("domain", UNSET)

        partner_consent_initiate = cls(
            app_id=app_id,
            client_secret=client_secret,
            domain=domain,
        )


        partner_consent_initiate.additional_properties = d
        return partner_consent_initiate

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
