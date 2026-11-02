from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzureARMTemplateDefinitionCreate")



@_attrs_define
class AzureARMTemplateDefinitionCreate:
    r""" AzureARMTemplateDefinitionCreate defines an Azure ARM template definition creation.

        Attributes:
            deployment_mode (int): Deployment mode for the ARM template.
                Valid values are either 1 ("incremental") or 2 ("complete") Example: 1.
            name (str): The name of the ARM template definition in cloudtamer.io Example: "My ARM Template".
            resource_group_name (str): Name of the resource group where these resources should be deployed Example: "sample-
                rg".
            resource_group_region_id (int | None): Database ID of the Azure region where the ARM template should be deployed
                Example: 1.
            template (str): Contents of the ARM template to be deployed. Example: {\"$schema\":\"https://schema.management.a
                zure.com/schemas/2015-01-01/deploymentTemplate.json#\",\"contentVersion\":\"1.0.0.0\",\"resources\":...}.
            description (str | Unset): A short description of the ARM template Example: "Deploys a VM".
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the Azure ARM template. Is
                required if no user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the Azure ARM template. Is required if
                no group IDs are listed. Example: [1, 2].
            template_parameters (str | Unset): Parameters to fill for the template. Should be the contents of the
                "properties" attribute on the traditional payload. Example: {\"parameterOne\":{\"value\":\"...\"}, ...}.
     """

    deployment_mode: int
    name: str
    resource_group_name: str
    resource_group_region_id: int | None
    template: str
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    template_parameters: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deployment_mode = self.deployment_mode

        name = self.name

        resource_group_name = self.resource_group_name

        resource_group_region_id: int | None
        resource_group_region_id = self.resource_group_region_id

        template = self.template

        description = self.description

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids

        template_parameters = self.template_parameters


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "deployment_mode": deployment_mode,
            "name": name,
            "resource_group_name": resource_group_name,
            "resource_group_region_id": resource_group_region_id,
            "template": template,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if template_parameters is not UNSET:
            field_dict["template_parameters"] = template_parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deployment_mode = d.pop("deployment_mode")

        name = d.pop("name")

        resource_group_name = d.pop("resource_group_name")

        def _parse_resource_group_region_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        resource_group_region_id = _parse_resource_group_region_id(d.pop("resource_group_region_id"))


        template = d.pop("template")

        description = d.pop("description", UNSET)

        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        template_parameters = d.pop("template_parameters", UNSET)

        azure_arm_template_definition_create = cls(
            deployment_mode=deployment_mode,
            name=name,
            resource_group_name=resource_group_name,
            resource_group_region_id=resource_group_region_id,
            template=template,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            template_parameters=template_parameters,
        )


        azure_arm_template_definition_create.additional_properties = d
        return azure_arm_template_definition_create

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
