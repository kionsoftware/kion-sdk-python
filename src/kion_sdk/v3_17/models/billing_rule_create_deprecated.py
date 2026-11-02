from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BillingRuleCreateDeprecated")



@_attrs_define
class BillingRuleCreateDeprecated:
    """ 
        Attributes:
            billing_source_ids (list[int] | None): List of Billing Source IDs attached to the billing rule. Example: [1, 2].
            description (str): Description of the billing rule. The description can be up to 1024 characters long. Example:
                This is a test billing rule..
            name (str): Name of the billing rule. The name can be up to 255 characters long. Example: Test Billing Rule.
            rule_type (int): Type of the billing rule. The allowed values are:

                1 - Rate Conversion
                2 - Markup
                3 - Discount Example: 1.
            rule_value (float): The Value of the Billing Rule.

                This is handled differently based on the Type of Billing Rules. For instance:

                For a 5% markup, the value would be 5.0
                For a 10% discount, the value would be 10.0
                For a 1.214 currency conversion, the value would be 1.214 Example: 5.
            start_month (int): Start month of the billing rule. This must be in the format YYYYMM where 202501 represents
                January 2025. Example: 202501.
            end_month (int | Unset): End month of the billing rule. This must be in the format YYYYMM where 202501
                represents January 2025.
                The end month is exclusive, e.g. if you want the rule to end in January 2025, send a value of 202502.
                Omit if the end month should be "Never Ends". If included, the value must be after the start month. Example:
                202501.
     """

    billing_source_ids: list[int] | None
    description: str
    name: str
    rule_type: int
    rule_value: float
    start_month: int
    end_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        billing_source_ids: list[int] | None
        if isinstance(self.billing_source_ids, list):
            billing_source_ids = self.billing_source_ids


        else:
            billing_source_ids = self.billing_source_ids

        description = self.description

        name = self.name

        rule_type = self.rule_type

        rule_value = self.rule_value

        start_month = self.start_month

        end_month = self.end_month


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "billing_source_ids": billing_source_ids,
            "description": description,
            "name": name,
            "rule_type": rule_type,
            "rule_value": rule_value,
            "start_month": start_month,
        })
        if end_month is not UNSET:
            field_dict["end_month"] = end_month

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


        description = d.pop("description")

        name = d.pop("name")

        rule_type = d.pop("rule_type")

        rule_value = d.pop("rule_value")

        start_month = d.pop("start_month")

        end_month = d.pop("end_month", UNSET)

        billing_rule_create_deprecated = cls(
            billing_source_ids=billing_source_ids,
            description=description,
            name=name,
            rule_type=rule_type,
            rule_value=rule_value,
            start_month=start_month,
            end_month=end_month,
        )


        billing_rule_create_deprecated.additional_properties = d
        return billing_rule_create_deprecated

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
