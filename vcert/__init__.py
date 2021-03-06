#
# Copyright 2019 Venafi, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .connection_cloud import CloudConnection
from .connection_tpp import TPPConnection
from .connection_fake import FakeConnection
from .common import CertificateRequest, CommonConnection, KeyTypes, RevocationRequest


def Connection(url=None, token=None, user=None, password=None, fake=False, http_request_kwargs=None):
    """
    Return connection based on credentials list.
    Venafi Platform (TPP) required URL, user, password
    Cloud required token and optional URL
    Fake required no parameters
    :param str url: TPP or Venafi Cloud URL (for Cloud is optional)
    :param str token: Venafi Cloud token
    :param str user: TPP user
    :param str password: TPP password
    :param bool fake: Use fake connection
    :param dict[str, Any] http_request_kwargs: Option for work with untrusted  https certificate (only for TPP).
    :rtype CommonConnection:
    """
    if fake:
        return FakeConnection()
    if url and user and password:
        return TPPConnection(user=user, password=password, url=url, http_request_kwargs=http_request_kwargs)
    if token:
        return CloudConnection(token=token, url=url, http_request_kwargs=http_request_kwargs)
    else:
        raise Exception("Bad credentials list")
