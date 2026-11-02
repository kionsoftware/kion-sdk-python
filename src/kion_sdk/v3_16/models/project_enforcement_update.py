from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectEnforcementUpdate")



@_attrs_define
class ProjectEnforcementUpdate:
    """ ProjectEnforcementUpdate .

        Attributes:
            amount_type (str | Unset): Type of the amount.
                Valid values are "custom", "last_month". Example: custom.
            cloud_rule_id (int | None | Unset): ID of cloud rule that is attached to the enforcement.
                Use endpoint /v3/cloud-rule to get a list of valid cloud rules and IDs.
                To clear the cloud rule, use the value 0. Example: 1.
            description (str | Unset): Optional, user-provided description of the enforcement. Example: This enforcement
                disables new service creation after monthly spend reaches $10,000.
            enabled (bool | None | Unset): Flag that specifies if the enforcement is enabled or disabled. Example: True.
            notification_emails (list[str] | None | Unset): List of external email addresses that will receive notifications
                from the enforcement. Example: ['user@example.com', 'admin@company.com'].
            notification_frequency (str | Unset): Frequency of notifications for this enforcement.
                Valid values are "daily". Example: daily.
            overburn (bool | None | Unset): Flag that specifies if enforcement will place project in a overburn state when
                triggered. Options are: true, false.
            service_id (int | None | Unset): ID of service to enforce against.
                Use endpoint /v3/cloud-provider/service to get a list of valid services and IDs.
                To clear the service, use the value 0. Example: 1.
            spend_option (str | Unset): Type of spend option.
                Valid values are "spend", "remaining", "spend_rate". Example: spend.
            threshold (int | Unset): Threshold value. Either a dollar amount or percent based on threshold type. Example:
                100.
            threshold_type (str | Unset): Type of the threshold value.
                Valid values are "dollar", "percent". Example: dollar.
            timeframe (str | Unset): Timeframe of the enforcement.
                Valid values are "day", "lifetime", "month", "year", "funding_source", "budget". Example: lifetime.
     """

    amount_type: str | Unset = UNSET
    cloud_rule_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    notification_emails: list[str] | None | Unset = UNSET
    notification_frequency: str | Unset = UNSET
    overburn: bool | None | Unset = UNSET
    service_id: int | None | Unset = UNSET
    spend_option: str | Unset = UNSET
    threshold: int | Unset = UNSET
    threshold_type: str | Unset = UNSET
    timeframe: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount_type = self.amount_type

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

        notification_emails: list[str] | None | Unset
        if isinstance(self.notification_emails, Unset):
            notification_emails = UNSET
        elif isinstance(self.notification_emails, list):
            notification_emails = self.notification_emails


        else:
            notification_emails = self.notification_emails

        notification_frequency = self.notification_frequency

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

        spend_option = self.spend_option

        threshold = self.threshold

        threshold_type = self.threshold_type

        timeframe = self.timeframe


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount_type is not UNSET:
            field_dict["amount_type"] = amount_type
        if cloud_rule_id is not UNSET:
            field_dict["cloud_rule_id"] = cloud_rule_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if notification_emails is not UNSET:
            field_dict["notification_emails"] = notification_emails
        if notification_frequency is not UNSET:
            field_dict["notification_frequency"] = notification_frequency
        if overburn is not UNSET:
            field_dict["overburn"] = overburn
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if spend_option is not UNSET:
            field_dict["spend_option"] = spend_option
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_type = d.pop("amount_type", UNSET)

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


        def _parse_notification_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_emails_type_0 = cast(list[str], data)

                return notification_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notification_emails = _parse_notification_emails(d.pop("notification_emails", UNSET))


        notification_frequency = d.pop("notification_frequency", UNSET)

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


        spend_option = d.pop("spend_option", UNSET)

        threshold = d.pop("threshold", UNSET)

        threshold_type = d.pop("threshold_type", UNSET)

        timeframe = d.pop("timeframe", UNSET)

        project_enforcement_update = cls(
            amount_type=amount_type,
            cloud_rule_id=cloud_rule_id,
            description=description,
            enabled=enabled,
            notification_emails=notification_emails,
            notification_frequency=notification_frequency,
            overburn=overburn,
            service_id=service_id,
            spend_option=spend_option,
            threshold=threshold,
            threshold_type=threshold_type,
            timeframe=timeframe,
        )


        project_enforcement_update.additional_properties = d
        return project_enforcement_update

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
