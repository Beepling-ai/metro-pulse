def names(env: str = "dev", catalog: str = "workspace") -> dict:
    """One place that decides where every table and file lives, per environment."""
    schema = f"metro_{env}"
    return {
        "catalog": catalog,
        "schema": schema,
        "fq": f"{catalog}.{schema}",
        "vol": f"/Volumes/{catalog}/{schema}",
    }
