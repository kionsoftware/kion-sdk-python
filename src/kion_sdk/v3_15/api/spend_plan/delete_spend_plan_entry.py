from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_spend_plan_entry_response_200 import DeleteSpendPlanEntryResponse200
from ...models.delete_spend_plan_entry_response_400 import DeleteSpendPlanEntryResponse400
from ...models.delete_spend_plan_entry_response_401 import DeleteSpendPlanEntryResponse401
from ...models.delete_spend_plan_entry_response_403 import DeleteSpendPlanEntryResponse403
from ...models.delete_spend_plan_entry_response_404 import DeleteSpendPlanEntryResponse404
from ...models.delete_spend_plan_entry_response_422 import DeleteSpendPlanEntryResponse422
from ...models.delete_spend_plan_entry_response_500 import DeleteSpendPlanEntryResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    fs_id: int,
    *,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["reprocess"] = reprocess

    params["skipValidation"] = skip_validation


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v4/project/{id}/spend-plan/funding-source/{fs_id}".format(id=quote(str(id), safe=""),fs_id=quote(str(fs_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteSpendPlanEntryResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteSpendPlanEntryResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteSpendPlanEntryResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteSpendPlanEntryResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteSpendPlanEntryResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteSpendPlanEntryResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteSpendPlanEntryResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    fs_id: int,
    *,
    client: AuthenticatedClient,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500]:
    """ Deletes an entry from a project spend plan.

    Args:
        id (int):
        fs_id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
fs_id=fs_id,
reprocess=reprocess,
skip_validation=skip_validation,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    fs_id: int,
    *,
    client: AuthenticatedClient,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500 | None:
    """ Deletes an entry from a project spend plan.

    Args:
        id (int):
        fs_id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500
     """


    return sync_detailed(
        id=id,
fs_id=fs_id,
client=client,
reprocess=reprocess,
skip_validation=skip_validation,

    ).parsed

async def asyncio_detailed(
    id: int,
    fs_id: int,
    *,
    client: AuthenticatedClient,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500]:
    """ Deletes an entry from a project spend plan.

    Args:
        id (int):
        fs_id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
fs_id=fs_id,
reprocess=reprocess,
skip_validation=skip_validation,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    fs_id: int,
    *,
    client: AuthenticatedClient,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500 | None:
    """ Deletes an entry from a project spend plan.

    Args:
        id (int):
        fs_id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSpendPlanEntryResponse200 | DeleteSpendPlanEntryResponse400 | DeleteSpendPlanEntryResponse401 | DeleteSpendPlanEntryResponse403 | DeleteSpendPlanEntryResponse404 | DeleteSpendPlanEntryResponse422 | DeleteSpendPlanEntryResponse500
     """


    return (await asyncio_detailed(
        id=id,
fs_id=fs_id,
client=client,
reprocess=reprocess,
skip_validation=skip_validation,

    )).parsed
