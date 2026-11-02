from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.adjustment_rule_definition_response import AdjustmentRuleDefinitionResponse
  from ..models.allocation_rule_definition_response import AllocationRuleDefinitionResponse
  from ..models.custom_line_item_rule_definition_response import CustomLineItemRuleDefinitionResponse





T = TypeVar("T", bound="BillingRuleSegmentResponse")



@_attrs_define
class BillingRuleSegmentResponse:
    """ BillingRuleSegmentResponse is one entry in the segments list returned to clients.

        Attributes:
            adjustment_rule (AdjustmentRuleDefinitionResponse | Unset): AdjustmentRuleDefinitionResponse is the public read
                shape of an adjustment-rule definition.
            allocation_rule (AllocationRuleDefinitionResponse | Unset): AllocationRuleDefinitionResponse is the public read
                shape of an allocation-rule definition.
            custom_line_item_rule (CustomLineItemRuleDefinitionResponse | Unset):
            end_month (int | Unset): End month of the segment in YYYYMM format (exclusive: the first month the segment no
                longer applies to). Null when the segment never ends.
            id (int | Unset): The segment's database ID (definition row ID, not the parent billing_rule ID).
            start_month (int | Unset): Start month of the segment, in YYYYMM format.
            version_id (int | None | Unset): Versioning counter for this segment relative to its parent rule.
     """

    adjustment_rule: AdjustmentRuleDefinitionResponse | Unset = UNSET
    allocation_rule: AllocationRuleDefinitionResponse | Unset = UNSET
    custom_line_item_rule: CustomLineItemRuleDefinitionResponse | Unset = UNSET
    end_month: int | Unset = UNSET
    id: int | Unset = UNSET
    start_month: int | Unset = UNSET
    version_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.adjustment_rule_definition_response import AdjustmentRuleDefinitionResponse
        from ..models.allocation_rule_definition_response import AllocationRuleDefinitionResponse
        from ..models.custom_line_item_rule_definition_response import CustomLineItemRuleDefinitionResponse
        adjustment_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.adjustment_rule, Unset):
            adjustment_rule = self.adjustment_rule.to_dict()

        allocation_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allocation_rule, Unset):
            allocation_rule = self.allocation_rule.to_dict()

        custom_line_item_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_line_item_rule, Unset):
            custom_line_item_rule = self.custom_line_item_rule.to_dict()

        end_month = self.end_month

        id = self.id

        start_month = self.start_month

        version_id: int | None | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
            version_id = self.version_id


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
        if end_month is not UNSET:
            field_dict["end_month"] = end_month
        if id is not UNSET:
            field_dict["id"] = id
        if start_month is not UNSET:
            field_dict["start_month"] = start_month
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adjustment_rule_definition_response import AdjustmentRuleDefinitionResponse
        from ..models.allocation_rule_definition_response import AllocationRuleDefinitionResponse
        from ..models.custom_line_item_rule_definition_response import CustomLineItemRuleDefinitionResponse
        d = dict(src_dict)
        _adjustment_rule = d.pop("adjustment_rule", UNSET)
        adjustment_rule: AdjustmentRuleDefinitionResponse | Unset
        if isinstance(_adjustment_rule,  Unset):
            adjustment_rule = UNSET
        else:
            adjustment_rule = AdjustmentRuleDefinitionResponse.from_dict(_adjustment_rule)




        _allocation_rule = d.pop("allocation_rule", UNSET)
        allocation_rule: AllocationRuleDefinitionResponse | Unset
        if isinstance(_allocation_rule,  Unset):
            allocation_rule = UNSET
        else:
            allocation_rule = AllocationRuleDefinitionResponse.from_dict(_allocation_rule)




        _custom_line_item_rule = d.pop("custom_line_item_rule", UNSET)
        custom_line_item_rule: CustomLineItemRuleDefinitionResponse | Unset
        if isinstance(_custom_line_item_rule,  Unset):
            custom_line_item_rule = UNSET
        else:
            custom_line_item_rule = CustomLineItemRuleDefinitionResponse.from_dict(_custom_line_item_rule)




        end_month = d.pop("end_month", UNSET)

        id = d.pop("id", UNSET)

        start_month = d.pop("start_month", UNSET)

        def _parse_version_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))


        billing_rule_segment_response = cls(
            adjustment_rule=adjustment_rule,
            allocation_rule=allocation_rule,
            custom_line_item_rule=custom_line_item_rule,
            end_month=end_month,
            id=id,
            start_month=start_month,
            version_id=version_id,
        )


        billing_rule_segment_response.additional_properties = d
        return billing_rule_segment_response

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
