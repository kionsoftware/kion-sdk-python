from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.null_time import NullTime
  from ..models.project_with_ou import ProjectWithOU





T = TypeVar("T", bound="ComplianceStandardProject")



@_attrs_define
class ComplianceStandardProject:
    """ ComplianceStandardProject represents a Project tied to Compliance Standards

        Attributes:
            active_findings (int | Unset):
            last_scan (NullTime | Unset): NullTime represents a time.Time that may be NULL.
            project (ProjectWithOU | Unset): ProjectWithOU defines a project with OU.
            suppressed_findings (int | Unset):
     """

    active_findings: int | Unset = UNSET
    last_scan: NullTime | Unset = UNSET
    project: ProjectWithOU | Unset = UNSET
    suppressed_findings: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_time import NullTime
        from ..models.project_with_ou import ProjectWithOU
        active_findings = self.active_findings

        last_scan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_scan, Unset):
            last_scan = self.last_scan.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        suppressed_findings = self.suppressed_findings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if active_findings is not UNSET:
            field_dict["active_findings"] = active_findings
        if last_scan is not UNSET:
            field_dict["last_scan"] = last_scan
        if project is not UNSET:
            field_dict["project"] = project
        if suppressed_findings is not UNSET:
            field_dict["suppressed_findings"] = suppressed_findings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_time import NullTime
        from ..models.project_with_ou import ProjectWithOU
        d = dict(src_dict)
        active_findings = d.pop("active_findings", UNSET)

        _last_scan = d.pop("last_scan", UNSET)
        last_scan: NullTime | Unset
        if isinstance(_last_scan,  Unset):
            last_scan = UNSET
        else:
            last_scan = NullTime.from_dict(_last_scan)




        _project = d.pop("project", UNSET)
        project: ProjectWithOU | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = ProjectWithOU.from_dict(_project)




        suppressed_findings = d.pop("suppressed_findings", UNSET)

        compliance_standard_project = cls(
            active_findings=active_findings,
            last_scan=last_scan,
            project=project,
            suppressed_findings=suppressed_findings,
        )


        compliance_standard_project.additional_properties = d
        return compliance_standard_project

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
