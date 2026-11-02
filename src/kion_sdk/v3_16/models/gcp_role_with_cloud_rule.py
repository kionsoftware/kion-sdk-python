from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cloud_rule import CloudRule
  from ..models.gcp_role import GCPRole





T = TypeVar("T", bound="GCPRoleWithCloudRule")



@_attrs_define
class GCPRoleWithCloudRule:
    """ GCPRoleWithCloudRule defines a struct mapping a cloud rule to a Google Cloud IAM role.

        Attributes:
            cloud_rule (CloudRule | Unset): CloudRule defines a Cloud Rule.
            exempted_project_ids (list[int] | None | Unset):
            gcp_iam_role (GCPRole | Unset): GCPRole defines a GCP Role.
     """

    cloud_rule: CloudRule | Unset = UNSET
    exempted_project_ids: list[int] | None | Unset = UNSET
    gcp_iam_role: GCPRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_rule import CloudRule
        from ..models.gcp_role import GCPRole
        cloud_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule, Unset):
            cloud_rule = self.cloud_rule.to_dict()

        exempted_project_ids: list[int] | None | Unset
        if isinstance(self.exempted_project_ids, Unset):
            exempted_project_ids = UNSET
        elif isinstance(self.exempted_project_ids, list):
            exempted_project_ids = self.exempted_project_ids


        else:
            exempted_project_ids = self.exempted_project_ids

        gcp_iam_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_iam_role, Unset):
            gcp_iam_role = self.gcp_iam_role.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cloud_rule is not UNSET:
            field_dict["cloud_rule"] = cloud_rule
        if exempted_project_ids is not UNSET:
            field_dict["exempted_project_ids"] = exempted_project_ids
        if gcp_iam_role is not UNSET:
            field_dict["gcp_iam_role"] = gcp_iam_role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_rule import CloudRule
        from ..models.gcp_role import GCPRole
        d = dict(src_dict)
        _cloud_rule = d.pop("cloud_rule", UNSET)
        cloud_rule: CloudRule | Unset
        if isinstance(_cloud_rule,  Unset):
            cloud_rule = UNSET
        else:
            cloud_rule = CloudRule.from_dict(_cloud_rule)




        def _parse_exempted_project_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exempted_project_ids_type_0 = cast(list[int], data)

                return exempted_project_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        exempted_project_ids = _parse_exempted_project_ids(d.pop("exempted_project_ids", UNSET))


        _gcp_iam_role = d.pop("gcp_iam_role", UNSET)
        gcp_iam_role: GCPRole | Unset
        if isinstance(_gcp_iam_role,  Unset):
            gcp_iam_role = UNSET
        else:
            gcp_iam_role = GCPRole.from_dict(_gcp_iam_role)




        gcp_role_with_cloud_rule = cls(
            cloud_rule=cloud_rule,
            exempted_project_ids=exempted_project_ids,
            gcp_iam_role=gcp_iam_role,
        )


        gcp_role_with_cloud_rule.additional_properties = d
        return gcp_role_with_cloud_rule

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
