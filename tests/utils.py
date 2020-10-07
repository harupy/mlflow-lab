import mlflow


def yield_artifacts(run_id, path=None):
    """
    Yields all artifacts in the specified run.
    """
    client = mlflow.tracking.MlflowClient()
    for item in client.list_artifacts(run_id, path):
        if item.is_dir:
            yield from yield_artifacts(run_id, item.path)
        else:
            yield item.path
