from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_cloud_access_favorite_cloud_service_provider import UserCloudAccessFavoriteCloudServiceProvider
from ..types import UNSET, Unset






T = TypeVar("T", bound="UserCloudAccessFavorite")



@_attrs_define
class UserCloudAccessFavorite:
    """ 
        Attributes:
            access_type (str): AccessType represents how a cloud access role is used by the user
            account_number (str | Unset): Account number to bind alias to. Example: 12345.
            account_region (str | Unset): Account region that the CSP account is linked to Example: us-east-1.
            alias_name (str | Unset): Name of the alias. Example: development-admin.
            cloud_access_role_name (str | Unset): Name of cloud access role (OU or Project) for the alias Example:
                developer-role.
            cloud_service_provider (UserCloudAccessFavoriteCloudServiceProvider | Unset): Name of the CSP for this account.
                Example: aws.
     """

    access_type: str
    account_number: str | Unset = UNSET
    account_region: str | Unset = UNSET
    alias_name: str | Unset = UNSET
    cloud_access_role_name: str | Unset = UNSET
    cloud_service_provider: UserCloudAccessFavoriteCloudServiceProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_type = self.access_type

        account_number = self.account_number

        account_region = self.account_region

        alias_name = self.alias_name

        cloud_access_role_name = self.cloud_access_role_name

        cloud_service_provider: str | Unset = UNSET
        if not isinstance(self.cloud_service_provider, Unset):
            cloud_service_provider = self.cloud_service_provider.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "access_type": access_type,
        })
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if account_region is not UNSET:
            field_dict["account_region"] = account_region
        if alias_name is not UNSET:
            field_dict["alias_name"] = alias_name
        if cloud_access_role_name is not UNSET:
            field_dict["cloud_access_role_name"] = cloud_access_role_name
        if cloud_service_provider is not UNSET:
            field_dict["cloud_service_provider"] = cloud_service_provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_type = d.pop("access_type")

        account_number = d.pop("account_number", UNSET)

        account_region = d.pop("account_region", UNSET)

        alias_name = d.pop("alias_name", UNSET)

        cloud_access_role_name = d.pop("cloud_access_role_name", UNSET)

        _cloud_service_provider = d.pop("cloud_service_provider", UNSET)
        cloud_service_provider: UserCloudAccessFavoriteCloudServiceProvider | Unset
        if isinstance(_cloud_service_provider,  Unset):
            cloud_service_provider = UNSET
        else:
            cloud_service_provider = UserCloudAccessFavoriteCloudServiceProvider(_cloud_service_provider)




        user_cloud_access_favorite = cls(
            access_type=access_type,
            account_number=account_number,
            account_region=account_region,
            alias_name=alias_name,
            cloud_access_role_name=cloud_access_role_name,
            cloud_service_provider=cloud_service_provider,
        )


        user_cloud_access_favorite.additional_properties = d
        return user_cloud_access_favorite

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
