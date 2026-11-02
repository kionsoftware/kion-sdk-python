from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_enforcement_response_200 import DeleteOUEnforcementResponse200
from ...models.delete_ou_enforcement_response_401 import DeleteOUEnforcementResponse401
from ...models.delete_ou_enforcement_response_500 import DeleteOUEnforcementResponse500
from typing import cast



def _get_kwargs(
    id: int,
    enforcement_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou/{id}/enforcement/{enforcement_id}".format(id=quote(str(id), safe=""),enforcement_id=quote(str(enforcement_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOUEnforcementResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteOUEnforcementResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = DeleteOUEnforcementResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500]:
    """ Deletes the specified enforcement.

    Args:
        id (int):
        enforcement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
enforcement_id=enforcement_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500 | None:
    """ Deletes the specified enforcement.

    Args:
        id (int):
        enforcement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500
     """


    return sync_detailed(
        id=id,
enforcement_id=enforcement_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500]:
    """ Deletes the specified enforcement.

    Args:
        id (int):
        enforcement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
enforcement_id=enforcement_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500 | None:
    """ Deletes the specified enforcement.

    Args:
        id (int):
        enforcement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUEnforcementResponse200 | DeleteOUEnforcementResponse401 | DeleteOUEnforcementResponse500
     """


    return (await asyncio_detailed(
        id=id,
enforcement_id=enforcement_id,
client=client,

    )).parsed
