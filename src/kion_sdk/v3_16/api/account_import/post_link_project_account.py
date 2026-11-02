from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.link_project_account import LinkProjectAccount
from ...models.post_link_project_account_response_200 import PostLinkProjectAccountResponse200
from ...models.post_link_project_account_response_400 import PostLinkProjectAccountResponse400
from ...models.post_link_project_account_response_401 import PostLinkProjectAccountResponse401
from ...models.post_link_project_account_response_403 import PostLinkProjectAccountResponse403
from ...models.post_link_project_account_response_422 import PostLinkProjectAccountResponse422
from ...models.post_link_project_account_response_500 import PostLinkProjectAccountResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: LinkProjectAccount,
    account_type: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["account_type"] = account_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/payer/{id}/link-project-account".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500 | None:
    if response.status_code == 200:
        response_200 = PostLinkProjectAccountResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostLinkProjectAccountResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostLinkProjectAccountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostLinkProjectAccountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostLinkProjectAccountResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostLinkProjectAccountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500]:
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
    body: LinkProjectAccount,
    account_type: str | Unset = UNSET,

) -> Response[PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500]:
    """ Links an account from the organization to a project.

    Args:
        id (int):
        account_type (str | Unset):
        body (LinkProjectAccount): LinkProjectAccount is used to link an account to a CT project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
account_type=account_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: LinkProjectAccount,
    account_type: str | Unset = UNSET,

) -> PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500 | None:
    """ Links an account from the organization to a project.

    Args:
        id (int):
        account_type (str | Unset):
        body (LinkProjectAccount): LinkProjectAccount is used to link an account to a CT project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
account_type=account_type,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: LinkProjectAccount,
    account_type: str | Unset = UNSET,

) -> Response[PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500]:
    """ Links an account from the organization to a project.

    Args:
        id (int):
        account_type (str | Unset):
        body (LinkProjectAccount): LinkProjectAccount is used to link an account to a CT project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
account_type=account_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: LinkProjectAccount,
    account_type: str | Unset = UNSET,

) -> PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500 | None:
    """ Links an account from the organization to a project.

    Args:
        id (int):
        account_type (str | Unset):
        body (LinkProjectAccount): LinkProjectAccount is used to link an account to a CT project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinkProjectAccountResponse200 | PostLinkProjectAccountResponse400 | PostLinkProjectAccountResponse401 | PostLinkProjectAccountResponse403 | PostLinkProjectAccountResponse422 | PostLinkProjectAccountResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
account_type=account_type,

    )).parsed
