from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_rule_show_response_200 import GetCloudRuleShowResponse200
from ...models.get_cloud_rule_show_response_401 import GetCloudRuleShowResponse401
from ...models.get_cloud_rule_show_response_403 import GetCloudRuleShowResponse403
from ...models.get_cloud_rule_show_response_404 import GetCloudRuleShowResponse404
from ...models.get_cloud_rule_show_response_500 import GetCloudRuleShowResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    source: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["source"] = source


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cloud-rule/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudRuleShowResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCloudRuleShowResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCloudRuleShowResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCloudRuleShowResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetCloudRuleShowResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    source: str | Unset = UNSET,

) -> Response[GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500]:
    """ Finds a Cloud Rule by ID in the application.

    Args:
        id (int):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
source=source,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    source: str | Unset = UNSET,

) -> GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500 | None:
    """ Finds a Cloud Rule by ID in the application.

    Args:
        id (int):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500
     """


    return sync_detailed(
        id=id,
client=client,
source=source,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    source: str | Unset = UNSET,

) -> Response[GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500]:
    """ Finds a Cloud Rule by ID in the application.

    Args:
        id (int):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
source=source,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    source: str | Unset = UNSET,

) -> GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500 | None:
    """ Finds a Cloud Rule by ID in the application.

    Args:
        id (int):
        source (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleShowResponse200 | GetCloudRuleShowResponse401 | GetCloudRuleShowResponse403 | GetCloudRuleShowResponse404 | GetCloudRuleShowResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
source=source,

    )).parsed
