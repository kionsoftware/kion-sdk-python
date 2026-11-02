from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloud_rule import CloudRule





T = TypeVar("T", bound="CloudRuleExemption")



@_attrs_define
class CloudRuleExemption:
    """ CloudRuleExemption defines an exemption on a cloud rule.

        Attributes:
            cloud_rule (CloudRule | Unset): CloudRule defines a Cloud Rule.
            exemption_id (int | None | Unset): ID of the exemption. Example: 1.
            source_ou_id (int | None | Unset): ID of OU the cloud rule is on Example: 1.
     """

    cloud_rule: CloudRule | Unset = UNSET
    exemption_id: int | None | Unset = UNSET
    source_ou_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_rule import CloudRule
        cloud_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule, Unset):
            cloud_rule = self.cloud_rule.to_dict()

        exemption_id: int | None | Unset
        if isinstance(self.exemption_id, Unset):
            exemption_id = UNSET
        else:
            exemption_id = self.exemption_id

        source_ou_id: int | None | Unset
        if isinstance(self.source_ou_id, Unset):
            source_ou_id = UNSET
        else:
            source_ou_id = self.source_ou_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cloud_rule is not UNSET:
            field_dict["cloud_rule"] = cloud_rule
        if exemption_id is not UNSET:
            field_dict["exemption_id"] = exemption_id
        if source_ou_id is not UNSET:
            field_dict["source_ou_id"] = source_ou_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_rule import CloudRule
        d = dict(src_dict)
        _cloud_rule = d.pop("cloud_rule", UNSET)
        cloud_rule: CloudRule | Unset
        if isinstance(_cloud_rule,  Unset):
            cloud_rule = UNSET
        else:
            cloud_rule = CloudRule.from_dict(_cloud_rule)




        def _parse_exemption_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exemption_id = _parse_exemption_id(d.pop("exemption_id", UNSET))


        def _parse_source_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_ou_id = _parse_source_ou_id(d.pop("source_ou_id", UNSET))


        cloud_rule_exemption = cls(
            cloud_rule=cloud_rule,
            exemption_id=exemption_id,
            source_ou_id=source_ou_id,
        )


        cloud_rule_exemption.additional_properties = d
        return cloud_rule_exemption

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
