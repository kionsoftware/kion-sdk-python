from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AzureARMTemplateDefinitionUpdate")



@_attrs_define
class AzureARMTemplateDefinitionUpdate:
    r""" AzureARMTemplateDefinitionUpdate defines an Azure ARM template definition update.

        Attributes:
            deployment_mode (int): Deployment mode for the ARM template.
                Valid values are either 1 ("incremental") or 2 ("complete") Example: 1.
            name (str): The name of the ARM template definition in cloudtamer.io Example: "My ARM Template".
            template (str): Contents of the ARM template to be deployed. Example: {\"$schema\":\"https://schema.management.a
                zure.com/schemas/2015-01-01/deploymentTemplate.json#\",\"contentVersion\":\"1.0.0.0\",\"resources\":...}.
            description (str | Unset): A short description of the ARM template Example: "Deploys a VM".
            template_parameters (str | Unset): Parameters to fill for the template. Should be the contents of the
                "properties" attribute on the traditional payload. Example: {\"parameterOne\":{\"value\":\"...\"}, ...}.
     """

    deployment_mode: int
    name: str
    template: str
    description: str | Unset = UNSET
    template_parameters: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deployment_mode = self.deployment_mode

        name = self.name

        template = self.template

        description = self.description

        template_parameters = self.template_parameters


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "deployment_mode": deployment_mode,
            "name": name,
            "template": template,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if template_parameters is not UNSET:
            field_dict["template_parameters"] = template_parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deployment_mode = d.pop("deployment_mode")

        name = d.pop("name")

        template = d.pop("template")

        description = d.pop("description", UNSET)

        template_parameters = d.pop("template_parameters", UNSET)

        azure_arm_template_definition_update = cls(
            deployment_mode=deployment_mode,
            name=name,
            template=template,
            description=description,
            template_parameters=template_parameters,
        )


        azure_arm_template_definition_update.additional_properties = d
        return azure_arm_template_definition_update

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
