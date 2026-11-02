from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ami import AMI
  from ..models.automation_policy import AutomationPolicy
  from ..models.azure_arm_template_definition import AzureARMTemplateDefinition
  from ..models.azure_policy_definition import AzurePolicyDefinition
  from ..models.azure_role import AzureRole
  from ..models.cft import CFT
  from ..models.cloud_rule import CloudRule
  from ..models.compliance_standard import ComplianceStandard
  from ..models.gcp_role import GCPRole
  from ..models.iam_policy import IAMPolicy
  from ..models.ou import OU
  from ..models.project import Project
  from ..models.service_catalog_portfolio import ServiceCatalogPortfolio
  from ..models.service_control_policy import ServiceControlPolicy
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="CloudRuleFull")



@_attrs_define
class CloudRuleFull:
    """ CloudRuleFull defines a Cloud Rule and all associations.

        Attributes:
            automation_policies (list[AutomationPolicy] | None | Unset): List of Automation Policies attached to the Cloud
                Rule
            aws_cloudformation_templates (list[CFT] | None | Unset): List of CloudFormation template IDs attached to the
                Cloud Rule.
            aws_iam_policies (list[IAMPolicy] | None | Unset): List of IAM Policy IDs attached to the Cloud Rule.
            azure_arm_template_definitions (list[AzureARMTemplateDefinition] | None | Unset): List of Azure ARM template
                definitions attached to the cloud rule.
            azure_policy_definitions (list[AzurePolicyDefinition] | None | Unset): List of Azure Policy Definitions attached
                to the Cloud Rule.
            azure_role_definitions (list[AzureRole] | None | Unset): List of Azure Roles attached to the Cloud Rule.
            cloud_rule (CloudRule | Unset): CloudRule defines a Cloud Rule.
            compliance_standards (list[ComplianceStandard] | None | Unset): List of Compliance Standards attached to the
                Cloud Rule
            gcp_iam_roles (list[GCPRole] | None | Unset): List of Google Cloud IAM role IDs attached to the Cloud Rule.
            internal_aws_amis (list[AMI] | None | Unset): List of AMIs attached to the Cloud Rule.
            internal_aws_service_catalog_portfolios (list[ServiceCatalogPortfolio] | None | Unset): List of Service Catalog
                Portfolio IDs attached to the Cloud Rule.
            ous (list[OU] | None | Unset): List of OUs where the Cloud Rule is applied.
            owner_user_groups (list[UGroup] | None | Unset): List of groups that own the Cloud Rule.
            owner_users (list[User] | None | Unset): List of users that own the Cloud Rule.
            projects (list[Project] | None | Unset): List of projects where the Cloud Rule is applied.
            service_control_policies (list[ServiceControlPolicy] | None | Unset): List of Service Control Policies attached
                to the Cloud Rule
     """

    automation_policies: list[AutomationPolicy] | None | Unset = UNSET
    aws_cloudformation_templates: list[CFT] | None | Unset = UNSET
    aws_iam_policies: list[IAMPolicy] | None | Unset = UNSET
    azure_arm_template_definitions: list[AzureARMTemplateDefinition] | None | Unset = UNSET
    azure_policy_definitions: list[AzurePolicyDefinition] | None | Unset = UNSET
    azure_role_definitions: list[AzureRole] | None | Unset = UNSET
    cloud_rule: CloudRule | Unset = UNSET
    compliance_standards: list[ComplianceStandard] | None | Unset = UNSET
    gcp_iam_roles: list[GCPRole] | None | Unset = UNSET
    internal_aws_amis: list[AMI] | None | Unset = UNSET
    internal_aws_service_catalog_portfolios: list[ServiceCatalogPortfolio] | None | Unset = UNSET
    ous: list[OU] | None | Unset = UNSET
    owner_user_groups: list[UGroup] | None | Unset = UNSET
    owner_users: list[User] | None | Unset = UNSET
    projects: list[Project] | None | Unset = UNSET
    service_control_policies: list[ServiceControlPolicy] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ami import AMI
        from ..models.automation_policy import AutomationPolicy
        from ..models.azure_arm_template_definition import AzureARMTemplateDefinition
        from ..models.azure_policy_definition import AzurePolicyDefinition
        from ..models.azure_role import AzureRole
        from ..models.cft import CFT
        from ..models.cloud_rule import CloudRule
        from ..models.compliance_standard import ComplianceStandard
        from ..models.gcp_role import GCPRole
        from ..models.iam_policy import IAMPolicy
        from ..models.ou import OU
        from ..models.project import Project
        from ..models.service_catalog_portfolio import ServiceCatalogPortfolio
        from ..models.service_control_policy import ServiceControlPolicy
        from ..models.u_group import UGroup
        from ..models.user import User
        automation_policies: list[dict[str, Any]] | None | Unset
        if isinstance(self.automation_policies, Unset):
            automation_policies = UNSET
        elif isinstance(self.automation_policies, list):
            automation_policies = []
            for automation_policies_type_0_item_data in self.automation_policies:
                automation_policies_type_0_item = automation_policies_type_0_item_data.to_dict()
                automation_policies.append(automation_policies_type_0_item)


        else:
            automation_policies = self.automation_policies

        aws_cloudformation_templates: list[dict[str, Any]] | None | Unset
        if isinstance(self.aws_cloudformation_templates, Unset):
            aws_cloudformation_templates = UNSET
        elif isinstance(self.aws_cloudformation_templates, list):
            aws_cloudformation_templates = []
            for aws_cloudformation_templates_type_0_item_data in self.aws_cloudformation_templates:
                aws_cloudformation_templates_type_0_item = aws_cloudformation_templates_type_0_item_data.to_dict()
                aws_cloudformation_templates.append(aws_cloudformation_templates_type_0_item)


        else:
            aws_cloudformation_templates = self.aws_cloudformation_templates

        aws_iam_policies: list[dict[str, Any]] | None | Unset
        if isinstance(self.aws_iam_policies, Unset):
            aws_iam_policies = UNSET
        elif isinstance(self.aws_iam_policies, list):
            aws_iam_policies = []
            for aws_iam_policies_type_0_item_data in self.aws_iam_policies:
                aws_iam_policies_type_0_item = aws_iam_policies_type_0_item_data.to_dict()
                aws_iam_policies.append(aws_iam_policies_type_0_item)


        else:
            aws_iam_policies = self.aws_iam_policies

        azure_arm_template_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.azure_arm_template_definitions, Unset):
            azure_arm_template_definitions = UNSET
        elif isinstance(self.azure_arm_template_definitions, list):
            azure_arm_template_definitions = []
            for azure_arm_template_definitions_type_0_item_data in self.azure_arm_template_definitions:
                azure_arm_template_definitions_type_0_item = azure_arm_template_definitions_type_0_item_data.to_dict()
                azure_arm_template_definitions.append(azure_arm_template_definitions_type_0_item)


        else:
            azure_arm_template_definitions = self.azure_arm_template_definitions

        azure_policy_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.azure_policy_definitions, Unset):
            azure_policy_definitions = UNSET
        elif isinstance(self.azure_policy_definitions, list):
            azure_policy_definitions = []
            for azure_policy_definitions_type_0_item_data in self.azure_policy_definitions:
                azure_policy_definitions_type_0_item = azure_policy_definitions_type_0_item_data.to_dict()
                azure_policy_definitions.append(azure_policy_definitions_type_0_item)


        else:
            azure_policy_definitions = self.azure_policy_definitions

        azure_role_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.azure_role_definitions, Unset):
            azure_role_definitions = UNSET
        elif isinstance(self.azure_role_definitions, list):
            azure_role_definitions = []
            for azure_role_definitions_type_0_item_data in self.azure_role_definitions:
                azure_role_definitions_type_0_item = azure_role_definitions_type_0_item_data.to_dict()
                azure_role_definitions.append(azure_role_definitions_type_0_item)


        else:
            azure_role_definitions = self.azure_role_definitions

        cloud_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule, Unset):
            cloud_rule = self.cloud_rule.to_dict()

        compliance_standards: list[dict[str, Any]] | None | Unset
        if isinstance(self.compliance_standards, Unset):
            compliance_standards = UNSET
        elif isinstance(self.compliance_standards, list):
            compliance_standards = []
            for compliance_standards_type_0_item_data in self.compliance_standards:
                compliance_standards_type_0_item = compliance_standards_type_0_item_data.to_dict()
                compliance_standards.append(compliance_standards_type_0_item)


        else:
            compliance_standards = self.compliance_standards

        gcp_iam_roles: list[dict[str, Any]] | None | Unset
        if isinstance(self.gcp_iam_roles, Unset):
            gcp_iam_roles = UNSET
        elif isinstance(self.gcp_iam_roles, list):
            gcp_iam_roles = []
            for gcp_iam_roles_type_0_item_data in self.gcp_iam_roles:
                gcp_iam_roles_type_0_item = gcp_iam_roles_type_0_item_data.to_dict()
                gcp_iam_roles.append(gcp_iam_roles_type_0_item)


        else:
            gcp_iam_roles = self.gcp_iam_roles

        internal_aws_amis: list[dict[str, Any]] | None | Unset
        if isinstance(self.internal_aws_amis, Unset):
            internal_aws_amis = UNSET
        elif isinstance(self.internal_aws_amis, list):
            internal_aws_amis = []
            for internal_aws_amis_type_0_item_data in self.internal_aws_amis:
                internal_aws_amis_type_0_item = internal_aws_amis_type_0_item_data.to_dict()
                internal_aws_amis.append(internal_aws_amis_type_0_item)


        else:
            internal_aws_amis = self.internal_aws_amis

        internal_aws_service_catalog_portfolios: list[dict[str, Any]] | None | Unset
        if isinstance(self.internal_aws_service_catalog_portfolios, Unset):
            internal_aws_service_catalog_portfolios = UNSET
        elif isinstance(self.internal_aws_service_catalog_portfolios, list):
            internal_aws_service_catalog_portfolios = []
            for internal_aws_service_catalog_portfolios_type_0_item_data in self.internal_aws_service_catalog_portfolios:
                internal_aws_service_catalog_portfolios_type_0_item = internal_aws_service_catalog_portfolios_type_0_item_data.to_dict()
                internal_aws_service_catalog_portfolios.append(internal_aws_service_catalog_portfolios_type_0_item)


        else:
            internal_aws_service_catalog_portfolios = self.internal_aws_service_catalog_portfolios

        ous: list[dict[str, Any]] | None | Unset
        if isinstance(self.ous, Unset):
            ous = UNSET
        elif isinstance(self.ous, list):
            ous = []
            for ous_type_0_item_data in self.ous:
                ous_type_0_item = ous_type_0_item_data.to_dict()
                ous.append(ous_type_0_item)


        else:
            ous = self.ous

        owner_user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_user_groups, Unset):
            owner_user_groups = UNSET
        elif isinstance(self.owner_user_groups, list):
            owner_user_groups = []
            for owner_user_groups_type_0_item_data in self.owner_user_groups:
                owner_user_groups_type_0_item = owner_user_groups_type_0_item_data.to_dict()
                owner_user_groups.append(owner_user_groups_type_0_item)


        else:
            owner_user_groups = self.owner_user_groups

        owner_users: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_users, Unset):
            owner_users = UNSET
        elif isinstance(self.owner_users, list):
            owner_users = []
            for owner_users_type_0_item_data in self.owner_users:
                owner_users_type_0_item = owner_users_type_0_item_data.to_dict()
                owner_users.append(owner_users_type_0_item)


        else:
            owner_users = self.owner_users

        projects: list[dict[str, Any]] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item = projects_type_0_item_data.to_dict()
                projects.append(projects_type_0_item)


        else:
            projects = self.projects

        service_control_policies: list[dict[str, Any]] | None | Unset
        if isinstance(self.service_control_policies, Unset):
            service_control_policies = UNSET
        elif isinstance(self.service_control_policies, list):
            service_control_policies = []
            for service_control_policies_type_0_item_data in self.service_control_policies:
                service_control_policies_type_0_item = service_control_policies_type_0_item_data.to_dict()
                service_control_policies.append(service_control_policies_type_0_item)


        else:
            service_control_policies = self.service_control_policies


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if automation_policies is not UNSET:
            field_dict["automation_policies"] = automation_policies
        if aws_cloudformation_templates is not UNSET:
            field_dict["aws_cloudformation_templates"] = aws_cloudformation_templates
        if aws_iam_policies is not UNSET:
            field_dict["aws_iam_policies"] = aws_iam_policies
        if azure_arm_template_definitions is not UNSET:
            field_dict["azure_arm_template_definitions"] = azure_arm_template_definitions
        if azure_policy_definitions is not UNSET:
            field_dict["azure_policy_definitions"] = azure_policy_definitions
        if azure_role_definitions is not UNSET:
            field_dict["azure_role_definitions"] = azure_role_definitions
        if cloud_rule is not UNSET:
            field_dict["cloud_rule"] = cloud_rule
        if compliance_standards is not UNSET:
            field_dict["compliance_standards"] = compliance_standards
        if gcp_iam_roles is not UNSET:
            field_dict["gcp_iam_roles"] = gcp_iam_roles
        if internal_aws_amis is not UNSET:
            field_dict["internal_aws_amis"] = internal_aws_amis
        if internal_aws_service_catalog_portfolios is not UNSET:
            field_dict["internal_aws_service_catalog_portfolios"] = internal_aws_service_catalog_portfolios
        if ous is not UNSET:
            field_dict["ous"] = ous
        if owner_user_groups is not UNSET:
            field_dict["owner_user_groups"] = owner_user_groups
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users
        if projects is not UNSET:
            field_dict["projects"] = projects
        if service_control_policies is not UNSET:
            field_dict["service_control_policies"] = service_control_policies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ami import AMI
        from ..models.automation_policy import AutomationPolicy
        from ..models.azure_arm_template_definition import AzureARMTemplateDefinition
        from ..models.azure_policy_definition import AzurePolicyDefinition
        from ..models.azure_role import AzureRole
        from ..models.cft import CFT
        from ..models.cloud_rule import CloudRule
        from ..models.compliance_standard import ComplianceStandard
        from ..models.gcp_role import GCPRole
        from ..models.iam_policy import IAMPolicy
        from ..models.ou import OU
        from ..models.project import Project
        from ..models.service_catalog_portfolio import ServiceCatalogPortfolio
        from ..models.service_control_policy import ServiceControlPolicy
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        def _parse_automation_policies(data: object) -> list[AutomationPolicy] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                automation_policies_type_0 = []
                _automation_policies_type_0 = data
                for automation_policies_type_0_item_data in (_automation_policies_type_0):
                    automation_policies_type_0_item = AutomationPolicy.from_dict(automation_policies_type_0_item_data)



                    automation_policies_type_0.append(automation_policies_type_0_item)

                return automation_policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AutomationPolicy] | None | Unset, data)

        automation_policies = _parse_automation_policies(d.pop("automation_policies", UNSET))


        def _parse_aws_cloudformation_templates(data: object) -> list[CFT] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_cloudformation_templates_type_0 = []
                _aws_cloudformation_templates_type_0 = data
                for aws_cloudformation_templates_type_0_item_data in (_aws_cloudformation_templates_type_0):
                    aws_cloudformation_templates_type_0_item = CFT.from_dict(aws_cloudformation_templates_type_0_item_data)



                    aws_cloudformation_templates_type_0.append(aws_cloudformation_templates_type_0_item)

                return aws_cloudformation_templates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CFT] | None | Unset, data)

        aws_cloudformation_templates = _parse_aws_cloudformation_templates(d.pop("aws_cloudformation_templates", UNSET))


        def _parse_aws_iam_policies(data: object) -> list[IAMPolicy] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_iam_policies_type_0 = []
                _aws_iam_policies_type_0 = data
                for aws_iam_policies_type_0_item_data in (_aws_iam_policies_type_0):
                    aws_iam_policies_type_0_item = IAMPolicy.from_dict(aws_iam_policies_type_0_item_data)



                    aws_iam_policies_type_0.append(aws_iam_policies_type_0_item)

                return aws_iam_policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IAMPolicy] | None | Unset, data)

        aws_iam_policies = _parse_aws_iam_policies(d.pop("aws_iam_policies", UNSET))


        def _parse_azure_arm_template_definitions(data: object) -> list[AzureARMTemplateDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_arm_template_definitions_type_0 = []
                _azure_arm_template_definitions_type_0 = data
                for azure_arm_template_definitions_type_0_item_data in (_azure_arm_template_definitions_type_0):
                    azure_arm_template_definitions_type_0_item = AzureARMTemplateDefinition.from_dict(azure_arm_template_definitions_type_0_item_data)



                    azure_arm_template_definitions_type_0.append(azure_arm_template_definitions_type_0_item)

                return azure_arm_template_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureARMTemplateDefinition] | None | Unset, data)

        azure_arm_template_definitions = _parse_azure_arm_template_definitions(d.pop("azure_arm_template_definitions", UNSET))


        def _parse_azure_policy_definitions(data: object) -> list[AzurePolicyDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_policy_definitions_type_0 = []
                _azure_policy_definitions_type_0 = data
                for azure_policy_definitions_type_0_item_data in (_azure_policy_definitions_type_0):
                    azure_policy_definitions_type_0_item = AzurePolicyDefinition.from_dict(azure_policy_definitions_type_0_item_data)



                    azure_policy_definitions_type_0.append(azure_policy_definitions_type_0_item)

                return azure_policy_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzurePolicyDefinition] | None | Unset, data)

        azure_policy_definitions = _parse_azure_policy_definitions(d.pop("azure_policy_definitions", UNSET))


        def _parse_azure_role_definitions(data: object) -> list[AzureRole] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_role_definitions_type_0 = []
                _azure_role_definitions_type_0 = data
                for azure_role_definitions_type_0_item_data in (_azure_role_definitions_type_0):
                    azure_role_definitions_type_0_item = AzureRole.from_dict(azure_role_definitions_type_0_item_data)



                    azure_role_definitions_type_0.append(azure_role_definitions_type_0_item)

                return azure_role_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureRole] | None | Unset, data)

        azure_role_definitions = _parse_azure_role_definitions(d.pop("azure_role_definitions", UNSET))


        _cloud_rule = d.pop("cloud_rule", UNSET)
        cloud_rule: CloudRule | Unset
        if isinstance(_cloud_rule,  Unset):
            cloud_rule = UNSET
        else:
            cloud_rule = CloudRule.from_dict(_cloud_rule)




        def _parse_compliance_standards(data: object) -> list[ComplianceStandard] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_standards_type_0 = []
                _compliance_standards_type_0 = data
                for compliance_standards_type_0_item_data in (_compliance_standards_type_0):
                    compliance_standards_type_0_item = ComplianceStandard.from_dict(compliance_standards_type_0_item_data)



                    compliance_standards_type_0.append(compliance_standards_type_0_item)

                return compliance_standards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceStandard] | None | Unset, data)

        compliance_standards = _parse_compliance_standards(d.pop("compliance_standards", UNSET))


        def _parse_gcp_iam_roles(data: object) -> list[GCPRole] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gcp_iam_roles_type_0 = []
                _gcp_iam_roles_type_0 = data
                for gcp_iam_roles_type_0_item_data in (_gcp_iam_roles_type_0):
                    gcp_iam_roles_type_0_item = GCPRole.from_dict(gcp_iam_roles_type_0_item_data)



                    gcp_iam_roles_type_0.append(gcp_iam_roles_type_0_item)

                return gcp_iam_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GCPRole] | None | Unset, data)

        gcp_iam_roles = _parse_gcp_iam_roles(d.pop("gcp_iam_roles", UNSET))


        def _parse_internal_aws_amis(data: object) -> list[AMI] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_aws_amis_type_0 = []
                _internal_aws_amis_type_0 = data
                for internal_aws_amis_type_0_item_data in (_internal_aws_amis_type_0):
                    internal_aws_amis_type_0_item = AMI.from_dict(internal_aws_amis_type_0_item_data)



                    internal_aws_amis_type_0.append(internal_aws_amis_type_0_item)

                return internal_aws_amis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AMI] | None | Unset, data)

        internal_aws_amis = _parse_internal_aws_amis(d.pop("internal_aws_amis", UNSET))


        def _parse_internal_aws_service_catalog_portfolios(data: object) -> list[ServiceCatalogPortfolio] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_aws_service_catalog_portfolios_type_0 = []
                _internal_aws_service_catalog_portfolios_type_0 = data
                for internal_aws_service_catalog_portfolios_type_0_item_data in (_internal_aws_service_catalog_portfolios_type_0):
                    internal_aws_service_catalog_portfolios_type_0_item = ServiceCatalogPortfolio.from_dict(internal_aws_service_catalog_portfolios_type_0_item_data)



                    internal_aws_service_catalog_portfolios_type_0.append(internal_aws_service_catalog_portfolios_type_0_item)

                return internal_aws_service_catalog_portfolios_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ServiceCatalogPortfolio] | None | Unset, data)

        internal_aws_service_catalog_portfolios = _parse_internal_aws_service_catalog_portfolios(d.pop("internal_aws_service_catalog_portfolios", UNSET))


        def _parse_ous(data: object) -> list[OU] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ous_type_0 = []
                _ous_type_0 = data
                for ous_type_0_item_data in (_ous_type_0):
                    ous_type_0_item = OU.from_dict(ous_type_0_item_data)



                    ous_type_0.append(ous_type_0_item)

                return ous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OU] | None | Unset, data)

        ous = _parse_ous(d.pop("ous", UNSET))


        def _parse_owner_user_groups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_groups_type_0 = []
                _owner_user_groups_type_0 = data
                for owner_user_groups_type_0_item_data in (_owner_user_groups_type_0):
                    owner_user_groups_type_0_item = UGroup.from_dict(owner_user_groups_type_0_item_data)



                    owner_user_groups_type_0.append(owner_user_groups_type_0_item)

                return owner_user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        owner_user_groups = _parse_owner_user_groups(d.pop("owner_user_groups", UNSET))


        def _parse_owner_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_users_type_0 = []
                _owner_users_type_0 = data
                for owner_users_type_0_item_data in (_owner_users_type_0):
                    owner_users_type_0_item = User.from_dict(owner_users_type_0_item_data)



                    owner_users_type_0.append(owner_users_type_0_item)

                return owner_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        owner_users = _parse_owner_users(d.pop("owner_users", UNSET))


        def _parse_projects(data: object) -> list[Project] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = []
                _projects_type_0 = data
                for projects_type_0_item_data in (_projects_type_0):
                    projects_type_0_item = Project.from_dict(projects_type_0_item_data)



                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Project] | None | Unset, data)

        projects = _parse_projects(d.pop("projects", UNSET))


        def _parse_service_control_policies(data: object) -> list[ServiceControlPolicy] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_control_policies_type_0 = []
                _service_control_policies_type_0 = data
                for service_control_policies_type_0_item_data in (_service_control_policies_type_0):
                    service_control_policies_type_0_item = ServiceControlPolicy.from_dict(service_control_policies_type_0_item_data)



                    service_control_policies_type_0.append(service_control_policies_type_0_item)

                return service_control_policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ServiceControlPolicy] | None | Unset, data)

        service_control_policies = _parse_service_control_policies(d.pop("service_control_policies", UNSET))


        cloud_rule_full = cls(
            automation_policies=automation_policies,
            aws_cloudformation_templates=aws_cloudformation_templates,
            aws_iam_policies=aws_iam_policies,
            azure_arm_template_definitions=azure_arm_template_definitions,
            azure_policy_definitions=azure_policy_definitions,
            azure_role_definitions=azure_role_definitions,
            cloud_rule=cloud_rule,
            compliance_standards=compliance_standards,
            gcp_iam_roles=gcp_iam_roles,
            internal_aws_amis=internal_aws_amis,
            internal_aws_service_catalog_portfolios=internal_aws_service_catalog_portfolios,
            ous=ous,
            owner_user_groups=owner_user_groups,
            owner_users=owner_users,
            projects=projects,
            service_control_policies=service_control_policies,
        )


        cloud_rule_full.additional_properties = d
        return cloud_rule_full

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
