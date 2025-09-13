from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random

# -------------------------------------------
# Domain model for a simple Zoo Management app
# Comments explain intent/decisions (the "why"),
# while docstrings explain usage and behavior. [1][4]
# -------------------------------------------


# ========== Base Classes ==========

class Animal(ABC):
    """
    Abstract base class for all animals.

    Required interface:
    - make_sound() -> str
    - move() -> str

    Shared state:
    - hunger_level: int in [0, 100] where larger means hungrier
    - health_status: coarse health indicator
    - last_fed: timestamp used to derive hunger over time

    Note:
    - ABC ensures concrete species must implement the abstract methods. [19][20]
    """

    def __init__(self, name: str, age: int, weight: float):
        """
        Initialize a new Animal.

        Parameters:
        - name: public display name
        - age: age in years
        - weight: weight in kilograms

        Behavior:
        - Starts moderately hungry (50/100) to showcase feeding UX.
        - last_fed is set 8h in the past so hunger dynamics are visible at start. [21]
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.hunger_level = 50  # 0–100 scale; 100 is very hungry
        self.health_status = "Healthy"
        self.last_fed = datetime.now() - timedelta(hours=8)  # seed meaningful elapsed time

    @abstractmethod
    def make_sound(self) -> str:
        """Return a species‑specific vocalization. Must be overridden by subclasses. [19]"""
        raise NotImplementedError

    @abstractmethod
    def move(self) -> str:
        """Return a species‑specific movement description. Must be overridden. [19]"""
        raise NotImplementedError

    def eat(self, food_amount: int = 20) -> str:
        """
        Feed the animal and update hunger/time.

        Parameters:
        - food_amount: amount of feeding effect (points to subtract from hunger_level)

        Effects:
        - Decreases hunger_level but never below 0
        - Updates last_fed to now so time‑based hunger resets [21]
        """
        self.hunger_level = max(0, self.hunger_level - food_amount)
        self.last_fed = datetime.now()
        return f"{self.name} has been fed. Hunger level: {self.hunger_level}"

    def get_status(self) -> str:
        """
        Compute a human‑friendly status string.

        Logic:
        - Derive hours since last_fed; if it's large (>12h), nudge hunger upwards.
        - Convert hunger_level to a coarse status bucket.

        Note:
        - This method mutates hunger_level when a long time passed to reflect reality. [21]
        """
        hours_since_fed = (datetime.now() - self.last_fed).total_seconds() / 3600
        if hours_since_fed > 12:
            # Late feeding penalty: increase hunger by elapsed hours (clamped to 100)
            self.hunger_level = min(100, self.hunger_level + int(hours_since_fed))

        status = (
            "Content" if self.hunger_level < 30
            else "Hungry" if self.hunger_level < 70
            else "Very Hungry"
        )
        return f"{self.name} ({self.__class__.__name__}): {status} | Health: {self.health_status}"

    def __str__(self) -> str:
        """Developer‑friendly single‑line summary for logs and menus. [2]"""
        return f"{self.__class__.__name__}: {self.name} (Age: {self.age}, Weight: {self.weight}kg)"


# ========== Animal Categories ==========

class Mammal(Animal):
    """
    Mammal category.

    Adds:
    - fur_color
    - stable body temperature typical of mammals
    """

    def __init__(self, name: str, age: int, weight: float, fur_color: str = "Brown"):
        super().__init__(name, age, weight)
        self.fur_color = fur_color
        self.body_temperature = 37.0  # °C nominal

    def move(self) -> str:
        """Default mammal movement; species may override for specificity."""
        return "walks on four legs"

    def regulate_temperature(self) -> str:
        """Illustrative mammalian trait."""
        return f"{self.name} maintains body temperature at {self.body_temperature}°C"


class Bird(Animal):
    """
    Bird category.

    Adds:
    - wingspan
    - can_fly toggle for species like penguin
    - feather_condition (toy attribute for demo)
    """

    def __init__(self, name: str, age: int, weight: float, wingspan: float, can_fly: bool = True):
        super().__init__(name, age, weight)
        self.wingspan = wingspan
        self.can_fly = can_fly
        self.feather_condition = "Excellent"

    def move(self) -> str:
        """Birds usually fly; some species override this (e.g., penguins)."""
        return "flies through the air" if self.can_fly else "walks and swims"

    def preen_feathers(self) -> str:
        """Flavor method indicating routine behavior."""
        return f"{self.name} is preening feathers to maintain {self.feather_condition} condition"


class Reptile(Animal):
    """
    Reptile category.

    Adds:
    - scale_type
    - variable body temperature
    - optional venom flag for species
    """

    def __init__(self, name: str, age: int, weight: float, scale_type: str = "Smooth"):
        super().__init__(name, age, weight)
        self.scale_type = scale_type
        self.body_temperature = 25.0  # varies with environment
        self.is_venomous = False

    def move(self) -> str:
        """Reptilian default movement."""
        return "slithers along the ground"

    def bask_in_sun(self) -> str:
        """Increase body temperature to simulate thermoregulation."""
        self.body_temperature = min(35.0, self.body_temperature + 2.0)
        return f"{self.name} is basking. Body temperature: {self.body_temperature}°C"


# ========== Specific Species ==========

class Lion(Mammal):
    """Lion (mammal): optionally a pride leader affecting sound intensity."""

    def __init__(self, name: str, age: int, weight: float = 190.0):
        super().__init__(name, age, weight, fur_color="Golden")
        # Random for fun variability in demo output; not persisted
        self.pride_leader = random.choice([True, False])

    def make_sound(self) -> str:
        """Roar intensity depends on pride_leader flag."""
        return "ROARRR!" if self.pride_leader else "roars"

    def hunt(self) -> str:
        """Species‑specific behavior."""
        return f"{self.name} stalks prey with powerful muscles and sharp claws"


class Eagle(Bird):
    """Eagle (bird): flying predator with large wingspan and strong vision."""

    def __init__(self, name: str, age: int, weight: float = 6.0):
        super().__init__(name, age, weight, wingspan=2.3, can_fly=True)
        self.sharp_vision = "Exceptional"

    def make_sound(self) -> str:
        """Eagle screech."""
        return "SCREECH!"

    def dive_attack(self) -> str:
        """Species‑specific behavior illustrating hunting style."""
        return f"{self.name} dives at 200+ km/h with {self.sharp_vision} vision"


class Penguin(Bird):
    """Penguin (bird): flightless; strong swimmer."""

    def __init__(self, name: str, age: int, weight: float = 25.0):
        super().__init__(name, age, weight, wingspan=0.6, can_fly=False)
        self.swimming_speed = 35  # km/h

    def make_sound(self) -> str:
        """Penguin vocalization."""
        return "honk honk!"

    def swim(self) -> str:
        """Species‑specific movement in water."""
        return f"{self.name} swims gracefully at {self.swimming_speed} km/h"


class Snake(Reptile):
    """Snake (reptile): optionally venomous; coils and strikes."""

    def __init__(self, name: str, age: int, weight: float = 8.0, is_venomous: bool = True):
        super().__init__(name, age, weight, scale_type="Overlapping")
        self.is_venomous = is_venomous
        self.length = 3.0  # meters

    def make_sound(self) -> str:
        """Snake hiss."""
        return "hissssss..."

    def coil_strike(self) -> str:
        """Species‑specific attack description including venom note."""
        venom_note = " with venomous fangs" if self.is_venomous else ""
        return f"{self.name} coils and strikes{venom_note}"


# ========== Zoo Management ==========

class Exhibit:
    """
    Exhibit/enclosure container.

    Responsibilities:
    - Hold a bounded list of animals
    - Describe climate and capacity
    - Provide simple add/remove/info APIs
    """

    def __init__(self, name: str, capacity: int, climate: str = "Temperate"):
        self.name = name
        self.capacity = capacity
        self.climate = climate
        self.animals: List[Animal] = []
        self.last_cleaned = datetime.now()

    def add_animal(self, animal: Animal) -> bool:
        """
        Try to add an animal respecting capacity.

        Returns:
        - True if added
        - False if at capacity
        """
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            return True
        return False

    def remove_animal(self, animal_name: str) -> bool:
        """Remove by name; returns True if removed, else False."""
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                return True
        return False

    def get_info(self) -> str:
        """One‑line summary of enclosure occupancy."""
        animal_list = [animal.name for animal in self.animals]
        return (
            f"Exhibit '{self.name}' ({self.climate}): "
            f"{len(self.animals)}/{self.capacity} animals - "
            f"{', '.join(animal_list) if animal_list else 'Empty'}"
        )


class Zoo:
    """
    Main zoo management façade.

    Composition:
    - animals: flat registry of all animals in the zoo
    - exhibits: optional grouping/assignment

    Also tracks simple operational data like visitors_today. [2]
    """

    def __init__(self, name: str):
        self.name = name
        self.animals: List[Animal] = []
        self.exhibits: List[Exhibit] = []
        self.visitors_today = 0
        self.established_date = datetime.now()

    def _species_label(self, animal: Animal) -> str:
        """
        Helper to format species with an emoji for friendlier UI.
        Purely cosmetic; safe to change without touching core logic.
        """
        species = animal.__class__.__name__
        emojis = {
            "Lion": "\U0001F981",     # 🦁
            "Eagle": "\U0001F985",    # 🦅
            "Penguin": "\U0001F427",  # 🐧
            "Snake": "\U0001F40D",    # 🐍
        }
        emoji = emojis.get(species, "")
        return f"{species} {emoji}".strip()

    # ---- Visitors ----

    def admit_visitors(self, count: int) -> str:
        """Increment today's visitor count; rejects negatives."""
        if count < 0:
            return "Visitor count cannot be negative"
        self.visitors_today += count
        return f"Admitted {count} visitors. Total today: {self.visitors_today}"

    def set_visitors_today(self, count: int) -> str:
        """Admin override for visitors_today; rejects negatives."""
        if count < 0:
            return "Visitor count cannot be negative"
        self.visitors_today = count
        return f"Visitors today set to {self.visitors_today}"

    def reset_daily_counters(self) -> str:
        """Reset simple counters (currently just visitors_today)."""
        self.visitors_today = 0
        return "Daily counters reset"

    # ---- Animals & Exhibits ----

    def add_animal(self, animal: Animal, exhibit_name: Optional[str] = None) -> str:
        """
        Add animal to the zoo and optionally place into an exhibit.

        Behavior:
        - Always registers animal in zoo.animals
        - If exhibit_name is given:
          - Attempts to place animal; reports success/failure reason
        - Returns a human‑friendly status line including species label
        """
        self.animals.append(animal)
        label = self._species_label(animal)

        if exhibit_name:
            exhibit = self.find_exhibit(exhibit_name)
            if exhibit and exhibit.add_animal(animal):
                return (
                    f"{animal.name} has been added to {exhibit_name} exhibit\n"
                    f"Category: {label}"
                )
            elif exhibit:
                return (
                    f"{animal.name} added to zoo but {exhibit_name} is full\n"
                    f"Category: {label}"
                )
            else:
                return (
                    f"{animal.name} added to zoo but exhibit '{exhibit_name}' not found\n"
                    f"Category: {label}"
                )

        return f"{animal.name} has been added to the zoo\nCategory: {label}"

    def create_exhibit(self, name: str, capacity: int, climate: str = "Temperate") -> str:
        """Create a new exhibit and register it with the zoo."""
        exhibit = Exhibit(name, capacity, climate)
        self.exhibits.append(exhibit)
        return f"Created exhibit '{name}' with capacity {capacity}"

    def find_exhibit(self, name: str) -> Optional[Exhibit]:
        """Case‑insensitive exhibit lookup by name; returns None if not found."""
        for exhibit in self.exhibits:
            if exhibit.name.lower() == name.lower():
                return exhibit
        return None

    def find_animal(self, name: str) -> Optional[Animal]:
        """Case‑insensitive animal lookup by display name; returns None if not found."""
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal
        return None

    def feed_animal(self, animal_name: str) -> str:
        """Feed a specific animal by name; returns status or error string."""
        animal = self.find_animal(animal_name)
        if animal:
            return animal.eat()
        return f"Animal '{animal_name}' not found"

    def feed_all_animals(self) -> List[str]:
        """
        Feed every animal in one go.

        Polymorphism:
        - Calls eat() on each Animal regardless of concrete type. [22]
        """
        return [animal.eat() for animal in self.animals]

    def daily_animal_show(self) -> List[str]:
        """
        Demonstrate polymorphism by invoking the same interface on different species. [22]
        """
        show_acts = []
        for animal in self.animals:
            act = f"{animal.name}: {animal.make_sound()} and {animal.move()}"
            show_acts.append(act)
        return show_acts

    def get_zoo_stats(self) -> Dict:
        """
        Compute basic operational metrics in one pass.

        Returns a dict with:
        - total_animals: count of registered animals
        - animal_types: mapping species -> count
        - total_exhibits: count of exhibits
        - total_weight: sum of weights (kg, rounded)
        - hungry_animals: count where hunger_level > 50
        - visitors_today: simple daily counter
        - established_date: human‑readable date string

        Rationale:
        - Handy for dashboards/logs without scanning lists in multiple places.
        """
        animal_types: Dict[str, int] = {}
        total_weight = 0.0
        hungry_animals = 0

        for animal in self.animals:
            species = animal.__class__.__name__
            animal_types[species] = animal_types.get(species, 0) + 1
            total_weight += animal.weight
            if animal.hunger_level > 50:
                hungry_animals += 1

        return {
            "total_animals": len(self.animals),
            "animal_types": animal_types,
            "total_exhibits": len(self.exhibits),
            "total_weight": round(total_weight, 2),
            "hungry_animals": hungry_animals,
            "visitors_today": self.visitors_today,
            "established_date": self.established_date.strftime('%d-%m-%Y'),
        }

    def list_all_animals(self) -> List[str]:
        """Return status strings for all animals (delegates to Animal.get_status)."""
        return [animal.get_status() for animal in self.animals]

    def list_all_exhibits(self) -> List[str]:
        """Return human‑readable info lines for each exhibit."""
        return [exhibit.get_info() for exhibit in self.exhibits]


