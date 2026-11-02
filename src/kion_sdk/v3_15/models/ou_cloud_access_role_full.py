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
  from ..models.azure_role import AzureRole
  from ..models.azure_role_with_cloud_rule import AzureRoleWithCloudRule
  from ..models.gcp_role import GCPRole
  from ..models.gcp_role_with_cloud_rule import GCPRoleWithCloudRule
  from ..models.iam_policy import IAMPolicy
  from ..models.iam_policy_with_cloud_rule import IAMPolicyWithCloudRule
  from ..models.ou import OU
  from ..models.ou_cloud_access_role import OUCloudAccessRole
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="OUCloudAccessRoleFull")



@_attrs_define
class OUCloudAccessRoleFull:
    """ OUCloudAccessRoleFull defines the json structure for the ou cloud access role's create action.

        Attributes:
            aws_iam_permissions_boundary (IAMPolicy | None | Unset):
            aws_iam_policies (list[IAMPolicy] | None | Unset):
            aws_session_tags (list[AWSSessionTag] | None | Unset):
            azure_role_definitions (list[AzureRole] | None | Unset):
            gcp_iam_roles (list[GCPRole] | None | Unset):
            inherited_aws_iam_policies (list[IAMPolicyWithCloudRule] | None | Unset):
            inherited_azure_role_definitions (list[AzureRoleWithCloudRule] | None | Unset):
            inherited_gcp_iam_roles (list[GCPRoleWithCloudRule] | None | Unset):
            ou (OU | Unset): OU defines an OU.
            ou_cloud_access_role (OUCloudAccessRole | Unset): OUCloudAccessRole defines a cloud access role for an ou.
            user_groups (list[UGroup] | None | Unset):
            users (list[User] | None | Unset):
     """

    aws_iam_permissions_boundary: IAMPolicy | None | Unset = UNSET
    aws_iam_policies: list[IAMPolicy] | None | Unset = UNSET
    aws_session_tags: list[AWSSessionTag] | None | Unset = UNSET
    azure_role_definitions: list[AzureRole] | None | Unset = UNSET
    gcp_iam_roles: list[GCPRole] | None | Unset = UNSET
    inherited_aws_iam_policies: list[IAMPolicyWithCloudRule] | None | Unset = UNSET
    inherited_azure_role_definitions: list[AzureRoleWithCloudRule] | None | Unset = UNSET
    inherited_gcp_iam_roles: list[GCPRoleWithCloudRule] | None | Unset = UNSET
    ou: OU | Unset = UNSET
    ou_cloud_access_role: OUCloudAccessRole | Unset = UNSET
    user_groups: list[UGroup] | None | Unset = UNSET
    users: list[User] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aws_session_tag import AWSSessionTag
        from ..models.azure_role import AzureRole
        from ..models.azure_role_with_cloud_rule import AzureRoleWithCloudRule
        from ..models.gcp_role import GCPRole
        from ..models.gcp_role_with_cloud_rule import GCPRoleWithCloudRule
        from ..models.iam_policy import IAMPolicy
        from ..models.iam_policy_with_cloud_rule import IAMPolicyWithCloudRule
        from ..models.ou import OU
        from ..models.ou_cloud_access_role import OUCloudAccessRole
        from ..models.u_group import UGroup
        from ..models.user import User
        aws_iam_permissions_boundary: dict[str, Any] | None | Unset
        if isinstance(self.aws_iam_permissions_boundary, Unset):
            aws_iam_permissions_boundary = UNSET
        elif isinstance(self.aws_iam_permissions_boundary, IAMPolicy):
            aws_iam_permissions_boundary = self.aws_iam_permissions_boundary.to_dict()
        else:
            aws_iam_permissions_boundary = self.aws_iam_permissions_boundary

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

        inherited_aws_iam_policies: list[dict[str, Any]] | None | Unset
        if isinstance(self.inherited_aws_iam_policies, Unset):
            inherited_aws_iam_policies = UNSET
        elif isinstance(self.inherited_aws_iam_policies, list):
            inherited_aws_iam_policies = []
            for inherited_aws_iam_policies_type_0_item_data in self.inherited_aws_iam_policies:
                inherited_aws_iam_policies_type_0_item = inherited_aws_iam_policies_type_0_item_data.to_dict()
                inherited_aws_iam_policies.append(inherited_aws_iam_policies_type_0_item)


        else:
            inherited_aws_iam_policies = self.inherited_aws_iam_policies

        inherited_azure_role_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.inherited_azure_role_definitions, Unset):
            inherited_azure_role_definitions = UNSET
        elif isinstance(self.inherited_azure_role_definitions, list):
            inherited_azure_role_definitions = []
            for inherited_azure_role_definitions_type_0_item_data in self.inherited_azure_role_definitions:
                inherited_azure_role_definitions_type_0_item = inherited_azure_role_definitions_type_0_item_data.to_dict()
                inherited_azure_role_definitions.append(inherited_azure_role_definitions_type_0_item)


        else:
            inherited_azure_role_definitions = self.inherited_azure_role_definitions

        inherited_gcp_iam_roles: list[dict[str, Any]] | None | Unset
        if isinstance(self.inherited_gcp_iam_roles, Unset):
            inherited_gcp_iam_roles = UNSET
        elif isinstance(self.inherited_gcp_iam_roles, list):
            inherited_gcp_iam_roles = []
            for inherited_gcp_iam_roles_type_0_item_data in self.inherited_gcp_iam_roles:
                inherited_gcp_iam_roles_type_0_item = inherited_gcp_iam_roles_type_0_item_data.to_dict()
                inherited_gcp_iam_roles.append(inherited_gcp_iam_roles_type_0_item)


        else:
            inherited_gcp_iam_roles = self.inherited_gcp_iam_roles

        ou: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ou, Unset):
            ou = self.ou.to_dict()

        ou_cloud_access_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ou_cloud_access_role, Unset):
            ou_cloud_access_role = self.ou_cloud_access_role.to_dict()

        user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.user_groups, Unset):
            user_groups = UNSET
        elif isinstance(self.user_groups, list):
            user_groups = []
            for user_groups_type_0_item_data in self.user_groups:
                user_groups_type_0_item = user_groups_type_0_item_data.to_dict()
                user_groups.append(user_groups_type_0_item)


        else:
            user_groups = self.user_groups

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)


        else:
            users = self.users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws_iam_permissions_boundary is not UNSET:
            field_dict["aws_iam_permissions_boundary"] = aws_iam_permissions_boundary
        if aws_iam_policies is not UNSET:
            field_dict["aws_iam_policies"] = aws_iam_policies
        if aws_session_tags is not UNSET:
            field_dict["aws_session_tags"] = aws_session_tags
        if azure_role_definitions is not UNSET:
            field_dict["azure_role_definitions"] = azure_role_definitions
        if gcp_iam_roles is not UNSET:
            field_dict["gcp_iam_roles"] = gcp_iam_roles
        if inherited_aws_iam_policies is not UNSET:
            field_dict["inherited_aws_iam_policies"] = inherited_aws_iam_policies
        if inherited_azure_role_definitions is not UNSET:
            field_dict["inherited_azure_role_definitions"] = inherited_azure_role_definitions
        if inherited_gcp_iam_roles is not UNSET:
            field_dict["inherited_gcp_iam_roles"] = inherited_gcp_iam_roles
        if ou is not UNSET:
            field_dict["ou"] = ou
        if ou_cloud_access_role is not UNSET:
            field_dict["ou_cloud_access_role"] = ou_cloud_access_role
        if user_groups is not UNSET:
            field_dict["user_groups"] = user_groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_session_tag import AWSSessionTag
        from ..models.azure_role import AzureRole
        from ..models.azure_role_with_cloud_rule import AzureRoleWithCloudRule
        from ..models.gcp_role import GCPRole
        from ..models.gcp_role_with_cloud_rule import GCPRoleWithCloudRule
        from ..models.iam_policy import IAMPolicy
        from ..models.iam_policy_with_cloud_rule import IAMPolicyWithCloudRule
        from ..models.ou import OU
        from ..models.ou_cloud_access_role import OUCloudAccessRole
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        def _parse_aws_iam_permissions_boundary(data: object) -> IAMPolicy | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                aws_iam_permissions_boundary_type_1 = IAMPolicy.from_dict(data)



                return aws_iam_permissions_boundary_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IAMPolicy | None | Unset, data)

        aws_iam_permissions_boundary = _parse_aws_iam_permissions_boundary(d.pop("aws_iam_permissions_boundary", UNSET))


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


        def _parse_inherited_aws_iam_policies(data: object) -> list[IAMPolicyWithCloudRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inherited_aws_iam_policies_type_0 = []
                _inherited_aws_iam_policies_type_0 = data
                for inherited_aws_iam_policies_type_0_item_data in (_inherited_aws_iam_policies_type_0):
                    inherited_aws_iam_policies_type_0_item = IAMPolicyWithCloudRule.from_dict(inherited_aws_iam_policies_type_0_item_data)



                    inherited_aws_iam_policies_type_0.append(inherited_aws_iam_policies_type_0_item)

                return inherited_aws_iam_policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IAMPolicyWithCloudRule] | None | Unset, data)

        inherited_aws_iam_policies = _parse_inherited_aws_iam_policies(d.pop("inherited_aws_iam_policies", UNSET))


        def _parse_inherited_azure_role_definitions(data: object) -> list[AzureRoleWithCloudRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inherited_azure_role_definitions_type_0 = []
                _inherited_azure_role_definitions_type_0 = data
                for inherited_azure_role_definitions_type_0_item_data in (_inherited_azure_role_definitions_type_0):
                    inherited_azure_role_definitions_type_0_item = AzureRoleWithCloudRule.from_dict(inherited_azure_role_definitions_type_0_item_data)



                    inherited_azure_role_definitions_type_0.append(inherited_azure_role_definitions_type_0_item)

                return inherited_azure_role_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AzureRoleWithCloudRule] | None | Unset, data)

        inherited_azure_role_definitions = _parse_inherited_azure_role_definitions(d.pop("inherited_azure_role_definitions", UNSET))


        def _parse_inherited_gcp_iam_roles(data: object) -> list[GCPRoleWithCloudRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inherited_gcp_iam_roles_type_0 = []
                _inherited_gcp_iam_roles_type_0 = data
                for inherited_gcp_iam_roles_type_0_item_data in (_inherited_gcp_iam_roles_type_0):
                    inherited_gcp_iam_roles_type_0_item = GCPRoleWithCloudRule.from_dict(inherited_gcp_iam_roles_type_0_item_data)



                    inherited_gcp_iam_roles_type_0.append(inherited_gcp_iam_roles_type_0_item)

                return inherited_gcp_iam_roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GCPRoleWithCloudRule] | None | Unset, data)

        inherited_gcp_iam_roles = _parse_inherited_gcp_iam_roles(d.pop("inherited_gcp_iam_roles", UNSET))


        _ou = d.pop("ou", UNSET)
        ou: OU | Unset
        if isinstance(_ou,  Unset):
            ou = UNSET
        else:
            ou = OU.from_dict(_ou)




        _ou_cloud_access_role = d.pop("ou_cloud_access_role", UNSET)
        ou_cloud_access_role: OUCloudAccessRole | Unset
        if isinstance(_ou_cloud_access_role,  Unset):
            ou_cloud_access_role = UNSET
        else:
            ou_cloud_access_role = OUCloudAccessRole.from_dict(_ou_cloud_access_role)




        def _parse_user_groups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_groups_type_0 = []
                _user_groups_type_0 = data
                for user_groups_type_0_item_data in (_user_groups_type_0):
                    user_groups_type_0_item = UGroup.from_dict(user_groups_type_0_item_data)



                    user_groups_type_0.append(user_groups_type_0_item)

                return user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        user_groups = _parse_user_groups(d.pop("user_groups", UNSET))


        def _parse_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in (_users_type_0):
                    users_type_0_item = User.from_dict(users_type_0_item_data)



                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))


        ou_cloud_access_role_full = cls(
            aws_iam_permissions_boundary=aws_iam_permissions_boundary,
            aws_iam_policies=aws_iam_policies,
            aws_session_tags=aws_session_tags,
            azure_role_definitions=azure_role_definitions,
            gcp_iam_roles=gcp_iam_roles,
            inherited_aws_iam_policies=inherited_aws_iam_policies,
            inherited_azure_role_definitions=inherited_azure_role_definitions,
            inherited_gcp_iam_roles=inherited_gcp_iam_roles,
            ou=ou,
            ou_cloud_access_role=ou_cloud_access_role,
            user_groups=user_groups,
            users=users,
        )


        ou_cloud_access_role_full.additional_properties = d
        return ou_cloud_access_role_full

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
