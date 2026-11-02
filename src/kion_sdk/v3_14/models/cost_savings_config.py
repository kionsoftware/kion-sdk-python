from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CostSavingsConfig")



@_attrs_define
class CostSavingsConfig:
    """ CostSavingsConfig defines the Cost Savings Config

        Attributes:
            cost_savings_allow_terminate (bool | None | Unset): Indicates whether resource termination is allowed in-app.
            cost_savings_enabled (bool | None | Unset): Indicates whether Cost Savings is enabled or not. Example: True.
            cost_savings_post_token_life_hours (int | Unset): Post token life (hours) for Cloud Custodian webhook actions to
                execute. Example: 1.
     """

    cost_savings_allow_terminate: bool | None | Unset = UNSET
    cost_savings_enabled: bool | None | Unset = UNSET
    cost_savings_post_token_life_hours: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cost_savings_allow_terminate: bool | None | Unset
        if isinstance(self.cost_savings_allow_terminate, Unset):
            cost_savings_allow_terminate = UNSET
        else:
            cost_savings_allow_terminate = self.cost_savings_allow_terminate

        cost_savings_enabled: bool | None | Unset
        if isinstance(self.cost_savings_enabled, Unset):
            cost_savings_enabled = UNSET
        else:
            cost_savings_enabled = self.cost_savings_enabled

        cost_savings_post_token_life_hours = self.cost_savings_post_token_life_hours


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cost_savings_allow_terminate is not UNSET:
            field_dict["cost_savings_allow_terminate"] = cost_savings_allow_terminate
        if cost_savings_enabled is not UNSET:
            field_dict["cost_savings_enabled"] = cost_savings_enabled
        if cost_savings_post_token_life_hours is not UNSET:
            field_dict["cost_savings_post_token_life_hours"] = cost_savings_post_token_life_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cost_savings_allow_terminate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cost_savings_allow_terminate = _parse_cost_savings_allow_terminate(d.pop("cost_savings_allow_terminate", UNSET))


        def _parse_cost_savings_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cost_savings_enabled = _parse_cost_savings_enabled(d.pop("cost_savings_enabled", UNSET))


        cost_savings_post_token_life_hours = d.pop("cost_savings_post_token_life_hours", UNSET)

        cost_savings_config = cls(
            cost_savings_allow_terminate=cost_savings_allow_terminate,
            cost_savings_enabled=cost_savings_enabled,
            cost_savings_post_token_life_hours=cost_savings_post_token_life_hours,
        )


        cost_savings_config.additional_properties = d
        return cost_savings_config

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
