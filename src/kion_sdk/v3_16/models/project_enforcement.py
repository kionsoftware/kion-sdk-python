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





T = TypeVar("T", bound="ProjectEnforcement")



@_attrs_define
class ProjectEnforcement:
    """ ProjectEnforcement defines a project enforcement.

        Attributes:
            amount_type (str | Unset): Type of the amount.
                Valid values are "custom", "last_month". Example: custom.
            cloud_rule_id (CloudRule | Unset): CloudRule defines a Cloud Rule.
            description (str | Unset): Optional, user-provided description of the enforcement. Example: This enforcement
                disables new service creation after monthly spend reaches $10,000.
            enabled (bool | None | Unset): Flag that specifies if the enforcement is enabled. Example: True.
            funding_source_id (int | None | Unset): If enforcemnt is from a funding source, this is the ID of the funding
                source. Example: 1.
            id (int | Unset): ID of the record in the application. Example: 1.
            notification_emails (list[str] | None | Unset): List of external email addresses that will receive notifications
                from the enforcement. Example: ['user@example.com', 'admin@company.com'].
            notification_frequency (str | Unset): Frequency of notifications for this enforcement.
                Valid values are "daily". This field is optional and defaults to "daily" if not provided. Example: daily.
            ou_id (int | None | Unset): If enforcemnt is from an OU, this is the ID of the OU. Example: 1.
            overburn (bool | None | Unset): Flag that specifies if enforcement will place project in a overburn state when
                triggered. Example: True.
            service (Service | Unset): Service .
            spend_option (str | Unset): Type of spend option.
                Valid values are "spend", "remaining", "spend_rate". Example: spend.
            threshold (int | Unset): Threshold value. Either a dollar amount or percent based on threshold type. Example:
                100.
            threshold_type (str | Unset): Type of the threshold value.
                Valid values are "dollar", "percent". Example: dollar.
            timeframe (str | Unset): Timeframe of the enforcement.
                Valid values are "day", "lifetime", "month", "year", "funding_source", "budget". Example: lifetime.
            triggered (bool | None | Unset): Flag that specifies if the enforcement is currently triggered. Example: True.
            user_group_ids (list[int] | None | Unset): List of user group IDs that will receive notifications from the
                enforcement. Example: [1].
            user_ids (list[int] | None | Unset): List of user IDs that will receive notifications from the enforcement.
                Example: [1].
     """

    amount_type: str | Unset = UNSET
    cloud_rule_id: CloudRule | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    funding_source_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    notification_emails: list[str] | None | Unset = UNSET
    notification_frequency: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    overburn: bool | None | Unset = UNSET
    service: Service | Unset = UNSET
    spend_option: str | Unset = UNSET
    threshold: int | Unset = UNSET
    threshold_type: str | Unset = UNSET
    timeframe: str | Unset = UNSET
    triggered: bool | None | Unset = UNSET
    user_group_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_rule import CloudRule
        from ..models.service import Service
        amount_type = self.amount_type

        cloud_rule_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule_id, Unset):
            cloud_rule_id = self.cloud_rule_id.to_dict()

        description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        funding_source_id: int | None | Unset
        if isinstance(self.funding_source_id, Unset):
            funding_source_id = UNSET
        else:
            funding_source_id = self.funding_source_id

        id = self.id

        notification_emails: list[str] | None | Unset
        if isinstance(self.notification_emails, Unset):
            notification_emails = UNSET
        elif isinstance(self.notification_emails, list):
            notification_emails = self.notification_emails


        else:
            notification_emails = self.notification_emails

        notification_frequency = self.notification_frequency

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id

        overburn: bool | None | Unset
        if isinstance(self.overburn, Unset):
            overburn = UNSET
        else:
            overburn = self.overburn

        service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        spend_option = self.spend_option

        threshold = self.threshold

        threshold_type = self.threshold_type

        timeframe = self.timeframe

        triggered: bool | None | Unset
        if isinstance(self.triggered, Unset):
            triggered = UNSET
        else:
            triggered = self.triggered

        user_group_ids: list[int] | None | Unset
        if isinstance(self.user_group_ids, Unset):
            user_group_ids = UNSET
        elif isinstance(self.user_group_ids, list):
            user_group_ids = self.user_group_ids


        else:
            user_group_ids = self.user_group_ids

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
        if amount_type is not UNSET:
            field_dict["amount_type"] = amount_type
        if cloud_rule_id is not UNSET:
            field_dict["cloud_rule_id"] = cloud_rule_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if funding_source_id is not UNSET:
            field_dict["funding_source_id"] = funding_source_id
        if id is not UNSET:
            field_dict["id"] = id
        if notification_emails is not UNSET:
            field_dict["notification_emails"] = notification_emails
        if notification_frequency is not UNSET:
            field_dict["notification_frequency"] = notification_frequency
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if overburn is not UNSET:
            field_dict["overburn"] = overburn
        if service is not UNSET:
            field_dict["service"] = service
        if spend_option is not UNSET:
            field_dict["spend_option"] = spend_option
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe
        if triggered is not UNSET:
            field_dict["triggered"] = triggered
        if user_group_ids is not UNSET:
            field_dict["user_group_ids"] = user_group_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_rule import CloudRule
        from ..models.service import Service
        d = dict(src_dict)
        amount_type = d.pop("amount_type", UNSET)

        _cloud_rule_id = d.pop("cloud_rule_id", UNSET)
        cloud_rule_id: CloudRule | Unset
        if isinstance(_cloud_rule_id,  Unset):
            cloud_rule_id = UNSET
        else:
            cloud_rule_id = CloudRule.from_dict(_cloud_rule_id)




        description = d.pop("description", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        def _parse_funding_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id", UNSET))


        id = d.pop("id", UNSET)

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

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


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




        spend_option = d.pop("spend_option", UNSET)

        threshold = d.pop("threshold", UNSET)

        threshold_type = d.pop("threshold_type", UNSET)

        timeframe = d.pop("timeframe", UNSET)

        def _parse_triggered(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        triggered = _parse_triggered(d.pop("triggered", UNSET))


        def _parse_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_group_ids_type_0 = cast(list[int], data)

                return user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_group_ids = _parse_user_group_ids(d.pop("user_group_ids", UNSET))


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


        project_enforcement = cls(
            amount_type=amount_type,
            cloud_rule_id=cloud_rule_id,
            description=description,
            enabled=enabled,
            funding_source_id=funding_source_id,
            id=id,
            notification_emails=notification_emails,
            notification_frequency=notification_frequency,
            ou_id=ou_id,
            overburn=overburn,
            service=service,
            spend_option=spend_option,
            threshold=threshold,
            threshold_type=threshold_type,
            timeframe=timeframe,
            triggered=triggered,
            user_group_ids=user_group_ids,
            user_ids=user_ids,
        )


        project_enforcement.additional_properties = d
        return project_enforcement

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
