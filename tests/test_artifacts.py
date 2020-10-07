import mlflow
import numpy as np
import pytest

import mlflow_lab
from tests.utils import yield_artifacts


@pytest.mark.parametrize("numpy_obj", [np.float(0.0), np.array([0.0])])
def test_log_numpy(numpy_obj):

    with mlflow.start_run() as run:
        mlflow_lab.artifacts.log_numpy(numpy_obj, "test.npy")
        mlflow_lab.artifacts.log_numpy(numpy_obj, "test.npy", artifact_path="dir")

    artifacts = set(yield_artifacts(run.info.run_id))
    assert artifacts == {"test.npy", "dir/test.npy"}
