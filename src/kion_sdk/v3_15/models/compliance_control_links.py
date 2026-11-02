from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceControlLinks")



@_attrs_define
class ComplianceControlLinks:
    """ ComplianceControlLinks defines a set of compliance-control to asset links in the system.

        Attributes:
            arm_template_definition_ids (list[int] | None | Unset): ARMTemplateDefinitionIDs is a set of ARM template ids
                applied to the control.
            aws_cloudformation_policy_ids (list[int] | None | Unset): AWSCloudformationPolicyIDs is a set of AWS
                cloudformation policy ids applied to the control.
            azure_policy_definition_ids (list[int] | None | Unset): AzurePolicyDefinitionIDs is a set of Azure policy ids
                applied to the control.
            cloud_provider_policy_ids (list[int] | None | Unset): CloudProviderPolicyIDs is a set of cloud provider policy
                ids applied to the control.
            compliance_check_ids (list[int] | None | Unset): ComplianceCheckIDs is a set of compliance check ids applied to
                the control.
            compliance_levels (list[int] | None | Unset): ComplianceLevels is a set of levels to which the control belongs.
     """

    arm_template_definition_ids: list[int] | None | Unset = UNSET
    aws_cloudformation_policy_ids: list[int] | None | Unset = UNSET
    azure_policy_definition_ids: list[int] | None | Unset = UNSET
    cloud_provider_policy_ids: list[int] | None | Unset = UNSET
    compliance_check_ids: list[int] | None | Unset = UNSET
    compliance_levels: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        arm_template_definition_ids: list[int] | None | Unset
        if isinstance(self.arm_template_definition_ids, Unset):
            arm_template_definition_ids = UNSET
        elif isinstance(self.arm_template_definition_ids, list):
            arm_template_definition_ids = self.arm_template_definition_ids


        else:
            arm_template_definition_ids = self.arm_template_definition_ids

        aws_cloudformation_policy_ids: list[int] | None | Unset
        if isinstance(self.aws_cloudformation_policy_ids, Unset):
            aws_cloudformation_policy_ids = UNSET
        elif isinstance(self.aws_cloudformation_policy_ids, list):
            aws_cloudformation_policy_ids = self.aws_cloudformation_policy_ids


        else:
            aws_cloudformation_policy_ids = self.aws_cloudformation_policy_ids

        azure_policy_definition_ids: list[int] | None | Unset
        if isinstance(self.azure_policy_definition_ids, Unset):
            azure_policy_definition_ids = UNSET
        elif isinstance(self.azure_policy_definition_ids, list):
            azure_policy_definition_ids = self.azure_policy_definition_ids


        else:
            azure_policy_definition_ids = self.azure_policy_definition_ids

        cloud_provider_policy_ids: list[int] | None | Unset
        if isinstance(self.cloud_provider_policy_ids, Unset):
            cloud_provider_policy_ids = UNSET
        elif isinstance(self.cloud_provider_policy_ids, list):
            cloud_provider_policy_ids = self.cloud_provider_policy_ids


        else:
            cloud_provider_policy_ids = self.cloud_provider_policy_ids

        compliance_check_ids: list[int] | None | Unset
        if isinstance(self.compliance_check_ids, Unset):
            compliance_check_ids = UNSET
        elif isinstance(self.compliance_check_ids, list):
            compliance_check_ids = self.compliance_check_ids


        else:
            compliance_check_ids = self.compliance_check_ids

        compliance_levels: list[int] | None | Unset
        if isinstance(self.compliance_levels, Unset):
            compliance_levels = UNSET
        elif isinstance(self.compliance_levels, list):
            compliance_levels = self.compliance_levels


        else:
            compliance_levels = self.compliance_levels


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if arm_template_definition_ids is not UNSET:
            field_dict["arm_template_definition_ids"] = arm_template_definition_ids
        if aws_cloudformation_policy_ids is not UNSET:
            field_dict["aws_cloudformation_policy_ids"] = aws_cloudformation_policy_ids
        if azure_policy_definition_ids is not UNSET:
            field_dict["azure_policy_definition_ids"] = azure_policy_definition_ids
        if cloud_provider_policy_ids is not UNSET:
            field_dict["cloud_provider_policy_ids"] = cloud_provider_policy_ids
        if compliance_check_ids is not UNSET:
            field_dict["compliance_check_ids"] = compliance_check_ids
        if compliance_levels is not UNSET:
            field_dict["compliance_levels"] = compliance_levels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_arm_template_definition_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                arm_template_definition_ids_type_0 = cast(list[int], data)

                return arm_template_definition_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        arm_template_definition_ids = _parse_arm_template_definition_ids(d.pop("arm_template_definition_ids", UNSET))


        def _parse_aws_cloudformation_policy_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_cloudformation_policy_ids_type_0 = cast(list[int], data)

                return aws_cloudformation_policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        aws_cloudformation_policy_ids = _parse_aws_cloudformation_policy_ids(d.pop("aws_cloudformation_policy_ids", UNSET))


        def _parse_azure_policy_definition_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_policy_definition_ids_type_0 = cast(list[int], data)

                return azure_policy_definition_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        azure_policy_definition_ids = _parse_azure_policy_definition_ids(d.pop("azure_policy_definition_ids", UNSET))


        def _parse_cloud_provider_policy_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cloud_provider_policy_ids_type_0 = cast(list[int], data)

                return cloud_provider_policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        cloud_provider_policy_ids = _parse_cloud_provider_policy_ids(d.pop("cloud_provider_policy_ids", UNSET))


        def _parse_compliance_check_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_check_ids_type_0 = cast(list[int], data)

                return compliance_check_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        compliance_check_ids = _parse_compliance_check_ids(d.pop("compliance_check_ids", UNSET))


        def _parse_compliance_levels(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_levels_type_0 = cast(list[int], data)

                return compliance_levels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        compliance_levels = _parse_compliance_levels(d.pop("compliance_levels", UNSET))


        compliance_control_links = cls(
            arm_template_definition_ids=arm_template_definition_ids,
            aws_cloudformation_policy_ids=aws_cloudformation_policy_ids,
            azure_policy_definition_ids=azure_policy_definition_ids,
            cloud_provider_policy_ids=cloud_provider_policy_ids,
            compliance_check_ids=compliance_check_ids,
            compliance_levels=compliance_levels,
        )


        compliance_control_links.additional_properties = d
        return compliance_control_links

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
