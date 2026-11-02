from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remove_google_account_linkage_response_200 import RemoveGoogleAccountLinkageResponse200
from ...models.remove_google_account_linkage_response_400 import RemoveGoogleAccountLinkageResponse400
from ...models.remove_google_account_linkage_response_401 import RemoveGoogleAccountLinkageResponse401
from ...models.remove_google_account_linkage_response_403 import RemoveGoogleAccountLinkageResponse403
from ...models.remove_google_account_linkage_response_500 import RemoveGoogleAccountLinkageResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account-linkages/google/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500 | None:
    if response.status_code == 200:
        response_200 = RemoveGoogleAccountLinkageResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RemoveGoogleAccountLinkageResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = RemoveGoogleAccountLinkageResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = RemoveGoogleAccountLinkageResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = RemoveGoogleAccountLinkageResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500]:
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

) -> Response[RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500]:
    """ Deletes an Google Account Linkage that you own.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500]
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

) -> RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500 | None:
    """ Deletes an Google Account Linkage that you own.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500]:
    """ Deletes an Google Account Linkage that you own.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500]
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

) -> RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500 | None:
    """ Deletes an Google Account Linkage that you own.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveGoogleAccountLinkageResponse200 | RemoveGoogleAccountLinkageResponse400 | RemoveGoogleAccountLinkageResponse401 | RemoveGoogleAccountLinkageResponse403 | RemoveGoogleAccountLinkageResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
