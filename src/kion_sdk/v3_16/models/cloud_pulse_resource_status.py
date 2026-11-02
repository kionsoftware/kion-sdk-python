from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CloudPulseResourceStatus")



@_attrs_define
class CloudPulseResourceStatus:
    """ CloudPulseResourceStatus represents aggregate status counts for resources

        Attributes:
            completed_count (int | Unset): The number of completed resources Example: 10.
            failure_count (int | Unset): The number of failed resources Example: 2.
            in_progress_count (int | Unset): The number of resources in progress Example: 3.
            pending_deployment_count (int | Unset): The number of resources pending deployment Example: 5.
            total (int | Unset): The total number of resources Example: 20.
     """

    completed_count: int | Unset = UNSET
    failure_count: int | Unset = UNSET
    in_progress_count: int | Unset = UNSET
    pending_deployment_count: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        completed_count = self.completed_count

        failure_count = self.failure_count

        in_progress_count = self.in_progress_count

        pending_deployment_count = self.pending_deployment_count

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if completed_count is not UNSET:
            field_dict["completed_count"] = completed_count
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count
        if in_progress_count is not UNSET:
            field_dict["in_progress_count"] = in_progress_count
        if pending_deployment_count is not UNSET:
            field_dict["pending_deployment_count"] = pending_deployment_count
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completed_count = d.pop("completed_count", UNSET)

        failure_count = d.pop("failure_count", UNSET)

        in_progress_count = d.pop("in_progress_count", UNSET)

        pending_deployment_count = d.pop("pending_deployment_count", UNSET)

        total = d.pop("total", UNSET)

        cloud_pulse_resource_status = cls(
            completed_count=completed_count,
            failure_count=failure_count,
            in_progress_count=in_progress_count,
            pending_deployment_count=pending_deployment_count,
            total=total,
        )


        cloud_pulse_resource_status.additional_properties = d
        return cloud_pulse_resource_status

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
