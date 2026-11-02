from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AWSAccessConfig")



@_attrs_define
class AWSAccessConfig:
    """ AWSAccessConfig represents the system settings for accessing AWS

        Attributes:
            aws_access_key_creation_enabled (bool | None | Unset): Indicates whether AWS access key creation is enabled or
                not Example: True.
            aws_access_key_lifespan (int | Unset): The lifespan of AWS access keys Example: -1.
            aws_access_key_notify_expiring (bool | None | Unset): Indicates whether a notification should be sent when AWS
                access keys are expiring or not
            aws_access_key_when_to_notify_expiring (int | Unset): When to send a notification for expiring AWS access keys
                Example: 10.
            aws_iam_role_prefix (str | Unset): Prefix used for creating AWS IAM roles Example: companyPrefix.
            aws_iam_role_prefix_enabled (bool | None | Unset): Indicates whether the AWS IAM role prefix is enabled or not
            aws_multi_session_enabled (bool | None | Unset): Indicates whether multi-session is enabled or not Example:
                True.
            aws_session_duration (int | Unset): The duration for AWS sessions Example: 59.
            aws_temporary_credentials_duration (int | Unset): The duration of AWS temporary credentials Example: 59.
            aws_temporary_credentials_enabled (bool | None | Unset): Indicates whether AWS temporary credentials are enabled
                or not Example: True.
            is_source_identity_enabled (bool | None | Unset): Indicates whether source identity is enabled or not Example:
                True.
     """

    aws_access_key_creation_enabled: bool | None | Unset = UNSET
    aws_access_key_lifespan: int | Unset = UNSET
    aws_access_key_notify_expiring: bool | None | Unset = UNSET
    aws_access_key_when_to_notify_expiring: int | Unset = UNSET
    aws_iam_role_prefix: str | Unset = UNSET
    aws_iam_role_prefix_enabled: bool | None | Unset = UNSET
    aws_multi_session_enabled: bool | None | Unset = UNSET
    aws_session_duration: int | Unset = UNSET
    aws_temporary_credentials_duration: int | Unset = UNSET
    aws_temporary_credentials_enabled: bool | None | Unset = UNSET
    is_source_identity_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        aws_access_key_creation_enabled: bool | None | Unset
        if isinstance(self.aws_access_key_creation_enabled, Unset):
            aws_access_key_creation_enabled = UNSET
        else:
            aws_access_key_creation_enabled = self.aws_access_key_creation_enabled

        aws_access_key_lifespan = self.aws_access_key_lifespan

        aws_access_key_notify_expiring: bool | None | Unset
        if isinstance(self.aws_access_key_notify_expiring, Unset):
            aws_access_key_notify_expiring = UNSET
        else:
            aws_access_key_notify_expiring = self.aws_access_key_notify_expiring

        aws_access_key_when_to_notify_expiring = self.aws_access_key_when_to_notify_expiring

        aws_iam_role_prefix = self.aws_iam_role_prefix

        aws_iam_role_prefix_enabled: bool | None | Unset
        if isinstance(self.aws_iam_role_prefix_enabled, Unset):
            aws_iam_role_prefix_enabled = UNSET
        else:
            aws_iam_role_prefix_enabled = self.aws_iam_role_prefix_enabled

        aws_multi_session_enabled: bool | None | Unset
        if isinstance(self.aws_multi_session_enabled, Unset):
            aws_multi_session_enabled = UNSET
        else:
            aws_multi_session_enabled = self.aws_multi_session_enabled

        aws_session_duration = self.aws_session_duration

        aws_temporary_credentials_duration = self.aws_temporary_credentials_duration

        aws_temporary_credentials_enabled: bool | None | Unset
        if isinstance(self.aws_temporary_credentials_enabled, Unset):
            aws_temporary_credentials_enabled = UNSET
        else:
            aws_temporary_credentials_enabled = self.aws_temporary_credentials_enabled

        is_source_identity_enabled: bool | None | Unset
        if isinstance(self.is_source_identity_enabled, Unset):
            is_source_identity_enabled = UNSET
        else:
            is_source_identity_enabled = self.is_source_identity_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws_access_key_creation_enabled is not UNSET:
            field_dict["aws_access_key_creation_enabled"] = aws_access_key_creation_enabled
        if aws_access_key_lifespan is not UNSET:
            field_dict["aws_access_key_lifespan"] = aws_access_key_lifespan
        if aws_access_key_notify_expiring is not UNSET:
            field_dict["aws_access_key_notify_expiring"] = aws_access_key_notify_expiring
        if aws_access_key_when_to_notify_expiring is not UNSET:
            field_dict["aws_access_key_when_to_notify_expiring"] = aws_access_key_when_to_notify_expiring
        if aws_iam_role_prefix is not UNSET:
            field_dict["aws_iam_role_prefix"] = aws_iam_role_prefix
        if aws_iam_role_prefix_enabled is not UNSET:
            field_dict["aws_iam_role_prefix_enabled"] = aws_iam_role_prefix_enabled
        if aws_multi_session_enabled is not UNSET:
            field_dict["aws_multi_session_enabled"] = aws_multi_session_enabled
        if aws_session_duration is not UNSET:
            field_dict["aws_session_duration"] = aws_session_duration
        if aws_temporary_credentials_duration is not UNSET:
            field_dict["aws_temporary_credentials_duration"] = aws_temporary_credentials_duration
        if aws_temporary_credentials_enabled is not UNSET:
            field_dict["aws_temporary_credentials_enabled"] = aws_temporary_credentials_enabled
        if is_source_identity_enabled is not UNSET:
            field_dict["is_source_identity_enabled"] = is_source_identity_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_aws_access_key_creation_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_access_key_creation_enabled = _parse_aws_access_key_creation_enabled(d.pop("aws_access_key_creation_enabled", UNSET))


        aws_access_key_lifespan = d.pop("aws_access_key_lifespan", UNSET)

        def _parse_aws_access_key_notify_expiring(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_access_key_notify_expiring = _parse_aws_access_key_notify_expiring(d.pop("aws_access_key_notify_expiring", UNSET))


        aws_access_key_when_to_notify_expiring = d.pop("aws_access_key_when_to_notify_expiring", UNSET)

        aws_iam_role_prefix = d.pop("aws_iam_role_prefix", UNSET)

        def _parse_aws_iam_role_prefix_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_iam_role_prefix_enabled = _parse_aws_iam_role_prefix_enabled(d.pop("aws_iam_role_prefix_enabled", UNSET))


        def _parse_aws_multi_session_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_multi_session_enabled = _parse_aws_multi_session_enabled(d.pop("aws_multi_session_enabled", UNSET))


        aws_session_duration = d.pop("aws_session_duration", UNSET)

        aws_temporary_credentials_duration = d.pop("aws_temporary_credentials_duration", UNSET)

        def _parse_aws_temporary_credentials_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_temporary_credentials_enabled = _parse_aws_temporary_credentials_enabled(d.pop("aws_temporary_credentials_enabled", UNSET))


        def _parse_is_source_identity_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_source_identity_enabled = _parse_is_source_identity_enabled(d.pop("is_source_identity_enabled", UNSET))


        aws_access_config = cls(
            aws_access_key_creation_enabled=aws_access_key_creation_enabled,
            aws_access_key_lifespan=aws_access_key_lifespan,
            aws_access_key_notify_expiring=aws_access_key_notify_expiring,
            aws_access_key_when_to_notify_expiring=aws_access_key_when_to_notify_expiring,
            aws_iam_role_prefix=aws_iam_role_prefix,
            aws_iam_role_prefix_enabled=aws_iam_role_prefix_enabled,
            aws_multi_session_enabled=aws_multi_session_enabled,
            aws_session_duration=aws_session_duration,
            aws_temporary_credentials_duration=aws_temporary_credentials_duration,
            aws_temporary_credentials_enabled=aws_temporary_credentials_enabled,
            is_source_identity_enabled=is_source_identity_enabled,
        )


        aws_access_config.additional_properties = d
        return aws_access_config

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
