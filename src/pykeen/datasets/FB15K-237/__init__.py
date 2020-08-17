# -*- coding: utf-8 -*-

"""Get triples from the FB15k-237 data set."""

import os

from ..base import PathDataSet

__all__ = [
    'FB15k237_TRAIN_PATH',
    'FB15k237_TEST_PATH',
    'FB15k237_VALIDATE_PATH',
    'FB15k237',
]

HERE = os.path.abspath(os.path.dirname(__file__))

FB15k237_TRAIN_PATH = os.path.join(HERE, 'train.txt')
FB15k237_TEST_PATH = os.path.join(HERE, 'test.txt')
FB15k237_VALIDATE_PATH = os.path.join(HERE, 'valid.txt')


class FB15k237(PathDataSet):
    """The FB15k-237 data set."""

    def __init__(self, **kwargs):
        super().__init__(
            training_path=FB15k237_TRAIN_PATH,
            testing_path=FB15k237_TEST_PATH,
            validation_path=FB15k237_VALIDATE_PATH,
            **kwargs,
        )
