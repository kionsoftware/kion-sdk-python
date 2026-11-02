from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AppConfig")



@_attrs_define
class AppConfig:
    """ AppConfig defines an AppConfig.

        Attributes:
            all_users_see_ou_names (bool | None | Unset): Indicates whether all users can see the names of OU's in the
                organization chart. Example: True.
            allocation_mode (bool | None | Unset): Indicates if allocation mode is enabled in the application. Example:
                True.
            allow_custom_permission_schemes (bool | None | Unset): Indicates whether custom permission schemes are allowed
                or not. Example: True.
            app_api_key_creation_enabled (bool | None | Unset): Indicates if App API Key creation is enabled. Example: True.
            app_api_key_lifespan (int | Unset): Indicates the lifespan of App API Keys in days. Example: 2.
            app_api_key_limit (int | Unset): Indicates the max amount of App API Keys per user. Example: 2.
            aws_access_key_creation_enabled (bool | None | Unset): Indicates whether AWS access keys creation is enabled.
                Example: True.
            budget_mode (bool | None | Unset): Indicates if budget mode is enabled in the application Example: True.
            cloud_rule_group_ownership_only (bool | None | Unset): Indicates if cloud rules are restricted to User Group
                ownership only.
                Setting this to true will remove all users from cloud rules.
                This cannot be undone.
            cost_savings_allow_terminate (bool | None | Unset): Indicates whether resource termination is allowed in-app.
            cost_savings_enabled (bool | None | Unset): Indicates whether Cost Savings is enabled or not. Example: True.
            cost_savings_post_token_life_hours (int | Unset): Post token life (hours) for Cloud Custodian webhook actions to
                execute. Example: 1.
            default_org_chart_view (str | Unset): Defines the default organization chart view.

                oneOf: list, policy, compliance, financial, spend Example: policy.
            enforce_funding (bool | None | Unset): Indicates whether spend plans or budgets must be created on all projects.

                examples: true
            enforce_funding_sources (bool | None | Unset): Indicates whether every project should have a funding source.
                Example: True.
            event_driven_enabled (bool | None | Unset): Indicates whether event driven is enabled or not.
            reserved_instances_enabled (bool | None | Unset): Indicates whether reserved instances are enabled or not.
                Example: True.
            resource_inventory_enabled (bool | None | Unset): Indicates whether resource inventory is enabled or not.
                Example: True.
            smtp_enabled (bool | None | Unset): Indicates whether SMTP is enabled or not. Example: True.
            smtp_from (str | Unset): The SMTP from address. Example: do-not-reply@company.com.
            smtp_host (str | Unset): The SMTP host. Example: "email-smtp.us-east-1.amazonaws.com".
            smtp_password (str | Unset): The SMTP password. Example: password.
            smtp_port (int | Unset): The SMTP port. Example: 587.
            smtp_skip_verify (bool | None | Unset): Indicates if the app should skip SMTP verification.
            smtp_username (str | Unset): The SMTP username. Example: username.
            supported_aws_regions (list[str] | None | Unset): The list of supported AWS regions Example: ['us-east-1', 'us-
                west-1'].
     """

    all_users_see_ou_names: bool | None | Unset = UNSET
    allocation_mode: bool | None | Unset = UNSET
    allow_custom_permission_schemes: bool | None | Unset = UNSET
    app_api_key_creation_enabled: bool | None | Unset = UNSET
    app_api_key_lifespan: int | Unset = UNSET
    app_api_key_limit: int | Unset = UNSET
    aws_access_key_creation_enabled: bool | None | Unset = UNSET
    budget_mode: bool | None | Unset = UNSET
    cloud_rule_group_ownership_only: bool | None | Unset = UNSET
    cost_savings_allow_terminate: bool | None | Unset = UNSET
    cost_savings_enabled: bool | None | Unset = UNSET
    cost_savings_post_token_life_hours: int | Unset = UNSET
    default_org_chart_view: str | Unset = UNSET
    enforce_funding: bool | None | Unset = UNSET
    enforce_funding_sources: bool | None | Unset = UNSET
    event_driven_enabled: bool | None | Unset = UNSET
    reserved_instances_enabled: bool | None | Unset = UNSET
    resource_inventory_enabled: bool | None | Unset = UNSET
    smtp_enabled: bool | None | Unset = UNSET
    smtp_from: str | Unset = UNSET
    smtp_host: str | Unset = UNSET
    smtp_password: str | Unset = UNSET
    smtp_port: int | Unset = UNSET
    smtp_skip_verify: bool | None | Unset = UNSET
    smtp_username: str | Unset = UNSET
    supported_aws_regions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        all_users_see_ou_names: bool | None | Unset
        if isinstance(self.all_users_see_ou_names, Unset):
            all_users_see_ou_names = UNSET
        else:
            all_users_see_ou_names = self.all_users_see_ou_names

        allocation_mode: bool | None | Unset
        if isinstance(self.allocation_mode, Unset):
            allocation_mode = UNSET
        else:
            allocation_mode = self.allocation_mode

        allow_custom_permission_schemes: bool | None | Unset
        if isinstance(self.allow_custom_permission_schemes, Unset):
            allow_custom_permission_schemes = UNSET
        else:
            allow_custom_permission_schemes = self.allow_custom_permission_schemes

        app_api_key_creation_enabled: bool | None | Unset
        if isinstance(self.app_api_key_creation_enabled, Unset):
            app_api_key_creation_enabled = UNSET
        else:
            app_api_key_creation_enabled = self.app_api_key_creation_enabled

        app_api_key_lifespan = self.app_api_key_lifespan

        app_api_key_limit = self.app_api_key_limit

        aws_access_key_creation_enabled: bool | None | Unset
        if isinstance(self.aws_access_key_creation_enabled, Unset):
            aws_access_key_creation_enabled = UNSET
        else:
            aws_access_key_creation_enabled = self.aws_access_key_creation_enabled

        budget_mode: bool | None | Unset
        if isinstance(self.budget_mode, Unset):
            budget_mode = UNSET
        else:
            budget_mode = self.budget_mode

        cloud_rule_group_ownership_only: bool | None | Unset
        if isinstance(self.cloud_rule_group_ownership_only, Unset):
            cloud_rule_group_ownership_only = UNSET
        else:
            cloud_rule_group_ownership_only = self.cloud_rule_group_ownership_only

        cost_savings_allow_terminate: bool | None | Unset
        if isinstance(self.cost_savings_allow_terminate, Unset):
            cost_savings_allow_terminate = UNSET
        else:
            cost_savings_allow_terminate = self.cost_savings_allow_terminate

        cost_savings_enabled: bool | None | Unset
        if isinstance(self.cost_savings_enabled, Unset):
            cost_savings_enabled = UNSET
        else:
            cost_savings_enabled = self.cost_savings_enabled

        cost_savings_post_token_life_hours = self.cost_savings_post_token_life_hours

        default_org_chart_view = self.default_org_chart_view

        enforce_funding: bool | None | Unset
        if isinstance(self.enforce_funding, Unset):
            enforce_funding = UNSET
        else:
            enforce_funding = self.enforce_funding

        enforce_funding_sources: bool | None | Unset
        if isinstance(self.enforce_funding_sources, Unset):
            enforce_funding_sources = UNSET
        else:
            enforce_funding_sources = self.enforce_funding_sources

        event_driven_enabled: bool | None | Unset
        if isinstance(self.event_driven_enabled, Unset):
            event_driven_enabled = UNSET
        else:
            event_driven_enabled = self.event_driven_enabled

        reserved_instances_enabled: bool | None | Unset
        if isinstance(self.reserved_instances_enabled, Unset):
            reserved_instances_enabled = UNSET
        else:
            reserved_instances_enabled = self.reserved_instances_enabled

        resource_inventory_enabled: bool | None | Unset
        if isinstance(self.resource_inventory_enabled, Unset):
            resource_inventory_enabled = UNSET
        else:
            resource_inventory_enabled = self.resource_inventory_enabled

        smtp_enabled: bool | None | Unset
        if isinstance(self.smtp_enabled, Unset):
            smtp_enabled = UNSET
        else:
            smtp_enabled = self.smtp_enabled

        smtp_from = self.smtp_from

        smtp_host = self.smtp_host

        smtp_password = self.smtp_password

        smtp_port = self.smtp_port

        smtp_skip_verify: bool | None | Unset
        if isinstance(self.smtp_skip_verify, Unset):
            smtp_skip_verify = UNSET
        else:
            smtp_skip_verify = self.smtp_skip_verify

        smtp_username = self.smtp_username

        supported_aws_regions: list[str] | None | Unset
        if isinstance(self.supported_aws_regions, Unset):
            supported_aws_regions = UNSET
        elif isinstance(self.supported_aws_regions, list):
            supported_aws_regions = self.supported_aws_regions


        else:
            supported_aws_regions = self.supported_aws_regions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if all_users_see_ou_names is not UNSET:
            field_dict["all_users_see_ou_names"] = all_users_see_ou_names
        if allocation_mode is not UNSET:
            field_dict["allocation_mode"] = allocation_mode
        if allow_custom_permission_schemes is not UNSET:
            field_dict["allow_custom_permission_schemes"] = allow_custom_permission_schemes
        if app_api_key_creation_enabled is not UNSET:
            field_dict["app_api_key_creation_enabled"] = app_api_key_creation_enabled
        if app_api_key_lifespan is not UNSET:
            field_dict["app_api_key_lifespan"] = app_api_key_lifespan
        if app_api_key_limit is not UNSET:
            field_dict["app_api_key_limit"] = app_api_key_limit
        if aws_access_key_creation_enabled is not UNSET:
            field_dict["aws_access_key_creation_enabled"] = aws_access_key_creation_enabled
        if budget_mode is not UNSET:
            field_dict["budget_mode"] = budget_mode
        if cloud_rule_group_ownership_only is not UNSET:
            field_dict["cloud_rule_group_ownership_only"] = cloud_rule_group_ownership_only
        if cost_savings_allow_terminate is not UNSET:
            field_dict["cost_savings_allow_terminate"] = cost_savings_allow_terminate
        if cost_savings_enabled is not UNSET:
            field_dict["cost_savings_enabled"] = cost_savings_enabled
        if cost_savings_post_token_life_hours is not UNSET:
            field_dict["cost_savings_post_token_life_hours"] = cost_savings_post_token_life_hours
        if default_org_chart_view is not UNSET:
            field_dict["default_org_chart_view"] = default_org_chart_view
        if enforce_funding is not UNSET:
            field_dict["enforce_funding"] = enforce_funding
        if enforce_funding_sources is not UNSET:
            field_dict["enforce_funding_sources"] = enforce_funding_sources
        if event_driven_enabled is not UNSET:
            field_dict["event_driven_enabled"] = event_driven_enabled
        if reserved_instances_enabled is not UNSET:
            field_dict["reserved_instances_enabled"] = reserved_instances_enabled
        if resource_inventory_enabled is not UNSET:
            field_dict["resource_inventory_enabled"] = resource_inventory_enabled
        if smtp_enabled is not UNSET:
            field_dict["smtp_enabled"] = smtp_enabled
        if smtp_from is not UNSET:
            field_dict["smtp_from"] = smtp_from
        if smtp_host is not UNSET:
            field_dict["smtp_host"] = smtp_host
        if smtp_password is not UNSET:
            field_dict["smtp_password"] = smtp_password
        if smtp_port is not UNSET:
            field_dict["smtp_port"] = smtp_port
        if smtp_skip_verify is not UNSET:
            field_dict["smtp_skip_verify"] = smtp_skip_verify
        if smtp_username is not UNSET:
            field_dict["smtp_username"] = smtp_username
        if supported_aws_regions is not UNSET:
            field_dict["supported_aws_regions"] = supported_aws_regions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_all_users_see_ou_names(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        all_users_see_ou_names = _parse_all_users_see_ou_names(d.pop("all_users_see_ou_names", UNSET))


        def _parse_allocation_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allocation_mode = _parse_allocation_mode(d.pop("allocation_mode", UNSET))


        def _parse_allow_custom_permission_schemes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_custom_permission_schemes = _parse_allow_custom_permission_schemes(d.pop("allow_custom_permission_schemes", UNSET))


        def _parse_app_api_key_creation_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        app_api_key_creation_enabled = _parse_app_api_key_creation_enabled(d.pop("app_api_key_creation_enabled", UNSET))


        app_api_key_lifespan = d.pop("app_api_key_lifespan", UNSET)

        app_api_key_limit = d.pop("app_api_key_limit", UNSET)

        def _parse_aws_access_key_creation_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_access_key_creation_enabled = _parse_aws_access_key_creation_enabled(d.pop("aws_access_key_creation_enabled", UNSET))


        def _parse_budget_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        budget_mode = _parse_budget_mode(d.pop("budget_mode", UNSET))


        def _parse_cloud_rule_group_ownership_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cloud_rule_group_ownership_only = _parse_cloud_rule_group_ownership_only(d.pop("cloud_rule_group_ownership_only", UNSET))


        def _parse_cost_savings_allow_terminate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cost_savings_allow_terminate = _parse_cost_savings_allow_terminate(d.pop("cost_savings_allow_terminate", UNSET))


        def _parse_cost_savings_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cost_savings_enabled = _parse_cost_savings_enabled(d.pop("cost_savings_enabled", UNSET))


        cost_savings_post_token_life_hours = d.pop("cost_savings_post_token_life_hours", UNSET)

        default_org_chart_view = d.pop("default_org_chart_view", UNSET)

        def _parse_enforce_funding(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enforce_funding = _parse_enforce_funding(d.pop("enforce_funding", UNSET))


        def _parse_enforce_funding_sources(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enforce_funding_sources = _parse_enforce_funding_sources(d.pop("enforce_funding_sources", UNSET))


        def _parse_event_driven_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        event_driven_enabled = _parse_event_driven_enabled(d.pop("event_driven_enabled", UNSET))


        def _parse_reserved_instances_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reserved_instances_enabled = _parse_reserved_instances_enabled(d.pop("reserved_instances_enabled", UNSET))


        def _parse_resource_inventory_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resource_inventory_enabled = _parse_resource_inventory_enabled(d.pop("resource_inventory_enabled", UNSET))


        def _parse_smtp_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        smtp_enabled = _parse_smtp_enabled(d.pop("smtp_enabled", UNSET))


        smtp_from = d.pop("smtp_from", UNSET)

        smtp_host = d.pop("smtp_host", UNSET)

        smtp_password = d.pop("smtp_password", UNSET)

        smtp_port = d.pop("smtp_port", UNSET)

        def _parse_smtp_skip_verify(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        smtp_skip_verify = _parse_smtp_skip_verify(d.pop("smtp_skip_verify", UNSET))


        smtp_username = d.pop("smtp_username", UNSET)

        def _parse_supported_aws_regions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_aws_regions_type_0 = cast(list[str], data)

                return supported_aws_regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        supported_aws_regions = _parse_supported_aws_regions(d.pop("supported_aws_regions", UNSET))


        app_config = cls(
            all_users_see_ou_names=all_users_see_ou_names,
            allocation_mode=allocation_mode,
            allow_custom_permission_schemes=allow_custom_permission_schemes,
            app_api_key_creation_enabled=app_api_key_creation_enabled,
            app_api_key_lifespan=app_api_key_lifespan,
            app_api_key_limit=app_api_key_limit,
            aws_access_key_creation_enabled=aws_access_key_creation_enabled,
            budget_mode=budget_mode,
            cloud_rule_group_ownership_only=cloud_rule_group_ownership_only,
            cost_savings_allow_terminate=cost_savings_allow_terminate,
            cost_savings_enabled=cost_savings_enabled,
            cost_savings_post_token_life_hours=cost_savings_post_token_life_hours,
            default_org_chart_view=default_org_chart_view,
            enforce_funding=enforce_funding,
            enforce_funding_sources=enforce_funding_sources,
            event_driven_enabled=event_driven_enabled,
            reserved_instances_enabled=reserved_instances_enabled,
            resource_inventory_enabled=resource_inventory_enabled,
            smtp_enabled=smtp_enabled,
            smtp_from=smtp_from,
            smtp_host=smtp_host,
            smtp_password=smtp_password,
            smtp_port=smtp_port,
            smtp_skip_verify=smtp_skip_verify,
            smtp_username=smtp_username,
            supported_aws_regions=supported_aws_regions,
        )


        app_config.additional_properties = d
        return app_config

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
