from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CloudRuleExemptionRequestCreate")



@_attrs_define
class CloudRuleExemptionRequestCreate:
    """ CloudRuleExemptionRequestCreate defines the structue for creating cloud rule exemption request.

        Attributes:
            cloud_rule_id (int | None): ID of cloud rule. Example: 1.
            comments (str | Unset): Optional comments for the request. Example: For auditing.
            ou_id (int | None | Unset): ID of OU to exempt from. If not specified, a request is generated for all instances
                of the cloud rule. Example: 1.
     """

    cloud_rule_id: int | None
    comments: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cloud_rule_id: int | None
        cloud_rule_id = self.cloud_rule_id

        comments = self.comments

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cloud_rule_id": cloud_rule_id,
        })
        if comments is not UNSET:
            field_dict["comments"] = comments
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cloud_rule_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cloud_rule_id = _parse_cloud_rule_id(d.pop("cloud_rule_id"))


        comments = d.pop("comments", UNSET)

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


        cloud_rule_exemption_request_create = cls(
            cloud_rule_id=cloud_rule_id,
            comments=comments,
            ou_id=ou_id,
        )


        cloud_rule_exemption_request_create.additional_properties = d
        return cloud_rule_exemption_request_create

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
