from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProjectLineItem")



@_attrs_define
class ProjectLineItem:
    """ ProjectLineItem defines a project line item.

        Attributes:
            amount (float | Unset): Amount for the project line item in the application.
            category_id (int | None | Unset): Category ID of related Category of the Project Line Item in the application.
                Example: 101.
            datecode (int | Unset): Datecode for the project line item in the application. Example: 201701.
            description (str | Unset): Description for the project line item in the application. Example: Project being used
                to test cloud migration..
            funding_source_id (int | None | Unset): Funding Source ID of related Funding Source of the Project Line Item in
                the application. Example: 101.
            id (int | Unset): ID of the record in the application. Example: 1.
            payer_id (int | None | Unset): Payer ID of related Payer of the Project Line Item in the application. Example:
                101.
            project_id (int | None | Unset): Project ID of the Project Line Item in the application. Example: 101.
     """

    amount: float | Unset = UNSET
    category_id: int | None | Unset = UNSET
    datecode: int | Unset = UNSET
    description: str | Unset = UNSET
    funding_source_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    payer_id: int | None | Unset = UNSET
    project_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        category_id: int | None | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        datecode = self.datecode

        description = self.description

        funding_source_id: int | None | Unset
        if isinstance(self.funding_source_id, Unset):
            funding_source_id = UNSET
        else:
            funding_source_id = self.funding_source_id

        id = self.id

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if datecode is not UNSET:
            field_dict["datecode"] = datecode
        if description is not UNSET:
            field_dict["description"] = description
        if funding_source_id is not UNSET:
            field_dict["funding_source_id"] = funding_source_id
        if id is not UNSET:
            field_dict["id"] = id
        if payer_id is not UNSET:
            field_dict["payer_id"] = payer_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        def _parse_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))


        datecode = d.pop("datecode", UNSET)

        description = d.pop("description", UNSET)

        def _parse_funding_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_source_id = _parse_funding_source_id(d.pop("funding_source_id", UNSET))


        id = d.pop("id", UNSET)

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


        project_line_item = cls(
            amount=amount,
            category_id=category_id,
            datecode=datecode,
            description=description,
            funding_source_id=funding_source_id,
            id=id,
            payer_id=payer_id,
            project_id=project_id,
        )


        project_line_item.additional_properties = d
        return project_line_item

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
