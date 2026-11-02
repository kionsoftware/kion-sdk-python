from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CloudPulseRegionCloudFormationStatus")



@_attrs_define
class CloudPulseRegionCloudFormationStatus:
    """ CloudPulseRegionCloudFormationStatus represents the CloudFormation status for a specific region

        Attributes:
            deployment_state (str | Unset): The deployment state of the CloudFormation stack Example: failed.
            last_status (str | Unset): The last status of the CloudFormation stack Example: CREATE_FAILED.
            region (str | Unset): The AWS region Example: us-east-1.
            root_cause (str | Unset): The root cause of any failures Example: Resource limit exceeded.
            stack_id (str | Unset): The CloudFormation stack ID Example: arn:aws:cloudformation:us-
                east-1:123456789012:stack/ExampleStack/00000000-0000-0000-0000-000000000000.
     """

    deployment_state: str | Unset = UNSET
    last_status: str | Unset = UNSET
    region: str | Unset = UNSET
    root_cause: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deployment_state = self.deployment_state

        last_status = self.last_status

        region = self.region

        root_cause = self.root_cause

        stack_id = self.stack_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if deployment_state is not UNSET:
            field_dict["deployment_state"] = deployment_state
        if last_status is not UNSET:
            field_dict["last_status"] = last_status
        if region is not UNSET:
            field_dict["region"] = region
        if root_cause is not UNSET:
            field_dict["root_cause"] = root_cause
        if stack_id is not UNSET:
            field_dict["stack_id"] = stack_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deployment_state = d.pop("deployment_state", UNSET)

        last_status = d.pop("last_status", UNSET)

        region = d.pop("region", UNSET)

        root_cause = d.pop("root_cause", UNSET)

        stack_id = d.pop("stack_id", UNSET)

        cloud_pulse_region_cloud_formation_status = cls(
            deployment_state=deployment_state,
            last_status=last_status,
            region=region,
            root_cause=root_cause,
            stack_id=stack_id,
        )


        cloud_pulse_region_cloud_formation_status.additional_properties = d
        return cloud_pulse_region_cloud_formation_status

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
