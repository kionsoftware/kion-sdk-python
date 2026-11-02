from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GoogleAccountLinkage")



@_attrs_define
class GoogleAccountLinkage:
    """ GoogleAccountLinkage represents an association between a cloudtamer.io user and a Google Account.

        Attributes:
            delete_finalized_at (str | Unset): Deletion finalization time (i.e. when the linked account was removed from all
                managed IAM bindings) Example: 2019-08-28T00:00:00.000Z.
            deleted_at (None | str | Unset): Deletion time of the linkage Example: 2019-08-28T00:00:00.000Z.
            google_email (str | Unset): User's Google Email Example: johndoe@mycompany.onmicrosoft.com.
            id (int | Unset): ID of the account linkage. Example: 1.
            service_account_id (int | None | Unset): ID of the service account to which this user is associated. This is
                done since the service account represents access to
                a Google Cloud environment. Example: 1.
            service_account_name (str | Unset): Name of the service account to which this user is associated. This is done
                since the service account represents access to
                a Google Cloud environment. Example: Service Account Name.
            user_id (int | None | Unset): ID of the user for this association Example: 1.
     """

    delete_finalized_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    google_email: str | Unset = UNSET
    id: int | Unset = UNSET
    service_account_id: int | None | Unset = UNSET
    service_account_name: str | Unset = UNSET
    user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        delete_finalized_at = self.delete_finalized_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        google_email = self.google_email

        id = self.id

        service_account_id: int | None | Unset
        if isinstance(self.service_account_id, Unset):
            service_account_id = UNSET
        else:
            service_account_id = self.service_account_id

        service_account_name = self.service_account_name

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if delete_finalized_at is not UNSET:
            field_dict["delete_finalized_at"] = delete_finalized_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if google_email is not UNSET:
            field_dict["google_email"] = google_email
        if id is not UNSET:
            field_dict["id"] = id
        if service_account_id is not UNSET:
            field_dict["service_account_id"] = service_account_id
        if service_account_name is not UNSET:
            field_dict["service_account_name"] = service_account_name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_finalized_at = d.pop("delete_finalized_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        google_email = d.pop("google_email", UNSET)

        id = d.pop("id", UNSET)

        def _parse_service_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        service_account_id = _parse_service_account_id(d.pop("service_account_id", UNSET))


        service_account_name = d.pop("service_account_name", UNSET)

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        google_account_linkage = cls(
            delete_finalized_at=delete_finalized_at,
            deleted_at=deleted_at,
            google_email=google_email,
            id=id,
            service_account_id=service_account_id,
            service_account_name=service_account_name,
            user_id=user_id,
        )


        google_account_linkage.additional_properties = d
        return google_account_linkage

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
