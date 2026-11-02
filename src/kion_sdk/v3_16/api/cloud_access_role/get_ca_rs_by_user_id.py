from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ca_rs_by_user_id_response_200 import GetCARsByUserIDResponse200
from ...models.get_ca_rs_by_user_id_response_401 import GetCARsByUserIDResponse401
from ...models.get_ca_rs_by_user_id_response_403 import GetCARsByUserIDResponse403
from ...models.get_ca_rs_by_user_id_response_404 import GetCARsByUserIDResponse404
from ...models.get_ca_rs_by_user_id_response_500 import GetCARsByUserIDResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    account_alias: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["account_alias"] = account_alias


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/user/{id}/cloud-access-role".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCARsByUserIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCARsByUserIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCARsByUserIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCARsByUserIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetCARsByUserIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500]:
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
    account_alias: str | Unset = UNSET,

) -> Response[GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500]:
    """ Returns a list of all cloud access roles that are available to a user.

    Args:
        id (int):
        account_alias (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
account_alias=account_alias,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    account_alias: str | Unset = UNSET,

) -> GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500 | None:
    """ Returns a list of all cloud access roles that are available to a user.

    Args:
        id (int):
        account_alias (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500
     """


    return sync_detailed(
        id=id,
client=client,
account_alias=account_alias,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    account_alias: str | Unset = UNSET,

) -> Response[GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500]:
    """ Returns a list of all cloud access roles that are available to a user.

    Args:
        id (int):
        account_alias (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
account_alias=account_alias,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    account_alias: str | Unset = UNSET,

) -> GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500 | None:
    """ Returns a list of all cloud access roles that are available to a user.

    Args:
        id (int):
        account_alias (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCARsByUserIDResponse200 | GetCARsByUserIDResponse401 | GetCARsByUserIDResponse403 | GetCARsByUserIDResponse404 | GetCARsByUserIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
account_alias=account_alias,

    )).parsed
