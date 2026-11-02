from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.integer_base_filter import IntegerBaseFilter
  from ..models.ou_base_filter import OUBaseFilter
  from ..models.spend_report_query_filter_account_labels import SpendReportQueryFilterAccountLabels
  from ..models.spend_report_query_filter_labels import SpendReportQueryFilterLabels
  from ..models.spend_report_query_filter_project_labels import SpendReportQueryFilterProjectLabels
  from ..models.spend_report_query_filter_tags import SpendReportQueryFilterTags
  from ..models.string_base_filter import StringBaseFilter





T = TypeVar("T", bound="SpendReportQueryFilter")



@_attrs_define
class SpendReportQueryFilter:
    """ SpendReportQueryFilter defines the filters for the spend report query

        Attributes:
            account_id (IntegerBaseFilter | Unset): IntegerBaseFilter defines filtering on a set of integers by including or
                excluding values
            account_labels (SpendReportQueryFilterAccountLabels | Unset): Filtering by labels on accounts Example:
                {'label1': {'is_exclusive': True, 'values': ['val1', 'val2']}, 'label2': {'values': ['val3', 'val4']}}.
            account_name (StringBaseFilter | Unset): StringBaseFilter defines filtering on a set of strings by including or
                excluding values
            account_number (StringBaseFilter | Unset): StringBaseFilter defines filtering on a set of strings by including
                or excluding values
            billing_source_id (IntegerBaseFilter | Unset): IntegerBaseFilter defines filtering on a set of integers by
                including or excluding values
            cloud_service_provider_id (IntegerBaseFilter | Unset): IntegerBaseFilter defines filtering on a set of integers
                by including or excluding values
            labels (SpendReportQueryFilterLabels | Unset): Filtering by labels
            ou_id (OUBaseFilter | Unset): OUBaseFilter defines filtering on a set of OUs
            project_id (IntegerBaseFilter | Unset): IntegerBaseFilter defines filtering on a set of integers by including or
                excluding values
            project_labels (SpendReportQueryFilterProjectLabels | Unset): Filtering by labels on projects
            project_name (StringBaseFilter | Unset): StringBaseFilter defines filtering on a set of strings by including or
                excluding values
            resource (StringBaseFilter | Unset): StringBaseFilter defines filtering on a set of strings by including or
                excluding values
            service (StringBaseFilter | Unset): StringBaseFilter defines filtering on a set of strings by including or
                excluding values
            tags (SpendReportQueryFilterTags | Unset): Filtering by tags Example: {'resourcetags/aws:createdby':
                {'is_exclusive': False, 'values': []}}.
     """

    account_id: IntegerBaseFilter | Unset = UNSET
    account_labels: SpendReportQueryFilterAccountLabels | Unset = UNSET
    account_name: StringBaseFilter | Unset = UNSET
    account_number: StringBaseFilter | Unset = UNSET
    billing_source_id: IntegerBaseFilter | Unset = UNSET
    cloud_service_provider_id: IntegerBaseFilter | Unset = UNSET
    labels: SpendReportQueryFilterLabels | Unset = UNSET
    ou_id: OUBaseFilter | Unset = UNSET
    project_id: IntegerBaseFilter | Unset = UNSET
    project_labels: SpendReportQueryFilterProjectLabels | Unset = UNSET
    project_name: StringBaseFilter | Unset = UNSET
    resource: StringBaseFilter | Unset = UNSET
    service: StringBaseFilter | Unset = UNSET
    tags: SpendReportQueryFilterTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.integer_base_filter import IntegerBaseFilter
        from ..models.ou_base_filter import OUBaseFilter
        from ..models.spend_report_query_filter_account_labels import SpendReportQueryFilterAccountLabels
        from ..models.spend_report_query_filter_labels import SpendReportQueryFilterLabels
        from ..models.spend_report_query_filter_project_labels import SpendReportQueryFilterProjectLabels
        from ..models.spend_report_query_filter_tags import SpendReportQueryFilterTags
        from ..models.string_base_filter import StringBaseFilter
        account_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_id, Unset):
            account_id = self.account_id.to_dict()

        account_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_labels, Unset):
            account_labels = self.account_labels.to_dict()

        account_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_name, Unset):
            account_name = self.account_name.to_dict()

        account_number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_number, Unset):
            account_number = self.account_number.to_dict()

        billing_source_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_source_id, Unset):
            billing_source_id = self.billing_source_id.to_dict()

        cloud_service_provider_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_service_provider_id, Unset):
            cloud_service_provider_id = self.cloud_service_provider_id.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        ou_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ou_id, Unset):
            ou_id = self.ou_id.to_dict()

        project_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = self.project_id.to_dict()

        project_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_labels, Unset):
            project_labels = self.project_labels.to_dict()

        project_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_name, Unset):
            project_name = self.project_name.to_dict()

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_labels is not UNSET:
            field_dict["account_labels"] = account_labels
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if billing_source_id is not UNSET:
            field_dict["billing_source_id"] = billing_source_id
        if cloud_service_provider_id is not UNSET:
            field_dict["cloud_service_provider_id"] = cloud_service_provider_id
        if labels is not UNSET:
            field_dict["labels"] = labels
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_labels is not UNSET:
            field_dict["project_labels"] = project_labels
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if resource is not UNSET:
            field_dict["resource"] = resource
        if service is not UNSET:
            field_dict["service"] = service
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integer_base_filter import IntegerBaseFilter
        from ..models.ou_base_filter import OUBaseFilter
        from ..models.spend_report_query_filter_account_labels import SpendReportQueryFilterAccountLabels
        from ..models.spend_report_query_filter_labels import SpendReportQueryFilterLabels
        from ..models.spend_report_query_filter_project_labels import SpendReportQueryFilterProjectLabels
        from ..models.spend_report_query_filter_tags import SpendReportQueryFilterTags
        from ..models.string_base_filter import StringBaseFilter
        d = dict(src_dict)
        _account_id = d.pop("account_id", UNSET)
        account_id: IntegerBaseFilter | Unset
        if isinstance(_account_id,  Unset):
            account_id = UNSET
        else:
            account_id = IntegerBaseFilter.from_dict(_account_id)




        _account_labels = d.pop("account_labels", UNSET)
        account_labels: SpendReportQueryFilterAccountLabels | Unset
        if isinstance(_account_labels,  Unset):
            account_labels = UNSET
        else:
            account_labels = SpendReportQueryFilterAccountLabels.from_dict(_account_labels)




        _account_name = d.pop("account_name", UNSET)
        account_name: StringBaseFilter | Unset
        if isinstance(_account_name,  Unset):
            account_name = UNSET
        else:
            account_name = StringBaseFilter.from_dict(_account_name)




        _account_number = d.pop("account_number", UNSET)
        account_number: StringBaseFilter | Unset
        if isinstance(_account_number,  Unset):
            account_number = UNSET
        else:
            account_number = StringBaseFilter.from_dict(_account_number)




        _billing_source_id = d.pop("billing_source_id", UNSET)
        billing_source_id: IntegerBaseFilter | Unset
        if isinstance(_billing_source_id,  Unset):
            billing_source_id = UNSET
        else:
            billing_source_id = IntegerBaseFilter.from_dict(_billing_source_id)




        _cloud_service_provider_id = d.pop("cloud_service_provider_id", UNSET)
        cloud_service_provider_id: IntegerBaseFilter | Unset
        if isinstance(_cloud_service_provider_id,  Unset):
            cloud_service_provider_id = UNSET
        else:
            cloud_service_provider_id = IntegerBaseFilter.from_dict(_cloud_service_provider_id)




        _labels = d.pop("labels", UNSET)
        labels: SpendReportQueryFilterLabels | Unset
        if isinstance(_labels,  Unset):
            labels = UNSET
        else:
            labels = SpendReportQueryFilterLabels.from_dict(_labels)




        _ou_id = d.pop("ou_id", UNSET)
        ou_id: OUBaseFilter | Unset
        if isinstance(_ou_id,  Unset):
            ou_id = UNSET
        else:
            ou_id = OUBaseFilter.from_dict(_ou_id)




        _project_id = d.pop("project_id", UNSET)
        project_id: IntegerBaseFilter | Unset
        if isinstance(_project_id,  Unset):
            project_id = UNSET
        else:
            project_id = IntegerBaseFilter.from_dict(_project_id)




        _project_labels = d.pop("project_labels", UNSET)
        project_labels: SpendReportQueryFilterProjectLabels | Unset
        if isinstance(_project_labels,  Unset):
            project_labels = UNSET
        else:
            project_labels = SpendReportQueryFilterProjectLabels.from_dict(_project_labels)




        _project_name = d.pop("project_name", UNSET)
        project_name: StringBaseFilter | Unset
        if isinstance(_project_name,  Unset):
            project_name = UNSET
        else:
            project_name = StringBaseFilter.from_dict(_project_name)




        _resource = d.pop("resource", UNSET)
        resource: StringBaseFilter | Unset
        if isinstance(_resource,  Unset):
            resource = UNSET
        else:
            resource = StringBaseFilter.from_dict(_resource)




        _service = d.pop("service", UNSET)
        service: StringBaseFilter | Unset
        if isinstance(_service,  Unset):
            service = UNSET
        else:
            service = StringBaseFilter.from_dict(_service)




        _tags = d.pop("tags", UNSET)
        tags: SpendReportQueryFilterTags | Unset
        if isinstance(_tags,  Unset):
            tags = UNSET
        else:
            tags = SpendReportQueryFilterTags.from_dict(_tags)




        spend_report_query_filter = cls(
            account_id=account_id,
            account_labels=account_labels,
            account_name=account_name,
            account_number=account_number,
            billing_source_id=billing_source_id,
            cloud_service_provider_id=cloud_service_provider_id,
            labels=labels,
            ou_id=ou_id,
            project_id=project_id,
            project_labels=project_labels,
            project_name=project_name,
            resource=resource,
            service=service,
            tags=tags,
        )


        spend_report_query_filter.additional_properties = d
        return spend_report_query_filter

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
