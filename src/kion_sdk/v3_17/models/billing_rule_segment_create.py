from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.billing_rule_segment_definition import BillingRuleSegmentDefinition





T = TypeVar("T", bound="BillingRuleSegmentCreate")



@_attrs_define
class BillingRuleSegmentCreate:
    """ Exactly one of AdjustmentRule / AllocationRule must be populated, matching the parent
    rule's type. The controller validates that match.

        Attributes:
            start_month (int): Start month of the segment, in YYYYMM format (e.g., 202501). Example: 202501.
            criteria (BillingRuleSegmentDefinition | Unset):
            end_month (int | Unset): End month of the segment, in YYYYMM format (exclusive: the first month the segment no
                longer applies to). Must be after start_month; a one-month segment starting 202501 ends
                202502. Omit for "Never Ends". Example: 202512.
     """

    start_month: int
    criteria: BillingRuleSegmentDefinition | Unset = UNSET
    end_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_rule_segment_definition import BillingRuleSegmentDefinition
        start_month = self.start_month

        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        end_month = self.end_month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "start_month": start_month,
        })
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if end_month is not UNSET:
            field_dict["end_month"] = end_month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_rule_segment_definition import BillingRuleSegmentDefinition
        d = dict(src_dict)
        start_month = d.pop("start_month")

        _criteria = d.pop("criteria", UNSET)
        criteria: BillingRuleSegmentDefinition | Unset
        if isinstance(_criteria,  Unset):
            criteria = UNSET
        else:
            criteria = BillingRuleSegmentDefinition.from_dict(_criteria)




        end_month = d.pop("end_month", UNSET)

        billing_rule_segment_create = cls(
            start_month=start_month,
            criteria=criteria,
            end_month=end_month,
        )


        billing_rule_segment_create.additional_properties = d
        return billing_rule_segment_create

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
