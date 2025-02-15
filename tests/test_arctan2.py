# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import textwrap

from apibase import APIBase

obj = APIBase("torch.arctan2")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([ 0.9041,  0.0196, -0.3108, -2.4423])
        other = torch.tensor([ 0.2341,  0.2539, -0.6256, -0.6448])
        result = torch.arctan2(input, other)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.arctan2(torch.tensor([ 0.9041,  0.0196, -0.3108, -2.4423]), torch.tensor([ 0.2341,  0.2539, -0.6256, -0.6448]))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([ 0.9041,  0.0196, -0.3108, -2.4423])
        other = torch.tensor([ 0.2341,  0.2539, -0.6256, -0.6448])
        out = torch.tensor(input)
        result = torch.arctan2(input, other, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])
