from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AzureAccountLinkageCreate")



@_attrs_define
class AzureAccountLinkageCreate:
    """ AzureAccountLinkageCreate is the request body for creating an Azure Account Linkage.

        Attributes:
            azure_object_id (str): Azure Object ID of the user (UUID format). Example: 11111111-2222-3333-4444-555555555555.
            azure_principal_name (str): Azure Principal Name (UPN) of the user. Example: jdoe@mycompany.onmicrosoft.com.
            payer_id (int | None): ID of the payer this linkage is associated with. Example: 1.
            user_id (int | None): ID of the Kion user to link. Example: 1.
     """

    azure_object_id: str
    azure_principal_name: str
    payer_id: int | None
    user_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        azure_object_id = self.azure_object_id

        azure_principal_name = self.azure_principal_name

        payer_id: int | None
        payer_id = self.payer_id

        user_id: int | None
        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "azure_object_id": azure_object_id,
            "azure_principal_name": azure_principal_name,
            "payer_id": payer_id,
            "user_id": user_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        azure_object_id = d.pop("azure_object_id")

        azure_principal_name = d.pop("azure_principal_name")

        def _parse_payer_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payer_id = _parse_payer_id(d.pop("payer_id"))


        def _parse_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user_id = _parse_user_id(d.pop("user_id"))


        azure_account_linkage_create = cls(
            azure_object_id=azure_object_id,
            azure_principal_name=azure_principal_name,
            payer_id=payer_id,
            user_id=user_id,
        )


        azure_account_linkage_create.additional_properties = d
        return azure_account_linkage_create

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
