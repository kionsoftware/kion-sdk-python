from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ComplianceProgramUpdate")



@_attrs_define
class ComplianceProgramUpdate:
    """ ComplianceProgramUpdate defines a Compliance Program update.

        Attributes:
            description (str | Unset): Description for the Compliance Program in the application. Example: ISO/IEC
                27001:2013 (International Organization for Standardization and International Electrotechnical Commission),.
            grouping_type (str | Unset): GroupType of the Compliance Program in the application. Example: baseline.
            name (str | Unset): Name of the Compliance Program in the application. Example: NIST 800-53.
            terse_name (str | Unset): TerseName of the Compliance Program in the application.
                This is a concise name meant for easy identification and small UI spaces like program icons. Example: ISO27001.
            verbose_name (str | Unset): VerboseName of the Compliance Program in the application.
                This is a more detailed program name meant to suppliment the Name or TerseName in specific contexts. Example:
                International Organization for Standardization and the International Electrotechnical Commission.
            version (str | Unset): Version of the Compliance Program in the application. Example: 1.0.
     """

    description: str | Unset = UNSET
    grouping_type: str | Unset = UNSET
    name: str | Unset = UNSET
    terse_name: str | Unset = UNSET
    verbose_name: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        grouping_type = self.grouping_type

        name = self.name

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
        if name is not UNSET:
            field_dict["name"] = name
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

        name = d.pop("name", UNSET)

        terse_name = d.pop("terse_name", UNSET)

        verbose_name = d.pop("verbose_name", UNSET)

        version = d.pop("version", UNSET)

        compliance_program_update = cls(
            description=description,
            grouping_type=grouping_type,
            name=name,
            terse_name=terse_name,
            verbose_name=verbose_name,
            version=version,
        )


        compliance_program_update.additional_properties = d
        return compliance_program_update

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
