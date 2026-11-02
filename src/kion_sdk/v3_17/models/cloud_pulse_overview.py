from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloud_pulse_resource_status import CloudPulseResourceStatus





T = TypeVar("T", bound="CloudPulseOverview")



@_attrs_define
class CloudPulseOverview:
    """ CloudPulseOverview represents a summary of cloud pulse overview data across accounts/cloud rules

        Attributes:
            account_status (CloudPulseResourceStatus | Unset): CloudPulseResourceStatus represents aggregate status counts
                for resources
            cloud_rule_status (CloudPulseResourceStatus | Unset): CloudPulseResourceStatus represents aggregate status
                counts for resources
            cloudformation_policy_id (int | None | Unset): The ID of the CloudFormation policy Example: 1.
            cloudformation_policy_name (str | Unset): The name of the CloudFormation policy Example: Example CloudFormation
                Policy.
     """

    account_status: CloudPulseResourceStatus | Unset = UNSET
    cloud_rule_status: CloudPulseResourceStatus | Unset = UNSET
    cloudformation_policy_id: int | None | Unset = UNSET
    cloudformation_policy_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_pulse_resource_status import CloudPulseResourceStatus
        account_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_status, Unset):
            account_status = self.account_status.to_dict()

        cloud_rule_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule_status, Unset):
            cloud_rule_status = self.cloud_rule_status.to_dict()

        cloudformation_policy_id: int | None | Unset
        if isinstance(self.cloudformation_policy_id, Unset):
            cloudformation_policy_id = UNSET
        else:
            cloudformation_policy_id = self.cloudformation_policy_id

        cloudformation_policy_name = self.cloudformation_policy_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_status is not UNSET:
            field_dict["account_status"] = account_status
        if cloud_rule_status is not UNSET:
            field_dict["cloud_rule_status"] = cloud_rule_status
        if cloudformation_policy_id is not UNSET:
            field_dict["cloudformation_policy_id"] = cloudformation_policy_id
        if cloudformation_policy_name is not UNSET:
            field_dict["cloudformation_policy_name"] = cloudformation_policy_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_pulse_resource_status import CloudPulseResourceStatus
        d = dict(src_dict)
        _account_status = d.pop("account_status", UNSET)
        account_status: CloudPulseResourceStatus | Unset
        if isinstance(_account_status,  Unset):
            account_status = UNSET
        else:
            account_status = CloudPulseResourceStatus.from_dict(_account_status)




        _cloud_rule_status = d.pop("cloud_rule_status", UNSET)
        cloud_rule_status: CloudPulseResourceStatus | Unset
        if isinstance(_cloud_rule_status,  Unset):
            cloud_rule_status = UNSET
        else:
            cloud_rule_status = CloudPulseResourceStatus.from_dict(_cloud_rule_status)




        def _parse_cloudformation_policy_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloudformation_policy_id = _parse_cloudformation_policy_id(d.pop("cloudformation_policy_id", UNSET))


        cloudformation_policy_name = d.pop("cloudformation_policy_name", UNSET)

        cloud_pulse_overview = cls(
            account_status=account_status,
            cloud_rule_status=cloud_rule_status,
            cloudformation_policy_id=cloudformation_policy_id,
            cloudformation_policy_name=cloudformation_policy_name,
        )


        cloud_pulse_overview.additional_properties = d
        return cloud_pulse_overview

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
