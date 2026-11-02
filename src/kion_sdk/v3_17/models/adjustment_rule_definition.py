from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AdjustmentRuleDefinition")



@_attrs_define
class AdjustmentRuleDefinition:
    """ 
        Attributes:
            billing_source_ids (list[int] | None): List of Billing Source IDs attached to the billing rule for adjustment-
                type rules (Rate Conversion, Markup, or Discount). Example: [1, 2].
            rule_value (float | Unset): The Value of the Billing Rule for adjustment-type rules (Rate Conversion, Markup, or
                Discount).

                This is handled differently based on the Type of Billing Rules. For instance:

                For a 5% markup, the value would be 5.0
                For a 10% discount, the value would be 10.0
                For a 1.214 currency conversion, the value would be 1.214 Example: 5.
     """

    billing_source_ids: list[int] | None
    rule_value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        billing_source_ids: list[int] | None
        if isinstance(self.billing_source_ids, list):
            billing_source_ids = self.billing_source_ids


        else:
            billing_source_ids = self.billing_source_ids

        rule_value = self.rule_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "billing_source_ids": billing_source_ids,
        })
        if rule_value is not UNSET:
            field_dict["rule_value"] = rule_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_billing_source_ids(data: object) -> list[int] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                billing_source_ids_type_0 = cast(list[int], data)

                return billing_source_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None, data)

        billing_source_ids = _parse_billing_source_ids(d.pop("billing_source_ids"))


        rule_value = d.pop("rule_value", UNSET)

        adjustment_rule_definition = cls(
            billing_source_ids=billing_source_ids,
            rule_value=rule_value,
        )


        adjustment_rule_definition.additional_properties = d
        return adjustment_rule_definition

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
