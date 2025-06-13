from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def introduce(self):
        pass


class Player(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__hits = 0
        self.__at_bats = 0

    def record_hit(self):
        self.__hits += 1
        self.__at_bats += 1

    def record_at_bat(self):
        self.__at_bats += 1

    def get_hits(self):
        return self.__hits

    def get_at_bats(self):
        return self.__at_bats

    def get_batting_average(self):
        if self.__at_bats == 0:
            return 0.0
        return round(self.__hits / self.__at_bats, 3)

    def introduce(self):
        return f"Player: {self.name}, Age: {self.age}, Batting Avg: {self.get_batting_average()}"


class Coach(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def introduce(self):
        return f"Coach: {self.name}, Age: {self.age}, Role: {self.role}"


class Team:
    def __init__(self):
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def remove_member(self, name):
        self.members = [m for m in self.members if m.name != name]

    def show_roster(self):
        for member in self.members:
            print(member.introduce())

    def get_player(self, name):
        for member in self.members:
            if isinstance(member, Player) and member.name == name:
                return member
        return None


def main():
    team = Team()

    while True:
        print("\n--- Baseball Team Manager ---")
        print("1. Add Player")
        print("2. Add Coach")
        print("3. Record Hit")
        print("4. Record At-Bat")
        print("5. Show Player Stats")
        print("6. Show Team Roster")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter player name: ")
            age = int(input("Enter age: "))
            team.add_member(Player(name, age))
        elif choice == "2":
            name = input("Enter coach name: ")
            age = int(input("Enter age: "))
            role = input("Enter role: ")
            team.add_member(Coach(name, age, role))
        elif choice == "3":
            name = input("Enter player name: ")
            player = team.get_player(name)
            if player:
                player.record_hit()
                print("Hit recorded.")
            else:
                print("Player not found.")
        elif choice == "4":
            name = input("Enter player name: ")
            player = team.get_player(name)
            if player:
                player.record_at_bat()
                print("At-bat recorded.")
            else:
                print("Player not found.")
        elif choice == "5":
            name = input("Enter player name: ")
            player = team.get_player(name)
            if player:
                print(player.introduce())
            else:
                print("Player not found.")
        elif choice == "6":
            team.show_roster()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
