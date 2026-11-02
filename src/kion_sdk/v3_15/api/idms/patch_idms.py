from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.idms_updatable import IDMSUpdatable
from ...models.patch_idms_response_200 import PatchIDMSResponse200
from ...models.patch_idms_response_400 import PatchIDMSResponse400
from ...models.patch_idms_response_401 import PatchIDMSResponse401
from ...models.patch_idms_response_403 import PatchIDMSResponse403
from ...models.patch_idms_response_404 import PatchIDMSResponse404
from ...models.patch_idms_response_422 import PatchIDMSResponse422
from ...models.patch_idms_response_500 import PatchIDMSResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: IDMSUpdatable | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/idms/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchIDMSResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchIDMSResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchIDMSResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchIDMSResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchIDMSResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchIDMSResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchIDMSResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500]:
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
    body: IDMSUpdatable | Unset = UNSET,

) -> Response[PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500]:
    """ Updates an existing IDMS in the application.

    Args:
        id (int):
        body (IDMSUpdatable | Unset): IDMSUpdatable defines an IDMS update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500]
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
    body: IDMSUpdatable | Unset = UNSET,

) -> PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500 | None:
    """ Updates an existing IDMS in the application.

    Args:
        id (int):
        body (IDMSUpdatable | Unset): IDMSUpdatable defines an IDMS update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500
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
    body: IDMSUpdatable | Unset = UNSET,

) -> Response[PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500]:
    """ Updates an existing IDMS in the application.

    Args:
        id (int):
        body (IDMSUpdatable | Unset): IDMSUpdatable defines an IDMS update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500]
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
    body: IDMSUpdatable | Unset = UNSET,

) -> PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500 | None:
    """ Updates an existing IDMS in the application.

    Args:
        id (int):
        body (IDMSUpdatable | Unset): IDMSUpdatable defines an IDMS update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchIDMSResponse200 | PatchIDMSResponse400 | PatchIDMSResponse401 | PatchIDMSResponse403 | PatchIDMSResponse404 | PatchIDMSResponse422 | PatchIDMSResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
