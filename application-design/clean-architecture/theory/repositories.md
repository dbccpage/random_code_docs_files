# Repositories

### **Repository Layer**

#### **Purpose:**

* Abstracts data access logic to **provide a consistent API** for the application core.
* Uses **Domain Entities** and **Data Transfer Objects (DTOs)** to communicate with the core logic.
* Ensures data access is **decoupled** from business logic.

#### **Components:**

* **Repository Interfaces (Contracts)** – Defined in the **Core Domain**.
* **Repository Implementations** – Implemented in the **Infrastructure Layer**.

#### **Example in C#:**

**Repository Interface (In Core Domain)**

```csharp
csharpCopyEditpublic interface IUserRepository
{
    Task<User> GetUserByIdAsync(int id);
    Task AddUserAsync(User user);
}
```

**Repository Implementation (In Infrastructure Layer)**

```csharp
csharpCopyEditpublic class UserRepository : IUserRepository
{
    private readonly ApplicationDbContext _context;

    public UserRepository(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<User> GetUserByIdAsync(int id)
    {
        return await _context.Users.FindAsync(id);
    }

    public async Task AddUserAsync(User user)
    {
        _context.Users.Add(user);
        await _context.SaveChangesAsync();
    }
}
```

* Here, **UserRepository** is responsible for **data retrieval and persistence**.
* The **Application Core** is not aware of how the data is stored (SQL, NoSQL, etc.), which provides **loose coupling**.
