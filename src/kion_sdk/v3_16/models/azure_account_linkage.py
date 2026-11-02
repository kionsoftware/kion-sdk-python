from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzureAccountLinkage")



@_attrs_define
class AzureAccountLinkage:
    """ AzureAccountLinkage represents an association between a CloudTamer user and an Azure Tenant.

        Attributes:
            azure_domain (str | Unset): Azure domain to which the user is associated Example: othercompany.onmicrosoft.com.
            azure_object_id (str | Unset): Azure ID of the linked user Example: 11111111-2222-3333-4444-555555555555.
            azure_username (str | Unset): User's username in Azure Example: johndoe@mycompany.onmicrosoft.com.
            created_at (str | Unset): Creation time of the linkage Example: 2019-08-28T00:00:00.000Z.
            delete_finalized_at (str | Unset): Deletion finalization time (i.e. when the linked account was removed from all
                managed azure groups) Example: 2019-08-28T00:00:00.000Z.
            deleted_at (None | str | Unset): Deletion time of the linkage Example: 2019-08-28T00:00:00.000Z.
            id (int | Unset): ID of the account linkage. Example: 1.
            payer_id (int | None | Unset): ID of the payer to which this user is associated Example: 1.
            updated_at (None | str | Unset): Update time of the linkage Example: 2019-08-28T00:00:00.000Z.
            user_id (int | None | Unset): ID of the user for this association Example: 1.
     """

    azure_domain: str | Unset = UNSET
    azure_object_id: str | Unset = UNSET
    azure_username: str | Unset = UNSET
    created_at: str | Unset = UNSET
    delete_finalized_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    id: int | Unset = UNSET
    payer_id: int | None | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        azure_domain = self.azure_domain

        azure_object_id = self.azure_object_id

        azure_username = self.azure_username

        created_at = self.created_at

        delete_finalized_at = self.delete_finalized_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        id = self.id

        payer_id: int | None | Unset
        if isinstance(self.payer_id, Unset):
            payer_id = UNSET
        else:
            payer_id = self.payer_id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if azure_domain is not UNSET:
            field_dict["azure_domain"] = azure_domain
        if azure_object_id is not UNSET:
            field_dict["azure_object_id"] = azure_object_id
        if azure_username is not UNSET:
            field_dict["azure_username"] = azure_username
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if delete_finalized_at is not UNSET:
            field_dict["delete_finalized_at"] = delete_finalized_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if id is not UNSET:
            field_dict["id"] = id
        if payer_id is not UNSET:
            field_dict["payer_id"] = payer_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        azure_domain = d.pop("azure_domain", UNSET)

        azure_object_id = d.pop("azure_object_id", UNSET)

        azure_username = d.pop("azure_username", UNSET)

        created_at = d.pop("created_at", UNSET)

        delete_finalized_at = d.pop("delete_finalized_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        id = d.pop("id", UNSET)

        def _parse_payer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payer_id = _parse_payer_id(d.pop("payer_id", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        azure_account_linkage = cls(
            azure_domain=azure_domain,
            azure_object_id=azure_object_id,
            azure_username=azure_username,
            created_at=created_at,
            delete_finalized_at=delete_finalized_at,
            deleted_at=deleted_at,
            id=id,
            payer_id=payer_id,
            updated_at=updated_at,
            user_id=user_id,
        )


        azure_account_linkage.additional_properties = d
        return azure_account_linkage

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
