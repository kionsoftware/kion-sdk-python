from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_scope_criteria_response_200 import DeleteScopeCriteriaResponse200
from ...models.delete_scope_criteria_response_400 import DeleteScopeCriteriaResponse400
from ...models.delete_scope_criteria_response_401 import DeleteScopeCriteriaResponse401
from ...models.delete_scope_criteria_response_403 import DeleteScopeCriteriaResponse403
from ...models.delete_scope_criteria_response_404 import DeleteScopeCriteriaResponse404
from ...models.delete_scope_criteria_response_422 import DeleteScopeCriteriaResponse422
from ...models.delete_scope_criteria_response_500 import DeleteScopeCriteriaResponse500
from typing import cast



def _get_kwargs(
    scope_id: int,
    criteria_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/beta/scope/{scope_id}/criteria/{criteria_id}".format(scope_id=quote(str(scope_id), safe=""),criteria_id=quote(str(criteria_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteScopeCriteriaResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteScopeCriteriaResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteScopeCriteriaResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteScopeCriteriaResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteScopeCriteriaResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteScopeCriteriaResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteScopeCriteriaResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scope_id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500]:
    """ Deletes a criteria record from an existing scope.

    Args:
        scope_id (int):
        criteria_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500]
     """


    kwargs = _get_kwargs(
        scope_id=scope_id,
criteria_id=criteria_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    scope_id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500 | None:
    """ Deletes a criteria record from an existing scope.

    Args:
        scope_id (int):
        criteria_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500
     """


    return sync_detailed(
        scope_id=scope_id,
criteria_id=criteria_id,
client=client,

    ).parsed

async def asyncio_detailed(
    scope_id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500]:
    """ Deletes a criteria record from an existing scope.

    Args:
        scope_id (int):
        criteria_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500]
     """


    kwargs = _get_kwargs(
        scope_id=scope_id,
criteria_id=criteria_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    scope_id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500 | None:
    """ Deletes a criteria record from an existing scope.

    Args:
        scope_id (int):
        criteria_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteScopeCriteriaResponse200 | DeleteScopeCriteriaResponse400 | DeleteScopeCriteriaResponse401 | DeleteScopeCriteriaResponse403 | DeleteScopeCriteriaResponse404 | DeleteScopeCriteriaResponse422 | DeleteScopeCriteriaResponse500
     """


    return (await asyncio_detailed(
        scope_id=scope_id,
criteria_id=criteria_id,
client=client,

    )).parsed
