from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_reattempts_response_200 import GetReattemptsResponse200
from ...models.get_reattempts_response_400 import GetReattemptsResponse400
from ...models.get_reattempts_response_401 import GetReattemptsResponse401
from ...models.get_reattempts_response_403 import GetReattemptsResponse403
from ...models.get_reattempts_response_500 import GetReattemptsResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account/{id}/reattempt".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetReattemptsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetReattemptsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetReattemptsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetReattemptsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetReattemptsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500]:
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

) -> Response[GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500]:
    """ Gets a list of all the re-attempts needed in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500]
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

) -> GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500 | None:
    """ Gets a list of all the re-attempts needed in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500]:
    """ Gets a list of all the re-attempts needed in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500]
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

) -> GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500 | None:
    """ Gets a list of all the re-attempts needed in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReattemptsResponse200 | GetReattemptsResponse400 | GetReattemptsResponse401 | GetReattemptsResponse403 | GetReattemptsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
