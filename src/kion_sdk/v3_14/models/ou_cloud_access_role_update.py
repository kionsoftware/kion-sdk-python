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





T = TypeVar("T", bound="OUCloudAccessRoleUpdate")



@_attrs_define
class OUCloudAccessRoleUpdate:
    """ OUCloudAccessRoleUpdate defines an updatable cloud access role for an ou.

        Attributes:
            aws_iam_permissions_boundary (int | None | Unset): ID of the AWS IAM policy to be used as a permissions boundary
                for this role. Example: 1.
            aws_session_tags (list[AWSSessionTag] | None | Unset): AWS Session Tags used in this role when accessing the AWS
                console.
            long_term_access_keys (bool | None | Unset): If long term key access is true, users of this cloud access role
                can generate aws long-term access keys. Example: True.
            name (str | Unset): Name of the cloud access role in the application. Example: Read Only.
            short_term_access_keys (bool | None | Unset): If short term key access is true, users of this cloud access role
                can generate short-term access keys. Example: True.
            web_access (bool | None | Unset): If web access is true, users of this cloud access role can log into the
                console Example: True.
     """

    aws_iam_permissions_boundary: int | None | Unset = UNSET
    aws_session_tags: list[AWSSessionTag] | None | Unset = UNSET
    long_term_access_keys: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    short_term_access_keys: bool | None | Unset = UNSET
    web_access: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aws_session_tag import AWSSessionTag
        aws_iam_permissions_boundary: int | None | Unset
        if isinstance(self.aws_iam_permissions_boundary, Unset):
            aws_iam_permissions_boundary = UNSET
        else:
            aws_iam_permissions_boundary = self.aws_iam_permissions_boundary

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

        long_term_access_keys: bool | None | Unset
        if isinstance(self.long_term_access_keys, Unset):
            long_term_access_keys = UNSET
        else:
            long_term_access_keys = self.long_term_access_keys

        name = self.name

        short_term_access_keys: bool | None | Unset
        if isinstance(self.short_term_access_keys, Unset):
            short_term_access_keys = UNSET
        else:
            short_term_access_keys = self.short_term_access_keys

        web_access: bool | None | Unset
        if isinstance(self.web_access, Unset):
            web_access = UNSET
        else:
            web_access = self.web_access


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws_iam_permissions_boundary is not UNSET:
            field_dict["aws_iam_permissions_boundary"] = aws_iam_permissions_boundary
        if aws_session_tags is not UNSET:
            field_dict["aws_session_tags"] = aws_session_tags
        if long_term_access_keys is not UNSET:
            field_dict["long_term_access_keys"] = long_term_access_keys
        if name is not UNSET:
            field_dict["name"] = name
        if short_term_access_keys is not UNSET:
            field_dict["short_term_access_keys"] = short_term_access_keys
        if web_access is not UNSET:
            field_dict["web_access"] = web_access

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_session_tag import AWSSessionTag
        d = dict(src_dict)
        def _parse_aws_iam_permissions_boundary(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        aws_iam_permissions_boundary = _parse_aws_iam_permissions_boundary(d.pop("aws_iam_permissions_boundary", UNSET))


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


        def _parse_long_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        long_term_access_keys = _parse_long_term_access_keys(d.pop("long_term_access_keys", UNSET))


        name = d.pop("name", UNSET)

        def _parse_short_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        short_term_access_keys = _parse_short_term_access_keys(d.pop("short_term_access_keys", UNSET))


        def _parse_web_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        web_access = _parse_web_access(d.pop("web_access", UNSET))


        ou_cloud_access_role_update = cls(
            aws_iam_permissions_boundary=aws_iam_permissions_boundary,
            aws_session_tags=aws_session_tags,
            long_term_access_keys=long_term_access_keys,
            name=name,
            short_term_access_keys=short_term_access_keys,
            web_access=web_access,
        )


        ou_cloud_access_role_update.additional_properties = d
        return ou_cloud_access_role_update

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
