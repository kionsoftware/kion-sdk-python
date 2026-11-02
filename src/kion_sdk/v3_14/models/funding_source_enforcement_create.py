from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FundingSourceEnforcementCreate")



@_attrs_define
class FundingSourceEnforcementCreate:
    """ FundingSourceEnforcementCreate .

        Attributes:
            threshold (int): Threshold value in dollars. Example: 100.
            timeframe (str): Timeframe of the enforcement.
                Valid values are "lifetime", "month", "year" Example: lifetime.
            cloud_rule_id (int | None | Unset): Optional ID of cloud rule that is attached to the enforcement.
                Use endpoint /v3/cloud-rule to get a list of valid cloud rules and IDs. Example: 1.
            description (str | Unset): Optional, user-provided description of the enforcement. Example: This enforcement
                disables new service creation after monthly spend reaches $10,000.
            overburn (bool | None | Unset): Flag that specifies if enforcement will place project in a overburn state when
                triggered. Options are: true, false. Default: False.
            spend_option (str | Unset): Type of spend option.
                Valid values are "spend", "remaining". Default: 'spend'. Example: spend.
            ugroup_ids (list[int] | None | Unset): List of user group IDs that will receive notifications from the
                enforcement. Is required if no user IDs are listed. Example: [1, 2].
            user_ids (list[int] | None | Unset): List of user IDs that will receive notifications from the enforcement. Is
                required if no user group IDs are listed. Example: [1, 2].
     """

    threshold: int
    timeframe: str
    cloud_rule_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    overburn: bool | None | Unset = False
    spend_option: str | Unset = 'spend'
    ugroup_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        threshold = self.threshold

        timeframe = self.timeframe

        cloud_rule_id: int | None | Unset
        if isinstance(self.cloud_rule_id, Unset):
            cloud_rule_id = UNSET
        else:
            cloud_rule_id = self.cloud_rule_id

        description = self.description

        overburn: bool | None | Unset
        if isinstance(self.overburn, Unset):
            overburn = UNSET
        else:
            overburn = self.overburn

        spend_option = self.spend_option

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
            "threshold": threshold,
            "timeframe": timeframe,
        })
        if cloud_rule_id is not UNSET:
            field_dict["cloud_rule_id"] = cloud_rule_id
        if description is not UNSET:
            field_dict["description"] = description
        if overburn is not UNSET:
            field_dict["overburn"] = overburn
        if spend_option is not UNSET:
            field_dict["spend_option"] = spend_option
        if ugroup_ids is not UNSET:
            field_dict["ugroup_ids"] = ugroup_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threshold = d.pop("threshold")

        timeframe = d.pop("timeframe")

        def _parse_cloud_rule_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_rule_id = _parse_cloud_rule_id(d.pop("cloud_rule_id", UNSET))


        description = d.pop("description", UNSET)

        def _parse_overburn(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overburn = _parse_overburn(d.pop("overburn", UNSET))


        spend_option = d.pop("spend_option", UNSET)

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


        funding_source_enforcement_create = cls(
            threshold=threshold,
            timeframe=timeframe,
            cloud_rule_id=cloud_rule_id,
            description=description,
            overburn=overburn,
            spend_option=spend_option,
            ugroup_ids=ugroup_ids,
            user_ids=user_ids,
        )


        funding_source_enforcement_create.additional_properties = d
        return funding_source_enforcement_create

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
