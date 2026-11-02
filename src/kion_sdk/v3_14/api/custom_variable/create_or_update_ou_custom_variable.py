from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_or_update_ou_custom_variable_response_400 import CreateOrUpdateOUCustomVariableResponse400
from ...models.create_or_update_ou_custom_variable_response_401 import CreateOrUpdateOUCustomVariableResponse401
from ...models.create_or_update_ou_custom_variable_response_403 import CreateOrUpdateOUCustomVariableResponse403
from ...models.create_or_update_ou_custom_variable_response_404 import CreateOrUpdateOUCustomVariableResponse404
from ...models.create_or_update_ou_custom_variable_response_422 import CreateOrUpdateOUCustomVariableResponse422
from ...models.create_or_update_ou_custom_variable_response_500 import CreateOrUpdateOUCustomVariableResponse500
from ...models.ou_custom_variable_create_or_update import OUCustomVariableCreateOrUpdate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    ou_id: int,
    custom_variable_id: int,
    *,
    body: OUCustomVariableCreateOrUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/ou/{ou_id}/custom-variable/{custom_variable_id}".format(ou_id=quote(str(ou_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = CreateOrUpdateOUCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateOrUpdateOUCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateOrUpdateOUCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateOrUpdateOUCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = CreateOrUpdateOUCustomVariableResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = CreateOrUpdateOUCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500]:
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
    body: OUCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500]:
    """ Creates or updates an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):
        body (OUCustomVariableCreateOrUpdate | Unset): OUCustomVariableCreateOrUpdate represents
            the fields necessary to create or update an OU custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,
body=body,

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
    body: OUCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500 | None:
    """ Creates or updates an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):
        body (OUCustomVariableCreateOrUpdate | Unset): OUCustomVariableCreateOrUpdate represents
            the fields necessary to create or update an OU custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500
     """


    return sync_detailed(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    ou_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: OUCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500]:
    """ Creates or updates an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):
        body (OUCustomVariableCreateOrUpdate | Unset): OUCustomVariableCreateOrUpdate represents
            the fields necessary to create or update an OU custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,
body=body,

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
    body: OUCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500 | None:
    """ Creates or updates an OU custom variable override.

    Args:
        ou_id (int):
        custom_variable_id (int):
        body (OUCustomVariableCreateOrUpdate | Unset): OUCustomVariableCreateOrUpdate represents
            the fields necessary to create or update an OU custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateOUCustomVariableResponse400 | CreateOrUpdateOUCustomVariableResponse401 | CreateOrUpdateOUCustomVariableResponse403 | CreateOrUpdateOUCustomVariableResponse404 | CreateOrUpdateOUCustomVariableResponse422 | CreateOrUpdateOUCustomVariableResponse500
     """


    return (await asyncio_detailed(
        ou_id=ou_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    )).parsed
