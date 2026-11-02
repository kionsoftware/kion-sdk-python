from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scope_criteria_record import ScopeCriteriaRecord





T = TypeVar("T", bound="Scope")



@_attrs_define
class Scope:
    """ Scope defines a Scope metadata.

        Attributes:
            active_criteria_record (ScopeCriteriaRecord | Unset): ScopeCriteriaRecord represents a versioned criteria entry
                for a scope.
            alias (str | Unset): Alias of the scope in the application. Example: GH-Dev.
            criteria_error (str | Unset): Criteria error message, if the criteria could not be parsed properly. Example:
                invalid json format at character 15.
            criteria_records (list[ScopeCriteriaRecord] | None | Unset): Versioned criteria records for the scope.
            description (str | Unset): Description of the scope in the application. Example: This scope includes all
                resources related to development environments..
            end_datecode (int | Unset): End datecode for the scope (YYYYMM format), if applicable. Example: 202512.
            id (int | Unset): ID of the record in the application. Example: 1.
            identifier (str | Unset): Unique identifier for the scope. Example: 4276ce30-9a33-49d2-96c1-ae1fcebde63d.
            latest_criteria_record (ScopeCriteriaRecord | Unset): ScopeCriteriaRecord represents a versioned criteria entry
                for a scope.
            name (str | Unset): Name of the scope in the application. Example: GitHub Development.
            project_id (int | None | Unset): ID of the project associated with this scope. Example: 42.
            start_datecode (int | Unset): Start datecode for the scope (YYYYMM format). Example: 202501.
     """

    active_criteria_record: ScopeCriteriaRecord | Unset = UNSET
    alias: str | Unset = UNSET
    criteria_error: str | Unset = UNSET
    criteria_records: list[ScopeCriteriaRecord] | None | Unset = UNSET
    description: str | Unset = UNSET
    end_datecode: int | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    latest_criteria_record: ScopeCriteriaRecord | Unset = UNSET
    name: str | Unset = UNSET
    project_id: int | None | Unset = UNSET
    start_datecode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.scope_criteria_record import ScopeCriteriaRecord
        active_criteria_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_criteria_record, Unset):
            active_criteria_record = self.active_criteria_record.to_dict()

        alias = self.alias

        criteria_error = self.criteria_error

        criteria_records: list[dict[str, Any]] | None | Unset
        if isinstance(self.criteria_records, Unset):
            criteria_records = UNSET
        elif isinstance(self.criteria_records, list):
            criteria_records = []
            for criteria_records_type_0_item_data in self.criteria_records:
                criteria_records_type_0_item = criteria_records_type_0_item_data.to_dict()
                criteria_records.append(criteria_records_type_0_item)


        else:
            criteria_records = self.criteria_records

        description = self.description

        end_datecode = self.end_datecode

        id = self.id

        identifier = self.identifier

        latest_criteria_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_criteria_record, Unset):
            latest_criteria_record = self.latest_criteria_record.to_dict()

        name = self.name

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
        if active_criteria_record is not UNSET:
            field_dict["active_criteria_record"] = active_criteria_record
        if alias is not UNSET:
            field_dict["alias"] = alias
        if criteria_error is not UNSET:
            field_dict["criteria_error"] = criteria_error
        if criteria_records is not UNSET:
            field_dict["criteria_records"] = criteria_records
        if description is not UNSET:
            field_dict["description"] = description
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if latest_criteria_record is not UNSET:
            field_dict["latest_criteria_record"] = latest_criteria_record
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scope_criteria_record import ScopeCriteriaRecord
        d = dict(src_dict)
        _active_criteria_record = d.pop("active_criteria_record", UNSET)
        active_criteria_record: ScopeCriteriaRecord | Unset
        if isinstance(_active_criteria_record,  Unset):
            active_criteria_record = UNSET
        else:
            active_criteria_record = ScopeCriteriaRecord.from_dict(_active_criteria_record)




        alias = d.pop("alias", UNSET)

        criteria_error = d.pop("criteria_error", UNSET)

        def _parse_criteria_records(data: object) -> list[ScopeCriteriaRecord] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                criteria_records_type_0 = []
                _criteria_records_type_0 = data
                for criteria_records_type_0_item_data in (_criteria_records_type_0):
                    criteria_records_type_0_item = ScopeCriteriaRecord.from_dict(criteria_records_type_0_item_data)



                    criteria_records_type_0.append(criteria_records_type_0_item)

                return criteria_records_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ScopeCriteriaRecord] | None | Unset, data)

        criteria_records = _parse_criteria_records(d.pop("criteria_records", UNSET))


        description = d.pop("description", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        _latest_criteria_record = d.pop("latest_criteria_record", UNSET)
        latest_criteria_record: ScopeCriteriaRecord | Unset
        if isinstance(_latest_criteria_record,  Unset):
            latest_criteria_record = UNSET
        else:
            latest_criteria_record = ScopeCriteriaRecord.from_dict(_latest_criteria_record)




        name = d.pop("name", UNSET)

        def _parse_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        start_datecode = d.pop("start_datecode", UNSET)

        scope = cls(
            active_criteria_record=active_criteria_record,
            alias=alias,
            criteria_error=criteria_error,
            criteria_records=criteria_records,
            description=description,
            end_datecode=end_datecode,
            id=id,
            identifier=identifier,
            latest_criteria_record=latest_criteria_record,
            name=name,
            project_id=project_id,
            start_datecode=start_datecode,
        )


        scope.additional_properties = d
        return scope

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
