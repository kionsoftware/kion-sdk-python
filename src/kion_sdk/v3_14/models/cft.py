from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CFT")



@_attrs_define
class CFT:
    r""" CFT defines a CloudFormation template.

        Attributes:
            regions (list[str] | None): List of the AWS regions where the CloudFormation template applies. Example: ['us-
                east-1'].
            description (str | Unset): Description of the Cloudformation template in the application. Example: Sets up a
                production VPC..
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the Cloudformation template in the application. Example: Production-VPC.
            policy (str | Unset): Body of the CloudFormation template in JSON or YAML.
            region (str | Unset): DEPRECATED! USE THE regions FIELD.
                AWS region where the CloudFormation template applies. Example: us-east-1.
            sns_arns (str | Unset): List of comma separated AWS SNS ARNs that will trigger once the CFT is done applying.
                Example: "arn:aws:sns:us-east-2:123456789012:MyTopic".
            system_managed (bool | None | Unset): Managed signifies that this CloudFormation template is managed by Kion
            template_parameters (str | Unset): List of CloudFormation parameters in a JSON array. Example:
                [{\"ParameterKey\": \"Subnets\",\"ParameterValue\": \"6\"},{\"ParameterKey\"...].
            termination_protection (bool | None | Unset): Sets the termination protection status for this CFT.
     """

    regions: list[str] | None
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    policy: str | Unset = UNSET
    region: str | Unset = UNSET
    sns_arns: str | Unset = UNSET
    system_managed: bool | None | Unset = UNSET
    template_parameters: str | Unset = UNSET
    termination_protection: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        regions: list[str] | None
        if isinstance(self.regions, list):
            regions = self.regions


        else:
            regions = self.regions

        description = self.description

        id = self.id

        name = self.name

        policy = self.policy

        region = self.region

        sns_arns = self.sns_arns

        system_managed: bool | None | Unset
        if isinstance(self.system_managed, Unset):
            system_managed = UNSET
        else:
            system_managed = self.system_managed

        template_parameters = self.template_parameters

        termination_protection: bool | None | Unset
        if isinstance(self.termination_protection, Unset):
            termination_protection = UNSET
        else:
            termination_protection = self.termination_protection


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "regions": regions,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if policy is not UNSET:
            field_dict["policy"] = policy
        if region is not UNSET:
            field_dict["region"] = region
        if sns_arns is not UNSET:
            field_dict["sns_arns"] = sns_arns
        if system_managed is not UNSET:
            field_dict["system_managed"] = system_managed
        if template_parameters is not UNSET:
            field_dict["template_parameters"] = template_parameters
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_regions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                regions_type_0 = cast(list[str], data)

                return regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        regions = _parse_regions(d.pop("regions"))


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        policy = d.pop("policy", UNSET)

        region = d.pop("region", UNSET)

        sns_arns = d.pop("sns_arns", UNSET)

        def _parse_system_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed = _parse_system_managed(d.pop("system_managed", UNSET))


        template_parameters = d.pop("template_parameters", UNSET)

        def _parse_termination_protection(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        termination_protection = _parse_termination_protection(d.pop("termination_protection", UNSET))


        cft = cls(
            regions=regions,
            description=description,
            id=id,
            name=name,
            policy=policy,
            region=region,
            sns_arns=sns_arns,
            system_managed=system_managed,
            template_parameters=template_parameters,
            termination_protection=termination_protection,
        )


        cft.additional_properties = d
        return cft

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
