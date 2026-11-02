from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.azure_role import AzureRole
  from ..models.cloud_rule import CloudRule





T = TypeVar("T", bound="AzureRoleWithCloudRule")



@_attrs_define
class AzureRoleWithCloudRule:
    """ AzureRoleWithCloudRule defines a struct mapping a cloud rule to an Azure policy definition.

        Attributes:
            azure_role_definition (AzureRole | Unset): AzureRole defines an Azure Role.
            cloud_rule (CloudRule | Unset): CloudRule defines a Cloud Rule.
            exempted_project_ids (list[int] | None | Unset):
     """

    azure_role_definition: AzureRole | Unset = UNSET
    cloud_rule: CloudRule | Unset = UNSET
    exempted_project_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.azure_role import AzureRole
        from ..models.cloud_rule import CloudRule
        azure_role_definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_role_definition, Unset):
            azure_role_definition = self.azure_role_definition.to_dict()

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if azure_role_definition is not UNSET:
            field_dict["azure_role_definition"] = azure_role_definition
        if cloud_rule is not UNSET:
            field_dict["cloud_rule"] = cloud_rule
        if exempted_project_ids is not UNSET:
            field_dict["exempted_project_ids"] = exempted_project_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_role import AzureRole
        from ..models.cloud_rule import CloudRule
        d = dict(src_dict)
        _azure_role_definition = d.pop("azure_role_definition", UNSET)
        azure_role_definition: AzureRole | Unset
        if isinstance(_azure_role_definition,  Unset):
            azure_role_definition = UNSET
        else:
            azure_role_definition = AzureRole.from_dict(_azure_role_definition)




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


        azure_role_with_cloud_rule = cls(
            azure_role_definition=azure_role_definition,
            cloud_rule=cloud_rule,
            exempted_project_ids=exempted_project_ids,
        )


        azure_role_with_cloud_rule.additional_properties = d
        return azure_role_with_cloud_rule

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
