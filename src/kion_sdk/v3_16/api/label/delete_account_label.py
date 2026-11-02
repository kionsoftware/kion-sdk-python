from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_account_label_response_200 import DeleteAccountLabelResponse200
from ...models.delete_account_label_response_400 import DeleteAccountLabelResponse400
from ...models.delete_account_label_response_401 import DeleteAccountLabelResponse401
from ...models.delete_account_label_response_404 import DeleteAccountLabelResponse404
from ...models.delete_account_label_response_422 import DeleteAccountLabelResponse422
from ...models.delete_account_label_response_500 import DeleteAccountLabelResponse500
from typing import cast



def _get_kwargs(
    account_id: int,
    label_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account/{account_id}/labels/{label_id}".format(account_id=quote(str(account_id), safe=""),label_id=quote(str(label_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteAccountLabelResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteAccountLabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteAccountLabelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteAccountLabelResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteAccountLabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteAccountLabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500]:
    """ Removes a label from the given account by label ID.

    Args:
        account_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
label_id=label_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500 | None:
    """ Removes a label from the given account by label ID.

    Args:
        account_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500
     """


    return sync_detailed(
        account_id=account_id,
label_id=label_id,
client=client,

    ).parsed

async def asyncio_detailed(
    account_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500]:
    """ Removes a label from the given account by label ID.

    Args:
        account_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
label_id=label_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500 | None:
    """ Removes a label from the given account by label ID.

    Args:
        account_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAccountLabelResponse200 | DeleteAccountLabelResponse400 | DeleteAccountLabelResponse401 | DeleteAccountLabelResponse404 | DeleteAccountLabelResponse422 | DeleteAccountLabelResponse500
     """


    return (await asyncio_detailed(
        account_id=account_id,
label_id=label_id,
client=client,

    )).parsed
