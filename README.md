# Design Patterns in Python

A collection of object-oriented programming principles and software design patterns implemented in **Python**.

This repository serves as a practical reference for understanding how common design patterns solve recurring software design problems, reduce coupling, improve extensibility, and support maintainable object-oriented code.

Each pattern is implemented with small, focused examples that demonstrate the problem, the design solution, and the relationships between the participating classes.

---

## Topics Covered

### 1. Object-Oriented Programming Fundamentals

The repository contains examples of core OOP concepts used throughout the design patterns:

- Classes
- Abstraction
- Encapsulation
- Inheritance
- Interfaces / Abstract Base Classes

---

## 2. Object Relationships

Understanding relationships between objects and classes is fundamental to object-oriented design.

### IS-A — Inheritance

An **IS-A** relationship means one class is a specialized version of another class.

For example:

> A `Dog` **IS-A** `Animal`.

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

Inheritance is commonly used to represent an IS-A relationship.

---

### HAS-A — Object Relationship

A **HAS-A** relationship means one object contains, owns, or uses another object.

For example:

> A `Car` **HAS-A** `Engine`.

```python
class Engine:
    pass


class Car:
    def __init__(self):
        self.engine = Engine()
```

HAS-A is a broad relationship. **Association, Aggregation, and Composition** are different forms of object relationships.

---

### Association

Association is a general relationship where two objects know about or interact with each other, but neither necessarily owns the other.

For example:

> A `Teacher` teaches a `Student`.

The teacher uses or interacts with the student, but both objects can exist independently.

```text
Teacher ───── Student
```

---

### Aggregation

Aggregation is a HAS-A relationship where one object contains another object, but the contained object can exist independently.

For example:

> A `Department` has `Professor` objects, but a professor can exist independently of a particular department.

```text
Department ◇──── Professor
```

Aggregation represents **weak ownership**.

---

### Composition

Composition is a stronger HAS-A relationship where the contained object conceptually belongs to the owner and its lifecycle is controlled by it.

For example:

> A `Car` owns an `Engine`.

```text
Car ◆──── Engine
```

Composition represents **strong ownership**.

### Relationship Cheat Sheet

| Relationship    | Meaning                                      | Example                |
| --------------- | -------------------------------------------- | ---------------------- |
| **IS-A**        | Inheritance                                  | Dog IS-A Animal        |
| **HAS-A**       | Contains or uses another object              | Car HAS-A Engine       |
| **Association** | Objects know/use each other                  | Teacher ↔ Student      |
| **Aggregation** | Weak ownership; part can exist independently | Department → Professor |
| **Composition** | Strong ownership; part belongs to the whole  | Car → Engine           |

---

## 3. SOLID Principles

SOLID is a set of five object-oriented design principles intended to make software easier to maintain, extend, and change.

### S — Single Responsibility Principle (SRP)

> A class should have **one responsibility** and therefore one primary reason to change.

Instead of giving one class many unrelated responsibilities, separate them into focused classes.

```text
One class → One responsibility
```

---

### O — Open/Closed Principle (OCP)

> Software entities should be **open for extension but closed for modification**.

When adding new functionality, we should ideally extend the system by adding new implementations instead of repeatedly modifying existing working code.

Large chains of type-based `if/elif` statements can sometimes indicate that behavior should instead be delegated through abstractions, polymorphism, dependency injection, or an appropriate factory/pattern.

```text
Extend behavior
      ↓
Add new implementation

instead of

Modify existing logic repeatedly
```

---

### L — Liskov Substitution Principle (LSP)

> A subclass should be usable wherever its parent class is expected without breaking the expected behavior of the program.

If `Dog` is a subtype of `Animal`, code designed to work with an `Animal` should continue to behave correctly when given a `Dog`.

```text
Parent expected
      ↑
Child should safely substitute
```

Inheritance should therefore preserve the behavioral contract of the parent abstraction.

---

### I — Interface Segregation Principle (ISP)

> Clients should not be forced to depend on methods they do not need.

Instead of creating one large interface with many unrelated methods, prefer smaller and more focused interfaces.

```text
Large interface
      ↓
Split into
      ↓
Small focused interfaces
```

This prevents classes from being forced to implement irrelevant operations.

---

### D — Dependency Inversion Principle (DIP)

> High-level classes should depend on **abstractions**, not concrete implementations.

Instead of:

```text
UserService
     ↓
MySQLDatabase
```

prefer:

```text
             Database
            /        \
           /          \
UserService        MySQLDatabase
                  PostgreSQLDatabase
```

`UserService` depends on the `Database` abstraction, allowing different database implementations to be supplied without changing the high-level service.

This reduces coupling and makes software easier to extend, test, and maintain.

### SOLID Cheat Sheet

| Principle   | Meaning                                                  |
| ----------- | -------------------------------------------------------- |
| **S — SRP** | One class, one responsibility                            |
| **O — OCP** | Extend without repeatedly modifying existing code        |
| **L — LSP** | A child should safely substitute for its parent          |
| **I — ISP** | Don't force classes to depend on methods they don't need |
| **D — DIP** | Depend on abstractions, not concrete implementations     |

---

# Design Patterns

Design patterns are reusable approaches to common software design problems.

They are generally divided into three categories:

1. **Behavioral** — communication and responsibilities between objects
2. **Structural** — how classes and objects are composed
3. **Creational** — how objects are created

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
| **Builder**          | Separate an object's construction process from its representation        |

---

## Key Design Principles Practiced

Throughout these examples, the patterns demonstrate concepts such as:

- Abstraction
- Encapsulation
- Polymorphism
- Loose coupling
- Dependency injection
- Composition over inheritance
- Separation of concerns
- Open/Closed Principle
- Dependency Inversion Principle

---

## Purpose

This repository was created to practice and understand **object-oriented design and design patterns in Python**.

The goal is not only to memorize pattern definitions, but to understand:

1. What design problem exists
2. Why the initial implementation can become difficult to maintain
3. Which design principles may be violated
4. How a design pattern restructures the solution
5. What advantages and trade-offs the pattern introduces

---

## Author

**Parham Abdolmohammadi**

Software Developer
