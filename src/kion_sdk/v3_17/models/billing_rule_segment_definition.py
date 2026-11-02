from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.adjustment_rule_definition import AdjustmentRuleDefinition
  from ..models.allocation_rule_definition import AllocationRuleDefinition
  from ..models.custom_line_item_rule_definition import CustomLineItemRuleDefinition





T = TypeVar("T", bound="BillingRuleSegmentDefinition")



@_attrs_define
class BillingRuleSegmentDefinition:
    """ 
        Attributes:
            adjustment_rule (AdjustmentRuleDefinition | Unset):
            allocation_rule (AllocationRuleDefinition | Unset):
            custom_line_item_rule (CustomLineItemRuleDefinition | Unset):
     """

    adjustment_rule: AdjustmentRuleDefinition | Unset = UNSET
    allocation_rule: AllocationRuleDefinition | Unset = UNSET
    custom_line_item_rule: CustomLineItemRuleDefinition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.adjustment_rule_definition import AdjustmentRuleDefinition
        from ..models.allocation_rule_definition import AllocationRuleDefinition
        from ..models.custom_line_item_rule_definition import CustomLineItemRuleDefinition
        adjustment_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adjustment_rule, Unset):
            adjustment_rule = self.adjustment_rule.to_dict()

        allocation_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allocation_rule, Unset):
            allocation_rule = self.allocation_rule.to_dict()

        custom_line_item_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_line_item_rule, Unset):
            custom_line_item_rule = self.custom_line_item_rule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if adjustment_rule is not UNSET:
            field_dict["adjustment_rule"] = adjustment_rule
        if allocation_rule is not UNSET:
            field_dict["allocation_rule"] = allocation_rule
        if custom_line_item_rule is not UNSET:
            field_dict["custom_line_item_rule"] = custom_line_item_rule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adjustment_rule_definition import AdjustmentRuleDefinition
        from ..models.allocation_rule_definition import AllocationRuleDefinition
        from ..models.custom_line_item_rule_definition import CustomLineItemRuleDefinition
        d = dict(src_dict)
        _adjustment_rule = d.pop("adjustment_rule", UNSET)
        adjustment_rule: AdjustmentRuleDefinition | Unset
        if isinstance(_adjustment_rule,  Unset):
            adjustment_rule = UNSET
        else:
            adjustment_rule = AdjustmentRuleDefinition.from_dict(_adjustment_rule)




        _allocation_rule = d.pop("allocation_rule", UNSET)
        allocation_rule: AllocationRuleDefinition | Unset
        if isinstance(_allocation_rule,  Unset):
            allocation_rule = UNSET
        else:
            allocation_rule = AllocationRuleDefinition.from_dict(_allocation_rule)




        _custom_line_item_rule = d.pop("custom_line_item_rule", UNSET)
        custom_line_item_rule: CustomLineItemRuleDefinition | Unset
        if isinstance(_custom_line_item_rule,  Unset):
            custom_line_item_rule = UNSET
        else:
            custom_line_item_rule = CustomLineItemRuleDefinition.from_dict(_custom_line_item_rule)




        billing_rule_segment_definition = cls(
            adjustment_rule=adjustment_rule,
            allocation_rule=allocation_rule,
            custom_line_item_rule=custom_line_item_rule,
        )


        billing_rule_segment_definition.additional_properties = d
        return billing_rule_segment_definition

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
