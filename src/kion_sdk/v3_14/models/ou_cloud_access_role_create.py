from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.aws_session_tag import AWSSessionTag





T = TypeVar("T", bound="OUCloudAccessRoleCreate")



@_attrs_define
class OUCloudAccessRoleCreate:
    """ OUCloudAccessRoleCreate defines the json structure for the ou cloud access role's create action.

        Attributes:
            name (str): Name of the cloud access role in the application. Example: Read Only.
            ou_id (int | None): ID of the OU where the cloud access role is attached. Example: 1.
            aws_iam_path (str | Unset): Text of the IAM Path in AWS to be stored in AWS. Example: /iam-path/.
            aws_iam_permissions_boundary (int | None | Unset): ID of the AWS IAM policy to be used as a permissions boundary
                for this role. Example: 1.
            aws_iam_policies (list[int] | None | Unset): IDs of the AWS IAM policies attached to this role. Example: [1, 2].
            aws_iam_role_name (str | Unset): AWS IAM role name corresponding to the cloud access role. Example: read-only.
            aws_session_tags (list[AWSSessionTag] | None | Unset): AWS Session Tags used in this role when accessing the AWS
                console.
            azure_role_definitions (list[int] | None | Unset): IDs of the Azure Role Definitions attached to this role.
                Example: [1, 2].
            gcp_iam_roles (list[int] | None | Unset): IDs of the GCP IAM roles attached to this role. Example: [1, 2].
            long_term_access_keys (bool | None | Unset): If long term access is true, users of this cloud access role can
                generate aws long-term access keys.
                Will default to false if not set. Example: True.
            short_term_access_keys (bool | None | Unset): If short term access is true, users of this cloud access role can
                generate short-term access keys.
                Will default to false if not set. Example: True.
            user_group_ids (list[int] | None | Unset): IDs of the user groups allowed to use this role to access the AWS
                console. Example: [1, 2].
            user_ids (list[int] | None | Unset): IDs of the users allowed to use this role to access the AWS console.
                Example: [1, 2].
            web_access (bool | None | Unset): If web access is true, users of this cloud access role can log into the
                console
                Will default to false if not set. Example: True.
     """

    name: str
    ou_id: int | None
    aws_iam_path: str | Unset = UNSET
    aws_iam_permissions_boundary: int | None | Unset = UNSET
    aws_iam_policies: list[int] | None | Unset = UNSET
    aws_iam_role_name: str | Unset = UNSET
    aws_session_tags: list[AWSSessionTag] | None | Unset = UNSET
    azure_role_definitions: list[int] | None | Unset = UNSET
    gcp_iam_roles: list[int] | None | Unset = UNSET
    long_term_access_keys: bool | None | Unset = UNSET
    short_term_access_keys: bool | None | Unset = UNSET
    user_group_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    web_access: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aws_session_tag import AWSSessionTag
        name = self.name

        ou_id: int | None
        ou_id = self.ou_id

        aws_iam_path = self.aws_iam_path

        aws_iam_permissions_boundary: int | None | Unset
        if isinstance(self.aws_iam_permissions_boundary, Unset):
            aws_iam_permissions_boundary = UNSET
        else:
            aws_iam_permissions_boundary = self.aws_iam_permissions_boundary

        aws_iam_policies: list[int] | None | Unset
        if isinstance(self.aws_iam_policies, Unset):
            aws_iam_policies = UNSET
        elif isinstance(self.aws_iam_policies, list):
            aws_iam_policies = self.aws_iam_policies


        else:
            aws_iam_policies = self.aws_iam_policies

        aws_iam_role_name = self.aws_iam_role_name

        aws_session_tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.aws_session_tags, Unset):
            aws_session_tags = UNSET
        elif isinstance(self.aws_session_tags, list):
            aws_session_tags = []
            for aws_session_tags_type_0_item_data in self.aws_session_tags:
                aws_session_tags_type_0_item = aws_session_tags_type_0_item_data.to_dict()
                aws_session_tags.append(aws_session_tags_type_0_item)


        else:
            aws_session_tags = self.aws_session_tags

        azure_role_definitions: list[int] | None | Unset
        if isinstance(self.azure_role_definitions, Unset):
            azure_role_definitions = UNSET
        elif isinstance(self.azure_role_definitions, list):
            azure_role_definitions = self.azure_role_definitions


        else:
            azure_role_definitions = self.azure_role_definitions

        gcp_iam_roles: list[int] | None | Unset
        if isinstance(self.gcp_iam_roles, Unset):
            gcp_iam_roles = UNSET
        elif isinstance(self.gcp_iam_roles, list):
            gcp_iam_roles = self.gcp_iam_roles


        else:
            gcp_iam_roles = self.gcp_iam_roles

        long_term_access_keys: bool | None | Unset
        if isinstance(self.long_term_access_keys, Unset):
            long_term_access_keys = UNSET
        else:
            long_term_access_keys = self.long_term_access_keys

        short_term_access_keys: bool | None | Unset
        if isinstance(self.short_term_access_keys, Unset):
            short_term_access_keys = UNSET
        else:
            short_term_access_keys = self.short_term_access_keys

        user_group_ids: list[int] | None | Unset
        if isinstance(self.user_group_ids, Unset):
            user_group_ids = UNSET
        elif isinstance(self.user_group_ids, list):
            user_group_ids = self.user_group_ids


        else:
            user_group_ids = self.user_group_ids

        user_ids: list[int] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids


        else:
            user_ids = self.user_ids

        web_access: bool | None | Unset
        if isinstance(self.web_access, Unset):
            web_access = UNSET
        else:
            web_access = self.web_access


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "ou_id": ou_id,
        })
        if aws_iam_path is not UNSET:
            field_dict["aws_iam_path"] = aws_iam_path
        if aws_iam_permissions_boundary is not UNSET:
            field_dict["aws_iam_permissions_boundary"] = aws_iam_permissions_boundary
        if aws_iam_policies is not UNSET:
            field_dict["aws_iam_policies"] = aws_iam_policies
        if aws_iam_role_name is not UNSET:
            field_dict["aws_iam_role_name"] = aws_iam_role_name
        if aws_session_tags is not UNSET:
            field_dict["aws_session_tags"] = aws_session_tags
        if azure_role_definitions is not UNSET:
            field_dict["azure_role_definitions"] = azure_role_definitions
        if gcp_iam_roles is not UNSET:
            field_dict["gcp_iam_roles"] = gcp_iam_roles
        if long_term_access_keys is not UNSET:
            field_dict["long_term_access_keys"] = long_term_access_keys
        if short_term_access_keys is not UNSET:
            field_dict["short_term_access_keys"] = short_term_access_keys
        if user_group_ids is not UNSET:
            field_dict["user_group_ids"] = user_group_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids
        if web_access is not UNSET:
            field_dict["web_access"] = web_access

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_session_tag import AWSSessionTag
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_ou_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ou_id = _parse_ou_id(d.pop("ou_id"))


        aws_iam_path = d.pop("aws_iam_path", UNSET)

        def _parse_aws_iam_permissions_boundary(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        aws_iam_permissions_boundary = _parse_aws_iam_permissions_boundary(d.pop("aws_iam_permissions_boundary", UNSET))


        def _parse_aws_iam_policies(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_iam_policies_type_0 = cast(list[int], data)

                return aws_iam_policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        aws_iam_policies = _parse_aws_iam_policies(d.pop("aws_iam_policies", UNSET))


        aws_iam_role_name = d.pop("aws_iam_role_name", UNSET)

        def _parse_aws_session_tags(data: object) -> list[AWSSessionTag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_session_tags_type_0 = []
                _aws_session_tags_type_0 = data
                for aws_session_tags_type_0_item_data in (_aws_session_tags_type_0):
                    aws_session_tags_type_0_item = AWSSessionTag.from_dict(aws_session_tags_type_0_item_data)



                    aws_session_tags_type_0.append(aws_session_tags_type_0_item)

                return aws_session_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AWSSessionTag] | None | Unset, data)

        aws_session_tags = _parse_aws_session_tags(d.pop("aws_session_tags", UNSET))


        def _parse_azure_role_definitions(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                azure_role_definitions_type_0 = cast(list[int], data)

                return azure_role_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        azure_role_definitions = _parse_azure_role_definitions(d.pop("azure_role_definitions", UNSET))


        def _parse_gcp_iam_roles(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gcp_iam_roles_type_0 = cast(list[int], data)

                return gcp_iam_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        gcp_iam_roles = _parse_gcp_iam_roles(d.pop("gcp_iam_roles", UNSET))


        def _parse_long_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        long_term_access_keys = _parse_long_term_access_keys(d.pop("long_term_access_keys", UNSET))


        def _parse_short_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        short_term_access_keys = _parse_short_term_access_keys(d.pop("short_term_access_keys", UNSET))


        def _parse_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_group_ids_type_0 = cast(list[int], data)

                return user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_group_ids = _parse_user_group_ids(d.pop("user_group_ids", UNSET))


        def _parse_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[int], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))


        def _parse_web_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        web_access = _parse_web_access(d.pop("web_access", UNSET))


        ou_cloud_access_role_create = cls(
            name=name,
            ou_id=ou_id,
            aws_iam_path=aws_iam_path,
            aws_iam_permissions_boundary=aws_iam_permissions_boundary,
            aws_iam_policies=aws_iam_policies,
            aws_iam_role_name=aws_iam_role_name,
            aws_session_tags=aws_session_tags,
            azure_role_definitions=azure_role_definitions,
            gcp_iam_roles=gcp_iam_roles,
            long_term_access_keys=long_term_access_keys,
            short_term_access_keys=short_term_access_keys,
            user_group_ids=user_group_ids,
            user_ids=user_ids,
            web_access=web_access,
        )


        ou_cloud_access_role_create.additional_properties = d
        return ou_cloud_access_role_create

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
