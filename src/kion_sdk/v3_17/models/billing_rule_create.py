from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.billing_rule_segment_create import BillingRuleSegmentCreate





T = TypeVar("T", bound="BillingRuleCreate")



@_attrs_define
class BillingRuleCreate:
    """ 
        Attributes:
            description (str): Description of the billing rule. The description can be up to 1024 characters long. Example:
                This is a test billing rule..
            name (str): Name of the billing rule. The name can be up to 255 characters long. Example: Test Billing Rule.
            rule_type (int): Type of the billing rule. The allowed values are:

                1 - Rate Conversion
                2 - Markup
                3 - Discount
                4 - Allocate Spend
                5 - Custom Line Item Example: 1.
            start_month (int): Start month of the billing rule. This must be in the format YYYYMM where 202501 represents
                January 2025. Example: 202501.
            end_month (int | Unset): End month of the billing rule. This must be in the format YYYYMM where 202501
                represents January 2025.
                The end month is exclusive, e.g. if you want the rule to end in January 2025, send a value of 202502.
                Omit if the end month should be "Never Ends". If included, the value must be after the start month. Example:
                202501.
            segments (list[BillingRuleSegmentCreate] | None | Unset):
     """

    description: str
    name: str
    rule_type: int
    start_month: int
    end_month: int | Unset = UNSET
    segments: list[BillingRuleSegmentCreate] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_rule_segment_create import BillingRuleSegmentCreate
        description = self.description

        name = self.name

        rule_type = self.rule_type

        start_month = self.start_month

        end_month = self.end_month

        segments: list[dict[str, Any]] | None | Unset
        if isinstance(self.segments, Unset):
            segments = UNSET
        elif isinstance(self.segments, list):
            segments = []
            for segments_type_0_item_data in self.segments:
                segments_type_0_item = segments_type_0_item_data.to_dict()
                segments.append(segments_type_0_item)


        else:
            segments = self.segments


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "description": description,
            "name": name,
            "rule_type": rule_type,
            "start_month": start_month,
        })
        if end_month is not UNSET:
            field_dict["end_month"] = end_month
        if segments is not UNSET:
            field_dict["segments"] = segments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_rule_segment_create import BillingRuleSegmentCreate
        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        rule_type = d.pop("rule_type")

        start_month = d.pop("start_month")

        end_month = d.pop("end_month", UNSET)

        def _parse_segments(data: object) -> list[BillingRuleSegmentCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                segments_type_0 = []
                _segments_type_0 = data
                for segments_type_0_item_data in (_segments_type_0):
                    segments_type_0_item = BillingRuleSegmentCreate.from_dict(segments_type_0_item_data)



                    segments_type_0.append(segments_type_0_item)

                return segments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BillingRuleSegmentCreate] | None | Unset, data)

        segments = _parse_segments(d.pop("segments", UNSET))


        billing_rule_create = cls(
            description=description,
            name=name,
            rule_type=rule_type,
            start_month=start_month,
            end_month=end_month,
            segments=segments,
        )


        billing_rule_create.additional_properties = d
        return billing_rule_create

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
