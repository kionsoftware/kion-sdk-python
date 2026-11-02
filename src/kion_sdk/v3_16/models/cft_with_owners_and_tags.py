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
  from ..models.cft import CFT
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="CFTWithOwnersAndTags")



@_attrs_define
class CFTWithOwnersAndTags:
    """ CFTWithOwnersAndTags defines the owners of a CloudFormation template.

        Attributes:
            cft (CFT | Unset): CFT defines a CloudFormation template.
            owner_user_groups (list[UGroup] | None | Unset): List of user groups that own the CloudFormation template.
            owner_users (list[User] | None | Unset): List of users that own the CloudFormation template.
            tags (list[AWSStackTag] | None | Unset): Stack Tags used in this role when accessing the AWS console.
     """

    cft: CFT | Unset = UNSET
    owner_user_groups: list[UGroup] | None | Unset = UNSET
    owner_users: list[User] | None | Unset = UNSET
    tags: list[AWSStackTag] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aws_stack_tag import AWSStackTag
        from ..models.cft import CFT
        from ..models.u_group import UGroup
        from ..models.user import User
        cft: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cft, Unset):
            cft = self.cft.to_dict()

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cft is not UNSET:
            field_dict["cft"] = cft
        if owner_user_groups is not UNSET:
            field_dict["owner_user_groups"] = owner_user_groups
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_stack_tag import AWSStackTag
        from ..models.cft import CFT
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        _cft = d.pop("cft", UNSET)
        cft: CFT | Unset
        if isinstance(_cft,  Unset):
            cft = UNSET
        else:
            cft = CFT.from_dict(_cft)




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


        cft_with_owners_and_tags = cls(
            cft=cft,
            owner_user_groups=owner_user_groups,
            owner_users=owner_users,
            tags=tags,
        )


        cft_with_owners_and_tags.additional_properties = d
        return cft_with_owners_and_tags

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
