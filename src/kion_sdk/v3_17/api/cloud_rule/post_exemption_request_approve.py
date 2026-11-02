from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_rule_exemption_request_update import CloudRuleExemptionRequestUpdate
from ...models.post_exemption_request_approve_response_200 import PostExemptionRequestApproveResponse200
from ...models.post_exemption_request_approve_response_400 import PostExemptionRequestApproveResponse400
from ...models.post_exemption_request_approve_response_401 import PostExemptionRequestApproveResponse401
from ...models.post_exemption_request_approve_response_403 import PostExemptionRequestApproveResponse403
from ...models.post_exemption_request_approve_response_404 import PostExemptionRequestApproveResponse404
from ...models.post_exemption_request_approve_response_500 import PostExemptionRequestApproveResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CloudRuleExemptionRequestUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/cloud-rule/exemption-request/{id}/approve".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500 | None:
    if response.status_code == 200:
        response_200 = PostExemptionRequestApproveResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostExemptionRequestApproveResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostExemptionRequestApproveResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostExemptionRequestApproveResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostExemptionRequestApproveResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PostExemptionRequestApproveResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500]:
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
    body: CloudRuleExemptionRequestUpdate | Unset = UNSET,

) -> Response[PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500]:
    """ Approves an exemption request and creates the exemption.

    Args:
        id (int):
        body (CloudRuleExemptionRequestUpdate | Unset): CloudRuleExemptionRequestUpdate defines
            the structure used for updating exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500]
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
    body: CloudRuleExemptionRequestUpdate | Unset = UNSET,

) -> PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500 | None:
    """ Approves an exemption request and creates the exemption.

    Args:
        id (int):
        body (CloudRuleExemptionRequestUpdate | Unset): CloudRuleExemptionRequestUpdate defines
            the structure used for updating exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500
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
    body: CloudRuleExemptionRequestUpdate | Unset = UNSET,

) -> Response[PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500]:
    """ Approves an exemption request and creates the exemption.

    Args:
        id (int):
        body (CloudRuleExemptionRequestUpdate | Unset): CloudRuleExemptionRequestUpdate defines
            the structure used for updating exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500]
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
    body: CloudRuleExemptionRequestUpdate | Unset = UNSET,

) -> PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500 | None:
    """ Approves an exemption request and creates the exemption.

    Args:
        id (int):
        body (CloudRuleExemptionRequestUpdate | Unset): CloudRuleExemptionRequestUpdate defines
            the structure used for updating exemption requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostExemptionRequestApproveResponse200 | PostExemptionRequestApproveResponse400 | PostExemptionRequestApproveResponse401 | PostExemptionRequestApproveResponse403 | PostExemptionRequestApproveResponse404 | PostExemptionRequestApproveResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
