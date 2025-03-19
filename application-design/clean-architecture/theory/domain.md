# Domain

### **Domain Layer (Enterprise Business Rules)**

#### **Purpose:**

* **Encapsulates core business rules and domain entities**.
* Contains **business logic, validations, and domain events**.
* **No dependencies** on external frameworks (e.g., EF Core, ASP.NET).

#### **Components:**

* **Entities** – Core business objects.
* **Value Objects** – Immutable domain types (e.g., `Money`, `Address`).
* **Domain Events** – Business events that trigger actions.
* **Aggregates** – Logical groupings of domain objects.

#### **Example in C#:**

**Domain Entity**

```csharp
csharpCopyEditpublic class User
{
    public int Id { get; private set; }
    public string Name { get; private set; }
    public string Email { get; private set; }

    public User(int id, string name, string email)
    {
        if (string.IsNullOrEmpty(name)) throw new ArgumentException("Name is required");
        if (!email.Contains("@")) throw new ArgumentException("Invalid email format");

        Id = id;
        Name = name;
        Email = email;
    }
}
```

* The **Domain Layer** defines the **real-world business concepts** and enforces **business rules**.
* This layer should **not** contain persistence logic (e.g., EF Core) to ensure **clean separation**.
