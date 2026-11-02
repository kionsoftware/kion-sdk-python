from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_rule_index_response_200 import GetCloudRuleIndexResponse200
from ...models.get_cloud_rule_index_response_401 import GetCloudRuleIndexResponse401
from ...models.get_cloud_rule_index_response_403 import GetCloudRuleIndexResponse403
from ...models.get_cloud_rule_index_response_500 import GetCloudRuleIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["name"] = name

    params["label"] = label

    params["label_key"] = label_key

    params["label_value"] = label_value

    params["label_id"] = label_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cloud-rule",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudRuleIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCloudRuleIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCloudRuleIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetCloudRuleIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> Response[GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500]:
    """ Returns a list of Cloud Rules from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500 | None:
    """ Returns a list of Cloud Rules from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500
     """


    return sync_detailed(
        client=client,
name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> Response[GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500]:
    """ Returns a list of Cloud Rules from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500 | None:
    """ Returns a list of Cloud Rules from the application.

    Args:
        name (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleIndexResponse200 | GetCloudRuleIndexResponse401 | GetCloudRuleIndexResponse403 | GetCloudRuleIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
name=name,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    )).parsed
