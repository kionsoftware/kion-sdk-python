from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPTriggerRoleImport")



@_attrs_define
class GCPTriggerRoleImport:
    """ GCPTriggerRoleImport is the request body for triggering gcp roles imports

        Attributes:
            account_id (int | None | Unset): If importing roles for a specific Google Cloud project (Kion Account) specify
                the account's id here
            organization_id (str | Unset): If importing roles for a specific GCPOrganization this should be its
                GCPOrganization.ResourceName
     """

    account_id: int | None | Unset = UNSET
    organization_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        organization_id = self.organization_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        organization_id = d.pop("organization_id", UNSET)

        gcp_trigger_role_import = cls(
            account_id=account_id,
            organization_id=organization_id,
        )


        gcp_trigger_role_import.additional_properties = d
        return gcp_trigger_role_import

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
