from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_billing_rule_segment_response_400 import DeleteBillingRuleSegmentResponse400
from ...models.delete_billing_rule_segment_response_401 import DeleteBillingRuleSegmentResponse401
from ...models.delete_billing_rule_segment_response_403 import DeleteBillingRuleSegmentResponse403
from ...models.delete_billing_rule_segment_response_500 import DeleteBillingRuleSegmentResponse500
from typing import cast



def _get_kwargs(
    id: int,
    segment_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/beta/billing-rule/{id}/segments/{segment_id}".format(id=quote(str(id), safe=""),segment_id=quote(str(segment_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteBillingRuleSegmentResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteBillingRuleSegmentResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteBillingRuleSegmentResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = DeleteBillingRuleSegmentResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    segment_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500]:
    """ 
    Args:
        id (int):
        segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
segment_id=segment_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    segment_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500 | None:
    """ 
    Args:
        id (int):
        segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500
     """


    return sync_detailed(
        id=id,
segment_id=segment_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    segment_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500]:
    """ 
    Args:
        id (int):
        segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
segment_id=segment_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    segment_id: int,
    *,
    client: AuthenticatedClient,

) -> Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500 | None:
    """ 
    Args:
        id (int):
        segment_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBillingRuleSegmentResponse400 | DeleteBillingRuleSegmentResponse401 | DeleteBillingRuleSegmentResponse403 | DeleteBillingRuleSegmentResponse500
     """


    return (await asyncio_detailed(
        id=id,
segment_id=segment_id,
client=client,

    )).parsed
