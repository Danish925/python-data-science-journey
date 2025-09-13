Zoo Simulator (OOP: inheritance + polymorphism)

Overview
A simple yet complete Zoo Management mini‑project that models animals and exhibits using object‑oriented design. It demonstrates inheritance, method overriding, and polymorphism through a CLI that adds animals, feeds them, shows a daily show, and reports basic stats.

Features

1.Class hierarchy: Animal → Mammal/Bird/Reptile → Lion, Eagle, Penguin, Snake.

2.Time‑based hunger and feeding, visitor counters, exhibits with capacity, and a daily animal show.

3.Simple CLI menus to add animals, create exhibits, feed animals, and view stats.

Folder structure

1.zoo.py — runnable CLI with full implementation and comments.

2.README.md — this file with run instructions and concepts.

Run

1.Python 3.9+ recommended.

2.From repository root:

  • cd projects/zoo-sim-oop

  • python zoo.py

3.In the menu, choose:

   • Add Animal to create Lion/Eagle/Penguin/Snake

   • Create Exhibit to make Savanna/Arctic/etc.

   • Feed Animal or Feed All Animals to update hunger

   • Daily Animal Show to see polymorphic behavior

   • Zoo Statistics for counts, species mix, weight sum, hungry count, visitors today

Concepts shown

1.Inheritance: Shared behavior lives in Animal; Mammal/Bird/Reptile add category traits; species specialize further.

2.Method overriding: Species redefine make_sound() and move() to express specific behavior.

3.Polymorphism: Code calls the same interface (eat(), make_sound(), move()) on different species without knowing their concrete types.

4.Composition: Zoo holds a list of animals and exhibits; Exhibit holds its own animals up to a capacity.

5.Time‑aware state: Hunger increases with elapsed time since last_fed; feeding resets the clock.

6.CLI patterns: A simple loop, input handling, and clear, numbered menu options.

Quick API tour

1.Animal base (abstract):

  • make_sound() and move() must be implemented by species.

  • eat(food_amount=20) lowers hunger_level and updates last_fed.

  • get_status() summarizes content/hungry/very hungry based on hunger_level.

2.Categories:

  • Mammal: fur_color, regulate_temperature().

  • Bird: wingspan, can_fly, preen_feathers(); Penguin overrides movement.

  • Reptile: scale_type, bask_in_sun(), optional venom.

3.Species:

  • Lion: pride_leader influences roar intensity; hunt() demo method.

  • Eagle: dive_attack() to illustrate hunting behavior.

  • Penguin: swim() to highlight aquatic motion.

  • Snake: coil_strike(), optional venom note.

4.Zoo management:

   • add_animal(animal, exhibit_name=None) registers animals and optionally places them.

   • create_exhibit(name, capacity, climate) groups animals under capacity.

   • feed_animal(name) and feed_all_animals() update hunger consistently.

   • daily_animal_show() demonstrates polymorphism at runtime.

   • get_zoo_stats() returns totals and a per‑species breakdown.

   • admit_visitors(), set_visitors_today(), reset_daily_counters() handle simple ops.

Example session

1.Start:

  • cd projects/zoo-sim-oop && python zoo.py

2.Choose “3. View All Animals” to see seeded animals.

3.Choose “6. Feed All Animals” and then “8. Zoo Statistics” to see hungry count change.

4.Choose “7. Daily Animal Show” to see different species respond to the same interface.

Notes

  • This is a teaching demo favoring clarity over production complexity.

  • The design makes it easy to add new species: subclass the right category, override make_sound()/move(), and you are done.



Consider a small persistence layer (save/load animals) for a follow‑up exercise.

