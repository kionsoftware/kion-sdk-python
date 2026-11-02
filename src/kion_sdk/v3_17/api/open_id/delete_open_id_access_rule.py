from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_open_id_access_rule_response_200 import DeleteOpenIDAccessRuleResponse200
from ...models.delete_open_id_access_rule_response_400 import DeleteOpenIDAccessRuleResponse400
from ...models.delete_open_id_access_rule_response_401 import DeleteOpenIDAccessRuleResponse401
from ...models.delete_open_id_access_rule_response_403 import DeleteOpenIDAccessRuleResponse403
from ...models.delete_open_id_access_rule_response_404 import DeleteOpenIDAccessRuleResponse404
from ...models.delete_open_id_access_rule_response_500 import DeleteOpenIDAccessRuleResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v4/idms/open-id/access-rule/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOpenIDAccessRuleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteOpenIDAccessRuleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOpenIDAccessRuleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOpenIDAccessRuleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOpenIDAccessRuleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteOpenIDAccessRuleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500]:
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

) -> Response[DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500]:
    """ Deletes an openID IDMS access rule from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500 | None:
    """ Deletes an openID IDMS access rule from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500]:
    """ Deletes an openID IDMS access rule from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500 | None:
    """ Deletes an openID IDMS access rule from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOpenIDAccessRuleResponse200 | DeleteOpenIDAccessRuleResponse400 | DeleteOpenIDAccessRuleResponse401 | DeleteOpenIDAccessRuleResponse403 | DeleteOpenIDAccessRuleResponse404 | DeleteOpenIDAccessRuleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
