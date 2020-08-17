# -*- coding: utf-8 -*-

"""Get triples from the NELL-995.test data set."""

import os

from ..base import PathDataSet

__all__ = [
    'NELL995_TRAIN_PATH',
    'NELL995_TEST_PATH',
    'NELL995_VALIDATE_PATH',
    'NELL995',
]

HERE = os.path.abspath(os.path.dirname(__file__))

NELL995_TRAIN_PATH = os.path.join(HERE, 'train.txt')
NELL995_TEST_PATH = os.path.join(HERE, 'test.txt')
NELL995_VALIDATE_PATH = os.path.join(HERE, 'valid.txt')


class NELL995(PathDataSet):
    """The NELL-995.test data set."""

    def __init__(self, **kwargs):
        super().__init__(
            training_path=NELL995_TRAIN_PATH,
            testing_path=NELL995_TEST_PATH,
            validation_path=NELL995_VALIDATE_PATH,
            **kwargs,
        )
