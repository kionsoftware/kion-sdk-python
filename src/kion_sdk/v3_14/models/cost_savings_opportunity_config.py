from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CostSavingsOpportunityConfig")



@_attrs_define
class CostSavingsOpportunityConfig:
    """ CostSavingsOpportunityConfig represents the system settings for cost savings opportunities

        Attributes:
            cost_savings_opportunity_stale_threshold_hours (int | Unset): The amount of time in hours before a cost savings
                opportunity is considered stale Example: 24.
     """

    cost_savings_opportunity_stale_threshold_hours: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cost_savings_opportunity_stale_threshold_hours = self.cost_savings_opportunity_stale_threshold_hours


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cost_savings_opportunity_stale_threshold_hours is not UNSET:
            field_dict["cost_savings_opportunity_stale_threshold_hours"] = cost_savings_opportunity_stale_threshold_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cost_savings_opportunity_stale_threshold_hours = d.pop("cost_savings_opportunity_stale_threshold_hours", UNSET)

        cost_savings_opportunity_config = cls(
            cost_savings_opportunity_stale_threshold_hours=cost_savings_opportunity_stale_threshold_hours,
        )


        cost_savings_opportunity_config.additional_properties = d
        return cost_savings_opportunity_config

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
