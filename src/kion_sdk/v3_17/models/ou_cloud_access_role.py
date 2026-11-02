from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OUCloudAccessRole")



@_attrs_define
class OUCloudAccessRole:
    """ OUCloudAccessRole defines a cloud access role for an ou.

        Attributes:
            aws_create_instance_profile (bool | None | Unset): Whether an instance profile is created for the role.
                Populated for
                non-User CARs (omitted for User CARs).
            aws_iam_path (str | Unset): Text of the IAM Path in AWS to be stored in AWS. Example: /iam-path/.
            aws_iam_role_name (str | Unset): AWS IAM role name corresponding to the cloud access role. Example: read-only.
            aws_iam_role_trust_policy (str | Unset): Raw AWS IAM role trust policy JSON. Set for Custom Trust CARs (2) from
                the
                request and for Service CARs (4) from aws_trusted_services. Empty for User
                (1) and Account (3) CARs, whose policies awsiamsync builds without storing. Example:
                {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"*"},"Action":"sts:AssumeRole"}]}.
            aws_partition (str | Unset): AWS partition the role is synced to. Populated for non-User CARs. Example: aws.
            aws_trusted_account_numbers (list[str] | None | Unset): For Account CARs (type 3), the list of AWS account IDs
                that are
                trusted to assume this role. Currently only a single entry is stored. Example: ['123456789012'].
            aws_trusted_services (list[str] | None | Unset): For Service CARs (type 4), the AWS service principals allowed
                to assume
                this role. Example: ['lambda.amazonaws.com'].
            cloud_access_role_type_id (int | None | Unset): Type of the cloud access role:
                1 = User (default, multi-cloud, assumable by Kion users/groups)
                2 = Custom Trust (AWS-only, custom trust policy)
                3 = Account (AWS-only, trusts another AWS account)
                4 = Service (AWS-only, trusts one or more AWS services) Example: 1.
            id (int | Unset): ID of the record in the application. Example: 1.
            long_term_access_keys (bool | None | Unset): If long term key access is true, users of this cloud access role
                can generate aws long-term access keys. Example: True.
            name (str | Unset): Name of the cloud access role in the application. Example: Read Only.
            ou_id (int | None | Unset): ID of the ou where the cloud access role is defined. Example: 1.
            short_term_access_keys (bool | None | Unset): If short term key access is true, users of this cloud access role
                can generate short-term access keys. Example: True.
            web_access (bool | None | Unset): If web access is true, users of this cloud access role can log into the
                console Example: True.
     """

    aws_create_instance_profile: bool | None | Unset = UNSET
    aws_iam_path: str | Unset = UNSET
    aws_iam_role_name: str | Unset = UNSET
    aws_iam_role_trust_policy: str | Unset = UNSET
    aws_partition: str | Unset = UNSET
    aws_trusted_account_numbers: list[str] | None | Unset = UNSET
    aws_trusted_services: list[str] | None | Unset = UNSET
    cloud_access_role_type_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    long_term_access_keys: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    short_term_access_keys: bool | None | Unset = UNSET
    web_access: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        aws_create_instance_profile: bool | None | Unset
        if isinstance(self.aws_create_instance_profile, Unset):
            aws_create_instance_profile = UNSET
        else:
            aws_create_instance_profile = self.aws_create_instance_profile

        aws_iam_path = self.aws_iam_path

        aws_iam_role_name = self.aws_iam_role_name

        aws_iam_role_trust_policy = self.aws_iam_role_trust_policy

        aws_partition = self.aws_partition

        aws_trusted_account_numbers: list[str] | None | Unset
        if isinstance(self.aws_trusted_account_numbers, Unset):
            aws_trusted_account_numbers = UNSET
        elif isinstance(self.aws_trusted_account_numbers, list):
            aws_trusted_account_numbers = self.aws_trusted_account_numbers


        else:
            aws_trusted_account_numbers = self.aws_trusted_account_numbers

        aws_trusted_services: list[str] | None | Unset
        if isinstance(self.aws_trusted_services, Unset):
            aws_trusted_services = UNSET
        elif isinstance(self.aws_trusted_services, list):
            aws_trusted_services = self.aws_trusted_services


        else:
            aws_trusted_services = self.aws_trusted_services

        cloud_access_role_type_id: int | None | Unset
        if isinstance(self.cloud_access_role_type_id, Unset):
            cloud_access_role_type_id = UNSET
        else:
            cloud_access_role_type_id = self.cloud_access_role_type_id

        id = self.id

        long_term_access_keys: bool | None | Unset
        if isinstance(self.long_term_access_keys, Unset):
            long_term_access_keys = UNSET
        else:
            long_term_access_keys = self.long_term_access_keys

        name = self.name

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id

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
        if aws_create_instance_profile is not UNSET:
            field_dict["aws_create_instance_profile"] = aws_create_instance_profile
        if aws_iam_path is not UNSET:
            field_dict["aws_iam_path"] = aws_iam_path
        if aws_iam_role_name is not UNSET:
            field_dict["aws_iam_role_name"] = aws_iam_role_name
        if aws_iam_role_trust_policy is not UNSET:
            field_dict["aws_iam_role_trust_policy"] = aws_iam_role_trust_policy
        if aws_partition is not UNSET:
            field_dict["aws_partition"] = aws_partition
        if aws_trusted_account_numbers is not UNSET:
            field_dict["aws_trusted_account_numbers"] = aws_trusted_account_numbers
        if aws_trusted_services is not UNSET:
            field_dict["aws_trusted_services"] = aws_trusted_services
        if cloud_access_role_type_id is not UNSET:
            field_dict["cloud_access_role_type_id"] = cloud_access_role_type_id
        if id is not UNSET:
            field_dict["id"] = id
        if long_term_access_keys is not UNSET:
            field_dict["long_term_access_keys"] = long_term_access_keys
        if name is not UNSET:
            field_dict["name"] = name
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if short_term_access_keys is not UNSET:
            field_dict["short_term_access_keys"] = short_term_access_keys
        if web_access is not UNSET:
            field_dict["web_access"] = web_access

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_aws_create_instance_profile(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_create_instance_profile = _parse_aws_create_instance_profile(d.pop("aws_create_instance_profile", UNSET))


        aws_iam_path = d.pop("aws_iam_path", UNSET)

        aws_iam_role_name = d.pop("aws_iam_role_name", UNSET)

        aws_iam_role_trust_policy = d.pop("aws_iam_role_trust_policy", UNSET)

        aws_partition = d.pop("aws_partition", UNSET)

        def _parse_aws_trusted_account_numbers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_trusted_account_numbers_type_0 = cast(list[str], data)

                return aws_trusted_account_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        aws_trusted_account_numbers = _parse_aws_trusted_account_numbers(d.pop("aws_trusted_account_numbers", UNSET))


        def _parse_aws_trusted_services(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_trusted_services_type_0 = cast(list[str], data)

                return aws_trusted_services_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        aws_trusted_services = _parse_aws_trusted_services(d.pop("aws_trusted_services", UNSET))


        def _parse_cloud_access_role_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_access_role_type_id = _parse_cloud_access_role_type_id(d.pop("cloud_access_role_type_id", UNSET))


        id = d.pop("id", UNSET)

        def _parse_long_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        long_term_access_keys = _parse_long_term_access_keys(d.pop("long_term_access_keys", UNSET))


        name = d.pop("name", UNSET)

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


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


        ou_cloud_access_role = cls(
            aws_create_instance_profile=aws_create_instance_profile,
            aws_iam_path=aws_iam_path,
            aws_iam_role_name=aws_iam_role_name,
            aws_iam_role_trust_policy=aws_iam_role_trust_policy,
            aws_partition=aws_partition,
            aws_trusted_account_numbers=aws_trusted_account_numbers,
            aws_trusted_services=aws_trusted_services,
            cloud_access_role_type_id=cloud_access_role_type_id,
            id=id,
            long_term_access_keys=long_term_access_keys,
            name=name,
            ou_id=ou_id,
            short_term_access_keys=short_term_access_keys,
            web_access=web_access,
        )


        ou_cloud_access_role.additional_properties = d
        return ou_cloud_access_role

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
