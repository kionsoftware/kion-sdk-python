from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reprioritize_spend_plan_entry_response_200 import ReprioritizeSpendPlanEntryResponse200
from ...models.reprioritize_spend_plan_entry_response_400 import ReprioritizeSpendPlanEntryResponse400
from ...models.reprioritize_spend_plan_entry_response_401 import ReprioritizeSpendPlanEntryResponse401
from ...models.reprioritize_spend_plan_entry_response_403 import ReprioritizeSpendPlanEntryResponse403
from ...models.reprioritize_spend_plan_entry_response_404 import ReprioritizeSpendPlanEntryResponse404
from ...models.reprioritize_spend_plan_entry_response_422 import ReprioritizeSpendPlanEntryResponse422
from ...models.reprioritize_spend_plan_entry_response_500 import ReprioritizeSpendPlanEntryResponse500
from ...models.spend_plan_reprioritize import SpendPlanReprioritize
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: SpendPlanReprioritize,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["reprocess"] = reprocess

    params["skipValidation"] = skip_validation


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/project/{id}/spend-plan/reprioritize".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500 | None:
    if response.status_code == 200:
        response_200 = ReprioritizeSpendPlanEntryResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ReprioritizeSpendPlanEntryResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ReprioritizeSpendPlanEntryResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ReprioritizeSpendPlanEntryResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ReprioritizeSpendPlanEntryResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = ReprioritizeSpendPlanEntryResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ReprioritizeSpendPlanEntryResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500]:
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
    body: SpendPlanReprioritize,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500]:
    """ Reprioritized the funding source order in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanReprioritize): SpendPlanReprioritize defines a list of funding source IDs
            for reprioritizing a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
reprocess=reprocess,
skip_validation=skip_validation,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SpendPlanReprioritize,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500 | None:
    """ Reprioritized the funding source order in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanReprioritize): SpendPlanReprioritize defines a list of funding source IDs
            for reprioritizing a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
reprocess=reprocess,
skip_validation=skip_validation,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SpendPlanReprioritize,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500]:
    """ Reprioritized the funding source order in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanReprioritize): SpendPlanReprioritize defines a list of funding source IDs
            for reprioritizing a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
reprocess=reprocess,
skip_validation=skip_validation,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SpendPlanReprioritize,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500 | None:
    """ Reprioritized the funding source order in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanReprioritize): SpendPlanReprioritize defines a list of funding source IDs
            for reprioritizing a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReprioritizeSpendPlanEntryResponse200 | ReprioritizeSpendPlanEntryResponse400 | ReprioritizeSpendPlanEntryResponse401 | ReprioritizeSpendPlanEntryResponse403 | ReprioritizeSpendPlanEntryResponse404 | ReprioritizeSpendPlanEntryResponse422 | ReprioritizeSpendPlanEntryResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
reprocess=reprocess,
skip_validation=skip_validation,

    )).parsed
