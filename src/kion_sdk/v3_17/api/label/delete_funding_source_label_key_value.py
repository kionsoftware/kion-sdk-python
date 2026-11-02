from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_funding_source_label_key_value_response_200 import DeleteFundingSourceLabelKeyValueResponse200
from ...models.delete_funding_source_label_key_value_response_400 import DeleteFundingSourceLabelKeyValueResponse400
from ...models.delete_funding_source_label_key_value_response_401 import DeleteFundingSourceLabelKeyValueResponse401
from ...models.delete_funding_source_label_key_value_response_404 import DeleteFundingSourceLabelKeyValueResponse404
from ...models.delete_funding_source_label_key_value_response_422 import DeleteFundingSourceLabelKeyValueResponse422
from ...models.delete_funding_source_label_key_value_response_500 import DeleteFundingSourceLabelKeyValueResponse500
from typing import cast



def _get_kwargs(
    funding_source_id: int,
    *,
    key: str,
    value: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["key"] = key

    params["value"] = value


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/funding-source/{funding_source_id}/labels".format(funding_source_id=quote(str(funding_source_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteFundingSourceLabelKeyValueResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteFundingSourceLabelKeyValueResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteFundingSourceLabelKeyValueResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteFundingSourceLabelKeyValueResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteFundingSourceLabelKeyValueResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteFundingSourceLabelKeyValueResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> Response[DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500]:
    """ Removes a label from the given funding source by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/funding-source/{funding_source_id}/labels?key=Department&value=Engineering</pre>

    Args:
        funding_source_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,
key=key,
value=value,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500 | None:
    """ Removes a label from the given funding source by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/funding-source/{funding_source_id}/labels?key=Department&value=Engineering</pre>

    Args:
        funding_source_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500
     """


    return sync_detailed(
        funding_source_id=funding_source_id,
client=client,
key=key,
value=value,

    ).parsed

async def asyncio_detailed(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> Response[DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500]:
    """ Removes a label from the given funding source by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/funding-source/{funding_source_id}/labels?key=Department&value=Engineering</pre>

    Args:
        funding_source_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500]
     """


    kwargs = _get_kwargs(
        funding_source_id=funding_source_id,
key=key,
value=value,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    funding_source_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500 | None:
    """ Removes a label from the given funding source by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/funding-source/{funding_source_id}/labels?key=Department&value=Engineering</pre>

    Args:
        funding_source_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFundingSourceLabelKeyValueResponse200 | DeleteFundingSourceLabelKeyValueResponse400 | DeleteFundingSourceLabelKeyValueResponse401 | DeleteFundingSourceLabelKeyValueResponse404 | DeleteFundingSourceLabelKeyValueResponse422 | DeleteFundingSourceLabelKeyValueResponse500
     """


    return (await asyncio_detailed(
        funding_source_id=funding_source_id,
client=client,
key=key,
value=value,

    )).parsed
