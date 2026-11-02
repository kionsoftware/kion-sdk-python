from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ou_updatable import OUUpdatable
from ...models.patch_ou_response_200 import PatchOUResponse200
from ...models.patch_ou_response_400 import PatchOUResponse400
from ...models.patch_ou_response_401 import PatchOUResponse401
from ...models.patch_ou_response_403 import PatchOUResponse403
from ...models.patch_ou_response_404 import PatchOUResponse404
from ...models.patch_ou_response_422 import PatchOUResponse422
from ...models.patch_ou_response_500 import PatchOUResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OUUpdatable,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/ou/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchOUResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchOUResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchOUResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchOUResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchOUResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchOUResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchOUResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500]:
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
    body: OUUpdatable,

) -> Response[PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500]:
    """ Updates an OU by ID in the application.

    Args:
        id (int):
        body (OUUpdatable): OUUpdatable defines an OU update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500]
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
    body: OUUpdatable,

) -> PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500 | None:
    """ Updates an OU by ID in the application.

    Args:
        id (int):
        body (OUUpdatable): OUUpdatable defines an OU update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500
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
    body: OUUpdatable,

) -> Response[PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500]:
    """ Updates an OU by ID in the application.

    Args:
        id (int):
        body (OUUpdatable): OUUpdatable defines an OU update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500]
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
    body: OUUpdatable,

) -> PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500 | None:
    """ Updates an OU by ID in the application.

    Args:
        id (int):
        body (OUUpdatable): OUUpdatable defines an OU update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOUResponse200 | PatchOUResponse400 | PatchOUResponse401 | PatchOUResponse403 | PatchOUResponse404 | PatchOUResponse422 | PatchOUResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
