from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloud_pulse_cloud_rule import CloudPulseCloudRule
  from ..models.cloud_pulse_region_cloud_formation_status import CloudPulseRegionCloudFormationStatus
  from ..models.cloud_pulse_resource_status import CloudPulseResourceStatus





T = TypeVar("T", bound="CloudPulseAccount")



@_attrs_define
class CloudPulseAccount:
    """ CloudPulseAccount represents a single cloud pulse account.

        Attributes:
            account_id (int | None | Unset): The ID of the account Example: 1.
            account_name (str | Unset): The name of the account Example: Production Account.
            account_number (str | Unset): The AWS account number Example: 123456789012.
            account_status (CloudPulseResourceStatus | Unset): CloudPulseResourceStatus represents aggregate status counts
                for resources
            cloud_rules (list[CloudPulseCloudRule] | None | Unset): The cloud rules associated with this account
            cloudformation_policy_id (int | None | Unset): The ID of the CloudFormation policy Example: 1.
            cloudformation_policy_name (str | Unset): The name of the CloudFormation policy Example: Example CloudFormation
                Policy.
            cloudformation_status (list[CloudPulseRegionCloudFormationStatus] | None | Unset): The CloudFormation deployment
                status across regions
     """

    account_id: int | None | Unset = UNSET
    account_name: str | Unset = UNSET
    account_number: str | Unset = UNSET
    account_status: CloudPulseResourceStatus | Unset = UNSET
    cloud_rules: list[CloudPulseCloudRule] | None | Unset = UNSET
    cloudformation_policy_id: int | None | Unset = UNSET
    cloudformation_policy_name: str | Unset = UNSET
    cloudformation_status: list[CloudPulseRegionCloudFormationStatus] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_pulse_cloud_rule import CloudPulseCloudRule
        from ..models.cloud_pulse_region_cloud_formation_status import CloudPulseRegionCloudFormationStatus
        from ..models.cloud_pulse_resource_status import CloudPulseResourceStatus
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_name = self.account_name

        account_number = self.account_number

        account_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_status, Unset):
            account_status = self.account_status.to_dict()

        cloud_rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.cloud_rules, Unset):
            cloud_rules = UNSET
        elif isinstance(self.cloud_rules, list):
            cloud_rules = []
            for cloud_rules_type_0_item_data in self.cloud_rules:
                cloud_rules_type_0_item = cloud_rules_type_0_item_data.to_dict()
                cloud_rules.append(cloud_rules_type_0_item)


        else:
            cloud_rules = self.cloud_rules

        cloudformation_policy_id: int | None | Unset
        if isinstance(self.cloudformation_policy_id, Unset):
            cloudformation_policy_id = UNSET
        else:
            cloudformation_policy_id = self.cloudformation_policy_id

        cloudformation_policy_name = self.cloudformation_policy_name

        cloudformation_status: list[dict[str, Any]] | None | Unset
        if isinstance(self.cloudformation_status, Unset):
            cloudformation_status = UNSET
        elif isinstance(self.cloudformation_status, list):
            cloudformation_status = []
            for cloudformation_status_type_0_item_data in self.cloudformation_status:
                cloudformation_status_type_0_item = cloudformation_status_type_0_item_data.to_dict()
                cloudformation_status.append(cloudformation_status_type_0_item)


        else:
            cloudformation_status = self.cloudformation_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if account_status is not UNSET:
            field_dict["account_status"] = account_status
        if cloud_rules is not UNSET:
            field_dict["cloud_rules"] = cloud_rules
        if cloudformation_policy_id is not UNSET:
            field_dict["cloudformation_policy_id"] = cloudformation_policy_id
        if cloudformation_policy_name is not UNSET:
            field_dict["cloudformation_policy_name"] = cloudformation_policy_name
        if cloudformation_status is not UNSET:
            field_dict["cloudformation_status"] = cloudformation_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_pulse_cloud_rule import CloudPulseCloudRule
        from ..models.cloud_pulse_region_cloud_formation_status import CloudPulseRegionCloudFormationStatus
        from ..models.cloud_pulse_resource_status import CloudPulseResourceStatus
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        account_name = d.pop("account_name", UNSET)

        account_number = d.pop("account_number", UNSET)

        _account_status = d.pop("account_status", UNSET)
        account_status: CloudPulseResourceStatus | Unset
        if isinstance(_account_status,  Unset):
            account_status = UNSET
        else:
            account_status = CloudPulseResourceStatus.from_dict(_account_status)




        def _parse_cloud_rules(data: object) -> list[CloudPulseCloudRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cloud_rules_type_0 = []
                _cloud_rules_type_0 = data
                for cloud_rules_type_0_item_data in (_cloud_rules_type_0):
                    cloud_rules_type_0_item = CloudPulseCloudRule.from_dict(cloud_rules_type_0_item_data)



                    cloud_rules_type_0.append(cloud_rules_type_0_item)

                return cloud_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CloudPulseCloudRule] | None | Unset, data)

        cloud_rules = _parse_cloud_rules(d.pop("cloud_rules", UNSET))


        def _parse_cloudformation_policy_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloudformation_policy_id = _parse_cloudformation_policy_id(d.pop("cloudformation_policy_id", UNSET))


        cloudformation_policy_name = d.pop("cloudformation_policy_name", UNSET)

        def _parse_cloudformation_status(data: object) -> list[CloudPulseRegionCloudFormationStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cloudformation_status_type_0 = []
                _cloudformation_status_type_0 = data
                for cloudformation_status_type_0_item_data in (_cloudformation_status_type_0):
                    cloudformation_status_type_0_item = CloudPulseRegionCloudFormationStatus.from_dict(cloudformation_status_type_0_item_data)



                    cloudformation_status_type_0.append(cloudformation_status_type_0_item)

                return cloudformation_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CloudPulseRegionCloudFormationStatus] | None | Unset, data)

        cloudformation_status = _parse_cloudformation_status(d.pop("cloudformation_status", UNSET))


        cloud_pulse_account = cls(
            account_id=account_id,
            account_name=account_name,
            account_number=account_number,
            account_status=account_status,
            cloud_rules=cloud_rules,
            cloudformation_policy_id=cloudformation_policy_id,
            cloudformation_policy_name=cloudformation_policy_name,
            cloudformation_status=cloudformation_status,
        )


        cloud_pulse_account.additional_properties = d
        return cloud_pulse_account

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
