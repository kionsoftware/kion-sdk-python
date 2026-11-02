from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloudtamer_partner_consent_link import CloudtamerPartnerConsentLink





T = TypeVar("T", bound="GetConsentLinkResponse201")



@_attrs_define
class GetConsentLinkResponse201:
    """ 
        Attributes:
            data (CloudtamerPartnerConsentLink | Unset): CloudtamerPartnerConsentLink contains a URL that can be visited on
                the frontend to provide access to a CSP's billing data
            status (int | Unset): HTTP status code of the response Example: 200.
     """

    data: CloudtamerPartnerConsentLink | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloudtamer_partner_consent_link import CloudtamerPartnerConsentLink
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloudtamer_partner_consent_link import CloudtamerPartnerConsentLink
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: CloudtamerPartnerConsentLink | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = CloudtamerPartnerConsentLink.from_dict(_data)




        status = d.pop("status", UNSET)

        get_consent_link_response_201 = cls(
            data=data,
            status=status,
        )


        get_consent_link_response_201.additional_properties = d
        return get_consent_link_response_201

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
