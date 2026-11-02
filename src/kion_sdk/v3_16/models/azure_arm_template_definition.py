from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzureARMTemplateDefinition")



@_attrs_define
class AzureARMTemplateDefinition:
    r""" AzureARMTemplateDefinition is the data for an ARM template in cloudtamer

        Attributes:
            created_by (str | Unset): The original creator of the ARM template. Will be either 'System' or 'User'. Example:
                "System".
            ct_managed (bool | None | Unset): Managed signifies that this arm template is managed by cloudtamer.io
            deployment_mode (int | Unset): Deployment mode for the ARM template. References a database ID. Example: 1.
            description (str | Unset): A short description of the ARM template Example: "Deploys a VM".
            id (int | Unset): The ID of the ARM template definition Example: 1.
            name (str | Unset): The name of the ARM template definition in cloudtamer.io Example: "My ARM Template".
            resource_group_name (str | Unset): Name of the resource group where these resources should be deployed Example:
                "sample-rg".
            resource_group_region_id (int | None | Unset): Database ID of the Azure Region where the ARM template should be
                deployed Example: 1.
            template (str | Unset): Contents of the template to be deployed. Example: {\"$schema\":\"https://schema.manageme
                nt.azure.com/schemas/2015-01-01/deploymentTemplate.json#\",\"contentVersion\":\"1.0.0.0\",\"resources\":...}.
            template_parameters (str | Unset): Parameters to fill for the template. Should be the contents of the
                "properties" attribute on the traditional payload. Example: {\"parameterOne\":{\"value\":\"...\"}, ...}.
            version (int | Unset): The version of the ARM template definition in cloudtamer.io
                Note: This value is managed by cloudtamer and cannot be changed by a user. Example: 1.
     """

    created_by: str | Unset = UNSET
    ct_managed: bool | None | Unset = UNSET
    deployment_mode: int | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    resource_group_name: str | Unset = UNSET
    resource_group_region_id: int | None | Unset = UNSET
    template: str | Unset = UNSET
    template_parameters: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_by = self.created_by

        ct_managed: bool | None | Unset
        if isinstance(self.ct_managed, Unset):
            ct_managed = UNSET
        else:
            ct_managed = self.ct_managed

        deployment_mode = self.deployment_mode

        description = self.description

        id = self.id

        name = self.name

        resource_group_name = self.resource_group_name

        resource_group_region_id: int | None | Unset
        if isinstance(self.resource_group_region_id, Unset):
            resource_group_region_id = UNSET
        else:
            resource_group_region_id = self.resource_group_region_id

        template = self.template

        template_parameters = self.template_parameters

        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if ct_managed is not UNSET:
            field_dict["ct_managed"] = ct_managed
        if deployment_mode is not UNSET:
            field_dict["deployment_mode"] = deployment_mode
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if resource_group_name is not UNSET:
            field_dict["resource_group_name"] = resource_group_name
        if resource_group_region_id is not UNSET:
            field_dict["resource_group_region_id"] = resource_group_region_id
        if template is not UNSET:
            field_dict["template"] = template
        if template_parameters is not UNSET:
            field_dict["template_parameters"] = template_parameters
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_by = d.pop("created_by", UNSET)

        def _parse_ct_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ct_managed = _parse_ct_managed(d.pop("ct_managed", UNSET))


        deployment_mode = d.pop("deployment_mode", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        resource_group_name = d.pop("resource_group_name", UNSET)

        def _parse_resource_group_region_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        resource_group_region_id = _parse_resource_group_region_id(d.pop("resource_group_region_id", UNSET))


        template = d.pop("template", UNSET)

        template_parameters = d.pop("template_parameters", UNSET)

        version = d.pop("version", UNSET)

        azure_arm_template_definition = cls(
            created_by=created_by,
            ct_managed=ct_managed,
            deployment_mode=deployment_mode,
            description=description,
            id=id,
            name=name,
            resource_group_name=resource_group_name,
            resource_group_region_id=resource_group_region_id,
            template=template,
            template_parameters=template_parameters,
            version=version,
        )


        azure_arm_template_definition.additional_properties = d
        return azure_arm_template_definition

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
