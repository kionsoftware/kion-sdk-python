from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPAccountCacheCreate")



@_attrs_define
class GCPAccountCacheCreate:
    """ GCPAccountCacheCreate defines a payload for a cached GCP project/account.

        Attributes:
            account_name (str): Name of the subscription in the application. Example: My Google Cloud Project.
            google_cloud_project_id (str): Google Cloud Project ID.
                Can be found in the project id field here: https://console.cloud.google.com/iam-admin/settings Example: my-
                project.
            payer_id (int | None): ID of the payer (aka Google Cloud Billing Account) Example: 1.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            account_type_id (int | None | Unset): The AccountTypeID is the corresponding account's type.
                Will default to 15 for GCP if not given. Default: 15. Example: 15.
            skip_access_checking (bool | None | Unset): When true, the application does not perform periodic access
                validation. Default is false.
     """

    account_name: str
    google_cloud_project_id: str
    payer_id: int | None
    account_alias: str | Unset = UNSET
    account_type_id: int | None | Unset = 15
    skip_access_checking: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        google_cloud_project_id = self.google_cloud_project_id

        payer_id: int | None
        payer_id = self.payer_id

        account_alias = self.account_alias

        account_type_id: int | None | Unset
        if isinstance(self.account_type_id, Unset):
            account_type_id = UNSET
        else:
            account_type_id = self.account_type_id

        skip_access_checking: bool | None | Unset
        if isinstance(self.skip_access_checking, Unset):
            skip_access_checking = UNSET
        else:
            skip_access_checking = self.skip_access_checking


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_name": account_name,
            "google_cloud_project_id": google_cloud_project_id,
            "payer_id": payer_id,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if account_type_id is not UNSET:
            field_dict["account_type_id"] = account_type_id
        if skip_access_checking is not UNSET:
            field_dict["skip_access_checking"] = skip_access_checking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("account_name")

        google_cloud_project_id = d.pop("google_cloud_project_id")

        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        account_alias = d.pop("account_alias", UNSET)

        def _parse_account_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_type_id = _parse_account_type_id(d.pop("account_type_id", UNSET))


        def _parse_skip_access_checking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_access_checking = _parse_skip_access_checking(d.pop("skip_access_checking", UNSET))


        gcp_account_cache_create = cls(
            account_name=account_name,
            google_cloud_project_id=google_cloud_project_id,
            payer_id=payer_id,
            account_alias=account_alias,
            account_type_id=account_type_id,
            skip_access_checking=skip_access_checking,
        )


        gcp_account_cache_create.additional_properties = d
        return gcp_account_cache_create

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