# ========== Interactive CLI ==========

def display_menu():
    """Print the main menu for the CLI; kept plain for easy scanning. [2]"""
    print("\n" + "=" * 50)
    print("🦁 WELCOME TO THE ZOO MANAGEMENT SYSTEM 🦁 ")
    print("=" * 50)
    print("1. Add Animal")
    print("2. Create Exhibit")
    print("3. View All Animals")
    print("4. View All Exhibits")
    print("5. Feed Animal")
    print("6. Feed All Animals")
    print("7. Daily Animal Show")
    print("8. Zoo Statistics")
    print("9. Admit Visitors")
    print("10. Set Visitors Today (Admin)")
    print("11. Reset Daily Counters")
    print("12. Exit")
    print("-" * 50)


def add_animal_interactive(zoo: Zoo):
    """
    Minimal CLI for adding a species instance.

    Notes:
    - For a real app, consider validation and error handling per field.
    - This demo uses a simple mapping to concrete classes.
    """
    print("\nChoose animal type:")
    print("1. Lion  2. Eagle  3. Penguin  4. Snake")

    choice = input("Enter choice (1-4): ").strip()
    name = input("Enter animal name: ").strip()
    age = int(input("Enter age: "))

    animal_map = {
        "1": Lion(name, age),
        "2": Eagle(name, age),
        "3": Penguin(name, age),
        "4": Snake(name, age),
    }

    if choice in animal_map:
        exhibit_name = input("Enter exhibit name (optional, press Enter to skip): ").strip()
        exhibit_name = exhibit_name if exhibit_name else None
        result = zoo.add_animal(animal_map[choice], exhibit_name)
        print(f"✅ {result}")
    else:
        print("❌ Invalid animal type")


