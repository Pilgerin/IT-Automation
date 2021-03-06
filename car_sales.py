# !/usr/bin/env python3

import json
import locale
import os
import sys
from reportlab.platypus import Paragraph, Spacer, Table, Image
import emails
import reports


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
    # locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0}
    popular_year = {}
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        # TODO: also handle max sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales["total_sales"] = item["total_sales"]
            max_sales["car_model"] = item["car"]["car_model"]

        # TODO: also handle most popular car_year
        if item["car"]["car_year"] not in popular_year.keys():
            popular_year[item["car"]["car_year"]] = item["total_sales"]
        else:
            popular_year[item["car"]["car_year"]] += item["total_sales"]
        all_values = popular_year.values()
        max_value = max(all_values)
        best_year = max(popular_year, key=popular_year.get)

        summary = ["The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
            "The {} had the most sales: {}".format(max_sales["car_model"], max_sales["total_sales"]),
            "The most popular year was {} with {} sales.".format(best_year, max_value), ]

        return summary


def cars_dict_to_table(cars):
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in cars:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data


if __name__ == "__main__":
    data = load_data("car_sales.json")
    summary = process_data(data)
    paragraph = "<br/>".join(summary)
    print(summary)
    reports.generate("cars.pdf", "Car report", paragraph, cars_dict_to_table(data))
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Sales summary for last month"
    body = "<\n>".join(summary)
    message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
    emails.send(message)
