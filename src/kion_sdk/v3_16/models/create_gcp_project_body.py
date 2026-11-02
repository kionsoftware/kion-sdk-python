from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateGCPProjectBody")



@_attrs_define
class CreateGCPProjectBody:
    """ CreateGCPProjectBody represents the parameters required to create a new google cloud project

        Attributes:
            alias (str | Unset): Alias of the account in the application Example: TP1.
            display_name (str | Unset): DisplayName is the user-friendly name for a project Example: lab #3.
            id (str | Unset): ID is the gcp project ID Example: twilight-zone-42.
            parent_name (str | Unset): ParentName is the fully qualified gcp resource identifier for the parent of the
                project Example: organizations/1026377682360.
            payer_id (int | None | Unset): PayerID is the ID of the payer that should be attached to the project Example:
                32.
            project_id (int | None | Unset): ID is the kion project id Example: 4.
            start_datecode (int | Unset): StartDatecode is the optional YYYYMM datecode for kion project start Example:
                202107.
     """

    alias: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    parent_name: str | Unset = UNSET
    payer_id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    start_datecode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        display_name = self.display_name

        id = self.id

        parent_name = self.parent_name

        payer_id: int | None | Unset
        if isinstance(self.payer_id, Unset):
            payer_id = UNSET
        else:
            payer_id = self.payer_id

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        start_datecode = self.start_datecode


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alias is not UNSET:
            field_dict["alias"] = alias
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if parent_name is not UNSET:
            field_dict["parent_name"] = parent_name
        if payer_id is not UNSET:
            field_dict["payer_id"] = payer_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alias = d.pop("alias", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        parent_name = d.pop("parent_name", UNSET)

        def _parse_payer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payer_id = _parse_payer_id(d.pop("payer_id", UNSET))


        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        create_gcp_project_body = cls(
            alias=alias,
            display_name=display_name,
            id=id,
            parent_name=parent_name,
            payer_id=payer_id,
            project_id=project_id,
            start_datecode=start_datecode,
        )


        create_gcp_project_body.additional_properties = d
        return create_gcp_project_body

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
