from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_label_response_200 import DeleteOULabelResponse200
from ...models.delete_ou_label_response_400 import DeleteOULabelResponse400
from ...models.delete_ou_label_response_401 import DeleteOULabelResponse401
from ...models.delete_ou_label_response_404 import DeleteOULabelResponse404
from ...models.delete_ou_label_response_422 import DeleteOULabelResponse422
from ...models.delete_ou_label_response_500 import DeleteOULabelResponse500
from typing import cast



def _get_kwargs(
    ou_id: int,
    label_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou/{ou_id}/labels/{label_id}".format(ou_id=quote(str(ou_id), safe=""),label_id=quote(str(label_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOULabelResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteOULabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOULabelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteOULabelResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteOULabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteOULabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ou_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500]:
    """ Removes a label from the given OU by label ID.

    Args:
        ou_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
label_id=label_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ou_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500 | None:
    """ Removes a label from the given OU by label ID.

    Args:
        ou_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500
     """


    return sync_detailed(
        ou_id=ou_id,
label_id=label_id,
client=client,

    ).parsed

async def asyncio_detailed(
    ou_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500]:
    """ Removes a label from the given OU by label ID.

    Args:
        ou_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
label_id=label_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ou_id: int,
    label_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500 | None:
    """ Removes a label from the given OU by label ID.

    Args:
        ou_id (int):
        label_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOULabelResponse200 | DeleteOULabelResponse400 | DeleteOULabelResponse401 | DeleteOULabelResponse404 | DeleteOULabelResponse422 | DeleteOULabelResponse500
     """


    return (await asyncio_detailed(
        ou_id=ou_id,
label_id=label_id,
client=client,

    )).parsed
