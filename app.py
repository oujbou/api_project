from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging
from fake_data_app import create_app

from datetime import date


store_dict = create_app()
app = FastAPI()


@app.get("/")
def visit(
    store_name: str, year: int, month: int, day: int, sensor_id: int | None = None
) -> JSONResponse:
    print("Hello!")

    # If store not in dictionary
    if not (store_name in store_dict.keys()):
        return JSONResponse(status_code=404, content="Store Not Found")

    # Check the value of the store_id
    if sensor_id and (sensor_id > 7 or sensor_id < 0):
        return JSONResponse(
            status_code=404, content="Sensor_id should be between 0 and 7"
        )

    # Check the year
    if year < 2021:
        return JSONResponse(status_code=404, content="No data before 2021")

    # Check the date
    try:
        requested_date = date(year, month, day)
    except ValueError as e:
        logging.error(f"Could not cast date: {e}")
        return JSONResponse(status_code=404, content="Enter a valid date")

    # Check the date is in the past
    if date.today() < requested_date:
        return JSONResponse(status_code=404, content="Chose a date in the past")

    # If no sensor chosen, return the visits for the whole store
    if sensor_id is None:
        visit_counts = store_dict[store_name].get_store_traffic(requested_date)
    else:
        visit_counts = store_dict[store_name].get_sensor_traffic(
            sensor_id, requested_date
        )

    if visit_counts < 0:
        return JSONResponse(
            status_code=404, content="The store was closed, try another date"
        )
    return JSONResponse(status_code=200, content=visit_counts)
