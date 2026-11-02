from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FundingSourceEnforcementUpdate")



@_attrs_define
class FundingSourceEnforcementUpdate:
    """ FundingSourceEnforcementUpdate .

        Attributes:
            cloud_rule_id (int | None | Unset): ID of cloud rule that is attached to the enforcement.
                Use endpoint /v3/cloud-rule to get a list of valid cloud rules and IDs.
                To clear the cloud rule, use the value 0. Example: 1.
            description (str | Unset): Optional, user-provided description of the enforcement. Example: This enforcement
                disables new service creation after monthly spend reaches $10,000.
            enabled (bool | None | Unset): Flag that specifies if the enforcement is enabled or disabled. Example: True.
            overburn (bool | None | Unset): Flag that specifies if enforcement will place project in a overburn state when
                triggered. Options are: true, false.
            spend_option (str | Unset): Type of spend option.
                Valid values are "spend", "remaining". Example: spend.
            threshold (int | Unset): Threshold value in dollars. Example: 100.
            timeframe (str | Unset): Timeframe of the enforcement.
                Valid values are "lifetime", "month", "year". Example: lifetime.
     """

    cloud_rule_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    overburn: bool | None | Unset = UNSET
    spend_option: str | Unset = UNSET
    threshold: int | Unset = UNSET
    timeframe: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cloud_rule_id: int | None | Unset
        if isinstance(self.cloud_rule_id, Unset):
            cloud_rule_id = UNSET
        else:
            cloud_rule_id = self.cloud_rule_id

        description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        overburn: bool | None | Unset
        if isinstance(self.overburn, Unset):
            overburn = UNSET
        else:
            overburn = self.overburn

        spend_option = self.spend_option

        threshold = self.threshold

        timeframe = self.timeframe


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cloud_rule_id is not UNSET:
            field_dict["cloud_rule_id"] = cloud_rule_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if overburn is not UNSET:
            field_dict["overburn"] = overburn
        if spend_option is not UNSET:
            field_dict["spend_option"] = spend_option
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cloud_rule_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_rule_id = _parse_cloud_rule_id(d.pop("cloud_rule_id", UNSET))


        description = d.pop("description", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        def _parse_overburn(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overburn = _parse_overburn(d.pop("overburn", UNSET))


        spend_option = d.pop("spend_option", UNSET)

        threshold = d.pop("threshold", UNSET)

        timeframe = d.pop("timeframe", UNSET)

        funding_source_enforcement_update = cls(
            cloud_rule_id=cloud_rule_id,
            description=description,
            enabled=enabled,
            overburn=overburn,
            spend_option=spend_option,
            threshold=threshold,
            timeframe=timeframe,
        )


        funding_source_enforcement_update.additional_properties = d
        return funding_source_enforcement_update

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
