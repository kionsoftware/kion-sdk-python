from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_custom_variable_response_400 import DeleteOUCustomVariableResponse400
from ...models.delete_ou_custom_variable_response_401 import DeleteOUCustomVariableResponse401
from ...models.delete_ou_custom_variable_response_403 import DeleteOUCustomVariableResponse403
from ...models.delete_ou_custom_variable_response_404 import DeleteOUCustomVariableResponse404
from ...models.delete_ou_custom_variable_response_500 import DeleteOUCustomVariableResponse500
from typing import cast



def _get_kwargs(
    ou_id: int,
    custom_variable_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou/{ou_id}/custom-variable/{custom_variable_id}".format(ou_id=quote(str(ou_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteOUCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOUCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOUCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOUCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteOUCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ou_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500]:
    """ Deletes an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ou_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500 | None:
    """ Deletes an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500
     """


    return sync_detailed(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,
client=client,

    ).parsed

async def asyncio_detailed(
    ou_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500]:
    """ Deletes an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ou_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500 | None:
    """ Deletes an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteOUCustomVariableResponse400 | DeleteOUCustomVariableResponse401 | DeleteOUCustomVariableResponse403 | DeleteOUCustomVariableResponse404 | DeleteOUCustomVariableResponse500
     """


    return (await asyncio_detailed(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,
client=client,

    )).parsed
