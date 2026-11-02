from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="WebhookManualRun")



@_attrs_define
class WebhookManualRun:
    """ WebhookManualRun contains the fields required to run a webhook manually.

        Attributes:
            cloud_rule_id (int | None): The ID of the Cloud Rule the webhook is attached to. Example: 1.
            id (int): ID of the webhook in the application. Example: 1.
            project_id (int | None): The ID of the project the webhook is running on. Example: 1.
            run_type (int): The type of webhook that is being run, 1 for pre-rule, 2 for post-rule Example: 1.
     """

    cloud_rule_id: int | None
    id: int
    project_id: int | None
    run_type: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cloud_rule_id: int | None
        cloud_rule_id = self.cloud_rule_id

        id = self.id

        project_id: int | None
        project_id = self.project_id

        run_type = self.run_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cloud_rule_id": cloud_rule_id,
            "id": id,
            "project_id": project_id,
            "run_type": run_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cloud_rule_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cloud_rule_id = _parse_cloud_rule_id(d.pop("cloud_rule_id"))


        id = d.pop("id")

        def _parse_project_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        project_id = _parse_project_id(d.pop("project_id"))


        run_type = d.pop("run_type")

        webhook_manual_run = cls(
            cloud_rule_id=cloud_rule_id,
            id=id,
            project_id=project_id,
            run_type=run_type,
        )


        webhook_manual_run.additional_properties = d
        return webhook_manual_run

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
