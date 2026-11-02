from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CloudRuleExemptionRequestUpdate")



@_attrs_define
class CloudRuleExemptionRequestUpdate:
    """ CloudRuleExemptionRequestUpdate defines the structure used for updating exemption requests.

        Attributes:
            comments (str | Unset): Optional comments for the approval or denial. Example: Sample comment.
     """

    comments: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        comments = self.comments


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments", UNSET)

        cloud_rule_exemption_request_update = cls(
            comments=comments,
        )


        cloud_rule_exemption_request_update.additional_properties = d
        return cloud_rule_exemption_request_update

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
