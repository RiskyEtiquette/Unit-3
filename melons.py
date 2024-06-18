import csv

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    def __repr__(self):
        return f"<Melon: {self.melon_id}, {self.common_name}>"

    def price_str(self):
        return f"${self.price:.2f}"

melon_dict = {}

with open("melons.csv", "r") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon = Melon(
            melon_id=row["melon_id"],
            common_name=row["common_name"],
            price=float(row["price"]),
            image_url=row["image_url"],
            color=row["color"],
            seedless=row["seedless"].lower() == 'true'
        )
        melon_dict[melon.melon_id] = melon

def get_by_id(melon_id):
    return melon_dict.get(melon_id)

def get_all():
    return list(melon_dict.values())
