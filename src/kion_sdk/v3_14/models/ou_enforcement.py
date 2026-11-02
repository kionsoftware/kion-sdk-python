from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloud_rule import CloudRule
  from ..models.service import Service





T = TypeVar("T", bound="OUEnforcement")



@_attrs_define
class OUEnforcement:
    """ OUEnforcement is an enforcement at the OU level.

        Attributes:
            cloud_rule (CloudRule | Unset): CloudRule defines a Cloud Rule.
            description (str | Unset): Optional, user-provided description of the enforcement. Example: This enforcement
                disables new service creation after monthly spend reaches $10,000.
            enabled (bool | None | Unset): Flag that specifies if the enforcement is enabled. Example: True.
            id (int | Unset): ID of the record in the application. Example: 1.
            overburn (bool | None | Unset): Flag that specifies if enforcement will place project in a overburn state when
                triggered. Example: True.
            service (Service | Unset): Service .
            threshold (int | Unset): Threshold value. Either a dollar amount or percent based on threshold type. Example:
                100.
            threshold_type (str | Unset): The type of the threshold value.
                Valid values are "dollar", "percent". Example: dollar.
            timeframe (str | Unset): Timeframe of the enforcement.
                Valid values are "lifetime", "month", "year" Example: lifetime.
            trigger_planned_amount_type (str | Unset): For OU percent enforcements, controls whether percentage is
                calculated against an aggregate budget or active threshold when applicable. Example: aggregate_budget.
            triggered (bool | None | Unset): Flag that specifies if the enforcement is currently triggered. Example: True.
            ugroup_ids (list[int] | None | Unset): List of user group IDs that will receive notifications from the
                enforcement. Example: [1].
            user_ids (list[int] | None | Unset): List of user IDs that will receive notifications from the enforcement.
                Example: [1].
     """

    cloud_rule: CloudRule | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    overburn: bool | None | Unset = UNSET
    service: Service | Unset = UNSET
    threshold: int | Unset = UNSET
    threshold_type: str | Unset = UNSET
    timeframe: str | Unset = UNSET
    trigger_planned_amount_type: str | Unset = UNSET
    triggered: bool | None | Unset = UNSET
    ugroup_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_rule import CloudRule
        from ..models.service import Service
        cloud_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule, Unset):
            cloud_rule = self.cloud_rule.to_dict()

        description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        id = self.id

        overburn: bool | None | Unset
        if isinstance(self.overburn, Unset):
            overburn = UNSET
        else:
            overburn = self.overburn

        service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        threshold = self.threshold

        threshold_type = self.threshold_type

        timeframe = self.timeframe

        trigger_planned_amount_type = self.trigger_planned_amount_type

        triggered: bool | None | Unset
        if isinstance(self.triggered, Unset):
            triggered = UNSET
        else:
            triggered = self.triggered

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
        if cloud_rule is not UNSET:
            field_dict["cloud_rule"] = cloud_rule
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if overburn is not UNSET:
            field_dict["overburn"] = overburn
        if service is not UNSET:
            field_dict["service"] = service
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe
        if trigger_planned_amount_type is not UNSET:
            field_dict["trigger_planned_amount_type"] = trigger_planned_amount_type
        if triggered is not UNSET:
            field_dict["triggered"] = triggered
        if ugroup_ids is not UNSET:
            field_dict["ugroup_ids"] = ugroup_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_rule import CloudRule
        from ..models.service import Service
        d = dict(src_dict)
        _cloud_rule = d.pop("cloud_rule", UNSET)
        cloud_rule: CloudRule | Unset
        if isinstance(_cloud_rule,  Unset):
            cloud_rule = UNSET
        else:
            cloud_rule = CloudRule.from_dict(_cloud_rule)




        description = d.pop("description", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        id = d.pop("id", UNSET)

        def _parse_overburn(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overburn = _parse_overburn(d.pop("overburn", UNSET))


        _service = d.pop("service", UNSET)
        service: Service | Unset
        if isinstance(_service,  Unset):
            service = UNSET
        else:
            service = Service.from_dict(_service)




        threshold = d.pop("threshold", UNSET)

        threshold_type = d.pop("threshold_type", UNSET)

        timeframe = d.pop("timeframe", UNSET)

        trigger_planned_amount_type = d.pop("trigger_planned_amount_type", UNSET)

        def _parse_triggered(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        triggered = _parse_triggered(d.pop("triggered", UNSET))


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


        ou_enforcement = cls(
            cloud_rule=cloud_rule,
            description=description,
            enabled=enabled,
            id=id,
            overburn=overburn,
            service=service,
            threshold=threshold,
            threshold_type=threshold_type,
            timeframe=timeframe,
            trigger_planned_amount_type=trigger_planned_amount_type,
            triggered=triggered,
            ugroup_ids=ugroup_ids,
            user_ids=user_ids,
        )


        ou_enforcement.additional_properties = d
        return ou_enforcement

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
