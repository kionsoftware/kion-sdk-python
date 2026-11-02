from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OUEnforcementUpdate")



@_attrs_define
class OUEnforcementUpdate:
    """ OUEnforcementUpdate is the model for updating an existing OU enforcement.

        Attributes:
            cloud_rule_id (int | None | Unset): ID of cloud rule that is attached to the enforcement.
                Use endpoint /v3/cloud-rule to get a list of valid cloud rules and IDs.
                To clear the cloud rule, use the value 0. Example: 1.
            description (str | Unset): Optional, user-provided description of the enforcement. Example: This enforcement
                disables new service creation after monthly spend reaches $10,000.
            enabled (bool | None | Unset): Flag that specifies if the enforcement is enabled or disabled. Example: True.
            overburn (bool | None | Unset): Flag that specifies if enforcement will place project in a overburn state when
                triggered. Options are: true, false.
            service_id (int | None | Unset): ID of service to enforce against.
                Use endpoint /v3/cloud-provider/service to get a list of valid services and IDs.
                To clear the service, use the value 0. Example: 1.
            threshold (int | Unset): Threshold value. Either a dollar amount or percent based on threshold type. Example:
                100.
            threshold_type (str | Unset): Type of the threshold value.
                Valid values are "dollar", "percent". Example: dollar.
            timeframe (str | Unset): Timeframe of the enforcement.
                Valid values are "lifetime", "month", "year". Example: lifetime.
            trigger_planned_amount_type (str | Unset): For OU percent enforcements, controls whether percentage is
                calculated against an aggregate budget or active threshold when applicable.
            ugroup_ids (list[int] | None | Unset): The set of user groups that should be notified when the enforcement is
                triggered. Example: [1].
            user_ids (list[int] | None | Unset): The set of user IDs that should be notified when the enforcement is
                triggered. Example: [1].
     """

    cloud_rule_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    overburn: bool | None | Unset = UNSET
    service_id: int | None | Unset = UNSET
    threshold: int | Unset = UNSET
    threshold_type: str | Unset = UNSET
    timeframe: str | Unset = UNSET
    trigger_planned_amount_type: str | Unset = UNSET
    ugroup_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
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

        service_id: int | None | Unset
        if isinstance(self.service_id, Unset):
            service_id = UNSET
        else:
            service_id = self.service_id

        threshold = self.threshold

        threshold_type = self.threshold_type

        timeframe = self.timeframe

        trigger_planned_amount_type = self.trigger_planned_amount_type

        ugroup_ids: list[int] | None | Unset
        if isinstance(self.ugroup_ids, Unset):
            ugroup_ids = UNSET
        elif isinstance(self.ugroup_ids, list):
            ugroup_ids = self.ugroup_ids


        else:
            ugroup_ids = self.ugroup_ids

        user_ids: list[int] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids


        else:
            user_ids = self.user_ids


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
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe
        if trigger_planned_amount_type is not UNSET:
            field_dict["trigger_planned_amount_type"] = trigger_planned_amount_type
        if ugroup_ids is not UNSET:
            field_dict["ugroup_ids"] = ugroup_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

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


        def _parse_service_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        service_id = _parse_service_id(d.pop("service_id", UNSET))


        threshold = d.pop("threshold", UNSET)

        threshold_type = d.pop("threshold_type", UNSET)

        timeframe = d.pop("timeframe", UNSET)

        trigger_planned_amount_type = d.pop("trigger_planned_amount_type", UNSET)

        def _parse_ugroup_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ugroup_ids_type_0 = cast(list[int], data)

                return ugroup_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        ugroup_ids = _parse_ugroup_ids(d.pop("ugroup_ids", UNSET))


        def _parse_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[int], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))


        ou_enforcement_update = cls(
            cloud_rule_id=cloud_rule_id,
            description=description,
            enabled=enabled,
            overburn=overburn,
            service_id=service_id,
            threshold=threshold,
            threshold_type=threshold_type,
            timeframe=timeframe,
            trigger_planned_amount_type=trigger_planned_amount_type,
            ugroup_ids=ugroup_ids,
            user_ids=user_ids,
        )


        ou_enforcement_update.additional_properties = d
        return ou_enforcement_update

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
