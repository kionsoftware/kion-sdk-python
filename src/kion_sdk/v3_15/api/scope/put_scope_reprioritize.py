from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.put_scope_reprioritize_response_200 import PutScopeReprioritizeResponse200
from ...models.put_scope_reprioritize_response_400 import PutScopeReprioritizeResponse400
from ...models.put_scope_reprioritize_response_401 import PutScopeReprioritizeResponse401
from ...models.put_scope_reprioritize_response_403 import PutScopeReprioritizeResponse403
from ...models.put_scope_reprioritize_response_422 import PutScopeReprioritizeResponse422
from ...models.put_scope_reprioritize_response_500 import PutScopeReprioritizeResponse500
from ...models.scope_reprioritize import ScopeReprioritize
from typing import cast



def _get_kwargs(
    *,
    body: ScopeReprioritize,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/beta/scope/reprioritize",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500 | None:
    if response.status_code == 200:
        response_200 = PutScopeReprioritizeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutScopeReprioritizeResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutScopeReprioritizeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutScopeReprioritizeResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PutScopeReprioritizeResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutScopeReprioritizeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ScopeReprioritize,

) -> Response[PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500]:
    """ Reprioritizes scopes based on provided list of scope IDs.

    Args:
        body (ScopeReprioritize): ScopeReprioritize defines a Scope reprioritization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: ScopeReprioritize,

) -> PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500 | None:
    """ Reprioritizes scopes based on provided list of scope IDs.

    Args:
        body (ScopeReprioritize): ScopeReprioritize defines a Scope reprioritization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ScopeReprioritize,

) -> Response[PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500]:
    """ Reprioritizes scopes based on provided list of scope IDs.

    Args:
        body (ScopeReprioritize): ScopeReprioritize defines a Scope reprioritization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ScopeReprioritize,

) -> PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500 | None:
    """ Reprioritizes scopes based on provided list of scope IDs.

    Args:
        body (ScopeReprioritize): ScopeReprioritize defines a Scope reprioritization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutScopeReprioritizeResponse200 | PutScopeReprioritizeResponse400 | PutScopeReprioritizeResponse401 | PutScopeReprioritizeResponse403 | PutScopeReprioritizeResponse422 | PutScopeReprioritizeResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
