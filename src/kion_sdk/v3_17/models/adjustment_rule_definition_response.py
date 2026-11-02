from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AdjustmentRuleDefinitionResponse")



@_attrs_define
class AdjustmentRuleDefinitionResponse:
    """ AdjustmentRuleDefinitionResponse is the public read shape of an adjustment-rule definition.

        Attributes:
            billing_rule_ids (list[int] | None | Unset):
            rule_value (float | Unset):
     """

    billing_rule_ids: list[int] | None | Unset = UNSET
    rule_value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        billing_rule_ids: list[int] | None | Unset
        if isinstance(self.billing_rule_ids, Unset):
            billing_rule_ids = UNSET
        elif isinstance(self.billing_rule_ids, list):
            billing_rule_ids = self.billing_rule_ids


        else:
            billing_rule_ids = self.billing_rule_ids

        rule_value = self.rule_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if billing_rule_ids is not UNSET:
            field_dict["billing_rule_ids"] = billing_rule_ids
        if rule_value is not UNSET:
            field_dict["rule_value"] = rule_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_billing_rule_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                billing_rule_ids_type_0 = cast(list[int], data)

                return billing_rule_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        billing_rule_ids = _parse_billing_rule_ids(d.pop("billing_rule_ids", UNSET))


        rule_value = d.pop("rule_value", UNSET)

        adjustment_rule_definition_response = cls(
            billing_rule_ids=billing_rule_ids,
            rule_value=rule_value,
        )


        adjustment_rule_definition_response.additional_properties = d
        return adjustment_rule_definition_response

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
