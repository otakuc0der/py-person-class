class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person in people:
        instance = Person.people[person.get("name")]

        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name is not None and wife_name in Person.people:
            instance.wife = Person.people[wife_name]
        elif husband_name is not None and husband_name in Person.people:
            instance.husband = Person.people[husband_name]

    return result
