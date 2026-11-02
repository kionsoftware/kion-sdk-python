from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CloudRuleAssociations")



@_attrs_define
class CloudRuleAssociations:
    """ CloudRuleAssociations defines a Cloud Rule association update.

        Attributes:
            automation_policy_ids (list[int] | None | Unset): List of Automation Policies where the Cloud Rule is applied
                Example: [1].
            azure_arm_template_definition_ids (list[int] | None | Unset): List of Azure ARM template IDs attached to the
                Cloud Rule. Example: [1].
            azure_policy_definition_ids (list[int] | None | Unset): List of Azure Policy IDs attached to the Cloud Rule.
                Example: [1].
            azure_role_definition_ids (list[int] | None | Unset): List of Azure Role IDs attached to the Cloud Rule.
                Example: [1].
            cft_ids (list[int] | None | Unset): List of CloudFormation template IDs attached to the Cloud Rule. Example:
                [1].
            compliance_standard_ids (list[int] | None | Unset): List of Compliance Standards where the Cloud Rule is applied
                Example: [1].
            gcp_iam_role_ids (list[int] | None | Unset): List of Google Cloud IAM role IDs attached to the Cloud Rule.
                Example: [1].
            iam_policy_ids (list[int] | None | Unset): List of IAM Policy IDs attached to the Cloud Rule. Example: [1].
            internal_ami_ids (list[int] | None | Unset): List of AMIs attached to the Cloud Rule. Example: [1].
            internal_portfolio_ids (list[int] | None | Unset): List of Service Catalog Portfolio IDs attached to the Cloud
                Rule. Example: [1].
            ou_ids (list[int] | None | Unset): List of OUs where the Cloud Rule is applied. Example: [1].
            project_ids (list[int] | None | Unset): List of projects where the Cloud Rule is applied. Example: [1].
            service_control_policy_ids (list[int] | None | Unset): List of Service Control Policies where the Cloud Rule is
                applied Example: [1].
     """

    automation_policy_ids: list[int] | None | Unset = UNSET
    azure_arm_template_definition_ids: list[int] | None | Unset = UNSET
    azure_policy_definition_ids: list[int] | None | Unset = UNSET
    azure_role_definition_ids: list[int] | None | Unset = UNSET
    cft_ids: list[int] | None | Unset = UNSET
    compliance_standard_ids: list[int] | None | Unset = UNSET
    gcp_iam_role_ids: list[int] | None | Unset = UNSET
    iam_policy_ids: list[int] | None | Unset = UNSET
    internal_ami_ids: list[int] | None | Unset = UNSET
    internal_portfolio_ids: list[int] | None | Unset = UNSET
    ou_ids: list[int] | None | Unset = UNSET
    project_ids: list[int] | None | Unset = UNSET
    service_control_policy_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        automation_policy_ids: list[int] | None | Unset
        if isinstance(self.automation_policy_ids, Unset):
            automation_policy_ids = UNSET
        elif isinstance(self.automation_policy_ids, list):
            automation_policy_ids = self.automation_policy_ids


        else:
            automation_policy_ids = self.automation_policy_ids

        azure_arm_template_definition_ids: list[int] | None | Unset
        if isinstance(self.azure_arm_template_definition_ids, Unset):
            azure_arm_template_definition_ids = UNSET
        elif isinstance(self.azure_arm_template_definition_ids, list):
            azure_arm_template_definition_ids = self.azure_arm_template_definition_ids


        else:
            azure_arm_template_definition_ids = self.azure_arm_template_definition_ids

        azure_policy_definition_ids: list[int] | None | Unset
        if isinstance(self.azure_policy_definition_ids, Unset):
            azure_policy_definition_ids = UNSET
        elif isinstance(self.azure_policy_definition_ids, list):
            azure_policy_definition_ids = self.azure_policy_definition_ids


        else:
            azure_policy_definition_ids = self.azure_policy_definition_ids

        azure_role_definition_ids: list[int] | None | Unset
        if isinstance(self.azure_role_definition_ids, Unset):
            azure_role_definition_ids = UNSET
        elif isinstance(self.azure_role_definition_ids, list):
            azure_role_definition_ids = self.azure_role_definition_ids


        else:
            azure_role_definition_ids = self.azure_role_definition_ids

        cft_ids: list[int] | None | Unset
        if isinstance(self.cft_ids, Unset):
            cft_ids = UNSET
        elif isinstance(self.cft_ids, list):
            cft_ids = self.cft_ids


        else:
            cft_ids = self.cft_ids

        compliance_standard_ids: list[int] | None | Unset
        if isinstance(self.compliance_standard_ids, Unset):
            compliance_standard_ids = UNSET
        elif isinstance(self.compliance_standard_ids, list):
            compliance_standard_ids = self.compliance_standard_ids


        else:
            compliance_standard_ids = self.compliance_standard_ids

        gcp_iam_role_ids: list[int] | None | Unset
        if isinstance(self.gcp_iam_role_ids, Unset):
            gcp_iam_role_ids = UNSET
        elif isinstance(self.gcp_iam_role_ids, list):
            gcp_iam_role_ids = self.gcp_iam_role_ids


        else:
            gcp_iam_role_ids = self.gcp_iam_role_ids

        iam_policy_ids: list[int] | None | Unset
        if isinstance(self.iam_policy_ids, Unset):
            iam_policy_ids = UNSET
        elif isinstance(self.iam_policy_ids, list):
            iam_policy_ids = self.iam_policy_ids


        else:
            iam_policy_ids = self.iam_policy_ids

        internal_ami_ids: list[int] | None | Unset
        if isinstance(self.internal_ami_ids, Unset):
            internal_ami_ids = UNSET
        elif isinstance(self.internal_ami_ids, list):
            internal_ami_ids = self.internal_ami_ids


        else:
            internal_ami_ids = self.internal_ami_ids

        internal_portfolio_ids: list[int] | None | Unset
        if isinstance(self.internal_portfolio_ids, Unset):
            internal_portfolio_ids = UNSET
        elif isinstance(self.internal_portfolio_ids, list):
            internal_portfolio_ids = self.internal_portfolio_ids


        else:
            internal_portfolio_ids = self.internal_portfolio_ids

        ou_ids: list[int] | None | Unset
        if isinstance(self.ou_ids, Unset):
            ou_ids = UNSET
        elif isinstance(self.ou_ids, list):
            ou_ids = self.ou_ids


        else:
            ou_ids = self.ou_ids

        project_ids: list[int] | None | Unset
        if isinstance(self.project_ids, Unset):
            project_ids = UNSET
        elif isinstance(self.project_ids, list):
            project_ids = self.project_ids


        else:
            project_ids = self.project_ids

        service_control_policy_ids: list[int] | None | Unset
        if isinstance(self.service_control_policy_ids, Unset):
            service_control_policy_ids = UNSET
        elif isinstance(self.service_control_policy_ids, list):
            service_control_policy_ids = self.service_control_policy_ids


        else:
            service_control_policy_ids = self.service_control_policy_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if automation_policy_ids is not UNSET:
            field_dict["automation_policy_ids"] = automation_policy_ids
        if azure_arm_template_definition_ids is not UNSET:
            field_dict["azure_arm_template_definition_ids"] = azure_arm_template_definition_ids
        if azure_policy_definition_ids is not UNSET:
            field_dict["azure_policy_definition_ids"] = azure_policy_definition_ids
        if azure_role_definition_ids is not UNSET:
            field_dict["azure_role_definition_ids"] = azure_role_definition_ids
        if cft_ids is not UNSET:
            field_dict["cft_ids"] = cft_ids
        if compliance_standard_ids is not UNSET:
            field_dict["compliance_standard_ids"] = compliance_standard_ids
        if gcp_iam_role_ids is not UNSET:
            field_dict["gcp_iam_role_ids"] = gcp_iam_role_ids
        if iam_policy_ids is not UNSET:
            field_dict["iam_policy_ids"] = iam_policy_ids
        if internal_ami_ids is not UNSET:
            field_dict["internal_ami_ids"] = internal_ami_ids
        if internal_portfolio_ids is not UNSET:
            field_dict["internal_portfolio_ids"] = internal_portfolio_ids
        if ou_ids is not UNSET:
            field_dict["ou_ids"] = ou_ids
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if service_control_policy_ids is not UNSET:
            field_dict["service_control_policy_ids"] = service_control_policy_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_automation_policy_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                automation_policy_ids_type_0 = cast(list[int], data)

                return automation_policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        automation_policy_ids = _parse_automation_policy_ids(d.pop("automation_policy_ids", UNSET))


        def _parse_azure_arm_template_definition_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_arm_template_definition_ids_type_0 = cast(list[int], data)

                return azure_arm_template_definition_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        azure_arm_template_definition_ids = _parse_azure_arm_template_definition_ids(d.pop("azure_arm_template_definition_ids", UNSET))


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


        def _parse_azure_role_definition_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_role_definition_ids_type_0 = cast(list[int], data)

                return azure_role_definition_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        azure_role_definition_ids = _parse_azure_role_definition_ids(d.pop("azure_role_definition_ids", UNSET))


        def _parse_cft_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cft_ids_type_0 = cast(list[int], data)

                return cft_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        cft_ids = _parse_cft_ids(d.pop("cft_ids", UNSET))


        def _parse_compliance_standard_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_standard_ids_type_0 = cast(list[int], data)

                return compliance_standard_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        compliance_standard_ids = _parse_compliance_standard_ids(d.pop("compliance_standard_ids", UNSET))


        def _parse_gcp_iam_role_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gcp_iam_role_ids_type_0 = cast(list[int], data)

                return gcp_iam_role_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        gcp_iam_role_ids = _parse_gcp_iam_role_ids(d.pop("gcp_iam_role_ids", UNSET))


        def _parse_iam_policy_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                iam_policy_ids_type_0 = cast(list[int], data)

                return iam_policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        iam_policy_ids = _parse_iam_policy_ids(d.pop("iam_policy_ids", UNSET))


        def _parse_internal_ami_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_ami_ids_type_0 = cast(list[int], data)

                return internal_ami_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        internal_ami_ids = _parse_internal_ami_ids(d.pop("internal_ami_ids", UNSET))


        def _parse_internal_portfolio_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_portfolio_ids_type_0 = cast(list[int], data)

                return internal_portfolio_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        internal_portfolio_ids = _parse_internal_portfolio_ids(d.pop("internal_portfolio_ids", UNSET))


        def _parse_ou_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ou_ids_type_0 = cast(list[int], data)

                return ou_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        ou_ids = _parse_ou_ids(d.pop("ou_ids", UNSET))


        def _parse_project_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_ids_type_0 = cast(list[int], data)

                return project_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        project_ids = _parse_project_ids(d.pop("project_ids", UNSET))


        def _parse_service_control_policy_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_control_policy_ids_type_0 = cast(list[int], data)

                return service_control_policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        service_control_policy_ids = _parse_service_control_policy_ids(d.pop("service_control_policy_ids", UNSET))


        cloud_rule_associations = cls(
            automation_policy_ids=automation_policy_ids,
            azure_arm_template_definition_ids=azure_arm_template_definition_ids,
            azure_policy_definition_ids=azure_policy_definition_ids,
            azure_role_definition_ids=azure_role_definition_ids,
            cft_ids=cft_ids,
            compliance_standard_ids=compliance_standard_ids,
            gcp_iam_role_ids=gcp_iam_role_ids,
            iam_policy_ids=iam_policy_ids,
            internal_ami_ids=internal_ami_ids,
            internal_portfolio_ids=internal_portfolio_ids,
            ou_ids=ou_ids,
            project_ids=project_ids,
            service_control_policy_ids=service_control_policy_ids,
        )


        cloud_rule_associations.additional_properties = d
        return cloud_rule_associations

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
