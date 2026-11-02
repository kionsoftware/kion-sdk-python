from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_global_custom_variable_response_400 import DeleteGlobalCustomVariableResponse400
from ...models.delete_global_custom_variable_response_401 import DeleteGlobalCustomVariableResponse401
from ...models.delete_global_custom_variable_response_403 import DeleteGlobalCustomVariableResponse403
from ...models.delete_global_custom_variable_response_404 import DeleteGlobalCustomVariableResponse404
from ...models.delete_global_custom_variable_response_500 import DeleteGlobalCustomVariableResponse500
from typing import cast



def _get_kwargs(
    custom_variable_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/custom-variable/{custom_variable_id}".format(custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteGlobalCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteGlobalCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteGlobalCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteGlobalCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteGlobalCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500]:
    """ Deletes a custom variable.

    Args:
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        custom_variable_id=custom_variable_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500 | None:
    """ Deletes a custom variable.

    Args:
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500
     """


    return sync_detailed(
        custom_variable_id=custom_variable_id,
client=client,

    ).parsed

async def asyncio_detailed(
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500]:
    """ Deletes a custom variable.

    Args:
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        custom_variable_id=custom_variable_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500 | None:
    """ Deletes a custom variable.

    Args:
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteGlobalCustomVariableResponse400 | DeleteGlobalCustomVariableResponse401 | DeleteGlobalCustomVariableResponse403 | DeleteGlobalCustomVariableResponse404 | DeleteGlobalCustomVariableResponse500
     """


    return (await asyncio_detailed(
        custom_variable_id=custom_variable_id,
client=client,

    )).parsed
