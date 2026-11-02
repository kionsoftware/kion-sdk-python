from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_global_custom_variable_response_201 import CreateGlobalCustomVariableResponse201
from ...models.create_global_custom_variable_response_400 import CreateGlobalCustomVariableResponse400
from ...models.create_global_custom_variable_response_401 import CreateGlobalCustomVariableResponse401
from ...models.create_global_custom_variable_response_403 import CreateGlobalCustomVariableResponse403
from ...models.create_global_custom_variable_response_422 import CreateGlobalCustomVariableResponse422
from ...models.create_global_custom_variable_response_500 import CreateGlobalCustomVariableResponse500
from ...models.global_custom_variable_create import GlobalCustomVariableCreate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: GlobalCustomVariableCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/custom-variable",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500 | None:
    if response.status_code == 201:
        response_201 = CreateGlobalCustomVariableResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = CreateGlobalCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateGlobalCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateGlobalCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = CreateGlobalCustomVariableResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = CreateGlobalCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GlobalCustomVariableCreate | Unset = UNSET,

) -> Response[CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500]:
    """ Creates a custom variable.

    Args:
        body (GlobalCustomVariableCreate | Unset): GlobalCustomVariableCreate represents the
            fields necessary to create a custom variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: GlobalCustomVariableCreate | Unset = UNSET,

) -> CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500 | None:
    """ Creates a custom variable.

    Args:
        body (GlobalCustomVariableCreate | Unset): GlobalCustomVariableCreate represents the
            fields necessary to create a custom variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GlobalCustomVariableCreate | Unset = UNSET,

) -> Response[CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500]:
    """ Creates a custom variable.

    Args:
        body (GlobalCustomVariableCreate | Unset): GlobalCustomVariableCreate represents the
            fields necessary to create a custom variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GlobalCustomVariableCreate | Unset = UNSET,

) -> CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500 | None:
    """ Creates a custom variable.

    Args:
        body (GlobalCustomVariableCreate | Unset): GlobalCustomVariableCreate represents the
            fields necessary to create a custom variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGlobalCustomVariableResponse201 | CreateGlobalCustomVariableResponse400 | CreateGlobalCustomVariableResponse401 | CreateGlobalCustomVariableResponse403 | CreateGlobalCustomVariableResponse422 | CreateGlobalCustomVariableResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
