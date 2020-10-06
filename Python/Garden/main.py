from plants import Flower, Tree
from garden import Garden

garden = Garden()

garden.add(Flower("yellow"))
garden.add(Flower("blue"))
garden.add(Tree("purple"))
garden.add(Tree("orange"))

garden.garden_status()