from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.aws_stack_tag import AWSStackTag





T = TypeVar("T", bound="CFTCreate")



@_attrs_define
class CFTCreate:
    r""" CFTCreate defines a CloudFormation template creation.

        Attributes:
            name (str): Name of the Cloudformation template in the application. Example: Production-VPC.
            policy (str): Body of the CloudFormation template in JSON or YAML. Example: {\"AWSTemplateFormatVersion\":
                \"2010-09-09\", \"Description\": \"Creates...}.
            regions (list[str] | None): List of the AWS regions where the CloudFormation template applies. Example: ['us-
                east-1'].
            description (str | Unset): Description of the Cloudformation template in the application. Example: Sets up a
                production VPC..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the CloudFormation template. Is
                required if no user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the CloudFormation template. Is
                required if no group IDs are listed. Example: [1, 2].
            region (str | Unset): DEPRECATED! USE THE regions FIELD.
                AWS region where the CloudFormation template applies. Example: us-east-1.
            sns_arns (str | Unset): List of comma separated AWS SNS ARNs that will trigger once the CFT is done applying.
                Example: "arn:aws:sns:us-east-2:123456789012:MyTopic".
            tags (list[AWSStackTag] | None | Unset): AWS Stack Tags used in this role when accessing the AWS console.
            template_parameters (str | Unset): List of CloudFormation parameters in a JSON array. Example:
                [{\"ParameterKey\": \"Subnets\",\"ParameterValue\": \"6\"},{\"ParameterKey\"...].
            termination_protection (bool | None | Unset): Sets the termination protection status for this CFT.
     """

    name: str
    policy: str
    regions: list[str] | None
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    region: str | Unset = UNSET
    sns_arns: str | Unset = UNSET
    tags: list[AWSStackTag] | None | Unset = UNSET
    template_parameters: str | Unset = UNSET
    termination_protection: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aws_stack_tag import AWSStackTag
        name = self.name

        policy = self.policy

        regions: list[str] | None
        if isinstance(self.regions, list):
            regions = self.regions


        else:
            regions = self.regions

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

        region = self.region

        sns_arns = self.sns_arns

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)


        else:
            tags = self.tags

        template_parameters = self.template_parameters

        termination_protection: bool | None | Unset
        if isinstance(self.termination_protection, Unset):
            termination_protection = UNSET
        else:
            termination_protection = self.termination_protection


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "policy": policy,
            "regions": regions,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if region is not UNSET:
            field_dict["region"] = region
        if sns_arns is not UNSET:
            field_dict["sns_arns"] = sns_arns
        if tags is not UNSET:
            field_dict["tags"] = tags
        if template_parameters is not UNSET:
            field_dict["template_parameters"] = template_parameters
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_stack_tag import AWSStackTag
        d = dict(src_dict)
        name = d.pop("name")

        policy = d.pop("policy")

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


        region = d.pop("region", UNSET)

        sns_arns = d.pop("sns_arns", UNSET)

        def _parse_tags(data: object) -> list[AWSStackTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in (_tags_type_0):
                    tags_type_0_item = AWSStackTag.from_dict(tags_type_0_item_data)



                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AWSStackTag] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


        template_parameters = d.pop("template_parameters", UNSET)

        def _parse_termination_protection(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        termination_protection = _parse_termination_protection(d.pop("termination_protection", UNSET))


        cft_create = cls(
            name=name,
            policy=policy,
            regions=regions,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            region=region,
            sns_arns=sns_arns,
            tags=tags,
            template_parameters=template_parameters,
            termination_protection=termination_protection,
        )


        cft_create.additional_properties = d
        return cft_create

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
