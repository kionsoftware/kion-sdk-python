from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gcp_billing_account_projects_data_body import GCPBillingAccountProjectsDataBody





T = TypeVar("T", bound="GCPBillingAccountProjectsData")



@_attrs_define
class GCPBillingAccountProjectsData:
    """ GCPBillingAccountProjectsResponse returns all the projects attached to the billing account

        Attributes:
            body (GCPBillingAccountProjectsDataBody | Unset): in:body
     """

    body: GCPBillingAccountProjectsDataBody | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_billing_account_projects_data_body import GCPBillingAccountProjectsDataBody
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if body is not UNSET:
            field_dict["Body"] = body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_billing_account_projects_data_body import GCPBillingAccountProjectsDataBody
        d = dict(src_dict)
        _body = d.pop("Body", UNSET)
        body: GCPBillingAccountProjectsDataBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = GCPBillingAccountProjectsDataBody.from_dict(_body)




        gcp_billing_account_projects_data = cls(
            body=body,
        )


        gcp_billing_account_projects_data.additional_properties = d
        return gcp_billing_account_projects_data

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
