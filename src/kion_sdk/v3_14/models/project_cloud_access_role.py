from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.null_time import NullTime





T = TypeVar("T", bound="ProjectCloudAccessRole")



@_attrs_define
class ProjectCloudAccessRole:
    """ ProjectCloudAccessRole defines a cloud access role for a project.

        Attributes:
            apply_to_all_accounts (bool | None | Unset): If apply all accounts is true, this cloud access role will be
                applied to all accounts under the project.
                This will only be for accounts that match the given CSP type Example: True.
            aws_iam_path (str | Unset): Text of the IAM Path in AWS to be stored in AWS. Example: /iam-path/.
            aws_iam_role_name (str | Unset): AWS IAM role name corresponding to the cloud access role. Example: read-only.
            created_at (NullTime | Unset): NullTime represents a time.Time that may be NULL.
            deleted_at (None | NullTime | Unset):
            future_accounts (bool | None | Unset): If future accounts is true, this cloud access role will be added to any
                account that is added to this project.
                This will only be for new accounts that match the given CSP type Example: True.
            id (int | Unset): ID of the record in the application. Example: 1.
            long_term_access_keys (bool | None | Unset): If long term key access is true, users of this cloud access role
                can generate aws long-term access keys. Example: True.
            name (str | Unset): Name of the cloud access role in the application. Example: Read Only.
            project_id (int | None | Unset): ID of the project where the cloud access role is attached. Example: 1.
            short_term_access_keys (bool | None | Unset): If short term key access is true, users of this cloud access role
                can generate short-term access keys. Example: True.
            updated_at (None | NullTime | Unset):
            web_access (bool | None | Unset): If web access is true, users of this cloud access role can log into the
                console Example: True.
     """

    apply_to_all_accounts: bool | None | Unset = UNSET
    aws_iam_path: str | Unset = UNSET
    aws_iam_role_name: str | Unset = UNSET
    created_at: NullTime | Unset = UNSET
    deleted_at: None | NullTime | Unset = UNSET
    future_accounts: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    long_term_access_keys: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    short_term_access_keys: bool | None | Unset = UNSET
    updated_at: None | NullTime | Unset = UNSET
    web_access: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_time import NullTime
        apply_to_all_accounts: bool | None | Unset
        if isinstance(self.apply_to_all_accounts, Unset):
            apply_to_all_accounts = UNSET
        else:
            apply_to_all_accounts = self.apply_to_all_accounts

        aws_iam_path = self.aws_iam_path

        aws_iam_role_name = self.aws_iam_role_name

        created_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        deleted_at: dict[str, Any] | None | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, NullTime):
            deleted_at = self.deleted_at.to_dict()
        else:
            deleted_at = self.deleted_at

        future_accounts: bool | None | Unset
        if isinstance(self.future_accounts, Unset):
            future_accounts = UNSET
        else:
            future_accounts = self.future_accounts

        id = self.id

        long_term_access_keys: bool | None | Unset
        if isinstance(self.long_term_access_keys, Unset):
            long_term_access_keys = UNSET
        else:
            long_term_access_keys = self.long_term_access_keys

        name = self.name

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        short_term_access_keys: bool | None | Unset
        if isinstance(self.short_term_access_keys, Unset):
            short_term_access_keys = UNSET
        else:
            short_term_access_keys = self.short_term_access_keys

        updated_at: dict[str, Any] | None | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, NullTime):
            updated_at = self.updated_at.to_dict()
        else:
            updated_at = self.updated_at

        web_access: bool | None | Unset
        if isinstance(self.web_access, Unset):
            web_access = UNSET
        else:
            web_access = self.web_access


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if apply_to_all_accounts is not UNSET:
            field_dict["apply_to_all_accounts"] = apply_to_all_accounts
        if aws_iam_path is not UNSET:
            field_dict["aws_iam_path"] = aws_iam_path
        if aws_iam_role_name is not UNSET:
            field_dict["aws_iam_role_name"] = aws_iam_role_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if future_accounts is not UNSET:
            field_dict["future_accounts"] = future_accounts
        if id is not UNSET:
            field_dict["id"] = id
        if long_term_access_keys is not UNSET:
            field_dict["long_term_access_keys"] = long_term_access_keys
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if short_term_access_keys is not UNSET:
            field_dict["short_term_access_keys"] = short_term_access_keys
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if web_access is not UNSET:
            field_dict["web_access"] = web_access

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_time import NullTime
        d = dict(src_dict)
        def _parse_apply_to_all_accounts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        apply_to_all_accounts = _parse_apply_to_all_accounts(d.pop("apply_to_all_accounts", UNSET))


        aws_iam_path = d.pop("aws_iam_path", UNSET)

        aws_iam_role_name = d.pop("aws_iam_role_name", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: NullTime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = NullTime.from_dict(_created_at)




        def _parse_deleted_at(data: object) -> None | NullTime | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_at_type_1 = NullTime.from_dict(data)



                return deleted_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NullTime | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        def _parse_future_accounts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        future_accounts = _parse_future_accounts(d.pop("future_accounts", UNSET))


        id = d.pop("id", UNSET)

        def _parse_long_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        long_term_access_keys = _parse_long_term_access_keys(d.pop("long_term_access_keys", UNSET))


        name = d.pop("name", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        def _parse_short_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        short_term_access_keys = _parse_short_term_access_keys(d.pop("short_term_access_keys", UNSET))


        def _parse_updated_at(data: object) -> None | NullTime | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_at_type_1 = NullTime.from_dict(data)



                return updated_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NullTime | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_web_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        web_access = _parse_web_access(d.pop("web_access", UNSET))


        project_cloud_access_role = cls(
            apply_to_all_accounts=apply_to_all_accounts,
            aws_iam_path=aws_iam_path,
            aws_iam_role_name=aws_iam_role_name,
            created_at=created_at,
            deleted_at=deleted_at,
            future_accounts=future_accounts,
            id=id,
            long_term_access_keys=long_term_access_keys,
            name=name,
            project_id=project_id,
            short_term_access_keys=short_term_access_keys,
            updated_at=updated_at,
            web_access=web_access,
        )


        project_cloud_access_role.additional_properties = d
        return project_cloud_access_role

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
