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
  from ..models.ou import OU
  from ..models.project import Project
  from ..models.request_user import RequestUser





T = TypeVar("T", bound="CloudRuleExemptionRequest")



@_attrs_define
class CloudRuleExemptionRequest:
    """ CloudRuleExemptionRequest defines a cloud rule exemption request.

        Attributes:
            cloud_rule (CloudRule | Unset): CloudRule defines a Cloud Rule.
            comments (str | Unset): Optional comments specified on the request Example: For auditing.
            ou (OU | Unset): OU defines an OU.
            project (Project | Unset): Project defines a project.
            request_id (int | None | Unset): ID of the request Example: 1.
            request_user (RequestUser | Unset): RequestUser defines a user that made exemption requests.
     """

    cloud_rule: CloudRule | Unset = UNSET
    comments: str | Unset = UNSET
    ou: OU | Unset = UNSET
    project: Project | Unset = UNSET
    request_id: int | None | Unset = UNSET
    request_user: RequestUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cloud_rule import CloudRule
        from ..models.ou import OU
        from ..models.project import Project
        from ..models.request_user import RequestUser
        cloud_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_rule, Unset):
            cloud_rule = self.cloud_rule.to_dict()

        comments = self.comments

        ou: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ou, Unset):
            ou = self.ou.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        request_id: int | None | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        request_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_user, Unset):
            request_user = self.request_user.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cloud_rule is not UNSET:
            field_dict["cloud_rule"] = cloud_rule
        if comments is not UNSET:
            field_dict["comments"] = comments
        if ou is not UNSET:
            field_dict["ou"] = ou
        if project is not UNSET:
            field_dict["project"] = project
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if request_user is not UNSET:
            field_dict["request_user"] = request_user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_rule import CloudRule
        from ..models.ou import OU
        from ..models.project import Project
        from ..models.request_user import RequestUser
        d = dict(src_dict)
        _cloud_rule = d.pop("cloud_rule", UNSET)
        cloud_rule: CloudRule | Unset
        if isinstance(_cloud_rule,  Unset):
            cloud_rule = UNSET
        else:
            cloud_rule = CloudRule.from_dict(_cloud_rule)




        comments = d.pop("comments", UNSET)

        _ou = d.pop("ou", UNSET)
        ou: OU | Unset
        if isinstance(_ou,  Unset):
            ou = UNSET
        else:
            ou = OU.from_dict(_ou)




        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)




        def _parse_request_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        request_id = _parse_request_id(d.pop("request_id", UNSET))


        _request_user = d.pop("request_user", UNSET)
        request_user: RequestUser | Unset
        if isinstance(_request_user,  Unset):
            request_user = UNSET
        else:
            request_user = RequestUser.from_dict(_request_user)




        cloud_rule_exemption_request = cls(
            cloud_rule=cloud_rule,
            comments=comments,
            ou=ou,
            project=project,
            request_id=request_id,
            request_user=request_user,
        )


        cloud_rule_exemption_request.additional_properties = d
        return cloud_rule_exemption_request

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
