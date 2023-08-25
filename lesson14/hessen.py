from random import choice

capital = "Wiesbaden"

rapper = "Reezy"

phone = "Samsung"

soccer_club = "Real Madrid"


def randomfunfact():
    funfacts = [
        "Hessen is the wealthiest state in Germany",
        "Element 110 on the periodic table, Darmstadtium, is named after Darmstadt, a city in Hessen",
        "The Frankfurt International Airport is one of the largest financial centers in the world.",
        "Hessen has a population of over 6 million people",
        "The english way of saying Hessen is Hesse.",
        "The term Hesse comes from the Germanic tribe Chatti"
	]

    index = choice("0123345")

    print(funfacts[int(index)])

if __name__ == "__main__": 
    randomfunfact()