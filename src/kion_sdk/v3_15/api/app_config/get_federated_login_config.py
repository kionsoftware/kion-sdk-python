from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_federated_login_config_response_200 import GetFederatedLoginConfigResponse200
from ...models.get_federated_login_config_response_401 import GetFederatedLoginConfigResponse401
from ...models.get_federated_login_config_response_403 import GetFederatedLoginConfigResponse403
from ...models.get_federated_login_config_response_500 import GetFederatedLoginConfigResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-config/federated-login",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = GetFederatedLoginConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetFederatedLoginConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetFederatedLoginConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetFederatedLoginConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500]:
    """ Gets the Federated Login enabled status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500]
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

) -> GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500 | None:
    """ Gets the Federated Login enabled status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500]:
    """ Gets the Federated Login enabled status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500]
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

) -> GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500 | None:
    """ Gets the Federated Login enabled status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFederatedLoginConfigResponse200 | GetFederatedLoginConfigResponse401 | GetFederatedLoginConfigResponse403 | GetFederatedLoginConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
