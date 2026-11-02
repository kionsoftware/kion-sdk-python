from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CFTWithStatus")



@_attrs_define
class CFTWithStatus:
    """ CFTWithStatus defines a CFT with status.

        Attributes:
            name (str | Unset): Fields of a CloudFormation template.
            reason (str | Unset): AWS reason for the status
            region (str | Unset): The region within the account for a cloudformation template.
            status (str | Unset): List of users that own the CloudFormation template.
     """

    name: str | Unset = UNSET
    reason: str | Unset = UNSET
    region: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        reason = self.reason

        region = self.region

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        reason = d.pop("reason", UNSET)

        region = d.pop("region", UNSET)

        status = d.pop("status", UNSET)

        cft_with_status = cls(
            name=name,
            reason=reason,
            region=region,
            status=status,
        )


        cft_with_status.additional_properties = d
        return cft_with_status

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
