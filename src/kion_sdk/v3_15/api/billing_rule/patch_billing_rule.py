from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.billing_rule_update import BillingRuleUpdate
from ...models.patch_billing_rule_response_400 import PatchBillingRuleResponse400
from ...models.patch_billing_rule_response_401 import PatchBillingRuleResponse401
from ...models.patch_billing_rule_response_403 import PatchBillingRuleResponse403
from ...models.patch_billing_rule_response_422 import PatchBillingRuleResponse422
from ...models.patch_billing_rule_response_500 import PatchBillingRuleResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: BillingRuleUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/billing-rule/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = PatchBillingRuleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchBillingRuleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchBillingRuleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PatchBillingRuleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchBillingRuleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500]:
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
    body: BillingRuleUpdate,

) -> Response[Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500]:
    """ Updates a BillingRules by ID in the application.

    Args:
        id (int):
        body (BillingRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BillingRuleUpdate,

) -> Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500 | None:
    """ Updates a BillingRules by ID in the application.

    Args:
        id (int):
        body (BillingRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BillingRuleUpdate,

) -> Response[Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500]:
    """ Updates a BillingRules by ID in the application.

    Args:
        id (int):
        body (BillingRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: BillingRuleUpdate,

) -> Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500 | None:
    """ Updates a BillingRules by ID in the application.

    Args:
        id (int):
        body (BillingRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchBillingRuleResponse400 | PatchBillingRuleResponse401 | PatchBillingRuleResponse403 | PatchBillingRuleResponse422 | PatchBillingRuleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
