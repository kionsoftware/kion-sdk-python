from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectFunding")



@_attrs_define
class ProjectFunding:
    """ ProjectFunding represents a project funding record in the system.

        Attributes:
            amount (float | Unset):
            end_datecode (int | Unset):
            funding_order (int | Unset):
            funding_source_id (int | None | Unset):
            id (int | Unset):
            project_id (int | None | Unset):
            start_datecode (int | Unset):
     """

    amount: float | Unset = UNSET
    end_datecode: int | Unset = UNSET
    funding_order: int | Unset = UNSET
    funding_source_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    project_id: int | None | Unset = UNSET
    start_datecode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        end_datecode = self.end_datecode

        funding_order = self.funding_order

        funding_source_id: int | None | Unset
        if isinstance(self.funding_source_id, Unset):
            funding_source_id = UNSET
        else:
            funding_source_id = self.funding_source_id

        id = self.id

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
        if amount is not UNSET:
            field_dict["amount"] = amount
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if funding_order is not UNSET:
            field_dict["funding_order"] = funding_order
        if funding_source_id is not UNSET:
            field_dict["funding_source_id"] = funding_source_id
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        funding_order = d.pop("funding_order", UNSET)

        def _parse_funding_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id", UNSET))


        id = d.pop("id", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        project_funding = cls(
            amount=amount,
            end_datecode=end_datecode,
            funding_order=funding_order,
            funding_source_id=funding_source_id,
            id=id,
            project_id=project_id,
            start_datecode=start_datecode,
        )


        project_funding.additional_properties = d
        return project_funding

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
