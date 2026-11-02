from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.put_spend_plan_response_200 import PutSpendPlanResponse200
from ...models.put_spend_plan_response_400 import PutSpendPlanResponse400
from ...models.put_spend_plan_response_401 import PutSpendPlanResponse401
from ...models.put_spend_plan_response_403 import PutSpendPlanResponse403
from ...models.put_spend_plan_response_404 import PutSpendPlanResponse404
from ...models.put_spend_plan_response_422 import PutSpendPlanResponse422
from ...models.put_spend_plan_response_500 import PutSpendPlanResponse500
from ...models.spend_plan_v4_put_list import SpendPlanV4PutList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: SpendPlanV4PutList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["reprocess"] = reprocess

    params["skipValidation"] = skip_validation


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v4/project/{id}/spend-plan".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500 | None:
    if response.status_code == 200:
        response_200 = PutSpendPlanResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutSpendPlanResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutSpendPlanResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutSpendPlanResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PutSpendPlanResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutSpendPlanResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutSpendPlanResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500]:
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
    body: SpendPlanV4PutList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500]:
    """ Updates a spend plan by project ID in the application.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PutList): SpendPlanV4PutList defines a full update for a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500]
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
    body: SpendPlanV4PutList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500 | None:
    """ Updates a spend plan by project ID in the application.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PutList): SpendPlanV4PutList defines a full update for a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500
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
    body: SpendPlanV4PutList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> Response[PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500]:
    """ Updates a spend plan by project ID in the application.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PutList): SpendPlanV4PutList defines a full update for a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500]
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
    body: SpendPlanV4PutList,
    reprocess: bool | Unset = UNSET,
    skip_validation: bool | Unset = UNSET,

) -> PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500 | None:
    """ Updates a spend plan by project ID in the application.

    Args:
        id (int):
        reprocess (bool | Unset):
        skip_validation (bool | Unset):
        body (SpendPlanV4PutList): SpendPlanV4PutList defines a full update for a spend plan.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSpendPlanResponse200 | PutSpendPlanResponse400 | PutSpendPlanResponse401 | PutSpendPlanResponse403 | PutSpendPlanResponse404 | PutSpendPlanResponse422 | PutSpendPlanResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
reprocess=reprocess,
skip_validation=skip_validation,

    )).parsed
