from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_move import AccountMove
from ...models.post_account_move_response_201 import PostAccountMoveResponse201
from ...models.post_account_move_response_400 import PostAccountMoveResponse400
from ...models.post_account_move_response_401 import PostAccountMoveResponse401
from ...models.post_account_move_response_403 import PostAccountMoveResponse403
from ...models.post_account_move_response_422 import PostAccountMoveResponse422
from ...models.post_account_move_response_500 import PostAccountMoveResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AccountMove,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account/{id}/move".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAccountMoveResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAccountMoveResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAccountMoveResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAccountMoveResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAccountMoveResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAccountMoveResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500]:
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
    body: AccountMove,

) -> Response[PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500]:
    """ Moves an account to a different project.

    Args:
        id (int):
        body (AccountMove): AccountMove defines an account move command

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AccountMove,

) -> PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500 | None:
    """ Moves an account to a different project.

    Args:
        id (int):
        body (AccountMove): AccountMove defines an account move command

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AccountMove,

) -> Response[PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500]:
    """ Moves an account to a different project.

    Args:
        id (int):
        body (AccountMove): AccountMove defines an account move command

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AccountMove,

) -> PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500 | None:
    """ Moves an account to a different project.

    Args:
        id (int):
        body (AccountMove): AccountMove defines an account move command

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountMoveResponse201 | PostAccountMoveResponse400 | PostAccountMoveResponse401 | PostAccountMoveResponse403 | PostAccountMoveResponse422 | PostAccountMoveResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
