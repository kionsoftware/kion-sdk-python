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





T = TypeVar("T", bound="CloudPulseMetrics")



@_attrs_define
class CloudPulseMetrics:
    """ CloudPulseMetrics represents top-level summary metrics for the dashboard

        Attributes:
            account_status (CloudPulseResourceStatus | Unset): CloudPulseResourceStatus represents aggregate status counts
                for resources
            cloud_rule_status (CloudPulseResourceStatus | Unset): CloudPulseResourceStatus represents aggregate status
                counts for resources
            cloudformation_status (CloudPulseResourceStatus | Unset): CloudPulseResourceStatus represents aggregate status
                counts for resources
     """

    account_status: CloudPulseResourceStatus | Unset = UNSET
    cloud_rule_status: CloudPulseResourceStatus | Unset = UNSET
    cloudformation_status: CloudPulseResourceStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_pulse_resource_status import CloudPulseResourceStatus
        account_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_status, Unset):
            account_status = self.account_status.to_dict()

        cloud_rule_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule_status, Unset):
            cloud_rule_status = self.cloud_rule_status.to_dict()

        cloudformation_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloudformation_status, Unset):
            cloudformation_status = self.cloudformation_status.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_status is not UNSET:
            field_dict["account_status"] = account_status
        if cloud_rule_status is not UNSET:
            field_dict["cloud_rule_status"] = cloud_rule_status
        if cloudformation_status is not UNSET:
            field_dict["cloudformation_status"] = cloudformation_status

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




        _cloudformation_status = d.pop("cloudformation_status", UNSET)
        cloudformation_status: CloudPulseResourceStatus | Unset
        if isinstance(_cloudformation_status,  Unset):
            cloudformation_status = UNSET
        else:
            cloudformation_status = CloudPulseResourceStatus.from_dict(_cloudformation_status)




        cloud_pulse_metrics = cls(
            account_status=account_status,
            cloud_rule_status=cloud_rule_status,
            cloudformation_status=cloudformation_status,
        )


        cloud_pulse_metrics.additional_properties = d
        return cloud_pulse_metrics

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
