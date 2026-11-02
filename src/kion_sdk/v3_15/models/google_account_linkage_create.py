from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GoogleAccountLinkageCreate")



@_attrs_define
class GoogleAccountLinkageCreate:
    """ GoogleAccountLinkageCreate is the request body for creating a Google Account Linkage.

        Attributes:
            google_email (str): Google email of the user. Example: jdoe@mycompany.com.
            service_account_id (int | None): ID of the GCP service account this linkage is associated with. Example: 1.
            user_id (int | None): ID of the Kion user to link. Example: 1.
     """

    google_email: str
    service_account_id: int | None
    user_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        google_email = self.google_email

        service_account_id: int | None
        service_account_id = self.service_account_id

        user_id: int | None
        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "google_email": google_email,
            "service_account_id": service_account_id,
            "user_id": user_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        google_email = d.pop("google_email")

        def _parse_service_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        service_account_id = _parse_service_account_id(d.pop("service_account_id"))


        def _parse_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user_id = _parse_user_id(d.pop("user_id"))


        google_account_linkage_create = cls(
            google_email=google_email,
            service_account_id=service_account_id,
            user_id=user_id,
        )


        google_account_linkage_create.additional_properties = d
        return google_account_linkage_create

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
