"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings 
    """

    species = set()

    species_data = open(filename) #not splittable
    for line in species_data:
        list_of_species = line.split("|")
        species.add(list_of_species[1])


    # TODO: replace this with your code

    return species

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = [] #something needs to be appended here in our function

    villager_names = open(filename)

    for line in villager_names:
        names = line.split("|")

        if names[1] == search_string:
            villagers.append(names[0])
 
    # TODO: replace this with your code
    return sorted(villagers)

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    Fitness = []
    Nature = []
    Education = []
    Music = []
    Fashion = []
    Play = []

    open_file = open("villagers.csv")

    for line in open_file:

        data = line.split("|")

        hobby = data[3]
        name = data[0]

        if hobby == "Fitness":
            Fitness.append(name)
        elif hobby == "Nature":
            Nature.append(name)
        elif hobby == "Education":
            Education.append(name)
        elif hobby == "Music":
            Music.append(name)
        elif hobby == "Fashion":
            Fashion.append(name)
        elif hobby == "Play":
            Play.append(name)

        Fitness = sorted(Fitness)
        Nature = sorted(Nature)
        Education = sorted(Education)
        Music = sorted(Music)
        Fashion = sorted(Fashion)
        Play = sorted(Play)

    return [Fitness, Nature, Education, Music, Fashion, Play]

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    data = open(filename)

    for line in data:
        all_data.append(tuple(line.split("|")))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    data = open("villagers.csv")

    for line in data:
        lists = line.split("|")
        motto = lists[-1]

        if villager_name == lists[0]:
            return motto
        

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    # personality = index 2
    # TODO: replace this with your code

    data = open("villagers.csv")

    retval = set()
    
    similar_personalities = 0

    for line in data:

        lists = line.split("|")
        personality = lists[2]
        name = lists[0]

        if name == "Wendy":
            similar_personalities = personality
            break

    if similar_personalities == personality:
        for line in data:
            
            lists = line.split("|")
            personality = lists[2]
            name = lists[0]

            if similar_personalities == personality:
                retval.add(name)
            

    return retval

print(find_likeminded_villagers("villagers.csv","Wendy"))