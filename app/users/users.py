from enum import Enum
from typing import List

import requests as requests
from flask import Blueprint, render_template, request
from pydantic import BaseModel

from config import settings

bp = Blueprint(
    import_name=__name__,
    name="Edamam",
    url_prefix="/",
    template_folder="templates",
)


class RequestEdamam:

    @staticmethod
    def get_food(food: str):
        url = f"https://api.edamam.com/api/food-database/v2/parser?app_id={settings.EDAMAM_APP_ID}&app_key={settings.EDAMAM_APP_KEY}&ingr={food}&nutrition-type=cooking"
        return requests.get(url)


class ProductEdamam:
    def __init__(self, new_product: str, mass: float):
        self.product = new_product
        self.mass = mass
        self.enerc_kcal: float = self.get_enerc_kcal() * self.mass / 100

    def get_enerc_kcal(self):
        req = RequestEdamam.get_food(self.product)
        if req.json()["parsed"]:
            return req.json()["parsed"][0]["food"]["nutrients"]["ENERC_KCAL"]
        return 0


class DailyProducts:
    def __init__(self):
        self.products: List[ProductEdamam] = []

    def add_product(self, new_product: ProductEdamam):
        self.products.append(new_product)


daily_products = DailyProducts()


@bp.route("/", methods=["GET"])
def get_html_index():

    kwargs = {
        "mass": 0,
        "height": 0,
        "age": 0,
        "sex": Sex.male,
    }
    return render_template("index.html", calculate=Calculate(**kwargs), daily_products=daily_products.products)


@bp.route("/", methods=["POST"])
def post_html_index():

    sexCustom = request.form.get("sexCustom", Sex.male)
    massCustom = float(request.form.get("massCustom", 0))
    ageCustom = float(request.form.get("ageCustom", 0))
    heightCustom = float(request.form.get("heightCustom", 0))
    kwargs = {
        "mass": massCustom,
        "height": heightCustom,
        "age": ageCustom,
        "sex": sexCustom,
    }
    if new_product := request.form.get("productCustom"):
        mass_product = float(request.form.get("productmassCustom", 0))
        np = ProductEdamam(new_product, mass_product)
        daily_products.add_product(np)

    return render_template("index.html", calculate=Calculate(**kwargs), daily_products=daily_products.products)


class Sex(Enum):
    male = "male"
    female = "female"


class Calculate(BaseModel):
    mass: float
    height: float
    age: float
    sex: Sex

    def _male_heat_production(self):
        return 13.7516 * self.mass + 5.0033 * self.height - 6.7550 * self.age + 66.4730

    def _female_heat_production(self):
        return 9.5634 * self.mass + 1.8496 * self.height - 4.6756 * self.age + 655.0955

    def heat_production(self):
        return (
            self._male_heat_production()
            if self.sex == Sex.male
            else self._female_heat_production()
        )


if __name__ == "__main__":
    pass
