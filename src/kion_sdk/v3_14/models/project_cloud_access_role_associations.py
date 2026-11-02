from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectCloudAccessRoleAssociations")



@_attrs_define
class ProjectCloudAccessRoleAssociations:
    """ ProjectCloudAccessRoleAssociations defines the json structure for the project cloud access role's create action.

        Attributes:
            account_ids (list[int] | None | Unset): Account IDs contains a list of accounts in this project that will be
                accessible via this cloud access role. Example: [101, 102].
            aws_iam_permissions_boundary (int | None | Unset): ID of the AWS IAM policy to be used as a permissions boundary
                for this role. Example: 1.
            aws_iam_policies (list[int] | None | Unset): IDs of the AWS IAM policies attached to this role. Example: [1, 2].
            azure_role_definitions (list[int] | None | Unset): IDs of the Azure Role Definitions attached to this role.
                Example: [1, 2].
            gcp_iam_roles (list[int] | None | Unset): IDs of the Google Cloud IAM roles attached to this role. Example: [1,
                2].
            user_group_ids (list[int] | None | Unset): IDs of the user groups allowed to use this role to access the AWS
                console. Example: [1, 2].
            user_ids (list[int] | None | Unset): IDs of the users allowed to use this role to access the AWS console.
                Example: [1, 2].
     """

    account_ids: list[int] | None | Unset = UNSET
    aws_iam_permissions_boundary: int | None | Unset = UNSET
    aws_iam_policies: list[int] | None | Unset = UNSET
    azure_role_definitions: list[int] | None | Unset = UNSET
    gcp_iam_roles: list[int] | None | Unset = UNSET
    user_group_ids: list[int] | None | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_ids: list[int] | None | Unset
        if isinstance(self.account_ids, Unset):
            account_ids = UNSET
        elif isinstance(self.account_ids, list):
            account_ids = self.account_ids


        else:
            account_ids = self.account_ids

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_ids is not UNSET:
            field_dict["account_ids"] = account_ids
        if aws_iam_permissions_boundary is not UNSET:
            field_dict["aws_iam_permissions_boundary"] = aws_iam_permissions_boundary
        if aws_iam_policies is not UNSET:
            field_dict["aws_iam_policies"] = aws_iam_policies
        if azure_role_definitions is not UNSET:
            field_dict["azure_role_definitions"] = azure_role_definitions
        if gcp_iam_roles is not UNSET:
            field_dict["gcp_iam_roles"] = gcp_iam_roles
        if user_group_ids is not UNSET:
            field_dict["user_group_ids"] = user_group_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = cast(list[int], data)

                return account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        account_ids = _parse_account_ids(d.pop("account_ids", UNSET))


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


        project_cloud_access_role_associations = cls(
            account_ids=account_ids,
            aws_iam_permissions_boundary=aws_iam_permissions_boundary,
            aws_iam_policies=aws_iam_policies,
            azure_role_definitions=azure_role_definitions,
            gcp_iam_roles=gcp_iam_roles,
            user_group_ids=user_group_ids,
            user_ids=user_ids,
        )


        project_cloud_access_role_associations.additional_properties = d
        return project_cloud_access_role_associations

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