def main():
    """Main event loop for the CLI demo."""
    zoo = Zoo("Safari Adventure Zoo")

    # Seed a few exhibits so “add to exhibit” works immediately.
    zoo.create_exhibit("Savanna", 5, "Hot")
    zoo.create_exhibit("Arctic", 8, "Cold")
    zoo.create_exhibit("Rainforest", 10, "Tropical")

    # Seed some animals for first‑run UX so menus show data.
    zoo.add_animal(Lion("Simba", 5), "Savanna")
    zoo.add_animal(Eagle("Freedom", 3), "Savanna")
    zoo.add_animal(Penguin("Pingu", 2), "Arctic")
    zoo.add_animal(Snake("Kaa", 4), "Rainforest")

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ").strip()

        if choice == "1":
            add_animal_interactive(zoo)

        elif choice == "2":
            name = input("Enter exhibit name: ").strip()
            capacity = int(input("Enter capacity: "))
            climate = input("Enter climate (Temperate/Hot/Cold/Tropical): ").strip()
            result = zoo.create_exhibit(name, capacity, climate)
            print(f"✅ {result}")

        elif choice == "3":
            animals = zoo.list_all_animals()
            print(f"\n📋 Animals in {zoo.name}:")
            for animal in animals:
                print(f"  • {animal}")

        elif choice == "4":
            exhibits = zoo.list_all_exhibits()
            print(f"\n🏛️  Exhibits in {zoo.name}:")
            for exhibit in exhibits:
                print(f"  • {exhibit}")

        elif choice == "5":
            name = input("Enter animal name to feed: ").strip()
            result = zoo.feed_animal(name)
            print(f"🍖 {result}")

        elif choice == "6":
            results = zoo.feed_all_animals()
            print("🍖 Feeding all animals:")
            for result in results:
                print(f"  • {result}")

        elif choice == "7":
            show_acts = zoo.daily_animal_show()
            print("\n🎭 DAILY ANIMAL SHOW:")
            for act in show_acts:
                print(f"  🎪 {act}")

        elif choice == "8":
            stats = zoo.get_zoo_stats()
            print(f"\n📊 Zoo Statistics for {zoo.name}:")
            print(f"  • Total Animals: {stats['total_animals']}")
            print(f"  • Animal Types: {stats['animal_types']}")
            print(f"  • Total Exhibits: {stats['total_exhibits']}")
            print(f"  • Combined Weight: {stats['total_weight']} kg")
            print(f"  • Hungry Animals: {stats['hungry_animals']}")
            print(f"  • Visitors Today: {stats['visitors_today']}")
            print(f"  • Established Date: {stats['established_date']}")

        elif choice == "9":
            try:
                count = int(input("Enter number of visitors to admit: ").strip())
            except ValueError:
                print("❌ Please enter a valid number")
                continue
            result = zoo.admit_visitors(count)
            print(f"👥 {result}")

        elif choice == "10":
            try:
                count = int(input("Enter visitors today (admin set): ").strip())
            except ValueError:
                print("❌ Please enter a valid number")
                continue
            result = zoo.set_visitors_today(count)
            print(f"🛠️  {result}")

        elif choice == "11":
            result = zoo.reset_daily_counters()
            print(f"♻️  {result}")

        elif choice == "12":
            print(f"🙏 Thank you for visiting {zoo.name}!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
