# Design Patterns in Python

A collection of object-oriented programming principles and software design patterns implemented in **Python**.

This repository serves as a practical reference for understanding how common design patterns solve recurring software design problems, reduce coupling, improve extensibility, and support maintainable object-oriented code.

Each pattern is implemented with small, focused examples that demonstrate the problem, the design solution, and the relationships between the participating classes.

---

## Topics Covered

### Object-Oriented Programming Fundamentals

The repository also contains examples of core OOP concepts used throughout the design patterns:

- Classes
- Abstraction
- Encapsulation
- Inheritance
- Interfaces / Abstract Base Classes

---

## Behavioral Design Patterns

Behavioral patterns focus on communication and responsibility between objects.

| Pattern                     | Purpose                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------ |
| **Memento**                 | Capture and restore an object's previous state                                       |
| **State**                   | Change an object's behavior when its internal state changes                          |
| **Strategy**                | Define interchangeable algorithms or behaviors                                       |
| **Iterator**                | Traverse a collection without exposing its internal representation                   |
| **Template Method**         | Define an algorithm skeleton while allowing subclasses to customize individual steps |
| **Command**                 | Encapsulate an operation or request as an object                                     |
| **Observer**                | Notify dependent objects when another object's state changes                         |
| **Mediator**                | Centralize communication between related objects                                     |
| **Chain of Responsibility** | Pass a request through a chain of handlers                                           |
| **Visitor**                 | Add new operations to an object structure without modifying its element classes      |

---

## Structural Design Patterns

Structural patterns focus on how classes and objects are composed.

| Pattern       | Purpose                                                                          |
| ------------- | -------------------------------------------------------------------------------- |
| **Composite** | Treat individual objects and groups of objects uniformly                         |
| **Adapter**   | Convert an incompatible interface into one expected by the client                |
| **Decorator** | Dynamically add behavior to an object through composition                        |
| **Facade**    | Provide a simplified interface to a complex subsystem                            |
| **Flyweight** | Reduce memory usage by sharing common object state                               |
| **Bridge**    | Separate an abstraction from its implementation so both can evolve independently |
| **Proxy**     | Provide a substitute that controls access to another object                      |

---

## Creational Design Patterns

Creational patterns focus on how objects are created.

| Pattern              | Purpose                                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| **Prototype**        | Create new objects by copying existing objects                           |
| **Singleton**        | Ensure a class has only one shared instance                              |
| **Factory Method**   | Delegate object creation to subclasses                                   |
| **Abstract Factory** | Create families of related objects without depending on concrete classes |
| **Builder**          | Separate the construction process of an object from its representation   |
