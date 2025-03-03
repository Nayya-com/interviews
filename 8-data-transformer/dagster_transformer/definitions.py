import dagster as dg

from dagster_transformer.assets import (
    read_sample_enrollment_data,
    transform_enrollment_data,
    write_enrollment_data_to_db,
)

defs = dg.Definitions(
    assets=[
        read_sample_enrollment_data,
        transform_enrollment_data,
        write_enrollment_data_to_db,
    ],
)
