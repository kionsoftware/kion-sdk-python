from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_project_label_key_value_response_200 import DeleteProjectLabelKeyValueResponse200
from ...models.delete_project_label_key_value_response_400 import DeleteProjectLabelKeyValueResponse400
from ...models.delete_project_label_key_value_response_401 import DeleteProjectLabelKeyValueResponse401
from ...models.delete_project_label_key_value_response_404 import DeleteProjectLabelKeyValueResponse404
from ...models.delete_project_label_key_value_response_422 import DeleteProjectLabelKeyValueResponse422
from ...models.delete_project_label_key_value_response_500 import DeleteProjectLabelKeyValueResponse500
from typing import cast



def _get_kwargs(
    project_id: int,
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
        "url": "/v3/project/{project_id}/labels".format(project_id=quote(str(project_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteProjectLabelKeyValueResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteProjectLabelKeyValueResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteProjectLabelKeyValueResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteProjectLabelKeyValueResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteProjectLabelKeyValueResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteProjectLabelKeyValueResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> Response[DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500]:
    """ Removes a label from the given project by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/project/{project_id}/labels?key=Department&value=Engineering</pre>

    Args:
        project_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
key=key,
value=value,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500 | None:
    """ Removes a label from the given project by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/project/{project_id}/labels?key=Department&value=Engineering</pre>

    Args:
        project_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500
     """


    return sync_detailed(
        project_id=project_id,
client=client,
key=key,
value=value,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> Response[DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500]:
    """ Removes a label from the given project by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/project/{project_id}/labels?key=Department&value=Engineering</pre>

    Args:
        project_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
key=key,
value=value,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,
    key: str,
    value: str,

) -> DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500 | None:
    """ Removes a label from the given project by key/value pair.

     You must pass a single key/value pair via the query string, for example:
    <pre>DELETE /v3/project/{project_id}/labels?key=Department&value=Engineering</pre>

    Args:
        project_id (int):
        key (str):
        value (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectLabelKeyValueResponse200 | DeleteProjectLabelKeyValueResponse400 | DeleteProjectLabelKeyValueResponse401 | DeleteProjectLabelKeyValueResponse404 | DeleteProjectLabelKeyValueResponse422 | DeleteProjectLabelKeyValueResponse500
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
key=key,
value=value,

    )).parsed
