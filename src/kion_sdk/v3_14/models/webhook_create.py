from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WebhookCreate")



@_attrs_define
class WebhookCreate:
    """ WebhookCreate defines a webhook creation.

        Attributes:
            callout_url (str): URL the application will call when the webhook is triggered. Example:
                http://www.example.com/run.
            name (str): Name of the webhook in the application. Example: Delete Default VPCs.
            timeout_in_seconds (int): The number of seconds the application will wait before considering the webhook "timed
                out". Example: 30.
            description (str | Unset): Description for the webhook in the application. Example: Webhook to remove default
                VPCs on new accounts..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the webhook. Is required if no
                owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the webhook. Is required if no owner
                group IDs are listed. Example: [1, 2].
            request_body (str | Unset): HTTP request payload body to use when the webhook is triggered. Example: {'aws_acces
                s_key_id':'XXXXXXXXXXXX','aws_access_key_secret':'XXXXXXXXXXXX','aws_session_token':'d9a8a257-cce8-4767-831d-
                cba6f8e2eee4','aws_account_number':'XXXXXXXXXXXX','aws_account_type':'Govcloud','account_name':'Sample
                Account','cloud_rule_name':'Sample Cloud Rule Name','event_state':'adhoc','project_name':'Sample
                Project','parent_ou_name':'Sample OU','action_type':'test','callback_url':'http://localhost:8081/v1/webhook/stop
                /fbb7f8c4-32ed-11ea-8a7e-acde48001122'}.
            request_headers (str | Unset): HTTP headers to use when the webhook is triggered. Example: {'x-custom-1':
                'your_custom_header_value1', 'x-custom-2': 'your_custom_header_value2'}.
            request_method (str | Unset): HTTP request method to use when the webhook is triggered. Example: GET.
            should_send_secure_info (bool | None | Unset): Will be true when the request to the webhook will include
                temporary AWS access keys. Example: True.
            skip_ssl (bool | None | Unset): Will be true when the request to the webhook will skip certificate verification.
            use_request_headers (bool | None | Unset): Will be true when intending to send the request headers specified
                above.
     """

    callout_url: str
    name: str
    timeout_in_seconds: int
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    request_body: str | Unset = UNSET
    request_headers: str | Unset = UNSET
    request_method: str | Unset = UNSET
    should_send_secure_info: bool | None | Unset = UNSET
    skip_ssl: bool | None | Unset = UNSET
    use_request_headers: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        callout_url = self.callout_url

        name = self.name

        timeout_in_seconds = self.timeout_in_seconds

        description = self.description

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids

        request_body = self.request_body

        request_headers = self.request_headers

        request_method = self.request_method

        should_send_secure_info: bool | None | Unset
        if isinstance(self.should_send_secure_info, Unset):
            should_send_secure_info = UNSET
        else:
            should_send_secure_info = self.should_send_secure_info

        skip_ssl: bool | None | Unset
        if isinstance(self.skip_ssl, Unset):
            skip_ssl = UNSET
        else:
            skip_ssl = self.skip_ssl

        use_request_headers: bool | None | Unset
        if isinstance(self.use_request_headers, Unset):
            use_request_headers = UNSET
        else:
            use_request_headers = self.use_request_headers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "callout_url": callout_url,
            "name": name,
            "timeout_in_seconds": timeout_in_seconds,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if request_body is not UNSET:
            field_dict["request_body"] = request_body
        if request_headers is not UNSET:
            field_dict["request_headers"] = request_headers
        if request_method is not UNSET:
            field_dict["request_method"] = request_method
        if should_send_secure_info is not UNSET:
            field_dict["should_send_secure_info"] = should_send_secure_info
        if skip_ssl is not UNSET:
            field_dict["skip_ssl"] = skip_ssl
        if use_request_headers is not UNSET:
            field_dict["use_request_headers"] = use_request_headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        callout_url = d.pop("callout_url")

        name = d.pop("name")

        timeout_in_seconds = d.pop("timeout_in_seconds")

        description = d.pop("description", UNSET)

        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        request_body = d.pop("request_body", UNSET)

        request_headers = d.pop("request_headers", UNSET)

        request_method = d.pop("request_method", UNSET)

        def _parse_should_send_secure_info(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        should_send_secure_info = _parse_should_send_secure_info(d.pop("should_send_secure_info", UNSET))


        def _parse_skip_ssl(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_ssl = _parse_skip_ssl(d.pop("skip_ssl", UNSET))


        def _parse_use_request_headers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_request_headers = _parse_use_request_headers(d.pop("use_request_headers", UNSET))


        webhook_create = cls(
            callout_url=callout_url,
            name=name,
            timeout_in_seconds=timeout_in_seconds,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            request_body=request_body,
            request_headers=request_headers,
            request_method=request_method,
            should_send_secure_info=should_send_secure_info,
            skip_ssl=skip_ssl,
            use_request_headers=use_request_headers,
        )


        webhook_create.additional_properties = d
        return webhook_create

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
