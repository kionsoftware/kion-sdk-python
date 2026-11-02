from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BudgetConfig")



@_attrs_define
class BudgetConfig:
    """ BudgetConfig defines a budget configuration.

        Attributes:
            end_datecode (str | Unset): Date when the AWS account will starting submitting payments against a funding source
                (YYYY-MM). Example: 2019-02.
            id (int | Unset): ID of the budget config object. Example: 1.
            name (str | Unset): Name of the budget. Example: Year 2019.
            ou_id (int | None | Unset): ID of OU this budget is attached to. Only present for OU thresholds. Example: 1.
            project_id (int | None | Unset): ID of project this budget is attached to. Only present for project budgets.
                Example: 1.
            start_datecode (str | Unset): Date when the AWS account will starting submitting payments against a funding
                source (YYYY-MM). Example: 2019-02.
     """

    end_datecode: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    start_datecode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_datecode = self.end_datecode

        id = self.id

        name = self.name

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id

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
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_datecode = d.pop("end_datecode", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        budget_config = cls(
            end_datecode=end_datecode,
            id=id,
            name=name,
            ou_id=ou_id,
            project_id=project_id,
            start_datecode=start_datecode,
        )


        budget_config.additional_properties = d
        return budget_config

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
