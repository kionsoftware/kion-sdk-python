from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_scope_criteria_response_200 import PatchScopeCriteriaResponse200
from ...models.patch_scope_criteria_response_400 import PatchScopeCriteriaResponse400
from ...models.patch_scope_criteria_response_401 import PatchScopeCriteriaResponse401
from ...models.patch_scope_criteria_response_403 import PatchScopeCriteriaResponse403
from ...models.patch_scope_criteria_response_404 import PatchScopeCriteriaResponse404
from ...models.patch_scope_criteria_response_422 import PatchScopeCriteriaResponse422
from ...models.patch_scope_criteria_response_500 import PatchScopeCriteriaResponse500
from ...models.scope_criteria_update import ScopeCriteriaUpdate
from typing import cast



def _get_kwargs(
    id: int,
    criteria_id: int,
    *,
    body: ScopeCriteriaUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/beta/scope/{id}/criteria/{criteria_id}".format(id=quote(str(id), safe=""),criteria_id=quote(str(criteria_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchScopeCriteriaResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchScopeCriteriaResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchScopeCriteriaResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchScopeCriteriaResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchScopeCriteriaResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchScopeCriteriaResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchScopeCriteriaResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,
    body: ScopeCriteriaUpdate,

) -> Response[PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500]:
    """ Updates a criteria record on an existing scope.

    Args:
        id (int):
        criteria_id (int):
        body (ScopeCriteriaUpdate): ScopeCriteriaUpdate defines a Scope Criteria update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
criteria_id=criteria_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,
    body: ScopeCriteriaUpdate,

) -> PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500 | None:
    """ Updates a criteria record on an existing scope.

    Args:
        id (int):
        criteria_id (int):
        body (ScopeCriteriaUpdate): ScopeCriteriaUpdate defines a Scope Criteria update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500
     """


    return sync_detailed(
        id=id,
criteria_id=criteria_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,
    body: ScopeCriteriaUpdate,

) -> Response[PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500]:
    """ Updates a criteria record on an existing scope.

    Args:
        id (int):
        criteria_id (int):
        body (ScopeCriteriaUpdate): ScopeCriteriaUpdate defines a Scope Criteria update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
criteria_id=criteria_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    criteria_id: int,
    *,
    client: AuthenticatedClient,
    body: ScopeCriteriaUpdate,

) -> PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500 | None:
    """ Updates a criteria record on an existing scope.

    Args:
        id (int):
        criteria_id (int):
        body (ScopeCriteriaUpdate): ScopeCriteriaUpdate defines a Scope Criteria update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchScopeCriteriaResponse200 | PatchScopeCriteriaResponse400 | PatchScopeCriteriaResponse401 | PatchScopeCriteriaResponse403 | PatchScopeCriteriaResponse404 | PatchScopeCriteriaResponse422 | PatchScopeCriteriaResponse500
     """


    return (await asyncio_detailed(
        id=id,
criteria_id=criteria_id,
client=client,
body=body,

    )).parsed
