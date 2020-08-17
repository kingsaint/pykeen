# -*- coding: utf-8 -*-

"""Get triples from the WN18RR data set."""

import os

from ..base import PathDataSet

__all__ = [
    'WN18RR_TRAIN_PATH',
    'WN18RR_TEST_PATH',
    'WN18RR_VALIDATE_PATH',
    'WN18RR',
]

HERE = os.path.abspath(os.path.dirname(__file__))

WN18RR_TRAIN_PATH = os.path.join(HERE, 'train.txt')
WN18RR_TEST_PATH = os.path.join(HERE, 'test.txt')
WN18RR_VALIDATE_PATH = os.path.join(HERE, 'valid.txt')


class WN18RR(PathDataSet):
    """The Kinships data set."""

    def __init__(self, **kwargs):
        super().__init__(
            training_path=WN18RR_TRAIN_PATH,
            testing_path=WN18RR_TEST_PATH,
            validation_path=WN18RR_VALIDATE_PATH,
            **kwargs,
        )
