from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPAccountCacheNewGCPProject")



@_attrs_define
class GCPAccountCacheNewGCPProject:
    """ GCPAccountCacheNewGCPProject defines a payload for creating a new GCP Project.

        Attributes:
            display_name (str): DisplayName is the user-friendly name for a project Example: lab #3.
            payer_id (int | None): PayerID is the ID of the payer that should be attached to the project Example: 32.
            account_alias (str | Unset): Alias of the account in the application. Example: TP1.
            google_cloud_parent_name (str | Unset): ParentName is the fully qualified gcp resource identifier for the parent
                of the project Example: organizations/1026377682360.
            google_cloud_project_id (str | Unset): Google Cloud Project ID. Example: my-project.
     """

    display_name: str
    payer_id: int | None
    account_alias: str | Unset = UNSET
    google_cloud_parent_name: str | Unset = UNSET
    google_cloud_project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        payer_id: int | None
        payer_id = self.payer_id

        account_alias = self.account_alias

        google_cloud_parent_name = self.google_cloud_parent_name

        google_cloud_project_id = self.google_cloud_project_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "display_name": display_name,
            "payer_id": payer_id,
        })
        if account_alias is not UNSET:
            field_dict["account_alias"] = account_alias
        if google_cloud_parent_name is not UNSET:
            field_dict["google_cloud_parent_name"] = google_cloud_parent_name
        if google_cloud_project_id is not UNSET:
            field_dict["google_cloud_project_id"] = google_cloud_project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name")

        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        account_alias = d.pop("account_alias", UNSET)

        google_cloud_parent_name = d.pop("google_cloud_parent_name", UNSET)

        google_cloud_project_id = d.pop("google_cloud_project_id", UNSET)

        gcp_account_cache_new_gcp_project = cls(
            display_name=display_name,
            payer_id=payer_id,
            account_alias=account_alias,
            google_cloud_parent_name=google_cloud_parent_name,
            google_cloud_project_id=google_cloud_project_id,
        )


        gcp_account_cache_new_gcp_project.additional_properties = d
        return gcp_account_cache_new_gcp_project

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
