# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
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


import pytest
from nemo.collections.common.tokenizers.column_coder import FloatCode
import pandas as pd
import numpy as np


class TestColumnCoder:

    @pytest.mark.unit
    def test_float(self):
        np.random.seed(1234)
        array = np.random.random(100)
        series = pd.Series(array)
        float_coder = FloatCode('t', series, 5, 0, 10, False)
        r = float_coder.encode('0.323')
        assert np.array_equal(np.array(r), np.array([37, 32, 27, 15, 1]))
        decoded = float_coder.decode(r)
        assert decoded == '0.32287'
        r = float_coder.encode('1.323')
        assert np.array_equal(np.array(r), np.array([37, 36, 24, 10, 1]))
        decoded = float_coder.decode(r)
        assert decoded == '0.90288'
        r = float_coder.encode('nan')
        assert np.array_equal(np.array(r), np.array([38, 36, 29, 19, 9]))
        decoded = float_coder.decode(r)
        assert decoded == 'nan'

        float_coder = FloatCode('t', series, 5, 0, 377, True)
        r = float_coder.encode('0.323')
        assert np.array_equal(np.array(r), np.array([1508, 1234, 1036, 613, 338]))
        decoded = float_coder.decode(r)
        assert decoded == '0.32299999995'
        r = float_coder.encode('nan')
        assert np.array_equal(np.array(r), np.array([1885, 1507, 1130, 753, 376]))
        decoded = float_coder.decode(r)
        assert decoded == 'nan'
 