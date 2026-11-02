from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_feature_flag_response_200 import GetFeatureFlagResponse200
from ...models.get_feature_flag_response_400 import GetFeatureFlagResponse400
from ...models.get_feature_flag_response_401 import GetFeatureFlagResponse401
from ...models.get_feature_flag_response_403 import GetFeatureFlagResponse403
from ...models.get_feature_flag_response_404 import GetFeatureFlagResponse404
from ...models.get_feature_flag_response_500 import GetFeatureFlagResponse500
from typing import cast



def _get_kwargs(
    flag: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/feature-flag/{flag}".format(flag=quote(str(flag), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500 | None:
    if response.status_code == 200:
        response_200 = GetFeatureFlagResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetFeatureFlagResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetFeatureFlagResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetFeatureFlagResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetFeatureFlagResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetFeatureFlagResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flag: str,
    *,
    client: AuthenticatedClient,

) -> Response[GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500]:
    """ Gets a feature flag or a nested feature

    Args:
        flag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500]
     """


    kwargs = _get_kwargs(
        flag=flag,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    flag: str,
    *,
    client: AuthenticatedClient,

) -> GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500 | None:
    """ Gets a feature flag or a nested feature

    Args:
        flag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500
     """


    return sync_detailed(
        flag=flag,
client=client,

    ).parsed

async def asyncio_detailed(
    flag: str,
    *,
    client: AuthenticatedClient,

) -> Response[GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500]:
    """ Gets a feature flag or a nested feature

    Args:
        flag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500]
     """


    kwargs = _get_kwargs(
        flag=flag,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    flag: str,
    *,
    client: AuthenticatedClient,

) -> GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500 | None:
    """ Gets a feature flag or a nested feature

    Args:
        flag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFeatureFlagResponse200 | GetFeatureFlagResponse400 | GetFeatureFlagResponse401 | GetFeatureFlagResponse403 | GetFeatureFlagResponse404 | GetFeatureFlagResponse500
     """


    return (await asyncio_detailed(
        flag=flag,
client=client,

    )).parsed
