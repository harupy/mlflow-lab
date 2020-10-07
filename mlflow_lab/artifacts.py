import os
import tempfile
from contextlib import contextmanager

import mlflow
import numpy as np


@contextmanager
def _log_artifact_contextmanager(filename, artifact_path=None):
    """
    A context manager to make it easier to log an artifact.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = os.path.join(tmp_dir, filename)
        yield tmp_path
        mlflow.log_artifact(tmp_path, artifact_path)


def log_numpy(numpy_obj, filename, artifact_path=None):
    """
    Log a numpy object.

    Parameters
    ----------
    numpy_obj : numpy object
        A numpy object to log.
    filename : str
        An output file name.
    artifact_path : str
        An artifact path to store the numpy object.

    Returns
    -------
    None
    """
    with _log_artifact_contextmanager(filename, artifact_path) as tmp_path:
        np.save(tmp_path, numpy_obj)
