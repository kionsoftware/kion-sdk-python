from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_ou_enforcement_response_201 import CreateOUEnforcementResponse201
from ...models.create_ou_enforcement_response_400 import CreateOUEnforcementResponse400
from ...models.create_ou_enforcement_response_401 import CreateOUEnforcementResponse401
from ...models.create_ou_enforcement_response_403 import CreateOUEnforcementResponse403
from ...models.create_ou_enforcement_response_404 import CreateOUEnforcementResponse404
from ...models.create_ou_enforcement_response_422 import CreateOUEnforcementResponse422
from ...models.create_ou_enforcement_response_500 import CreateOUEnforcementResponse500
from ...models.ou_enforcement_create import OUEnforcementCreate
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OUEnforcementCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou/{id}/enforcement".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500 | None:
    if response.status_code == 201:
        response_201 = CreateOUEnforcementResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = CreateOUEnforcementResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateOUEnforcementResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateOUEnforcementResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateOUEnforcementResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = CreateOUEnforcementResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = CreateOUEnforcementResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500]:
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
    body: OUEnforcementCreate,

) -> Response[CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500]:
    """ Create a new enforcement on an OU.

    Args:
        id (int):
        body (OUEnforcementCreate): OUEnforcementCreate is the payload for creating a new OU
            enforcement

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500]
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
    body: OUEnforcementCreate,

) -> CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500 | None:
    """ Create a new enforcement on an OU.

    Args:
        id (int):
        body (OUEnforcementCreate): OUEnforcementCreate is the payload for creating a new OU
            enforcement

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500
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
    body: OUEnforcementCreate,

) -> Response[CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500]:
    """ Create a new enforcement on an OU.

    Args:
        id (int):
        body (OUEnforcementCreate): OUEnforcementCreate is the payload for creating a new OU
            enforcement

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500]
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
    body: OUEnforcementCreate,

) -> CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500 | None:
    """ Create a new enforcement on an OU.

    Args:
        id (int):
        body (OUEnforcementCreate): OUEnforcementCreate is the payload for creating a new OU
            enforcement

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOUEnforcementResponse201 | CreateOUEnforcementResponse400 | CreateOUEnforcementResponse401 | CreateOUEnforcementResponse403 | CreateOUEnforcementResponse404 | CreateOUEnforcementResponse422 | CreateOUEnforcementResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
