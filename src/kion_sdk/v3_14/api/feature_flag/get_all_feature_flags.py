from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_all_feature_flags_response_200 import GetAllFeatureFlagsResponse200
from ...models.get_all_feature_flags_response_400 import GetAllFeatureFlagsResponse400
from ...models.get_all_feature_flags_response_401 import GetAllFeatureFlagsResponse401
from ...models.get_all_feature_flags_response_403 import GetAllFeatureFlagsResponse403
from ...models.get_all_feature_flags_response_500 import GetAllFeatureFlagsResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/feature-flag",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAllFeatureFlagsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAllFeatureFlagsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAllFeatureFlagsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAllFeatureFlagsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAllFeatureFlagsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500]:
    """ Gets a list of all feature flags and nested features in the system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500 | None:
    """ Gets a list of all feature flags and nested features in the system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500]:
    """ Gets a list of all feature flags and nested features in the system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500 | None:
    """ Gets a list of all feature flags and nested features in the system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllFeatureFlagsResponse200 | GetAllFeatureFlagsResponse400 | GetAllFeatureFlagsResponse401 | GetAllFeatureFlagsResponse403 | GetAllFeatureFlagsResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
