from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountMove")



@_attrs_define
class AccountMove:
    """ AccountMove defines an account move command

        Attributes:
            financials (str | Unset): How to handle existing financial data when moving an account.
                One of:
                preserve - Preserve financial history on the current project
                move - Move financial history to the new project Example: move.
            move_datecode (int | Unset): The start date to use when moving financial data in YYYYMM format.
                This only applies when financials is set to move.
                If provided, only financial data from this date to the current month will be moved to the new project.
                If omitted or 0, all financial data will be moved to the new project. Example: 202301.
            project_id (int | None | Unset): The ID of the project to move this account to. Example: 3.
     """

    financials: str | Unset = UNSET
    move_datecode: int | Unset = UNSET
    project_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        financials = self.financials

        move_datecode = self.move_datecode

        project_id: int | None | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if financials is not UNSET:
            field_dict["financials"] = financials
        if move_datecode is not UNSET:
            field_dict["move_datecode"] = move_datecode
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        financials = d.pop("financials", UNSET)

        move_datecode = d.pop("move_datecode", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        account_move = cls(
            financials=financials,
            move_datecode=move_datecode,
            project_id=project_id,
        )


        account_move.additional_properties = d
        return account_move

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
