from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceConfig")



@_attrs_define
class ComplianceConfig:
    """ ComplianceConfig represents the system settings for compliance token and custodian cache

        Attributes:
            custodian_cache_exclude_critical (bool | None | Unset): Exclude critical severity checks from the compliance
                resource cache Example: True.
            custodian_cache_interval_hours (int | Unset): The Cloud Custodian cache interval (in hours) Example: 2.
            post_token_life_hours (int | Unset): The amount of time allowed for Cloud Custodian webhook action to execute.
                Must be at least 1 hour Example: 1.
     """

    custodian_cache_exclude_critical: bool | None | Unset = UNSET
    custodian_cache_interval_hours: int | Unset = UNSET
    post_token_life_hours: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        custodian_cache_exclude_critical: bool | None | Unset
        if isinstance(self.custodian_cache_exclude_critical, Unset):
            custodian_cache_exclude_critical = UNSET
        else:
            custodian_cache_exclude_critical = self.custodian_cache_exclude_critical

        custodian_cache_interval_hours = self.custodian_cache_interval_hours

        post_token_life_hours = self.post_token_life_hours


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if custodian_cache_exclude_critical is not UNSET:
            field_dict["custodian_cache_exclude_critical"] = custodian_cache_exclude_critical
        if custodian_cache_interval_hours is not UNSET:
            field_dict["custodian_cache_interval_hours"] = custodian_cache_interval_hours
        if post_token_life_hours is not UNSET:
            field_dict["post_token_life_hours"] = post_token_life_hours

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_custodian_cache_exclude_critical(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        custodian_cache_exclude_critical = _parse_custodian_cache_exclude_critical(d.pop("custodian_cache_exclude_critical", UNSET))


        custodian_cache_interval_hours = d.pop("custodian_cache_interval_hours", UNSET)

        post_token_life_hours = d.pop("post_token_life_hours", UNSET)

        compliance_config = cls(
            custodian_cache_exclude_critical=custodian_cache_exclude_critical,
            custodian_cache_interval_hours=custodian_cache_interval_hours,
            post_token_life_hours=post_token_life_hours,
        )


        compliance_config.additional_properties = d
        return compliance_config

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
