from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_spend_plan_entry_response_200 import PatchSpendPlanEntryResponse200
from ...models.patch_spend_plan_entry_response_400 import PatchSpendPlanEntryResponse400
from ...models.patch_spend_plan_entry_response_401 import PatchSpendPlanEntryResponse401
from ...models.patch_spend_plan_entry_response_403 import PatchSpendPlanEntryResponse403
from ...models.patch_spend_plan_entry_response_404 import PatchSpendPlanEntryResponse404
from ...models.patch_spend_plan_entry_response_422 import PatchSpendPlanEntryResponse422
from ...models.patch_spend_plan_entry_response_500 import PatchSpendPlanEntryResponse500
from ...models.spend_plan_v4_patch_list import SpendPlanV4PatchList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: SpendPlanV4PatchList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["reprocess"] = reprocess

    params["skipValidation"] = skip_validation


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v4/project/{id}/spend-plan".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchSpendPlanEntryResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchSpendPlanEntryResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchSpendPlanEntryResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchSpendPlanEntryResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchSpendPlanEntryResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchSpendPlanEntryResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchSpendPlanEntryResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500]:
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
    body: SpendPlanV4PatchList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500]:
    """ Updates one or more entries in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PatchList): SpendPlanV4PatchList defines a list of spend plan records to
            be updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500]
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
    body: SpendPlanV4PatchList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500 | None:
    """ Updates one or more entries in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PatchList): SpendPlanV4PatchList defines a list of spend plan records to
            be updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500
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
    body: SpendPlanV4PatchList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500]:
    """ Updates one or more entries in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PatchList): SpendPlanV4PatchList defines a list of spend plan records to
            be updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500]
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
    body: SpendPlanV4PatchList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500 | None:
    """ Updates one or more entries in a spend plan.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PatchList): SpendPlanV4PatchList defines a list of spend plan records to
            be updates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSpendPlanEntryResponse200 | PatchSpendPlanEntryResponse400 | PatchSpendPlanEntryResponse401 | PatchSpendPlanEntryResponse403 | PatchSpendPlanEntryResponse404 | PatchSpendPlanEntryResponse422 | PatchSpendPlanEntryResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
reprocess=reprocess,
skip_validation=skip_validation,

    )).parsed
