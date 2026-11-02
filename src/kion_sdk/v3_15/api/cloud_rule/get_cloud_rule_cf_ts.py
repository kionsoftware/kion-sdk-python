from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_rule_cf_ts_response_200 import GetCloudRuleCFTsResponse200
from ...models.get_cloud_rule_cf_ts_response_401 import GetCloudRuleCFTsResponse401
from ...models.get_cloud_rule_cf_ts_response_403 import GetCloudRuleCFTsResponse403
from ...models.get_cloud_rule_cf_ts_response_404 import GetCloudRuleCFTsResponse404
from ...models.get_cloud_rule_cf_ts_response_500 import GetCloudRuleCFTsResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cloud-rule/{id}/cft".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudRuleCFTsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCloudRuleCFTsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCloudRuleCFTsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCloudRuleCFTsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetCloudRuleCFTsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500]:
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

) -> Response[GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500]:
    """ Gets the CFTs associated with this Cloud Rule.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500 | None:
    """ Gets the CFTs associated with this Cloud Rule.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500]:
    """ Gets the CFTs associated with this Cloud Rule.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500 | None:
    """ Gets the CFTs associated with this Cloud Rule.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRuleCFTsResponse200 | GetCloudRuleCFTsResponse401 | GetCloudRuleCFTsResponse403 | GetCloudRuleCFTsResponse404 | GetCloudRuleCFTsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
