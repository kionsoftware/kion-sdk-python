from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceProgram")



@_attrs_define
class ComplianceProgram:
    """ ComplianceProgram defines a compliance program.

        Attributes:
            description (str | Unset): Description for the compliance program in the application. Example: Find unattached
                EBS volumes..
            grouping_type (str | Unset):  Example: "baseline".
            id (int | Unset): ID of the compliance program in the application. Example: 1.
            managed_resource_library_checksum (str | Unset): The checksum for the compliance program in our resource
                library.
            managed_resource_library_id (str | Unset): The ID of the compliance program in our resource library.
            name (str | Unset): Name of the compliance program in the application. Example: No Unattached EBS.
            parent_program_id (int | None | Unset): ParentProgramID of the compliance program. Example: 1.
            system_managed_program (bool | None | Unset): True if the compliance program is managed by Kion.
            terse_name (str | Unset): TerseName of the compliance program in the application. Example: No Unattached EBS.
            verbose_name (str | Unset): VerboseName of the compliance program in the application. Example: No Unattached
                EBS.
            version (str | Unset): Version of the compliance program in the application. Example: Find unattached EBS
                volumes..
     """

    description: str | Unset = UNSET
    grouping_type: str | Unset = UNSET
    id: int | Unset = UNSET
    managed_resource_library_checksum: str | Unset = UNSET
    managed_resource_library_id: str | Unset = UNSET
    name: str | Unset = UNSET
    parent_program_id: int | None | Unset = UNSET
    system_managed_program: bool | None | Unset = UNSET
    terse_name: str | Unset = UNSET
    verbose_name: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        grouping_type = self.grouping_type

        id = self.id

        managed_resource_library_checksum = self.managed_resource_library_checksum

        managed_resource_library_id = self.managed_resource_library_id

        name = self.name

        parent_program_id: int | None | Unset
        if isinstance(self.parent_program_id, Unset):
            parent_program_id = UNSET
        else:
            parent_program_id = self.parent_program_id

        system_managed_program: bool | None | Unset
        if isinstance(self.system_managed_program, Unset):
            system_managed_program = UNSET
        else:
            system_managed_program = self.system_managed_program

        terse_name = self.terse_name

        verbose_name = self.verbose_name

        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if grouping_type is not UNSET:
            field_dict["grouping_type"] = grouping_type
        if id is not UNSET:
            field_dict["id"] = id
        if managed_resource_library_checksum is not UNSET:
            field_dict["managed_resource_library_checksum"] = managed_resource_library_checksum
        if managed_resource_library_id is not UNSET:
            field_dict["managed_resource_library_id"] = managed_resource_library_id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_program_id is not UNSET:
            field_dict["parent_program_id"] = parent_program_id
        if system_managed_program is not UNSET:
            field_dict["system_managed_program"] = system_managed_program
        if terse_name is not UNSET:
            field_dict["terse_name"] = terse_name
        if verbose_name is not UNSET:
            field_dict["verbose_name"] = verbose_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        grouping_type = d.pop("grouping_type", UNSET)

        id = d.pop("id", UNSET)

        managed_resource_library_checksum = d.pop("managed_resource_library_checksum", UNSET)

        managed_resource_library_id = d.pop("managed_resource_library_id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_parent_program_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_program_id = _parse_parent_program_id(d.pop("parent_program_id", UNSET))


        def _parse_system_managed_program(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed_program = _parse_system_managed_program(d.pop("system_managed_program", UNSET))


        terse_name = d.pop("terse_name", UNSET)

        verbose_name = d.pop("verbose_name", UNSET)

        version = d.pop("version", UNSET)

        compliance_program = cls(
            description=description,
            grouping_type=grouping_type,
            id=id,
            managed_resource_library_checksum=managed_resource_library_checksum,
            managed_resource_library_id=managed_resource_library_id,
            name=name,
            parent_program_id=parent_program_id,
            system_managed_program=system_managed_program,
            terse_name=terse_name,
            verbose_name=verbose_name,
            version=version,
        )


        compliance_program.additional_properties = d
        return compliance_program

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
